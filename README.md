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

To access the Frontend, go to `http://localhost:8001/`

## Services in the Docker compose

### 

- db
  - Refers to the MySQL service
    - Can be accessed by using the development credentials in a GUI and pointing to port 25000.

- app
  - Refers to the Django Backend service
    - Can be accessed by going to http://localhost:8000

- frontend
  - Refers to the React application.
    - Can be accessed by visiting http://localhost:3001
- mailhog
  - local mail server in order to simulate sending and receiving in a development environment
    - can be accessed by going to http://localhost:8025
