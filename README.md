## Prerequisites

- [Docker](https://docs.docker.com/engine/install/)
- [Docker-compose](https://docs.docker.com/compose/install/)


## Project Components
- Django
- React
- MySQL

## Steps to run 

Make sure that Docker Desktop is running by running the command, `docker ps`.  

1. Clone the Repository
2. Go the the root of the project by running `cd upou-207`.
3. In the root directory, run `docker-compose build`.

If there is an error in the frontend container, run `cd frontend && npm install`, the run `docker-compose build` and `docker-compose up`.

## Services in the Docker compose

### 

- db
  Refers to the MySQL service

- app
  Refers to the Django Backend service

- frontend
   Refers to the React application.
