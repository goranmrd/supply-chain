# Opply - Django Backend Project

This project is the backend for a mobile application, allowing customers to order products. It's built with Django and uses Docker and Docker Compose for containerization and PostgreSQL for the database.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Running the Project](#running-the-project)
   - [Docker Compose](#docker-compose)
   - [Testing with Swagger](#testing-with-swagger)
4. [Additional Information](#additional-information)

## Project Overview
This project serves as the backend for a mobile application. It provides:
- Authentication via token-based authentication.
- CRUD operations for products, orders, and customers.
- PostgreSQL as the database backend.
- Containerization with Docker and Docker Compose.

## Getting Started
### Prerequisites
Ensure you have the following installed on your system:
- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```
2. Build the Docker Compose project:
   ```bash
   docker-compose build
   ```

3. Start the Docker Compose project:
   ```bash
   docker-compose up
   ```

## Running the Project

### Docker Compose
After running docker-compose up, the project starts with the following services:

`db`: The PostgreSQL database. \
`web`: The Django backend.
`test`: Running Django tests and exits

The Django server is accessible on http://localhost:8000/ but no endpoints are available for root.

## Testing with Swagger
The project uses Swagger for API documentation and testing. To access the Swagger UI, visit http://localhost:8000/docs/ in your web browser.

## API Endpoints:
You can test API endpoints and inspect their schema using Swagger. \
**Authorization**: Ensure you use token-based authentication to access protected endpoints. \

## Additional Information

### Custom Management Command
The project includes a custom management command that creates a test user if it doesn't already exist. This command runs automatically after docker-compose up.
Your auto created user for testing, credentials are `testuser:testpass`

### PostgreSQL Configuration
The PostgreSQL service is set up with the following default configuration:

Database Name: mydatabase
Database User: test_user
Database Password: test_password
Database Host: db (Docker Compose service name)

### Pre-commit - DEV
To enable pre-commit for development (strongly recommended), run:
```bash
  pre-commit install
```
It will run auto after each commit or if you want to run it manually:
```bash
  pre-commit run --all-files
```
### Troubleshooting
If you encounter issues, check the Docker logs for detailed information:
```bash
    docker-compose logs
```

If you need to rebuild the project, you can use the following commands:
```bash
    docker-compose down
    docker-compose build
    docker-compose up
```

For additional assistance, refer to the [Django documentation](https://docs.djangoproject.com/en/stable/) or the [Docker documentation](https://docs.docker.com/).
