# Architecture d'une API 

Structuration d'une API

### Les méthodes

Les méthodes sont comme la grammaire de communication d'une API avec le reste du monde.  Lorsque l'on communique avec quelqu'un et qu'on souhaite recevoir quelque chose de cette personne, il faut précisier si on a besoin d'une information, qu'on veut lui transmettre quelque chose ou revenir sur ce qu'on s'est dit précédemment. 
Les méthodes nous permettent de faire cela avec les APIs:  

- GET : permet de demander une ressource au serveur
- POST : permet d'envoyer et (souvent) de créer une ressource coté serveur
- PUT/PATCH: permettent de modifier tout ou partie d'une ressource
- DELETE : permet de supprimer une ressource

FastAPI met à disposition des décorateurs qui permettent de définir ces méthodes.

```python
@router.get("/{id}", tags=["posts"])
@router.post("/", tags=["posts"])
@router.put("/{id}", tags=["posts"])
@router.delete("/{id}", tags=["posts"])
```

La combinaison de ces méthodes avec le path des routes vers celles-ci permettent de structurer une API. 

### Path

Le path est le chemin qui permet d'accéder à une ressource. Il est très important de bien structurer ce chemin d'accés pour garder une certaine cohérence et compréhension du fonctionnement. 

Dans FastAPI c'est très simple il suffit de définir pour chaque méthode vu plus haut, la string permettant d'accéder aux ressources.

```python
@router.get("/users", tags=["users"])
```

permettrait de récupérer l'ensemble des utilisateurs.

```python
@router.get("/user/{user_id}")
```

permettrait de récupérer l'utilisateur spécifique correspondant à l'id. 

```python
@router.get("/user/{user_id}/posts/", tags=["posts"])
```

permettrait de récupérer l'ensemble des posts d'un utilisateur.
Et si on combine avec la méthode POST


```python
@router.post("/user/{user_id}/posts", tags=["posts"])
```

permettrait de créer un nouveau post pour cet utilisateur.

Ce chemin est équivalent au chemin utilisé par le navigateur web pour naviguer sur un site web. 

- https://www.lemonde.fr/ : La page de garde
- https://www.lemonde.fr/economie-mondiale/ : On accède à une catégorie spécifique du site. 
- https://www.lemonde.fr/argent/article/2021/09/06/bourse-est-ce-le-moment-d-investir-sur-les-marches-emergents-notamment-chinois_6093537_1657007.html : on accède à un a un article spécifique dans une catégorie déterminée. 

## Routes
Les routes représente la structure globale de l'api. Elles définissent l'interface de communication et l'interface d'interaction avec votre application. Ces routes utilisent les deux concepts vu plus haut, c'est la combinaisaon d'un chemin et d'une méthode.  

Très souvent on peut retrouver des routes de base qui répondent au principe CRUD. 

CRUD (create, read, update, delete) (créer, lire, mettre à jour, supprimer) est un acronyme pour les façons dont on peut fonctionner sur des données stockées. 
C'est un moyen mnémotechnique pour les quatre fonctions de base du stockage persistant. CRUD fait généralement référence aux opérations effectuées dans une base de données ou un magasin de données, mais peut également s'appliquer aux fonctions de niveau supérieur d'une application telles que les suppressions logicielles lorsque les données ne sont pas supprimées mais marquées comme supprimées via un état.

Ici on peut définir les routes permettant de réaliser ces opérations CRUD sur nos Posts.

```python
@router.post("/posts", tags=["posts"])
async def create_post(**kwargs):
   pass  
```
Permet de créer un nouveau post grâce à la méthode POST

```python
@router.get("/posts", tags=["posts"])
async def get_posts(**kwargs):
    pass
```

Ici on utilise la méthode GET sur le même path qui nous permet de récupérer l'ensemble des posts.

```python
@router.get("/posts/{post_id}", tags=["posts"])
async def get_post_by_id(post_id: str, **kwargs):
    pass
```

Permet de récupérer le post précédemment créé grace à son id. Vous voyez aussi, que le template du path permet de récupérer l'id du post dans les paramètres de la fonction, et donc de l'utiliser directement dans le code. 
```python
@router.put("/posts/{post_id}", tags=["posts"])
async def update_post_by_id(post_id: str, **kwargs):
    pass
```

Permet de mettre à jour un post grâce son id.

```python
@router.delete("/{post_id}", tags=["posts"])
async def delete_post_by_id(post_id: str, **kwargs):
    pass
```

Et ici de le supprimer.

## La gestion des données

Afin de gérer la création, la consultation et la mise à jour des données il faut mettre en correspondance les routes à des méthodes permettant de récupérer et stocker les données. 

Il y a de nombreuses manières de communiquer de la données avec l'API. 

- Path parameters
- Query paramters
- Request Body


