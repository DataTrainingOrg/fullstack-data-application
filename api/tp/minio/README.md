```python
#!pip install minio
```

# Minio

## Use case

Minio est un gestionnaire distribué Open Source de stockage d'objets hautes performances. Minio permet donc de gérer des vidéos, des images, des documents pdfs par exemple. Minio est compatible et interfacable avec le système d'AWS de buckets. 

## Installation

avec docker

```
docker run \
   -p 9000:9000 \
   -p 9001:9001 \
   -e "MINIO_ROOT_USER=root" \
   -e "MINIO_ROOT_PASSWORD=rootpassword" \
   quay.io/minio/minio server /data --console-address ":9001"

```

avec `docker-compose.yml`


```
services:
  minio:
    container_name: minio
    image: quay.io/minio/minio
    ports:
        - 9000:9000
    environment:
      MINIO_ROOT_USER: root
      MINIO_ROOT_PASSWORD: rootpassword
    command: server /data
```

## Utilisation 

Comme expliqué plus haut, Minio permet de stocker et de gérer des médias. On peut 


```python
from minio import Minio
```

Pour se connecter et créer un client Minio il suffit de le configurer.


```python
client = Minio("localhost:9000", "root", "rootpassword", secure=False)
```

## Buckets

Les buckets sont la structure de base de stockage. Ils sont la notion la plus grossière, c'est le dossier parent. Les buckets permettent de stocker tout un ensemble de hiérarchie de fichiers.

### Créer et supprimer des buckets

Pour créer un bucket


```python
client.make_bucket("my-bucket")
```


```python
client.list_buckets()
```




    [Bucket('my-bucket'),
     Bucket('my-bucket1'),
     Bucket('my-bucket10'),
     Bucket('my-bucket2'),
     Bucket('my-bucket3'),
     Bucket('my-bucket4'),
     Bucket('my-bucket5'),
     Bucket('my-bucket6'),
     Bucket('my-bucket7'),
     Bucket('my-bucket8'),
     Bucket('my-bucket9')]



On ne peut pas créer deux buckets avec le même nom.


