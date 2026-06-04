# Payment Checkout Microservices

## CI/CD Status

GitHub Actions workflow is configured to run flake8 and API tests automatically on every push and pull request.

## Project Description

This project demonstrates a microservice architecture using FastAPI, Docker, Docker Compose and GitHub Actions.

The system consists of two services:

- checkout_service
- payment_gateway

## Features

### Checkout Service

- GET /orders
- POST /orders

### Payment Gateway

- GET /payments
- POST /payments

## Technologies

- Python 3.10
- FastAPI
- Docker
- Docker Compose
- GitHub Actions
- Flake8
- Newman

## Project Structure

```text
.github/workflows/
checkout_service/
payment_gateway/
docker-compose.yml
README.md
```

## Docker

Both services are containerized using Docker and launched together through Docker Compose.

## CI/CD Pipeline

The GitHub Actions workflow automatically:

1. Runs flake8 linting
2. Builds services
3. Executes Newman API tests

## Personalization

Student number: 2

- Checkout Service Port: 8002
- Payment Gateway Port: 9002
- Object IDs start from 200
- All JSON responses include `"student_id": 2`
