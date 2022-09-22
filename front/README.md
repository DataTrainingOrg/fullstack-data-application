# Frontend

- [Frontend](#frontend)
  - [Langage JavaScript](#langage-javascript)
  - [Website rendering](#website-rendering)
    - [Server-side rendering](#server-side-rendering)
    - [Client-side rendering](#client-side-rendering)
  - [Frameworks](#frameworks)
    - [Client-side frameworks](#client-side-frameworks)
    - [Server-side frameworks](#server-side-frameworks)
  - [Consommation d'API](#consommation-dapi)
    - [Synchrone](#synchrone)
    - [Asynchrone](#asynchrone)
    - [Implémentation](#implémentation)
  - [Préparation](#préparation)
    - [JavaScript](#javascript)
    - [NodeJS](#nodejs)
      - [Environnement de développement](#environnement-de-développement)
      - [Execution du code](#execution-du-code)
    - [Frameworks](#frameworks-1)
      - [Server-side](#server-side)
      - [Client-side](#client-side)

## Langage JavaScript

Le langage de programmation principal du frontend moderne est le JavaScript. Il nécessite que le navigateur du client possède un moteur JavaScript capable d'exécuter le code. De nos jours, les principaux navigateurs ont tous un moteur JavaScript.

Le code JavaScript inclus dans les sites web permet d'enrichir l'expérience utilisateur, afin qu'il puisse interagir et en réponse voir le DOM être modifié. Le DOM est le Document Object Model et contrôle la structure, le style et le contenu de la page.

L'organisation ECMA est responsable de la standardisation du langage de programmation, et permet l'ajout de nouvelles features environ chaque année.

## Website rendering

En développement web, le rendering est le processus qui permet de transformer le code d'une page en une page visuelle et interactive. Il existe deux manières de procéder.

Un mot sur les sites statique et dynamique; un site est dit statique si tous les clients reçoivent un contenu identique, sans aucune personnalisation. Un site dynamique retourne des pages aux contenus différents pour ses utilisateurs, car une logique est appliquée aux pages avec, par exemple, des transformations des données du contenu qui sont personnalisées selon les utilisateurs.

### Server-side rendering

<br>![server-side-rendering](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Fetching_data/web-site-architechture@2x.png)

Le fonctionnement: le client veut visiter un site et fait la requête à son web server, puis le web server retourne le code du site dynamique entièrement généré au client. Lorsque le client clique sur un lien sur la page, il effectue une nouvelle requête et le serveur renvoie une nouvelle page entière au client.

### Client-side rendering

Le fonctionnement: le client veut visiter un site et fait la requête à son web server, puis le web server retourne le code du site non-généré, non-enrichi et en JavaScript au client, qui va render la page et l'enrichir dans son navigateur.

Le site client-side rendered peut lui-même requêter du nouveau contenu de manière continue, par exemple suite aux intéractions de l'utilisateur avec la page, et ce sans qu'il y ait besoin de rafraîchir la page toute entière.

## Frameworks

Les frameworks permettent d'améliorer l'expérience utilisateur, mais aussi développeur, en fournissant des implémentations afin de gérer l'interactivité dans les sites.

### Client-side frameworks

Les frameworks sont en JavaScript et les plus utilisés actuellement pour de nouveaux projets sont VueJS et ReactJS. Ils proposent des outils de développement facilitant de nombreuses tâches, comme par exemple le rafraîchissement automatique du site en cours de développement à chaque sauvegarde de code (hot reload). La popularité de ces frameworks fait que leur communauté est active et la plupart des questions ou problèmes que l'on rencontre ont déjà trouvé réponse.

### Server-side frameworks

Les plus utilisés sont Laravel en PHP, Ruby on Rails, et Django et Flask en Python. Ils utilisent des moteurs de templating pour pouvoir injecter de la logique de leur langage dans le contenu de la page HTML. L'intégration puissante du frontend et du backend présente un risque de couplage ou dépendance entre les deux parties. De nos jours, c'est une pratique déconseillée, on préfère exposer le backend sous forme d'APIs et consommer ces APIs depuis le frontend afin de découpler les deux parties.

## Consommation d'API

### Synchrone

L'exécution synchrone d'une requête API bloque le code en attendant que l'API retourne le résultat de la requête.

### Asynchrone

L'exécution asynchrone d'une requête API ne bloque pas le code suivant. Une fois la réponse retournée, une fonction de callback que l'on a définie auparavant est exécutée.

### Implémentation

En JavaScript, l'implémentation se fait avec le type `Promise` qui représente l'éventuelle complétion d'une opération asynchrone et sa valeur.
Une `Promise` a 3 états possibles: pending, fulfilled et rejected. Lorsque l'on définit soi-même une `Promise`, il faut préciser en cas de succès le `resolve()`, et en cas d'échec le `reject()`. 

Au moment d'appeler la fonction asynchrone, la syntaxe est d'appeler la `Promise`, puis `then` est la méthode qui retourne la `Promise`, et on lui spécifie comme argument la fonction de callback, qui sera exécutée en cas de succès. `catch` va de la même manière exécuter sa fonction de callback passée en argument en cas d'échec.

Voici un exemple de définition:
```
const done = true

const isItDoneYet = new Promise((resolve, reject) => {
  if (done) {
    const workDone = 'Here is the thing I built'
    resolve(workDone)
  } else {
    const why = 'Still working on something else'
    reject(why)
  }
})

const checkIfItsDone = () => {
  isItDoneYet
    .then(ok => {
      console.log(ok)
    })
    .catch(err => {
      console.error(err)
    })
}

checkIfItsDone()
```

Documentation:
- [promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [then](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)
- [catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)

## Préparation

### JavaScript

Le site de Mozilla offre une documentation référence de la syntax de JavaScript. Il est recommandé de consulter les pages suivantes:
- [courte introduction](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
- [guide du langage](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)

Implémentations principales:
- variables [const](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const) et [let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
- [fonction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions): on note qu'en JS, les arrow fonctions sont souvent utilisées comme versions courtes des fonctions traditionnelles, comme par exemple `() => {}` 
- [if/else](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#if...else_statement)
- [array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects#objects_and_properties)
- méthodes d'array: [map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map), [reduce](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce), [filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter), [forEach](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
- [callback/closure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#closures)
- [undefined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)

### NodeJS

Le site de NodeJS offre [documentation](https://nodejs.dev/learn/introduction-to-nodejs) de concepts tels que le fonctionnement de l'event loop, les promesses, et également une introduction au package manager par défaut de NodeJS `npm`. L'installation des packages se fait avec `npm install package_name`.

`yarn` est également un package manager connu créé par Facebook et qui peut être installé [de cette manière](https://classic.yarnpkg.com/en/docs/install#mac-stable). L'installation des packages se fait avec `yarn add package_name`.

#### Environnement de développement

NodeJS est utilisé pour développer en JavaScript sur son poste local. On peut installer un environnement NodeJS en utilisant Docker:
1. `docker pull node:alpine`
2. Depuis le terminal, naviguer dans le répertoire de travail
3. `docker run -it --name node_dev -v $PWD:/app -w /app -p 3000:3000 -p 8080:8080 node:alpine /bin/sh`

Il est aussi possible aussi d'utiliser un Dockerfile:
```
FROM node:alpine

WORKDIR /app

COPY . .

ENTRYPOINT ["/bin/sh"]
```

#### Execution du code

L'API fetch n'est pas incluse par défaut et il faut l'installer:
```
npm install node-fetch
```

Il faut créer un fichier `.js` avec le code suivant ([source](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)):
```
const fetch = require('node-fetch')

fetch('http://example.com/movies.json')
  .then(response => response.json())
  .then(data => console.log(data));
```

Puis exécuter le code:
```
node fichier.js
```

### Frameworks

#### Server-side

Les modules Python `flask` et `requests` doivent être installés avec `pip` ou `pipenv`. `requests` permet de faire les requêtes API.

Concernant le déploiement en production, la pratique est de placer un [WSGI](https://www.appdynamics.com/blog/engineering/an-introduction-to-python-wsgi-servers-part-1/) devant le serveur du framework Python. WSGI signifie Web Server Gateway Interface et a été introduit parce que dans le passé, les web servers ne pouvaient pas communiquer avec les serveurs Python, car ils ne comprenaient et ne pouvaient pas interpréter le langage. WSGI est uniquement capable de gérer des requêtes synchrones.

Quelques WSGI fréquemment utilisés: Gunicorn, uWSGI, Waitress, Bjoern.

ASGI - Asynchronous Server Gateway Interface - est un standard plus récent proposant une interface à la fois asynchrone et synchrone. Par exemple, une implémentation est [Uvicorn](https://www.uvicorn.org/).

#### Client-side

Les frameworks VueJS et ReactJS existent sous la forme de packages npm que l'on installe dans son environnement de développement.

- [Lien](https://cli.vuejs.org/guide/installation.html) pour installer VueJS, puis [lien](https://cli.vuejs.org/guide/creating-a-project.html#vue-create) pour créer le projet (on choisira les options proposées par défaut).
- [Lien](https://reactjs.org/docs/create-a-new-react-app.html#create-react-app) pour installer ReactJS et le projet

La création du projet génère répertoire du projet un fichier `package.json`. Il contient des metadatas sur le projet mais surtout des 'scripts', une liste de raccourcis pour lancer les commandes comme le lancement du site et le build du site pour la production.

Exemple pour Vue:
```
"scripts": {
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build",
    "lint": "vue-cli-service lint"
}
```
La commande `yarn serve` lance le site en mode dev. Le port par défaut est `8080`.

Exemple pour React:
```
"scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
}
```
La commande `yarn start` lance le site en mode dev. Le port par défaut est `3000`.

Il est maintenant possible de modifier le code Vue ou React, puis de sauvegarder afin que le serveur de développement update la page avec les changements.
