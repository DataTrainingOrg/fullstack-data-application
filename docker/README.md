# Docker

Afin de pouvoir travailler dans les meilleurs conditions, nous allons travailler à partir de la technologie Docker. Docker est une technologie de conteneurs utilisés par les DevOps pour permettre un déploiement plus simple et plus rapide. Par rapport à des machines virtuelles, Docker est plus léger.

![](docs/docker_archi.png)

## Créer une image

Pour créer l'image utilisée dans le projet, on utilise le ``Dockerfile`` présent dans le répertoire (jeter un oeil à ce fichier pour comprendre les composants utilisés)  :


```
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY ./app /app/app
```

``` bash
docker build -t <image_name>  .
```

L'opération se termine correctement si ``Successfully built`` est affiché. La chaîne alphanumérique qui suit permet d'identifier l'image sans ambiguité.

## Créer un conteneur


A partir de cette image, on peut créer une instance (conteneur) dans lequel on va travailler (on remplacera ``<WORKDIR>`` par son propre répertoire de travail) :

```bash
docker run --name <conteneur_name> -v `pwd`:/home/dev/code/ -p 8888:8888 <image_name>
```

Le prompt ``#`` est celui du conteneur dans lequel on est ``root``. On peut alors lancer les commandes incluses dans le conteneur(ici l'interpréteur Python).

Il n'est pas rare de lancer plusieurs conteneurs instanciés à partir de la même image. Contrairement à une machine virtuelle, docker utilise la même base et les mêmes composants pour tous ces conteneurs et donc réduire l'impact mémoire de ces derniers.

Pour revenir un peu sur la commande ``docker run --name <conteneur_name> -v `pwd`:/home/dev/code/ -p 8888:8888 <image_name>``

- docker run : permet de lancer un conteneur à partir d'une image précédement buildée.
- ̀-it  permet de passer en mode intéractif, ie: le terminal du conteneur prend la main sur le terminal de votre machine
- --name  <conteneur_name> donne un nom au conteneur pour pouvoir le trouver plus facilement
- -v `pwd`:/home/dev/code/ permet de faire mapping entre le dossier à l'intérieur du conteneur et le dossier de votre machine, ie: tous les modifications de fichier dans votre conteneur ou sur votre machine se répercuteront respectivement sur votre machine et dans votre conteneur.
- <image_name> en fin de ligne, est le nom de l'image à utiliser pour créer votre conteneur

## Logs 

```docker logs -f <conteneur_name|conteneur_id>``` permet d'afficher les logs de l'instance du conteneur.

L'option `-f` permet de garder la main sur les logs dans le terminal. La commande ne rend pas la main.
Regarder les logs d'un conteneur permet souvent de trouver les bugs que vous pouvez rencontrer.

## Exec

Lorsque vous voulez vous connecter à une instance pour lancer des commandes par exemple, vous pouvez le faire via la commande suivante. 

```docker exec -it <conteneur_name|conteneur_id> bash``` permet d'afficher les logs de l'instance du conteneur.

l'option `-it ` permet de prendre la main sur le terminal de l'instance. En l'enlevant, vous executer juste la commande sur l'instance.

## Docker compose

Docker compose permet de gérer l'ensemble d'une application. Elle permet de mettre en relation plusieurs définition d'images et donc de conteneurs. 

Le fichier `docker-compose.yml` permet de définir, l'ensemble des services et les relier entre eux.

## Exercices

Réaliser les commandes vu précédemment pour lancer flask directement dans Docker.