## Schemas
Les schémas sont un moyen de garantir la validité des données utilisées par l'application. Les données provenant des utilisateurs sont souvent incomplètes ou ne correspondent pas aux attentes de votre application. Les schémas de données sont utilisés pour valider le bon format, le bon remplissage des champs de vos objets. 
Vous pouvez par exemple :
- Que l'age est bien un nombre entier compris entre 18 et 99 ans 
- Valider une adresse email
- Valider une adresse postale
- Valider la longueur d'un mot de passe 
- Que le mot de passe et la confirmation sont identiques
- La taille d'une chaine de characteres (comme sur Twitter)
- La présence obligatoire de la date de naissance dans un formulaire

Toutes ces validations, permettent de garantir une cohérence des données échangées. Ce format d'échange de données entre le front (les utilisateurs) et le back (votre application) ou entre deux backs avec une application tierce.
  
- Serialization (Load) : 
Permet de déterminer comment est ce que la donnée brute va être traitée par le schéma. La donnée brute est ingérée par le schéma, traitée par les règles définies et produit un objet Python utilisable. 
Certains champs ne pourront pas être modifié par l'utilisateur, par exemple l'identifiant géré par la base de données ou la date de création de l'objet seront souvent des champs qui seront impossible à modifier et qui seront ignorés par cette phase de serialisation.
- Deserialization (Dump)
La Déserialization permet de traduire un objet métier afin de le partager avec vos utilisateurs ou avec une application tierce. Cette phase permet de transformer des données pour les rendre interpretable par des utilisateurs exterieurs. 
Par exemple, cette phase est utilisée pour traduire des champs dans une certaine langue, transformer certains champs textuels pour les rendre plus propres, arrondir des nombres décimaux.


```python
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4
from typing_extensions import Annotated


class Post(BaseModel):
    id: Annotated[str, Field(default_factory=lambda: uuid4().hex)]
    title: str
    description: Optional[str]
    created_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]
    updated_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]

    class Config:
        orm_mode = True

 ```


## Base de données
Les différentes bases de données
- SQL 
Les principales bases de données SQL utilisées seront MySQL ou POSTGRESQL. Elles sont simples d'utilisation et les formats de données sont assez courant ce qui permet de trouver énormément de documentation sur la structuration des données. 
- NoSQL 
Les bases de données NoSQL sont très puissantes mais beaucoup plus complexes à gérer. Les modèles de données complexes sont plus fastidieux à mettre en place car elles utilisent des concepts différentes des habitudes de la plupart des gens. 

Pour créer les connexions à la base de données il faut : 

-> api/app/models/database.py
https://fastapi.tiangolo.com/tutorial/sql-databases/
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 


POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")


SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres/{POSTGRES_DB}"
print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

BaseSQL = declarative_base()

```

### Models
Le model est la structuration de la donnée d'un point de vue de la base de données. 
Les modèles sont plus ou moins figés ou complêtement dynamiques en fonction du type de base de données utilisé mais il reste un point essentiel pour structurer de manière méthodique les données qui vont être utilisées par l'application.


-> api/app/models/post.py
```python
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from .database import BaseSQL


class Post(BaseSQL):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    created_at = Column(DateTime())
    updated_at = Column(DateTime())

```

Pour créer la connexion avec la base de données, il nous faut définir les points d'accès que FastAPI par le biais de SQLAlchemy va utiliser pour `discuter` avec votre base de données. Pour cela il nous faut définir l'URL de connexion ainsi que les paramètres d'authentification. On créé un engine et une session, c'est ce qui nous permettra d'intéragire avec notre BDD.

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 


POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")


SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres/{POSTGRES_DB}"
print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

BaseSQL = declarative_base()
```

Lors de la première synchronisation avec la base de données, SQLAlchemy doit pouvoir créer le schéma de données en base. C'est à dire créer les tables et les colonnes avec les types correspondants. Pour cela nous devons appeler une méthode à l'initiation de FastAPI.

```python
from .models import BaseSQL

@app.on_event("startup")
async def startup_event():
    BaseSQL.metadata.create_all(bind=engine)
```

Ici on utilise une méthode asynchrone qui est triggered avec un evenement `startup` envoyé par FastAPI à son instanciation. Cette méthode permet donc de créer si il n'existe pas le format de données dans la base de données PostgresSQL dans ce cas.

### Les services

La structuration sous forme de service permet de décorréler la partie base de données et schemas (donc données brutes) de la partie routes. 
Les services font le lien entre la partie gestion métier et la structuration de l'API. 

```python
from typing import List

from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
from .. import models, schemas


def get_post_by_id(post_id: str, db: Session) -> models.Post:
    record = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Not Found") 
    record.id = str(record.id)
    return record

``` 

Ici on peut définir une méthode qui nous permet de récupérer un post grâce à son identifiant unique. 
On peut en définir un second qui permet de créer un post grace aux données fournies en entrée.

