# TP Authentification

## Run Front
```bash
python -m flask run
```

## Run API 
```bash
uvicorn app:app --reload --port 1235
```

## Identity Provider

`http://localhost:8080/auth/realms/master/account/̀`

### Github
Developer Settings 
OAuth Apps
Authorization Callback URL : localhost:5000/*
Récupérer et stocker le client ID
Générer, récupérer et stocker le client secret

Ajouter toutes ces informations dans keycloak directement

à la validation, vous pouvez tester que le bouton github apparait bien sur votre écran de login 

http://localhost:8080/auth/realms/master/account/



### Gitlab

To add a new application for your user:

In the top-right corner, select your avatar.
Select Edit profile.
In the left sidebar, select Applications.
Enter a Name, Redirect URI and select openid, email, profile, api scopes as defined in Authorized Applications.
 The Redirect URI is the URL where users are sent after they authorize with GitLab.
 
Select Save application. GitLab provides:

The OAuth 2 Client ID in the Application ID field.
The OAuth 2 Client Secret, accessible: Using the Copy button on the Secret field in GitLab 14.2 and later.


### Facebook

### Google 
https://keycloakthemes.com/blog/how-to-setup-sign-in-with-google-using-keycloak