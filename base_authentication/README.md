# Notions abordées dans ce chapitre

- Notion de clé étrangère (foreign key) dans une base de données ainsi qui sont implémentation en FastAPI
- Notion d'encodage et de décodage de token JWT (JSON WebToken)
- Systême d'authentification de base avec FastAPI

# Foreign Key

## Concept
Dans les bases de données relationnelles, la notion de clé étrangère est extrêmement importante.
Elle permet d'établir un lien entre deux tables et d'effectuer des opérations entre elles.
Le concept est très simple, dans la base de données, il faut simplement définir une colonne qui va indiquer une colonne dans une autre table.

Ici, nous étudions le cas de la clé étrangère (ForeignKey) qui permet de représenter une relation de "un à plusieurs" entre deux tables.
Il va nous permettre de lier plusieurs objets d'une table à un seul objet d'une autre table. 

Parmi les autres types de relation que l'on peut retrouver dans les bases de données relationnelles, on peut citer :
- La relation "un à un" : un objet d'une table est lié à un seul objet d'une autre table. Ce n'est qu'un cas particulier de la relation "un à plusieurs". Il existe alors une contrainte d'unicité sur la clé étrangère.
- La relation "plusieurs à plusieurs" : un objet d'une table est lié à plusieurs objets d'une autre table et vice versa. Pour cela, on utilise une table de jointure appelée Many To Many.

## Exemple

Reprenons notre application avec le model Post créé précedemment.
Voici la représentation écrite en python pour la table Post:
```
class Post(BaseSQL):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    created_at = Column(DateTime())
    updated_at = Column(DateTime())
```


Imaginons maintenant que l'on veuille savoir quel utilisateur de notre application a créé un post.
Nous aurons donc besoin d'un nouvel objet (table) User qui va contenir les informations de l'utilisateur.

```
class User(BaseSQL):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    created_at = Column(DateTime())
    updated_at = Column(DateTime())
```

Ainsi, nous pouvons sauvegarder les informations liés a nos utilisateurs.
Nous devons donc maintenant créer un lien entre ces deux tables.

Pour cela, nous allons ajouter une colonne `user_id` dans la table Post qui va contenir l'id de l'utilisateur qui a créé le post.

```
class Post(BaseSQL):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    created_at = Column(DateTime())
    updated_at = Column(DateTime())
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
```

Ainsi, nous avons créé une relation entre les tables Post et User.

Pour récupérer les informations de l'utilisateur qui a créé un post, il suffit de filter les posts par l'id de l'utilisateur.

```
user_posts = session.query(Post).filter(Post.user_id == user_id).first()
```

Il existe un moyen plus directe de récupérer les informations de l'utilisateur qui a créé un post en utilisant la méthode `relationship` de SQLAlchemy.

```
class Post(BaseSQL):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    created_at = Column(DateTime())
    updated_at = Column(DateTime())
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user = relationship("User", back_populates="posts")
```

En premier argument, on retrouve le nom de la table User et en second argument, le nom de l'attribut `backpopulates` qui désigne le nom
de l'attribut de l'objet User pour y retrouver tous ses posts.
On peut donc maintenant récupérer l'utilisateur depuis un `Post`

```
post = session.query(Post).filter(Post.id == post_id).first()
user = post.user
all_user_posts = user.posts
```

Ou bien 

```
user = session.query(User).filter(User.id == user_id).first()
user_posts = user.posts
```

# Authentication

Dans cette section, nous allons voir comment mettre en place un système d'authentification basique avec FastAPI.
A partir d'un login classique avec username et mot de passe, nous allons générer un Token JWT (JSON Web Token)
qui sera ensuite utilisé pour s'authentifier sur nos endpoints qui seront configurés en conséquence.
Chaque endpoint qui attend une authentification acceptera un header `Authorization`. La valeur de ce header commencera par le mot `Bearer` suivi du token.

```
Authorization: Bearer <xxx>
```


## JWT Token


Un JWT (JSON Web Token) est un moyen sécurisé d'échanger des informations entre deux parties.

Un tel token est constitué de trois parties : un header, un payload et une signature.

