# Exemple de Docker Compose

- Se placer dans ce répertoire `fullstack-data-application/docker/docker-compose-example` contenant le `docker-compose.yml`
- Lancer les instances: `docker-compose up -d`
- Checker le status des conteneurs: `docker-compose ps -a`
- Checker les logs des conteneurs: `docker-compose logs -f`
- Checker les logs du conteneur API: `docker-compose logs -f api`
- Aller sur `localhost:8080` et cliquer sur le bouton
- Aller sur `localhost:5000`
- Aller sur `localhost:5000/db`
- Stopper le Docker Compose: `docker-compose down`