# Cinema Management API

This Django project provides an API for managing movies, theaters, and sessions in a cinema.

## Features

- CRUD operations for movies, theaters, and sessions.
- Swagger UI for API documentation.

## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Usage

1. Clone the repository:

   ```
   git clone https://github.com/JonasNogueira/CinemaAPI.git

2. Build and run the Docker containers:
    ``` 
        docker-compose up --build

3. Apply migrations:
    ```
        docker-compose exec web python manage.py migrate

4. Open your web browser and go to http://localhost:8000 to view the Swagger UI for API documentation.
   

## API Endpoints
   /api/movie/: CRUD operations for movies.
   /api/theater/: CRUD operations for theaters.
   /api/session/: CRUD operations for sessions.


