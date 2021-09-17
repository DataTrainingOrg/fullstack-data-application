# Docker

- [Docker](#docker)
  - [Créer une image](#créer-une-image)
  - [Créer un conteneur](#créer-un-conteneur)
  - [Logs](#logs)
  - [Exec](#exec)
  - [Docker compose](#docker-compose)
  - [Exercices](#exercices)
- [Aller plus loin](#aller-plus-loin)
  - [Images de base](#images-de-base)
  - [Multi-stage builds](#multi-stage-builds)
  - [Docker registry](#docker-registry)
  - [Développer depuis un conteneur](#développer-depuis-un-conteneur)
  - [Kubernetes](#kubernetes)

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

## Kubernetes

Kubernetes est une technologie open-source de la CNCF - Cloud Native Computing Foundation - originellement créée par Google et dont la première release a été sortie en Juin 2014. C'est une technologie phare du cloud grâce à ces caractéristiques suivantes:

- Resource pooling: la mise en commun des ressources et leur management à partir d'un point central permet de mettre à disposition sa flotte de serveurs pour son grand nombre de conteneurs.
- Resource packing: la capacité d'attribuer les ressources nécessaires aux conteneurs selon leurs besoins
- Elasticité et ténacité (self-healing): la capacité de mettre en échelle, scaler le nombre de conteneurs, détecter lesquels sont unhealthy et défaillants et les remplacer
- Rollout et rollbacks et automatiques: de manière progressive et contrôlée, les nouveaux conteneurs avec une plus récente version du code peuvent être deployés tandis que les existants sont mis hors service puis supprimés. S'il s'avère que les nouveaux conteneurs ne fonctionnent pas, les anciens sont remis en service.

C'est une technologie extrêmement puissante et complexe à implémenter. Il est primordial d'en évaluer les avantages et désavantages en raison des barrières à l'entrée et au maintien.

https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/