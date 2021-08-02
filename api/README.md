# Backend

## Pourquoi ?

Pourquoi créer une API

## Différents types
### REST

REST est un ensemble de contraintes architecturales. Il ne s'agit ni d'un protocole, ni d'une norme. Les développeurs d'API peuvent mettre en œuvre REST de nombreuses manières.

Lorsqu'un client émet une requête par le biais d'une API RESTful, celle-ci transfère une représentation de l'état de la ressource au demandeur ou point de terminaison. Cette information, ou représentation, est fournie via le protocole HTTP dans l'un des formats suivants : JSON (JavaScript Object Notation), HTML, XLT, Python, PHP ou texte brut. Le langage de programmation le plus communément utilisé est JSON, car, contrairement à ce que son nom indique, il ne dépend pas d'un langage et peut être lu aussi bien par les humains que par les machines. 

Autre point à retenir : les en-têtes et paramètres jouent également un rôle majeur dans les méthodes HTTP d'une requête HTTP d'API RESTful, car ils contiennent des informations d'identification importantes concernant la requête (métadonnées, autorisation, URI, mise en cache, cookies, etc.). Il existe des en-têtes de requête et des en-têtes de réponse. Chacun dispose de ses propres informations de connexion HTTP et codes d'état.

Une API RESTful doit remplir les critères suivants :

    - Une architecture client-serveur constituée de clients, de serveurs et de ressources, avec des requêtes gérées via HTTP
    - Des communications client-serveur stateless, c'est-à-dire que les informations du client ne sont jamais stockées entre les requêtes GET, qui doivent être traitées séparément, de manière totalement indépendante
    - La possibilité de mettre en cache des données afin de rationaliser les interactions client-serveur
    - Une interface uniforme entre les composants qui permet un transfert standardisé des informations Cela implique que :
        - les ressources demandées soient identifiables et séparées des représentations envoyées au client ;
        - les ressources puissent être manipulées par le client au moyen de la représentation reçue, qui contient suffisamment d'informations ;
        - les messages autodescriptifs renvoyés au client contiennent assez de détails pour décrire la manière dont celui-ci doit traiter les informations ;
        - l'API possède un hypertexte/hypermédia, qui permet au client d'utiliser des hyperliens pour connaître toutes les autres actions disponibles après avoir accédé à une ressource.
    - Un système à couches, invisible pour le client, qui permet de hiérarchiser les différents types de serveurs (pour la sécurité, l'équilibrage de charge, etc.) impliqués dans la récupération des informations demandées
    - Du code à la demande (facultatif), c'est-à-dire la possibilité d'envoyer du code exécutable depuis le serveur vers le client (lorsqu'il le demande) afin d'étendre les fonctionnalités d'un client 

Bien que l'API REST doive répondre à l'ensemble de ces critères, elle est considérée comme étant plus simple à utiliser qu'un protocole tel que SOAP (Simple Object Access Protocol), qui est soumis à des contraintes spécifiques, dont la messagerie XML, la sécurité intégrée et la conformité des transactions, ce qui le rend plus lourd et moins rapide.
 
### WebSocket
L'API WebSocket est une technologie évoluée qui permet d'ouvrir un canal de communication bidirectionnelle entre un navigateur (côté client) et un serveur. Avec cette API vous pouvez envoyer des messages à un serveur et recevoir ses réponses de manière événementielle sans avoir à aller consulter le serveur pour obtenir une réponse.


## FastAPI
Asynchrone
REST + WebSocket
Autodocumentation

### Introduction

## Autres frameworks

- Django
- Flask
- Tornado

### Les différences ?

### Exemples de codes
