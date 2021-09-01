from fastapi import FastAPI, Depends
from keycloak import KeycloakOpenID
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Configure client
keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
                                 client_id="fastapi",
                                 realm_name="master",
                                 client_secret_key="97e13e2d-90e6-447f-9e3b-914b27653821")


@app.get("/protected")
def protected(token: str = Depends(oauth2_scheme)):
    return {
        "Hello": "World",
        "user_infos": token
    }
