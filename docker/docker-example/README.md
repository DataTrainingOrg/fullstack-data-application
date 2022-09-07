# Commandes

- Build l'image du conteneur: `docker build -t python_app .`
- Instancier le conteneur: `docker run --name python_app -it -v $PWD:/app -p 5000:5000 python_app`
- Tester l'API: http://localhost:5000/
- Supprimer le conteneur: `docker rm -f python_app`
