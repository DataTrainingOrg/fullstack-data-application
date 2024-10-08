# Exercice 

## Première partie
A partir de l'app mise en place dans le dossier `app/`, ajouter un système d'authentification basique avec FastAPI sur les 
endpoints que vous jugerez bon de sécuriser.

## Deuxième partie

Vous remarquerez certainement que pour chaque endpoint sécurisé, vous devrez vérifier le token JWT à chaque fois.
Ce qui implique une duplication de code. 
A l'aide de la documentation de FastAPI, mettez en place un système permettant de gérer
l'authentification de manière automatique pour un endpoint.

## Troisième partie

Ecrivez une fonction qui récupère l'ID du user à partir du token JWT. 
En entrant dans la fonction de l'endpoint, le programme devra avoir valider le token et avoir l'ID de l'utilisateur à disposition

## Quatrième partie 

A l'aide de la librairie `requests`, écrivez un script python pour effectuer une requête vers un de vos endpoint sécurisé.

