# Payment Checkout Microservices

![Python CI Application](https://github.com/annalahmaniuk/payment-checkout-microservices/actions/workflows/python-app.yml/badge.svg)

Система з двох мікросервісів на FastAPI, яка демонструє роботу контейнеризації через Docker та автоматизацію CI/CD процесів.

## Основний функціонал

### Payment Gateway (порт 8001)
- Обробка платіжних запитів
- Валідація вхідних даних
- Збереження історії операцій

### Checkout Service (порт 8002)
- Створення замовлень
- Формування checkout-операцій
- Підрахунок статистики замовлень

## Технології

- Python 3.13
- FastAPI
- Docker
- Docker Compose
- GitHub Actions
- Flake8

## Структура проєкту

```text
.github/workflows/     CI/CD pipeline
payment_gateway/       Payment service
checkout_service/      Checkout service
docker-compose.yml     Docker configuration
```

## Запуск проєкту

```bash
docker compose up --build
```

## CI/CD

Проєкт використовує GitHub Actions для:

- автоматичної перевірки коду;
- запуску Flake8;
- перевірки Pull Request;
- контролю якості перед злиттям у main.
