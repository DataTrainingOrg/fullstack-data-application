# Projet Formulaire Hopital

Ce projet a été réalisé par Thomas Faillaufaix, Nathan Chatenet et Juliette Rochon, dans le but de réduire le temps d'attente dans les hôpitaux
liés aux formulaires administratifs.

Les technologies utilisées sont FastAPI pour la partie backend, React pour la partie frontend, et nous avons utilisés les schémas Pydantic.

Nous avions choisi initialement d’utiliser React en frontend, et Flask en backend. En effet, nous connaissions la technologie Flask. Cependant, nous nous sommes rendus compte que ce choix n’était pas le plus optimal, et que choisir FastAPI en backend serait plus judicieux.

Cette application permet de faciliter la prise en charge des patients dans les hôpitaux. Pour ce faire, nous nous sommes interrogés quant aux aspects administratifs d’une prise en charge patient. Le patient doit remplir un formulaire à son arrivée, et si ce dernier se voit changer de service, certains hôpitaux ont légalement besoin de lui faire remplir à nouveau l’exact même formulaire. Il en est de même d’une hospitalisation à l’autre. Pourtant, certaines données comme le prénom du patient, son nom, son numéro de sécurité sociale, sa date de naissance, etc. ne changent pas.

## Lancer l'application web

Pour décorreler la partie frontend du backend, nous avons créer à la racine du projet un dossier frontend et un dossier backend.

Pour démarrer l'application, il y a plusieurs étapes :

``npm start`` dans le dossier frontend

``python main.py`` dans le dossier backend

## Améliorations possibles

Si nous avions eu plus de temps, nous aurions utilisé les technologies Keycloak et Kong. De plus, il aurait été très pratique que cette application génère un QR code qui permette de transférer les informations du formulaire d’une interface à une autre aisément (de la même manière que le fait TousAntiCovid)
