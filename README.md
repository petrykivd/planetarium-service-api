# Planetarium Service API

Welcome to the Planetarium Service API! This API is a Django-based web application designed to manage astronomy shows, show sessions, reservations, and related data for a planetarium. It provides various endpoints for administrators and authenticated users to interact with the system, offering features such as viewing and filtering astronomy shows, managing show sessions, creating reservations, and more.
## Getting Started

### Prerequisites

Before you begin, make sure you have the following tools and technologies installed:

- Python (>=3.6)
- Django
- Django REST framework

## Installing / Getting started
> A quick introduction of the setup you need to get run a project.

### Using Git
1. Clone the repo:
```shell
git clone https://github.com/petrykivd/planetarium-service-api
```
2. You can open project in IDE and configure .env file using [.env.sample](.env.sample) file as an example.
<details>
<summary>Parameters for .env file:</summary>

- **POSTGRES_DB**: `Name of your DB`
- **POSTGRES_USER**: `Name of your user for DB`
- **POSTGRES_PASSWORD**: `Your password in DB`
- **POSTGRES_HOST** `Host of your DB`
</details>

3. Run docker-compose command to build and run containers:
```shell
docker-compose up --build
```
### Using Docker Hub
1. Login into the Docker:
```shell
docker login
```

2. Pull the project:
```shell
docker pull petrykivd/planetarium_service_api:latest
```

3. Run the containers:
```shell
docker-compose up
```


> To access browsable api, use http://localhost:8000/api/planetarium/
> 
> To get access to the content, visit http://localhost:8000/api/user/token/ to get JWT token.
> 
> Use the following admin user:
> - Email: admin@gmail.com
> - Password: 12345

## API Endpoints
<details>
  <summary>Astronomy Shows</summary>

- **List Astronomy Shows**: `GET /api/planetarium/astronomy-shows/`
- **Create Astronomy Show**: `POST /api/planetarium/astronomy-shows/`
- **Retrieve Astronomy Show**: `GET /api/planetarium/astronomy-shows/{astronomy_show_id}/`
- **Update Astronomy Show**: `PUT /api/planetarium/astronomy-shows/{astronomy_show_id}/`
- **Partial Update** `PATCH /api/planetarium/astronomy-shows/{astronomy_show_id}/`
- **Delete Astronomy Show**: `DELETE /api/planetarium/astronomy-shows/{astronomy_show_id}/`
- **Upload Astronomy Show Image**: `POST /api/planetarium/astronomy-shows/{astronomy_show_id}/upload-image/`
</details>

<details>
  <summary>Show Sessions</summary>
  
- **List Show Sessions**: `GET /api/planetarium/show-sessions/`
- **Create Show Session**: `POST /api/planetarium/show-sessions/`
- **Retrieve Show Session**: `GET /api/planetarium/show-sessions/{show_session_id}/`
- **Update Show Session**: `PUT /api/planetarium/show-sessions/{show_session_id}/`
- **Partial Update** `PATCH /api/planetarium/show-sessions/{show_session_id}/`
- **Delete Show Session**: `DELETE /api/planetarium/show-sessions/{show_session_id}/`
</details>

<details>
  <summary>Reservations</summary>
  
- **List Reservations**: `GET /api/planetarium/reservations/`
- **Create Reservation**: `POST /api/planetarium/reservations/`
- **Retrieve Reservation**: `GET /api/planetarium/reservations/{reservation_id}/`
- **Update Reservation**: `PUT /api/planetarium/reservations/{reservation_id}/`
- **Partial Update** `PATCH /api/planetarium/reservations/{reservation_id}/`
- **Delete Reservation**: `DELETE /api/planetarium/reservations/{reservation_id}/`
</details>

<details>
  <summary>Show Themes</summary>
  
- **List Show Themes**: `GET /api/planetarium/show-themes/`
- **Create Show Theme**: `POST /api/planetarium/show-themes/`
- **Retrieve Show Theme**: `GET /api/planetarium/show-themes/{show_theme_id}/`
- **Update Show Theme**: `PUT /api/planetarium/show-themes/{show_theme_id}/`
- **Partial Update** `PATCH /api/planetarium/show-themes/{show_theme_id}/`
- **Delete Show Theme**: `DELETE /api/planetarium/show-themes/{show_theme_id}/`
</details>

<details>
  <summary>Planetarium Domes</summary>
  
- **List Planetarium Domes**: `GET /api/planetarium/planetarium-domes/`
- **Create Planetarium Dome**: `POST /api/planetarium/planetarium-domes/`
- **Retrieve Planetarium Dome**: `GET /api/planetarium/planetarium-domes/{planetarium_dome_id}/`
- **Update Planetarium Dome**: `PUT /api/planetarium/planetarium-domes/{planetarium_dome_id}/`
- **Partial Update** `PATCH /api/planetarium/planetarium-domes/{planetarium_dome_id}/`
- **Delete Planetarium Dome**: `DELETE /api/planetarium/planetarium-domes/{planetarium_dome_id}/`
</details>

<details>
  <summary>User</summary>
  
- **Information about current User**: `GET /api/user/me/`
- **Update User**: `PUT /api/user/me/`
- **Partial Update** `PATCH /api/user/me/`
- **Create new User** `POST /api/user/register/`
- **Create access and refresh tokens** `POST /api/user/token/`
- **Refresh access token** `POST /api/user/token/refresh/`
- **Verify tokens**: `POST /api/user/token/verify/`
</details>


## Authentication
- The API uses token-based authentication for user access. Users need to obtain an authentication token by logging in.
- Administrators and authenticated users can access all endpoints, but only administrators can change information about astronomy shows, show sessions, and related entities. Each authenticated user can access and create their own reservations.

## Documentation
- The API is documented using the OpenAPI standard.
- Access the API documentation by running the server and navigating to http://localhost:8000/api/doc/swagger/ or http://localhost:8000/api/doc/redoc/.

## DB Structure

## Endpoints

## License
This project is licensed under the MIT License.