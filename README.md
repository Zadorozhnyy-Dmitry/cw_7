# Курсовая 8. Docker
Курсовая работа №7 "Трекер полезных привычек" завернута в Docker

## Технологии
- [Python v.3.10]()
- [Django v.5.1.3]()
- [Django REST Framework (DRF) v.3.15.2]()
- [Django JWT v.5.3.1]()
- [Celery v.5.4.0]()
- [Django celery-beat v.2.7.0]()
- [Redis v.5.2.0]()
- [CORS v.4.6.0]()
- [Docker v.27.3.1]()
- [Docker Compose v2.29.7]()


## Использование
#### Для запуска проекта создайте в корне проекта файл .env следующего вида:
```commandline
# настройки Джанго
SECRET_KEY=***

# настройки БД
POSTGRES_DB=***
POSTGRES_USER=***
POSTGRES_PASSWORD=***
POSTGRES_HOST=db
POSTGRES_PORT=5432

# настройки редис для Celery
CELERY_BROKER_URL=***
CELERY_RESULT_BACKEND=***

# настройки телеграмм-бота
BOT_TOKEN=***
```
Введите команду
```commandline
sudo docker compose up -d --build
```


### Выполняются требования:

+ Для сервисов django, postgresql, redis, celery, celery-beat созданы отдельные контейнеры
+ Оформлены Dockerfile и docker-compose.yaml


Автор Задорожный Дмитрий