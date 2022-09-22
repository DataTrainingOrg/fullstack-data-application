# TP

## Goals

- Complete Docker setup
- Get familiar with Docker
- Learn some networking basics, i.e. exposing ports
- Learn some command-line basics, i.e. Linux navigation
- Learn about container orchestration

## Exercises

### Run basic Docker commands

1. Build and start the example image and container in the folder `./tp/api`. Some tips:
- expose the right ports. See [docs](https://docs.docker.com/config/containers/container-networking/#published-ports).
- container names are unique, so kill previously created ones before starting new ones
- use the `-d` parameter to start a container in detached mode
2. Request the container api using: 
- your browser
- the terminal command `curl`. See [docs](https://linuxize.com/post/curl-rest-api/). 
- an api request application like [Insomnia](https://insomnia.rest/) or [Postman](https://www.postman.com/downloads/)
3. Kill the container

### Create your own container

1. In `./tp/front`, build and start the container with port 8080 exposed
2. Browse `localhost:8080`
3. Open a shell in the container using: `docker exec -it`. See [docs](https://docs.docker.com/engine/reference/commandline/exec/#run-docker-exec-on-a-running-container).
4. Kill the container

### Container orchestration

1. Complete the `docker-compose.yml` in the `./tp` folder:
- expose port 8080 for the front container
- mount the local folder `./front` to the container folder `./app`
2. Start the docker compose
3. In `./tp/front`:
- in `app.py`, uncomment lines 6-11 and replace `API_URL` with the correct value
- in `./template/index.html`, add:
```
<p>API response: {{ request_api() }}</p>
```
4. Browse the front application and check that it can request the api
5. Change the HTML in `./template/index.html` with anything you want and browse the webpage again
6. Open a shell in one of the containers using `docker compose exec`.

Note: Docker Compose services can talk to each other using their service names. It means that if service_a has IP address `172.28.0.1`, service_b can communicate with using either its IP `172.28.0.1` or simply its hostname `service_a`. See [docs](https://docs.docker.com/compose/networking/).