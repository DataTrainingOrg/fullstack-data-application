# Apprendre Docker

- [Apprendre Docker](#apprendre-docker)
  - [Dockerfile et image](#dockerfile-et-image)
  - [Docker container](#docker-container)
  - [Docker Compose](#docker-compose)
    - [Commandes de base](#commandes-de-base)
    - [Communication entre les conteneurs](#communication-entre-les-conteneurs)
- [Aller plus loin](#aller-plus-loin)
  - [Images de base](#images-de-base)
  - [Multi-stage builds](#multi-stage-builds)
  - [Docker registry](#docker-registry)
  - [Développer depuis un conteneur](#développer-depuis-un-conteneur)
  - [Kubernetes](#kubernetes)

## Dockerfile et image

Le Dockerfile définit l'environnement de l'application:
- l'image de base avec le nom puis le tag/la variante:  `FROM ubuntu:latest`, `FROM python:3.8`, `FROM node:alpine`
- la préparation de l'environnement avec des commandes à exécuter: `RUN pip install -r requirements.txt`, `RUN npm install`, `RUN apt install`, `RUN rm -rf`
- la choix du répertoire de travail: `WORKDIR /app`, `WORKDIR /home`
- la copie de fichiers locaux vers le futur conteneur: pour copier tout le répertoire local dans le répertoire `WORKDIR` on peut utiliser `COPY . .`, `COPY requirements.txt /app`
- les variables d'environnement: `ENV NODE_ENV=production`, `ENV PORT=8080`
- l'exposition de ports: `EXPOSE 8080`, `EXPOSE 5000 4000 3000`
- les commandes à lancer lors du démarrage du conteneur:
  1. la commande par défaut: `ENTRYPOINT ["python"]`
  2. les arguments par défaut: `CMD ["file.py"]`

Pour build l'image, on utilise la commande `docker build`. Le paramètre `-t` spécifie le nom de l'image puis `:` de son tag, qui peut être la version de l'image, ou sa variante selon l'OS (debian, ubuntu, alpine,  windowsservercore). Le paramètre `.` spécifie le context du build, c'est-à-dire le répertoire context qui est nécessaire aux instructions de `COPY`. Le paramètre `-f` permet de spécifier un Dockerfile avec un nom et dans un répertoire spécifique.

Exemple de Dockerfile:
```
FROM python:3.8

WORKDIR /app

COPY . .

RUN apt update && apt install -y ca-certificates
RUN pip install -r requirements.txt

ENV PORT=8080

EXPOSE 8080

ENTRYPOINT ["python"]
CMD ["file.py]
```

Exemples de commandes de build:
```
docker build -t python_app .
docker build -t python_app:2.0 .
docker build -t python_app -f ../Dockerfile.different.name .
```

Pour lister les images:
```
docker images
docker image ls
```

Pour supprimer une image:
```
docker rmi image_name
docker image rm image_name
```

## Docker container

Une fois l'image du conteneur créée, on peut instancier un conteneur basé sur cette image. On utilise pour cela la commande `docker run`.
Les paramètres les plus répandus sont: 
- `-it`: interactive + tty permet apres le lancement du conteneur d'y ouvrir un terminal. En utilisant `-idt`, `-d` signifiant 'detached', il est possible de lancer un conteneur sans terminal, et qui passe directement en arrière-plan.
- `--name`: nom du conteneur. Plusieurs conteneurs ne peuvent pas partager un même nom.
- `-v`: volume(s) à partager. `$PWD:/app` veut dire que le répertoire local est monté sur le répertoire `/app` du conteneur. Créer, modifier et supprimer un fichier dans un des répertoires entraîne la même action dans l'autre. Par défaut, les conteneurs sont totalement isolés du système local, et leur stockage est éphémère et n'est pas conservé lorsque le conteneur est supprimé.
- `-p`: port(s) à forward. Le conteneur est isolé et pour pouvoir accéder à une application du conteneur tournant sur un certain port, il faut le rediriger vers le port de la machine locale. `8080:80` signifie que le port `80` du conteneur est redirigé vers le port `8080` de la machine locale.
- `--env`: une variable d'environnement qui sera exportée par le conteneur à son lancement. Par exemple `--env VAR1=value1`.
- `--env-file`: un fichier de variables d'environnement. Par exemple `--env-file .env`.
- l'image du conteneur doit être spécifiée en avant-dernier ou dernier argument
- une commande peut être spécifiée pour le lancement du conteneur. Par exemple, utiliser `/bin/sh` devrait toujours fonctionner et permettre d'ouvrir un terminal.

Exemple:
```
docker run --name python_app -it -p 8080:8080 python_app
docker run --name python_app -it -p 8080:8080 python_app /bin/sh
docker run --name python_app -it -v $PWD:/home -p 8080:8080 -p 5000:5000 python_app
```

Pour lister les conteneurs actifs:
```
docker ps
docker container ls
```

Pour lister les conteneurs actifs et inactifs:
```
docker ps -a
docker container ls -a
```

Pour checker les logs du conteneur: `docker logs container_name`

Pour checker les logs continus du conteneur: `docker logs -f container_name`

Pour stopper un conteneur: `docker stop container_name`

Pour supprimer un conteneur: `docker rm container_name`

Pour supprimer un conteneur avec force, sans qu'il ait besoin d'être stoppé avant: `docker rm -f container_name`

Pour se rattacher à un conteneur, par exemple lorsque l'on a quitté le terminal du conteneur:
`docker attach container_name`

## Docker Compose

Docker Compose est un outil de Docker permettant d'orchestrer, de manager plusieurs conteneurs à la fois. C'est utile lorsque ces conteneurs forment ensemble une application et nécessitent de communiquer entre eux.

On peut citer deux méchanismes importants:
- facilement lancer et stopper les conteneurs qui forment l'application
- permettre la communication entre des conteneurs isolés

### Commandes de base

D'abord, voici un exemple d'une configuraiton `docker-compose.yml`:
```
version: "3.8"
services:
  api:
    build:
      context: ./api-example
    volumes:
      - ./api-example/:/app
    ports:
      - "5000:5000"
  frontend:
    build:
      context: ./frontend-example
    volumes:
      - ./frontend-example/:/app
    ports:
      - "8080:8080"
```

Paramètres de configuration:
- version: il existe plusieurs [versions de Docker Compose](https://docs.docker.com/compose/compose-file/compose-versioning/) que l'on peut spécifier. Certaines acceptent des paramètres de configuration, d'autres non.
- services: sous ce paramètre, on a une liste de conteneurs. Par défaut, ce sont les noms des conteneurs.
- par service: on retrouve des paramètres similaires au Dockerfile comme le port, le volume, les variables d'environnement. En plus de cela, le paramètre `build` permet de spécifier comment cette image doit être buildée; avec quel contexte, quel nom de Dockerfile. Si l'on utilise une image prébuildée, il est possible de spécifier `image` à la place de `build`.

Pour lancer le Docker Compose: `docker-compose up`
Pour lister les conteneurs du Docker Compose: `docker-compose ps`
Pour lancer le Docker Compose en arrière-plan: `docker-compose up -d`
Pour lancer le Docker Compose et rebuild les images: `docker-compose up --build`
Pour lancer le Docker Compose et rebuild l'image d'un conteneur en particulier: `docker-compose up --build api`
Pour stopper le Docker Compose: `docker-compose down`
Pour suivre les logs du Docker Compose: `docker-compose logs -f`
Pour relancer le Docker Compose: `docker-compose restart`
Pour ouvrir un terminal dans le container du Docker Compose: `docker-compose exec api /bin/sh`

### Communication entre les conteneurs

Comme les conteneurs sont tous isolés les uns des autres, il n'est pas possible de communiquer depuis une API avec une database comme on le fait en développement local, comme par exemple avec l'adresse `localhost:5432`. Docker Compose propose une fonctionnalité de DNS, Domain Name System, qui associe l'IP + le port d'un conteneur avec son nom. Ainsi, communiquer depuis le frontend avec la database se fait tout simplement avec `db`.

Il y a un exception pour le frontend client-side. Comme il est côté client, le navigateur ne peut par exemple pas comprendre `api` dont l'adresse est résolue par Docker Compose, mais pas par la machine locale. Du point de vue du navigateur, l'API est donc `localhost:5000`, et c'est cette adresse qu'il faut utiliser lors d'une requête faite depuis le frontend.

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