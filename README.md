# PhoneAuthService

Сервис аутентификации пользователей по номеру телефона с использованием OTP-кодов и JWT-токенов

## Описание проекта

Проект реализует backend-сервис авторизации позльзователей по номеру телефона.
Аутентификация проходит в два этапа:
1. Отправка одноразового кода на номер телефона.
2. Проверка кода и выдача JWT-токенов.

## Технологии
- Python 3.11+
- Django
- Django REST Framework
- PostgreSQL
- SimpleJWT
- OpenAPI Docs
- Docker
- Git

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/username/phoneauthservice.git
```
2. Создайте файл окружения на основе шаблона .env.sample.

### Пример файла .env.sample
```
SECRET_KEY=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
```
3. Откройте файл .env и заполните необходимые переменные:
```
SECRET_KEY=your_secret_key
POSTGRES_DB=habittracker
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_postgras_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```
4. Соберите и запустите контейнеры:
```
docker compose up --build
```
5. Примените миграции:
```
docker compose exec web python manage.py migrate
```
6. Создайте суперпользователя:
```
docker compose exec web python manage.py createsuperuser
```
## Доступ к сервисам:

Перейти в браузере:

Главная старница: http://localhost:8000/
Админка: http://localhost:8000/admin/
Swagger документация: http://localhost:8000/swagger/
ReDoc документация: http://localhost:8000/redoc/

## Проверка работоспособности:

После запуска проекта
```
docker compose up -d --build
```
убедитесь что все сервисы работают корректно:

1. "web" - Django сервер

Откройте в браузере http://localhost:8000/swagger/
Если страница открывается - сервис работает

Проверка через логи
```
docker compose logs -f web
```
2. "db" - PostgreSQL

Проверка подключения к базе:
```
docker compose exec db psql -U postgres
```
Если удалось войти в консоль PostgreSQL - база работает

Проверка таблиц:
```
\dt
```

## Настройка сервера:

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
5. Запустите
```
docker compose up --build
```
## Авторизация

POST /auth/send-code/

Запрос:
```
{
    "phone": "+79991234567"
}
```
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
## Пользователь

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
## Безопасность

- JWT-аутентификация
- OTP одноразового использования
- Ограничения доступа через permissions
- Валидация входных данных через serializers

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).