```python
from typing import List

from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
from .. import models, schemas

def create_post(db: Session, post: schemas.Post) -> models.Post:
    record = db.query(models.Post).filter(models.Post.id == post.id).first()
    if record:
        raise HTTPException(status_code=409, detail="Already exists")
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    db_post.id = str(db_post.id)
    return db_post

```

On peut remarquer qu'ici l'entrée du service sera le schéma du Post envoyé par l'utilisateur. Ici le service récupère donc un objet Post déjà validé, propre et prêt à être utilisé. 


### Headers

Les headers sont des informations complémentaires envoyés par le protocol http. Votre navigateur envoie des informations au serveur du site duquel vous essayez d'accéder.  Si vous allez dans la console de Google Chrome et que vous allez dans l'onglet Network vous pouvez choisir une requête réalisée par votre navigateur. Vous pouvez ensuite regarder dans les headers, vous verez que Chrome envoie un nombre incalculable d'autres informations. Cela permet au site de réagir de la meilleure manière.

Pour récupérer ces headers dans FastAPI c'est très simple, vous ajoutez un paramètre à la  fonction de votre route. FastAPI va se charger d'aller chercher ce header directement pour vous.  

```python

@app.get("/api/headers")
def read_headers(x_userinfo: Optional[str] = Header(None), ):
    pass
```

Souvent les headers possèdent des tirets, pour que Python puisse utiliser cette variable il faut juste lui préciser de transformer ces tirets en underscores.
```python

@app.get("/api/headers")
def read_headers(x_userinfo: Optional[str] = Header(None,  convert_underscores=True), ):
    pass
```

### Les codes HTTP
#### Les succés
- 200 : OK - Requête traitée avec succès. La réponse dépendra de la méthode de requête utilisée. 
- 201 : CREATED - Requête traitée avec succès et création d’un document.
- 202 : ACCEPTED - Requête traitée, mais sans garantie de résultat.

Ces codes de succès peuvent être utilisés dans plusieurs cas différents. Pour la création d'un objet, sa mise à jour ou même le succès de sa suppression. 
Ces codes sont là pour communiquer de façon simple avec l'exterieur, ils permettent de savoir très rapidement si l'action qui vient d'être demandé à été exécuté avec succès. 

#### Les erreurs
	
- 400 : Bad Request - La syntaxe de la requête est erronée.
Par exemple il manque des données dans le formulaire, le schéma après sa validation va renvoyer directement une erreur 400 car les données sont éronées. 
- 401 : Unauthorized - Une authentification est nécessaire pour accéder à la ressource.
Si l'utilisateur essaye d'accéder à une ressource sans être connecté. 
- 402 : Payment Required - Paiement requis pour accéder à la ressource.
Si l'utilisateur essaye d'accéder à une ressource payant de votre application
- 403 : Forbidden - Le serveur a compris la requête, mais refuse de l'exécuter.
Si l'utilisateur essaye d'accéder à une ressource qu'il n'a pas le droit de modifier ou de consulter.
- 404 : Not Found -	Ressource non trouvée.
Cette erreur est la plus connue, elle permet de déterminer qu'une ressource n'est pas disponible, cela peut arriver pour plusieurs raisons. La page demandée n'existe pas ou à été supprimée, l'item demandé peut être en rupture ou plus disponible sur un site e-commerce.  
- 405 : Method Not Allowed - Méthode de requête non autorisée. 
Quand on essaye de réaliser une méthode spécifique qui n'est pas autorisée. Par exemple un DELETE sur une route qui n'accepte que les GET ou les POST, le serveur renverra une erreur 405. Le serveur accepte les demandes à cette adresse mais pas ce type de demandes. 
- 408 :	Request Time-out - Temps d’attente d’une requête du client, écoulé côté serveur.
- 409 : Conflict - La requête ne peut être traitée en l’état actuel. 
Ces erreurs peuvent survenir quand un item existe déjà par exemple. 

Avec FastAPI c'est très simple de renvoyer une erreur spécifique en fonction de ce que l'on souhaite communiquer. Il suffit de raise une erreur Python avec le code et le détail. 

```python
from fastapi import HTTPException

already_exists = True 

if already_exists:
    raise HTTPException(status_code=409, detail="Already exists")
else:
    raise HTTPException(status_code=404, detail="Not Found")
```

https://fastapi.tiangolo.com/tutorial/handling-errors/

### Middlewares

https://fastapi.tiangolo.com/tutorial/middleware/

Les Middlewares sont des briques logicielles utilisées pour effectuer des opérations en entrée ou en sortie de l'API. Ils permettent de gérer les erreurs, de gérer l'authentification des utilisateurs, d'empecher des intrusions. 

### Background Tasks

https://fastapi.tiangolo.com/tutorial/background-tasks/
Les backgrounds tasks permettent de réaliser des tâches gourmandes en ressources qui peuvent attendre.