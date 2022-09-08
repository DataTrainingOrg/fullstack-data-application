# Docker

- [Docker](#docker)
  - [Install Docker Desktop](#install-docker-desktop)
  - [Build an image](#build-an-image)
  - [Launch a container](#launch-a-container)
  - [Manage image and container](#manage-image-and-container)
  - [Logs](#logs)
  - [Exec](#exec)
  - [Docker Compose](#docker-compose)
- [Aller plus loin](#aller-plus-loin)
  - [Images de base](#images-de-base)
  - [Multi-stage builds](#multi-stage-builds)
  - [Docker registry](#docker-registry)
  - [Développer depuis un conteneur](#développer-depuis-un-conteneur)

## Install Docker Desktop

Windows: https://docs.docker.com/desktop/install/windows-install/

MacOS: https://docs.docker.com/desktop/install/mac-install/

## Build an image

The container image is built using the Dockerfile.

Dockerfile
```
FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "--debug", "run", "--host=0.0.0.0" ]
```

Build image
```
docker build -t image_name  .
```


## Launch a container


Launch container
```
docker run --name container_name image_name
```
Specify port
```
docker run --name container_name -p local_port:container_port image_name
```
Specify volume
```
docker run --name container_name -v local_folder:container_folder image_name
```
Launch container in detached mode
```
docker run -d --name container_name image_name
```

## Manage image and container
- List images:
`docker images` or `docker image ls`

- List containers: `docker ps` or `docker container ls`

- Delete container: `docker rm container_name`

- Force-delete container: `docker rm -f container_name` (useful if the container is still running)

- Delete image: `docker rmi image_name`

## Logs

Display container logs

```
docker logs container_name
```

Display container logs and follow them
```
docker logs -f container_name
```

## Exec

You can "go inside" a container using the exec command.
```
docker exec -it container_name bash
```
Note: `-it` stands for interactive

Exit with `CTRL-D`

## Docker Compose

Launch containers
```
docker-compose up
```
Launch containers and force rebuild
```
docker-compose up --build
```
Launch containers in detached mode
```
docker-compose up -d
```
Stop containers
```
docker-compose down
```
List containers
```
docker-compose ps
```

# Aller plus loin

## Images de base

La première ligne du Dockerfile est l'image de base. Elle peut indiquer le langage de programmation utilisé: Python, Golang, Java, Ruby. Elle peut spécifier la version de ce langage: python:3.8, python:3.7, python:3. Elle peut spécifier le système d'exploitation: buster, bullseye (deux versions de Debian), windowsservercore, alpine.

En particulier, [Alpine Linux](https://alpinelinux.org/about/) tourne exclusivement sur conteneur et est très populaire pour son poids léger (moins de 6 MB), sa simplicité et sa sécurité sans sacrifier sa capacité à être la base de la majorité des conteneurs livrés en production.

## Multi-stage builds

Chaque ligne d'un Dockerfile ajoute une couche à l'image. Il est possible de composer un Dockerfile avec plusieurs stages ou couches avec l'objectif de se débarrasser de couches temporaires, par exemple de dépendances, qui ne sont pas nécessaires à l'image finale. Typiquement, on distingue deux Dockerfiles; un pour une image en phase de développement contenant tous les outils nécessaires, un deuxième pour l'image de production livrée avec le strict minimum pour l'application de prod.

Exemple:
```
# first stage
FROM python:3.8 AS builder
COPY requirements.txt .

# Install dependencies required to compile Python packages
RUN apk add --no-cache libffi-dev musl-dev gcc

# install dependencies to the local user directory (eg. /root/.local)
RUN pip install --user -r requirements.txt

# second unnamed stage
FROM python:3.8-slim

# copy only the dependencies installation from the 1st stage image
COPY --from=builder /root/.local /root/.local
COPY ./src .

CMD [ "python", "./server.py" ]
```

https://docs.docker.com/develop/develop-images/multistage-build/

## Docker registry

Pour le moment, après avoir build nos images, nous avons simplement créé des conteneurs basés sur ces images. C'est tout à fait normal en phase de développement de build les images dans son environnement local afin de pouvoir ajuster le Dockerfile si besoin, ou encore build des images qui contiennent tous les outils de développement requis.

En revanche, dans un contexte de production, une fois que l'image a été optimisée et que son fonctionnement a été validé grâce aux tests d'intégration, la pratique la plus courante est de push cette image dans un registre d'images, puis de lancer des conteneurs à partir de ces images depuis l'environnement de production. Cela permet d'économiser du temps, des ressources pour build les images, et des mauvaises surprises dus à des build ratés.

Un des principaux registre d'images est [Dockerhub](https://hub.docker.com/), qui est pour la plus grande partie gratuit au "pull" et hôte la plupart des images les plus connues. Il existe des registres ciblant les professionnels tels que Artifactory, Nexus, AWS Elastic Container Registry, Google Container Registry ou il est encore possible de host son propre registre en utilisant Docker.

## Développer depuis un conteneur

Dans le but de développer les applications que l'on puisse faire tourner sur tous les environnements comme ceux de nos collègues ou ceux de production, il est possible, voire même recommandé, de développer directement depuis les conteneurs.

Cela est possible grâce principalement au partage de volume, qui permet de travailler sur des fichiers locaux rendus directement accessibles au conteneur dans le répertoire spécifié.
```
docker run -it --name python_dev -v $PWD:/app python:3.8-alpine /bin/sh
```

Développer directement depuis un conteneur est avantageux, car on ne va pas polluer son ordinateur avec des dépendances. Si l'on rate la configuration de son conteneur, on peut simplement le supprimer et recommencer.

Un tip supplémentaire est d'utiliser l'extension de Visual Studio Code qui s'appelle Remote - Containers. Elle permet d'ouvrir une fenêtre de l'IDE avec les fichiers du conteneur et des terminaux intégrés directement depuis son intérieur.
