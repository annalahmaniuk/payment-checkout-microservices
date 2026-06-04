
# Payment Checkout Microservices

[![Python CI Application](https://github.com/annalahmaniuk/payment-checkout-microservices/actions/workflows/python-app.yml/badge.svg)](https://github.com/annalahmaniuk/payment-checkout-microservices/actions/workflows/python-app.yml)

## Опис проєкту

Проєкт демонструє мікросервісну архітектуру з використанням FastAPI, Docker, Docker Compose та GitHub Actions.

Система складається з двох сервісів:

- checkout_service
- payment_gateway

## Функціональність

### Checkout Service

- GET /orders
- POST /orders

### Payment Gateway

- GET /payments
- POST /payments

## Використані технології

- Python 3.10
- FastAPI
- Docker
- Docker Compose
- GitHub Actions
- Flake8
- Newman

## Структура проєкту

.github/workflows/
checkout_service/
payment_gateway/
docker-compose.yml
README.md

## Контейнеризація

Кожен сервіс має власний Dockerfile та запускається у контейнері Docker.

## Оркестрація

Сервіси запускаються за допомогою docker-compose.yml. Для сервісу-залежності використовується директива depends_on.

## CI/CD

GitHub Actions автоматично виконує:

- перевірку коду через flake8;
- запуск тестів Newman;
- перевірку pull request та push.

## Персоналізація

Номер студента: 2

- Порт checkout_service: 8002
- Порт payment_gateway: 9002
- Початкові ID об'єктів: 200
- Усі JSON-відповіді містять поле `"student_id": 2`
