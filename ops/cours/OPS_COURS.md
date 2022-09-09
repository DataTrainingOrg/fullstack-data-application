# Operations

- [Operations](#operations)
  - [Histoire du déploiement](#histoire-du-déploiement)
    - [Bare-metal](#bare-metal)
    - [Machines virtuelles](#machines-virtuelles)
    - [Conteneurs](#conteneurs)
  - [Histoire du développement](#histoire-du-développement)
    - [Développement en cascade](#développement-en-cascade)
    - [Méthode agile](#méthode-agile)
    - [Approche DevOps](#approche-devops)
    - [Première conclusion](#première-conclusion)
  - [Mutable and immutable infrastructures](#mutable-and-immutable-infrastructures)
    - [Infrastructure mutable](#infrastructure-mutable)
    - [Infrastructure immuable](#infrastructure-immuable)
    - [Deuxième conclusion](#deuxième-conclusion)
  - [Horizontal and vertical scaling](#horizontal-and-vertical-scaling)
    - [Scaling vertical](#scaling-vertical)
    - [Scaling horizontal](#scaling-horizontal)
    - [Troisième conclusion](#troisième-conclusion)

## Histoire du déploiement

### Bare-metal

Généralement dans un data center, une machine physique qui n'appartient qu'à un seul tenant, ou locataire en français, qui n'a pas à partager de ressources avec quiconque. 

Les avantages sont la sécurité et l'exploitation de toutes les ressources. Les désavantages sont le coût élevé, le temps de mise en service, les risques des défaillances hardware et la difficulté d'upgrade.

### Machines virtuelles 

Une couche hyperviseur installée sur le hardware ou un OS, aussi appelée moniteur de machine virtuelle, permet de créer et manager des machines virtuelles. 

Les avantages sont la capacité d'avoir plusieurs machines simultanément, la configuration virtuelle du réseau et l'utilisation améliorée des ressources, la solidité face aux pannes grâce aux sauvegardes. Les désavantages sont le coût relativement élevé des licences, le besoin en ressources de chaque machine et son OS, long temps de mise en marche. 

### Conteneurs

Partant du principe de virtualisation et d'isolation des machines virtuelles, les conteneurs tournent sur l'OS de l'hôte tout en étant isolés les uns des autres. Le conteneur runtime, tel que ceux de Docker et containerd, permet aux conteneurs de fonctionner. Il n'y pas (presque) pas de dépendance vis-à-vis de l'OS. 

Les avantages sont le poids des images et conteneurs, la rapidité de mise en marche, la faible consommation en ressources, le fonctionnement sur tous les OS, le découplage des applications qui sont des pièces indépendantes, et enfin et surtout la compatibilité avec les philosophies Agile et DevOps. Les désavantages sont la barrière d'apprentissage, le besoin parfois de convertir son code et ses déploiements existants, le manque parfois d'un OS traditionnel et... l'avancé technologique rapide nécessitant d'être régulièrement à jour.

## Histoire du développement

### Développement en cascade

Les étapes sont la liste des besoins, le design, l'implémentation, la vérification et la maintenance. Comme le monde n'est pas parfait et que la vie est injuste, la combinaison d'une part d'un cycle de développement long et d'autre part de multiples développeurs travaillant en même temps font que cette approche est obsolète dans le contexte technologique actuel.

### Méthode agile

A l'origine un [manifeste](http://agilemanifesto.org/) décrivant les valeurs et principes à prioriser dans le développement de logiciels. Les cycles de développement sont courts (2 semaines) et des évènements particuliers permettent d'améliorer le flow de développement:
- sprint planning: définition et priorisation des tâches à réaliser durant le sprint actuel
- daily standup: debrief quotidien du status des tâches actuelles et à venir, ainsi que des points bloquants.
- demo: démonstration des tâches réalisées et retours sur celles-ci
- retrospective: identification des points d'amélioration pour les sprints futurs

En terme de développement, l'agilité est synonyme de livraison continue du code ou CI, continuous integration. Livrer de manière itérative du code de qualité nécessite des bonnes pratiques de planification, de test et de peer review. 

### Approche DevOps

Le DevOps est une méthode et philosophie organisationnelle avec pour but d'accélerer le cycle de vie d'une idée jusqu'à sa livraison en production. En terme de développement, cela est permis grâce au CI et au CD - continuous delivery (and deployment).

### Première conclusion

Les conteneurs permettent de packager les applications dans des environnements identiques, de la machine locale de développement, en passant par l'environnement de staging, jusqu'à l'environnement de production. Cette capacité permet de répondre aux besoins Agile et DevOps de CI/CD sur des cycles courts.

## Mutable and immutable infrastructures

Les infrastructures mutable et immuable sont aussi connues sous l'expression 'pets vs cattle' - animaux vs troupeau. 

### Infrastructure mutable

L'infrastructure mutable signifie qu'au long de sa vie, une machine virtuelle par exemple sera créée, lancée, configurée avec des applications, puis elle sera patchée régulièrement, son OS sera mis à jour quelques fois, les applications seront mises à jours elles aussi, et enfin elle est décomissionnée. Ce cycle est généralement long et nécessite des interventions souvent manuelles et ponctuelles.

### Infrastructure immuable

L'infrastructure immuable typique consiste à créer des machines avec une version d'un OS, une version d'une application et des ressources fixes, et de les lancer. Dès qu'une mise à jour est requise, de nouvelles machines sont créées avec les versions désirées, mises en marche et remplacent les précédentes machines, qui sont supprimées.

Le fait de ne pas changer la configuration dans l'infrastructure immuable à comme avantage de rendre le déploiement simple, fiable et cohérent au fil du temps et mises à jour. Le risque de faire une mise à jour sur une machine, et surtout de ne pas la documenter est de causer un configuration drift, ou décalage de configuration par rapport à l'état initial ou documenté. 

### Deuxième conclusion

Avec le cloud à grande échelle, l'approche immuable est préférée, voire parfois même la seule option possible. Il n'est pas envisageable de manager chaque instance de sa flotte de machines, mais il est possible de développer et déployer les applications de manière à ce qu'elles soient 'cloud native'.

Les conteneurs sont simples et rapides à livrer, lancer et disposer. Combinés avec un orchestrateur tel que Kubernetes, ils sont capables de répondre aux problématiques du cloud.

## Horizontal and vertical scaling

### Scaling vertical

Cela signifie que pour répondre à une augmentation croissante du trafic d'une application, en terme de nombre d'utilisateurs, la réponse est d'augmenter les ressources de la machine qui héberge l'application. Par exemple, en augmentant le nombre de CPUs, en ajoutant de la RAM et du stockage. C'est une solution simple, en particulier avec une architecture muable. Un défaut majeur est que les ressources nouvellement attribuées ne sont pas simples à récupérer tant que la machine est en marche, et selon l'application, il n'est pas garanti qu'ajouter des ressources aide.

### Scaling horizontal

Cette approche va répondre à une demande croissante en ajoutant des machines qui hébergent une même application, avec combiné à cela une redirection du trafic afin qu'il soit réparti parmi les machines de la flotte. Une fois que le trafic retourne à la normale, la pratique est de supprimer les machines supplémentaires afin de redistribuer les ressources à la pool commune.

### Troisième conclusion

Quand l'application le permet, la pratique répandue est le scaling horizontal, qui est particulièrement bien adapté à une infrastructure immuable. Toutefois, s'il ne suffit pas, il est envisageable d'augmenter les ressources des machines créées puis de les déployer horizontalement.
