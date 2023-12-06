# Django REST API with Docker

This repository contains a Django REST API project that is designed to be deployed using Docker.

## Prerequisites
- Docker
- Docker Compose

## Environment Variables

First and foremost we need to include/specify the variables in ***.env*** file.
The important ones are:
- DEBUG
- SECRET_KEY
- DATABASE related variables

## API Endpoints

When we create app it is crucial to specify endpoints depending on our application:
- GET
- POST
- DELETE 
- etc.

## Dockerfile and Docker Compose

In **Dockerfile** we specify the dependencies that we need for our app to be run and some other specifications.
Then we must configure **Docker Compose** file ***(docker-compose.yml)***, create services \
(mysql and the app from Dockerfile), specify some options etc.

## Build and Run the Docker Containers

And after that we run `docker-copmose up -d --build` command, to build the Docker images and start the containers \
in the background.

## Testing

To test our app in browser we type `localhost:8000` and this will open the page of our REST API, where we then specify
the endpoint we need.

To check the mysql and the database with its tables we can run `docker exec -it <mysql_container> bash`, then
in the prompt run `mysql -u <username> -p` command.