# PhoneAuthService

Сервис аутентификации пользователей по номеру телефона с использованием OTP-кодов и JWT-токенов

## Описание проекта

Проект реализует backend-сервис авторизации пользователей по номеру телефона.
Аутентификация проходит в два этапа:
1. Отправка одноразового кода (OTP) на номер телефона.
2. Проверка кода и выдача JWT-токенов.

## Принцип работы OTP

1. Пользователь отправляет номер телефона.
2. Генерируется одноразовый код.
3. Код выводится в консоль (в режиме разработки).
4. Пользователь отправляет код обратно.
5. При успешной проверке выдается JWT-токен.

## Технологии
- Python 3.11+
- Django
- Django REST Framework
- PostgreSQL
- SimpleJWT
- OpenAPI Docs
- Docker/Docker Compose
- Git

## Особенности проекта
- Кастомная модель пользователя (телефон, как логин)
- Разделение бизнес логики (services layer)
- Одноразовые OTP-коды с защитой от повторного использования
- JWT-аутентификация
- Автоматическая документация API (Swagger/ReDoc)
- Контейнеризация приложения и базы данных через Docker

## Архитектура проекта

apps/
  |--users/  # кастомная модель пользователя
  |--otp/    # OTP-коды и логика проверки
services/    # бизнес-логика авторизации
config/      # настройки проекта

## Быстрый старт

```
git clone https://github.com/username/phoneauthservice.git
cd phoneauthservice
cp .env.sample .env
docker compose up --build
docker compose exec web python manage.py migrate
```

## Настройка переменных окружения

Создайте файл .env
```
SECRET_KEY=your_secret_key
POSTGRES_DB=phoneauthservice
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```
## Запуск проекта (Docker)

Сборка и запуск контейнеров
```
docker compose up -d --build
```
Применение миграций
```
docker compose exec web python manage.py migrate
```
Создание суперпользователя
```
docker compose exec web python manage.py createsuperuser
```
## Доступ к сервису:

Главная страница: http://localhost:8000/

Админка: http://localhost:8000/admin/

Swagger документация: http://localhost:8000/swagger/

ReDoc документация: http://localhost:8000/redoc/

## API Endpoints

### Авторизация

Отправка кода

POST /auth/send-code/

Запрос:
```
{
    "phone": "+79991234567"
}
```
Проверка кода

POST /auth/verify-code/

Запрос:
```
{
    "phone": "+79991234567",
    "code": "123456"
}
```
Ответ:
```
{
    "message": "Успешная авторизация",
    "tokens": {
        "access": "jwt_access_token",
        "refresh": "jwt_refresh_token",
}
```
### Пользователь

GET /users/me/

Headers:
```
Authorization: Bearer <jwt_access_token>
```
Ответ:
```
{
    "id": "1",
    "phone": "+79991234567"
}
```

## Проверка работоспособности:

Проверка web-сервиса:
```
docker compose logs -f web
```
Откройте в браузере http://localhost:8000/swagger/

Если страница открывается - сервис работает

Проверка базы данных:
```
docker compose exec db psql -U postgres
```
Если удалось войти в консоль PostgreSQL - база работает

Проверка таблиц:
```
\dt
```

## Развертывание на сервере:

1. Подключитесь к серверу.
```
ssh user@server_ip
```
2. Установите Docker.
```
sudo apt update
sudo apt install docker.io docker-compose -y
```
3. Клонируйте проект.
```
git clone <repo_url>
cd project
```
4. Создайте ".env"
```
cp .env.sample .env
```
5. Запустите
```
docker compose up --build
```

## Безопасность

- JWT-аутентификация
- OTP одноразового использования
- Ограничения доступа через permissions
- Валидация входных данных через serializers

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).