Le header contient des informations sur le type de token et l'algorithme de cryptage utilisé pour le signer (HMAC, RSA...).
Le payload contient les données que l'on veut transmettre (comme l'ID d'utilisateur, les rôles, etc.). Ces données peuvent être publiques ou privées.
Signature : C'est une sorte de vérification qui permet de s'assurer que le token n'a pas été modifié. Elle est créée en combinant le header, le payload et une clé secrète.

Voici un exemple de JWT Token

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoibW9uX2lkIn0.qIBDak2Hk554hDP0hgHfMeQmt-D74kV21qQiHQ7AIow
```

Les trois parties distinctes sont séparées par un `.`.

## Encodage et décodage de JWT Token

Pour encoder un JWT Token, on utilise une librairie qui va nous permettre de générer un token à partir d'un payload et d'une clé secrète.

``` python
import jwt
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "should-be-an-environment-variable")
JWT_SECRET_ALGORITHM = os.getenv("JWT_SECRET_ALGORITHM", "HS256")

def _encode_jwt(user: User) -> str:
    return jwt.encode(
        {
            "user_id": "mon_id",
        },
        JWT_SECRET_KEY,
        algorithm=JWT_SECRET_ALGORITHM,
    )
```

Il est fortement recommandé de stocker la clé secrète dans une variable d'environnement.

Pour décoder un JWT Token, on utilise la même librairie qui va nous permettre de vérifier la signature du token et de récupérer les données du payload.

``` python
def _decode_jwt(token: str) -> dict:
    return jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_SECRET_ALGORITHM])
```

Ainsi, un tier ne possédant pas la clé secrète ne pourra pas vérifier la signature d'un token, en créer un ou en décoder un.

Par contre, un JWT Token en tant que tel est facilement décodable et lisible par n'importe qui.
En effet, il s'agit simplement d'une concaténation d'information en base64.

Par exemple, on peut retrouver les informations encodées dans le token précédent en utilisant un décodeur en ligne (https://jwt.io/).

Lors de la création d'un token, on y associe généralement un temps d'expiration pour des raisons de sécurité.

## API endpoint avec authentification

Nous devons maintenant configurer nos endpoints pour recevoir un JWT Token, vérifier son intégrité et autoriser l'accès aux ressources.

Pour cela, nous allons utiliser une dépendance FastAPI qui va nous permettre de vérifier la validité du token.

```python
from fastapi.security import HTTPBearer

security=HTTPBearer()

@router.get("/{post_id}", dependencies=[Depends(security)], tags=["posts"])
async def get_post_by_id(post_id: str, request: Request, db: Session = Depends(models.get_db)):
    auth_header  = request.headers.get("Authorization")

    token = verify_autorization_header(auth_header)

    post = posts_service.get_post_by_id(post_id=post_id, db=db)

    if str(post.user_id) != token.get("user_id"):
        raise HTTPException(status_code=403, detail=f"Forbidden {post.user_id} {token.get('user_id')}")

    return post
```

Pour une simple authentification, FastAPI nous fournit une dépendance `HTTPBearer` qui va nous permettre de vérifier la présence d'un token dans le header `Authorization`.
Vous verrez apparaitre un petit cadenas à côté de l'endpoint pour indiquer qu'il est sécurisé.

![img.png](img.png)

Pour s'authentifier, il suffit de générer un token et de l'envoyer dans le header `Authorization` de la requête HTTP.
La documentation de l'API vous offre un bouton pour tester l'endpoint avec un token.
En cliquant sur le cadenas, vous verrez une fenêtre s'ouvrir pour vous permettre de rentrer un token.

![img_1.png](img_1.png)

Il nous faut désormais décoder ce token pour vérifier l'identité de l'utilisateur.
Voici un exemple de fonction qui va nous permettre de vérifier le token.

```python
def verify_autorization_header(access_token: str):
    if not access_token or not access_token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="No auth provided.")

    try:
        token = access_token.split("Bearer ")[1]
        auth = jwt.decode(
            token, JWT_SECRET_KEY, JWT_SECRET_ALGORITHM
        )
    except jwt.InvalidTokenError as err:
        raise HTTPException(status_code=401, detail=f"Invalid token.")

    return auth
```

Ainsi, nous avons mis en place un système d'authentification basique avec FastAPI. 
Toutes les requêtes vers les endpoints sécurisés devront être accompagnées d'un token valide. Sinon la requete sera rejetée
