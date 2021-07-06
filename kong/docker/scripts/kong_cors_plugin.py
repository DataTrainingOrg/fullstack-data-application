import requests
import os
# from dotenv import load_dotenv
# load_dotenv("../../.env")

KONG_HOST_IP = os.environ.get("KONG_HOST_IP")
KONG_PORT = os.environ.get("KONG_PORT")
KEYCLOAK_HOST_IP = os.environ.get("KEYCLOAK_HOST_IP")
KEYCLOAK_PORT = os.environ.get("KEYCLOAK_PORT")

BACKEND_URI = os.environ.get("BACKEND_URI")
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

ENKI_API_SERVICE_ID = os.environ.get("ENKI_API_SERVICE_ID")
BACKEND_HOST_IP = os.environ.get("BACKEND_HOST_IP")

data = [
  ('name', 'cors'),
  ('config.origins', 'http://localhost:1337/*'),
  ('config.methods', 'GET'),
  ('config.methods', 'POST'),
  ('config.methods', 'OPTIONS'),
  ('config.methods', 'PUT'),
  ('config.methods', 'DELETE'),
  ('config.headers', 'Accept'),
  ('config.headers', 'Accept-Version'),
  ('config.headers', 'Content-Length'),
  ('config.headers', 'Content-MD5'),
  ('config.headers', 'Content-Type'),
  ('config.headers', 'Authorization'),
  ('config.headers', 'Date'),
  ('config.headers', 'X-Auth-Token'),
  ('config.exposed_headers', 'X-Auth-Token'),
  ('config.credentials', 'true'),
  ('config.max_age', '3600')
]


def get_enki_service_id():
  response = requests.get(f'http://{KONG_HOST_IP}:{KONG_PORT}/services')
  print(response.json()["data"])
  enki_api_id = [elt["id"] for elt in response.json()["data"] if elt["host"] == BACKEND_HOST_IP][0]
  return enki_api_id

enki_service_id = get_enki_service_id()

response = requests.post(f'http://{KONG_HOST_IP}:{KONG_PORT}/services/{enki_service_id}/plugins', data=data)
