import requests
import os
import uuid
# from dotenv import load_dotenv
# load_dotenv("../../.env")

KONG_HOST_IP = "kong"
KONG_PORT = "8001"

BACKEND_URI = os.environ.get("BACKEND_URI")
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REALM_NAME = "master"
KEYCLOAK_URL = f"http://{KEYCLOAK_HOST_IP}:{KEYCLOAK_PORT}/auth/"


services = [
    {
        'name': "front_service",
        'url': f'http://nginx:7777/front',
        'path': "front"

    },
        {
        'name': "api_service",
        'url': f'http://nginx:7777/api',
        'path': "api"

    }
]

#def clean():
response = requests.get(f'http://{KONG_HOST_IP}:{KONG_PORT}/routes')
for _id in [e["id"] for e in response.json()["data"]]:
    requests.delete(f'http://{KONG_HOST_IP}:{KONG_PORT}/routes/{_id}')
response = requests.get(f'http://{KONG_HOST_IP}:{KONG_PORT}/services')
for _id in [e["id"] for e in response.json()["data"]]:
    requests.delete(f'http://{KONG_HOST_IP}:{KONG_PORT}/services/{_id}')

from keycloak import KeycloakAdmin

# Create kong client on Keycloak
keycloak_admin = KeycloakAdmin(server_url=KEYCLOAK_URL,
                               username=KEYCLOAK_ADMIN_USER,
                                password=KEYCLOAK_ADMIN_PASSWORD,
                               verify=True)

CLIENT_KONG_KEYCLOAK_ID = str(uuid.uuid4())
keycloak_admin.create_client({
     "id":CLIENT_KONG_KEYCLOAK_ID,
     "clientId":CLIENT_ID,
     "name":CLIENT_ID,
     "enabled": True,
     "redirectUris":[ "/front/*", "/api/*", "/*", "*" ],
})

CLIENT_SECRET = keycloak_admin.get_client_secrets(CLIENT_KONG_KEYCLOAK_ID)["value"]

introspection_url = f'http://{KEYCLOAK_HOST_IP}:{KEYCLOAK_PORT}/auth/realms/{REALM_NAME}/protocol/openid-connect/token/introspect'
discovery_url = f'http://{KEYCLOAK_HOST_IP}:{KEYCLOAK_PORT}/auth/realms/{REALM_NAME}/.well-known/openid-configuration'


for service in services:
    data = service

    # Create Service
    response = requests.post(f'http://{KONG_HOST_IP}:{KONG_PORT}/services', data=data)
    created_service_id = response.json()["id"]

    # Create route
    data = {
        'service.id': f'{created_service_id}',
        'paths[]': f'/{service["path"]}',
    }

    response = requests.post(f'http://{KONG_HOST_IP}:{KONG_PORT}/services/{service["name"]}/routes', data=data)
    # Configure OIDC
    data = {
        'name': 'oidc',
        'config.client_id': f'{CLIENT_ID}',
        'config.client_secret': f'{CLIENT_SECRET}',
        'config.realm': f'{REALM_NAME}',
        'config.bearer_only': 'true',
        'config.introspection_endpoint': introspection_url,
        'config.discovery': discovery_url
    }

    response = requests.post(f'http://{KONG_HOST_IP}:{KONG_PORT}/services/{created_service_id}/plugins', data=data)