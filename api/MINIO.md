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

Comme expliqué plus haut, Minio permet de stocker et de gérer des médias. 