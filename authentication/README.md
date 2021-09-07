# Authentification

## SSO Qu'est ce que c'est ?

L'authentification unique, souvent désigné par le sigle anglais SSO (de single sign-on) est une méthode permettant à un utilisateur d'accéder à plusieurs applications informatiques (ou sites web sécurisés) en ne procédant qu'à une seule authentification.

### Objectifs
Les objectifs sont multiples :

simplifier pour l'utilisateur la gestion de ses mots de passe ;
simplifier la gestion des données personnelles détenues par les différents services en ligne, en les coordonnant par des mécanismes de type méta-annuaire ;
simplifier la définition et la mise en œuvre de politiques de sécurité.

### Avantages
Les avantages de l'authentification unique incluent :

la réduction de la fatigue de mot de passe : manque de souplesse liée à l'utilisation de différentes combinaisons de nom d'utilisateur et de mot de passe1 ;
la réduction du temps passé à saisir le même mot de passe pour le même compte ;
la réduction du temps passé en support informatique pour des oublis de mots de passe2 ;
la centralisation des systèmes d'authentification ;
la sécurisation à tous les niveaux d'entrée/de sortie/d'accès aux systèmes sans sollicitation multiple des utilisateurs ;
la centralisation des informations de contrôles d'accès pour les tests de conformités aux différentes normes.
Les technologies fournissant des SSO utilisent des serveurs centralisés d'authentification que tous les autres systèmes et applications utilisent pour l'authentification, combinant ceux-ci avec des techniques logicielles pour s'assurer que les utilisateurs n'aient pas à entrer leurs identifiants plus d'une fois.

### Critiques
Comme un SSO donne accès à de potentiellement nombreuses ressources une fois l'utilisateur authentifié (il a les « clés du château »), les pertes peuvent être lourdes si une personne mal intentionnée a accès à des informations d'identification des utilisateurs. Avec un SSO, une attention particulière doit donc être prêtée à ces informations, et des méthodes d'authentification forte devraient idéalement être combinées (par exemple, utilisation de cartes à puce, de clés de sécurité physique)


## Keycloak pourquoi ?

Keycloak est un logiciel à code source ouvert permettant d'instaurer une méthode d'authentification unique au travers la gestion par identité et par accès. Initialement développé par les équipes JBoss, le projet est depuis mars 2018 sous la gérance de Red Hat qui l'utilise en amont de sa solution RH-SSO1. Keycloak se définit comme une application rendant possible la sécurisation de n'importe quelle application web moderne avec un apport minimum en termes de code.

### Fonctionnalités
Keycloak inclut notamment les fonctionnalités suivantes :

- Inscription des utilisateurs
- Social login
- Authentification unique sur l'ensemble du "realm"
- Authentification en deux étapes
- Intégration Lightweight Directory Access Protocol (LDAP)
- Kerberos (protocole)
- Customisation des interfaces utilisateurs par un système de thème

## Client <> Users

Keycloak propose plusieurs concepts de base qu'il faut bien différencier. Les clients et les utilisateurs. 

### Utilisateurs

Les utilistateurs sont des personnes physiques souhaitant se connecter à une application. Lorsqu'ils vont tenter de se connecter à un site web, le site va directement renvoyer vers Keycloak afin de gérer la partie authentification. 

### Clients

Les clients sont des applications tierces qui utiliseront la solution Keycloak pour gérer leur utilisateurs. C'est la plupart du temps des applications back ou front qui sont authentifiées auprès de Keycloak et qui possèdent des droits spécifiques. En plus de ces droits, nous pouvons aussi restreindre les données utilisateurs auxquelles ces applications ont accès.

## Oauth2 et OIDC

### OAuth2

OAuth est un protocole libre qui permet d'autoriser un site web, un logiciel ou une application (dite « consommateur ») à utiliser l'API sécurisée d'un autre site web (dit « fournisseur ») pour le compte d'un utilisateur. OAuth n'est pas un protocole d'authentification, mais de « délégation d'autorisation ».

OAuth permet aux utilisateurs de donner, au site ou logiciel « consommateur », l'accès à ses informations personnelles qu'il a stockées sur le site « fournisseur » de service ou de données, ceci tout en protégeant le pseudonyme et le mot de passe des utilisateurs. Par exemple, un site de manipulation de vidéos pourra éditer les vidéos enregistrées sur Dailymotion d'un utilisateur des deux sites, à sa demande.

#### Mode de fonctionnement 

OAuth dans sa version 2.01 repose sur des échanges entre quatre acteurs. Le resource owner (utilisateur) est capable d’accorder l’accès à la ressource pour une application client. L’authorization server (serveur d’autorisation) occupe le rôle central au sein du protocole, il est chargé d’authentifier le resource owner et de délivrer son autorisation sous la forme d’un jeton appelé access token. Le resource server quant à lui correspond au serveur où sont stockées les ressources protégées2.

Lorsque l'application cliente souhaite demander une ressource à l'utilisateur, il envoie une requête au serveur d’autorisation composé à la fois d'une adresse URI de retour et d'un scope. Le scope définit le type et le périmètre des ressources demandées. Sur cette base, le serveur d’autorisation authentifie l'utilisateur et recueille son consentement pour la transmission de la ressource. Le serveur d’autorisation va envoyer un authorization code au client en paramètre de l'adresse URI de retour. Lorsque l'utilisateur se connecte à cette URI complétée de l'authorization code, le client renvoie l'authorization code au serveur d’autorisation pour se voir fournir un access token (jeton d'accès). Finalement, le client envoie le jeton d'accès au resource server pour obtenir les ressources de l'utilisateur.

Ce mécanisme3 de va-et-vient avec l'authorization code et jeton d'accès a plusieurs avantages :

il respecte une convention de type sécurité backend4. La machine cliente est jugée peu sécurisée. En cas d'interception des requêtes sur cette dernière, l'authorization code ne permet pas de récupérer les ressources de l'utilisateur. L'échange du jeton d'accès se fait par un canal contrôlé par les deux services professionnels.
Oauth permet ainsi aux développeurs, n'ayant pas de serveur avec certificat SSL proprement configuré, de faire appel à d'autres protocoles d'échange sécurisés que HTTPS pour l'échange du jeton d'accès.
Les jetons d'accès5 (comme les JSON Web Token par exemple) peuvent être signés par le serveur d’autorisation. Ils peuvent également contenir une date de péremption.

### OIDC

OpenID Connect (OIDC) est une simple couche d'identification basée sur OAuth 2.0, un dispositif d'autorisation1. Ce standard est géré par la fondation OpenID.

#### Description
OpenID Connect est une simple couche d'identification basée sur le protocole OAuth 2.0, qui autorise les clients à vérifier l'identité d'un utilisateur final en se basant sur l'authentification fournie par un serveur d'autorisation, en suivant le processus d'obtention d'une simple information du profil de l'utilisateur final. Ce processus est basé sur un dispositif interopérable de type REST. En termes techniques, OpenID Connect spécifie une interface HTTP RESTful, en utilisant JSON comme format de données.

OpenID Connect permet à un éventail de clients, y compris web, mobiles et JavaScript, de demander et recevoir des informations sur la session authentifiée et l'utilisateur final. Cet ensemble de spécifications est extensible, supporte des fonctionnalités optionnelles telle le chiffrement des données d'identité, la découverte dynamique de fournisseurs OpenID et la gestion de sessions2.

![test](identity_broker_flow.png)

## Exemple de France Connect

L'insee à notamment développé un package permettant aux utilisateurs de Keycloak d'utiliser la brique France connect pour s'authentifier.

https://github.com/InseeFr/Keycloak-FranceConnect