```python
client.make_bucket("my-bucket")
```


    ---------------------------------------------------------------------------

    S3Error                                   Traceback (most recent call last)

    <ipython-input-92-5082a41625e0> in <module>
    ----> 1 client.make_bucket("my-bucket")
    

    ~/anaconda3/lib/python3.8/site-packages/minio/api.py in make_bucket(self, bucket_name, location, object_lock)
        624             SubElement(element, "LocationConstraint", location)
        625             body = getbytes(element)
    --> 626         self._url_open(
        627             "PUT",
        628             location,


    ~/anaconda3/lib/python3.8/site-packages/minio/api.py in _url_open(self, method, region, bucket_name, object_name, body, headers, query_params, preload_content, no_body_trace)
        387             self._region_map.pop(bucket_name, None)
        388 
    --> 389         raise response_error
        390 
        391     def _execute(


    S3Error: S3 operation failed; code: BucketAlreadyOwnedByYou, message: Your previous request to create the named bucket succeeded and you already own it., resource: /my-bucket, request_id: 16A553E786AA3496, host_id: 1fd209d2-9d84-4231-8bf0-da6051d4978b, bucket_name: my-bucket


Pour supprimer un bucket, 


```python
client.remove_bucket("my-bucket")
```

Pour lister l'ensemble des buckets présents


```python
client.list_buckets()
```




    [Bucket('my-bucket1'),
     Bucket('my-bucket10'),
     Bucket('my-bucket2'),
     Bucket('my-bucket3'),
     Bucket('my-bucket4'),
     Bucket('my-bucket5'),
     Bucket('my-bucket6'),
     Bucket('my-bucket7'),
     Bucket('my-bucket8'),
     Bucket('my-bucket9')]




```python
for i in range(10): 
    client.make_bucket(f"my-bucket{i+1}")
```


    ---------------------------------------------------------------------------

    S3Error                                   Traceback (most recent call last)

    <ipython-input-24-98d1d3fa9b98> in <module>
          1 for i in range(10):
    ----> 2     client.make_bucket(f"my-bucket{i+1}")
    

    ~/anaconda3/lib/python3.8/site-packages/minio/api.py in make_bucket(self, bucket_name, location, object_lock)
        624             SubElement(element, "LocationConstraint", location)
        625             body = getbytes(element)
    --> 626         self._url_open(
        627             "PUT",
        628             location,


    ~/anaconda3/lib/python3.8/site-packages/minio/api.py in _url_open(self, method, region, bucket_name, object_name, body, headers, query_params, preload_content, no_body_trace)
        387             self._region_map.pop(bucket_name, None)
        388 
    --> 389         raise response_error
        390 
        391     def _execute(


    S3Error: S3 operation failed; code: BucketAlreadyOwnedByYou, message: Your previous request to create the named bucket succeeded and you already own it., resource: /my-bucket1, request_id: 16A54DC754BF6CCF, host_id: 1fd209d2-9d84-4231-8bf0-da6051d4978b, bucket_name: my-bucket1



```python
buckets = client.list_buckets()
for bucket in buckets:
    print(bucket.name, bucket.creation_date)
    #client.remove_bucket(bucket.name)
```

A l'instanciation il est souvent intéressant de vérifier qu'un bucket existe bien.


```python
if client.bucket_exists("my-bucket"):
    print("my-bucket exists")
else:
    print("my-bucket does not exist")
```

    my-bucket does not exist


### Objets

Les objets sont la structure la plus fine de stockage dans Minio. C'est un concept un peu différent des fichiers. Ils regroupent les fichiers ainsi que la structure de dossiers parents. 
Pour donner un exemple l'objet avec le nom `/dossier_parent/dossier_enfant/nom_de_lobjet` integrera aussi la création et le stockage dans les deux dossiers `dossier_parent` et ̀`dossier_enfant`. Pour gérer la structure de rangement des objets il faudra donc aussi jouer sur l'ensemble du chemin vers ce dernier.

On peut stocker n'importe quel fichier ou média dans minio. Une bonne pratique est de préciser le content type qui correspond au type de document stocké. Cela permet au client qui va lire ensuite ce document de savoir comment réagir, est ce que c'est un pdf ? Si oui, je dois l'afficher d'une certaine facon avec potentiellement plusieurs pages, est ce que c'est une video ? Si oui, je dois afficher un lecteur. 

### Ajouter des objets 


```python
import io
import requests
import urllib
```

#### Bytes


```python
result = client.put_object(
    "my-bucket", "my-bytes-object", io.BytesIO(b"hello"), 5,
)
```

#### Csv 


```python
url_velib = "https://www.data.gouv.fr/fr/datasets/r/0845c838-6f18-40c3-936f-da204107759a"

# Upload unknown sized data.
data = urllib.request.urlopen(url_velib)
result = client.put_object(
    "my-bucket", "velib-data", data, length=-1, part_size=10*1024*1024, content_type="application/csv",
)
```

Une image, on peut ajouter des métadatas. 


```python
image_url = "https://media.istockphoto.com/photos/couple-relax-on-the-beach-enjoy-beautiful-sea-on-the-tropical-island-picture-id1160947136?k=20&m=1160947136&s=612x612&w=0&h=TdExAS2--H3tHQv2tc5woAl7e0zioUVB5dbIz6At0I4="
# Upload unknown sized data.
data = urllib.request.urlopen(image_url)
result = client.put_object(
    "my-bucket", "image-plage", data, length=-1, part_size=10*1024*1024, content_type="image/jpeg",
    metadata={"description": "une belle plage"},
)
```


```python

```

### Exercices

1. Importer une vidéo 

### Lister des objets


```python
# List objects information.
objects = client.list_objects("my-bucket")
for obj in objects:
    print(obj, obj.object_name)
```

    <minio.datatypes.Object object at 0x7f6c47da48e0> image-plage
    <minio.datatypes.Object object at 0x7f6c47da4be0> my-bytes-object
    <minio.datatypes.Object object at 0x7f6c47da4c70> velib-data
    <minio.datatypes.Object object at 0x7f6c47da4c40> path_0/
    <minio.datatypes.Object object at 0x7f6c47da4bb0> path_1/
    <minio.datatypes.Object object at 0x7f6c47da4af0> path_10/
    <minio.datatypes.Object object at 0x7f6c47da4130> path_11/
    <minio.datatypes.Object object at 0x7f6c47da4e50> path_12/
    <minio.datatypes.Object object at 0x7f6c47da49d0> path_13/
    <minio.datatypes.Object object at 0x7f6c47da4fd0> path_14/
    <minio.datatypes.Object object at 0x7f6c47da4a30> path_15/
    <minio.datatypes.Object object at 0x7f6c47da47c0> path_16/
    <minio.datatypes.Object object at 0x7f6c479a6b20> path_17/
    <minio.datatypes.Object object at 0x7f6c479a6eb0> path_18/
    <minio.datatypes.Object object at 0x7f6c479a6190> path_19/
    <minio.datatypes.Object object at 0x7f6c479a6280> path_2/
    <minio.datatypes.Object object at 0x7f6c479a6640> path_20/
    <minio.datatypes.Object object at 0x7f6c479a68b0> path_21/
    <minio.datatypes.Object object at 0x7f6c479a6730> path_22/
    <minio.datatypes.Object object at 0x7f6c47d9e460> path_23/
    <minio.datatypes.Object object at 0x7f6c47d9e580> path_24/
    <minio.datatypes.Object object at 0x7f6c47d9e490> path_25/
    <minio.datatypes.Object object at 0x7f6c47ffd160> path_26/
    <minio.datatypes.Object object at 0x7f6c47ffd8b0> path_27/
    <minio.datatypes.Object object at 0x7f6c47ffd850> path_28/
    <minio.datatypes.Object object at 0x7f6c47ffdaf0> path_29/
    <minio.datatypes.Object object at 0x7f6c47ffd0d0> path_3/
    <minio.datatypes.Object object at 0x7f6c47ffd970> path_4/
    <minio.datatypes.Object object at 0x7f6c47ffd040> path_5/
    <minio.datatypes.Object object at 0x7f6c47ffd070> path_6/
    <minio.datatypes.Object object at 0x7f6c47ffd3d0> path_7/
    <minio.datatypes.Object object at 0x7f6c47ffd8e0> path_8/
    <minio.datatypes.Object object at 0x7f6c47ffd7c0> path_9/



```python
for i in range(30):
    for j in range(30):
        result = client.put_object(
            "my-bucket", f"path_{i}/my-bytes-object-{j}", io.BytesIO(f"hello {i} and {j}".encode()), 13,
        )
```

On peut lister l'ensemble des objets correspondants à un certain prefix


```python
# List objects information.
objects = client.list_objects("my-bucket", recursive=True)
for obj in objects:
    print(obj, obj.object_name)
```

    <minio.datatypes.Object object at 0x7f6c47becd30> image-plage
    <minio.datatypes.Object object at 0x7f6c47bec520> my-bytes-object
    <minio.datatypes.Object object at 0x7f6c47becf70> path_0/0-my-bytes-object
    <minio.datatypes.Object object at 0x7f6c5417bbb0> path_0/1-my-bytes-object
    ....
    <minio.datatypes.Object object at 0x7f6c46e318b0> velib-data



```python
objects = client.list_objects("my-bucket", prefix="path_10/")
for obj in objects:
    print(obj.object_name)
```

    path_10/0-my-bytes-object
    path_10/1-my-bytes-object
    path_10/10-my-bytes-object
    path_10/11-my-bytes-object
    path_10/12-my-bytes-object
    path_10/13-my-bytes-object
    path_10/14-my-bytes-object
    path_10/15-my-bytes-object
    path_10/16-my-bytes-object
    path_10/17-my-bytes-object
    path_10/18-my-bytes-object
    path_10/19-my-bytes-object
    path_10/2-my-bytes-object
    path_10/20-my-bytes-object
    path_10/21-my-bytes-object
    path_10/22-my-bytes-object
    path_10/23-my-bytes-object
    path_10/24-my-bytes-object
    path_10/25-my-bytes-object
    path_10/26-my-bytes-object
    path_10/27-my-bytes-object
    path_10/28-my-bytes-object
    path_10/29-my-bytes-object
    path_10/3-my-bytes-object
    path_10/4-my-bytes-object
    path_10/5-my-bytes-object
    path_10/6-my-bytes-object
    path_10/7-my-bytes-object
    path_10/8-my-bytes-object
    path_10/9-my-bytes-object
    path_10/my-bytes-object-0
    path_10/my-bytes-object-1
    path_10/my-bytes-object-10
    path_10/my-bytes-object-11
    path_10/my-bytes-object-12
    path_10/my-bytes-object-13
    path_10/my-bytes-object-14
    path_10/my-bytes-object-15
    path_10/my-bytes-object-16
    path_10/my-bytes-object-17
    path_10/my-bytes-object-18
    path_10/my-bytes-object-19
    path_10/my-bytes-object-2
    path_10/my-bytes-object-20
    path_10/my-bytes-object-21
    path_10/my-bytes-object-22
    path_10/my-bytes-object-23
    path_10/my-bytes-object-24
    path_10/my-bytes-object-25
    path_10/my-bytes-object-26
    path_10/my-bytes-object-27
    path_10/my-bytes-object-28
    path_10/my-bytes-object-29
    path_10/my-bytes-object-3
    path_10/my-bytes-object-4
    path_10/my-bytes-object-5
    path_10/my-bytes-object-6
    path_10/my-bytes-object-7
    path_10/my-bytes-object-8
    path_10/my-bytes-object-9


### Créer des URLS présigner 

Les méthodes précédentes sont très intéressantes pour communiquer entre une API et Minio. L'inconvéniant est que le média doit forcément passer par le serveur. Pour des raisons de performances réseaux, il est beaucoup plus intéressant d'utiliser les clients pour envoyer directement les données volumineuses.

Pour cela il faut permettre aux clients de s'authentifier directement sur Minio. Evidemment on ne peut pas donner aux clients (Les utilisateurs mobiles ou navigateurs les informations de connexion qui peuvent être stockés dans l'API), on utilisera alors des URLs présignés. Ces URLs un peu complexes à lire intègrent directement plusieurs informations permettant au client de s'authentifier. Pour des raisons de sécurité il est aussi important de rendre ces URLs inutilisable au bout d'un certain temps. Les clés générées sont à usage unique. 

Il faut alors créer des URLs présigner pour uploader des médias mais aussi pour y accéder. Ces URLs doivent être générés par l'API. Les clients doivent demander à l'API, "puis-je poster un média ?" ou "puis-je voir ce média ?" si la réponse est oui , alors l'API génère un URL qui peut ensuite être utilisé pour réaliser l'action.


```python
from datetime import timedelta
```

Pour envoyer un média


```python
put_url  = client.get_presigned_url(
    "PUT",
    "my-bucket",
    "my-object",
    expires=timedelta(days=1),
    response_headers={"response-content-type": "application/json"},
)
print(url)
```

    http://localhost:9000/my-bucket/my-object?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=root%2F20210916%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210916T132448Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=c98daa553660fc8b20424301f190d14c76506d7c3fe288728f66cb53630f0786



```python
import requests
```


```python
response = requests.put(put_url, json={"key":"value"})
response
```




    <Response [200]>



Pour lire un média.


```python
get_url = client.get_presigned_url(
    "GET",
    "my-bucket",
    "my-object",
    expires=timedelta(hours=2),
)
print(url)
```

    http://localhost:9000/my-bucket/my-object?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=root%2F20210916%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210916T132448Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=c98daa553660fc8b20424301f190d14c76506d7c3fe288728f66cb53630f0786



```python
response = requests.get(get_url)
response.json()
```




    {'key': 'value'}



## Intégration avec L'API 

Pour ajouter un fichier directement depuis l'API, on peut créer une route dans notre application FastAPI. Pour cela on doit utiliser le paramètre suivant `file: UploadFile = File(...)` dans la définition de la route. Si on se réfère à la documentation auto générée par FastAPI on peut directement upload un fichier grâce au bouton créé.

Dans le corps de la fonction définissant la route, on récupère directement le fichier. Il suffit ensuite de l'envoyer directement grâce au client Minio. 

`result = client.put_object('le nom de votre fichier', file.filename, file.file)`


par exemple : 

```
@app.post('/file/upload/')
async def upload_file(file: UploadFile = File(...)):
    result = client.put_object('le nom de votre fichier', file.filename, file.file)
    return {'result': result}
```

## Exercices API

1. Ajouter une route permettant d'uploader directement un fichier sur minio
2. Ajouter une route permettant de créer un URL présigné PUT
3. Ajouter une route permettant de récupérer un URL présigné GET en fonction d'un document
4. Ajouter une route permettant de lister l'ensemble des objets présents dans un bucket.
5. Ajouter un paramètre permettant de rendre ce listing reccursif. 
