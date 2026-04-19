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
## Тестирование

В проекте используется pytest для тестирования backend-логики

### Покрытые сценарии

- отправка OTP-кода
- проверка OTP-кода
- ошибка при неверном или просроченном коде
- доступ к защищенному эндпоинту
- генерация JWT-токенов

### Запуск тестов
```
pytest
```
## Безопасность

- JWT-аутентификация
- OTP одноразового использования
- Ограничения доступа через permissions
- Валидация входных данных через serializers

## Автоматический деплой (CI/CD)

В проекте настроен GitHub Actions workflow, который автоматически выполняет проверку кода и деплой приложения на сервер.

### Как работает workflow

При каждом push выполняются следующие шаги:

1. Проверка кода литером (flake8)
2. Запуск тестов Django
3. Сборка Docker-образа
4. Деплой на удаленный сервер через SSH

Если тесты выполняются с ошибкой - деплой НЕ выполняется

### Необходимые Secrets в GitHub

В репозитории должны быть добавлены следующие секреты:

## SSH доступ к серверу:

- SSH_HOST - IP-адрес сервера
- SSH_USER - пользователь сервера
- SSH_KEY - приватный SSH-ключ
- DEPLOY_DIR - директория проекта на сервере

## Переменные окружения проекта:

- SECRET_KEY=секретный ключ Django
- POSTGRES_DB=имя базы данных
- POSTGRES_USER=пользователь PostgreSQL
- POSTGRES_PASSWORD=пароль PostgreSQL
- POSTGRES_HOST=хост базы данных
- POSTGRES_PORT=порт базы данных

### Как происходит деплой

GitHub Actions подключается к серверу по SSH и выполняет команды:

```
cd $DEPLOY_DIR
git pull

docker compose down
docker compose up -d --build

docker compose exec -T web python manage.py migrate
docker compose exec -T web python manage.py collectstatic --noinput
```
## Важно

На сервере должен быть создан файл .env в директории проекта:

```
SECRET_KEY=your_secret_key
POSTGRES_DB=phoneauthservice
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

### Как запустить деплой вручную

1. Закомитить изменения:
```
git add .
git commit -m "update"
git push origin develop
```
2. Перейдите во вкладку "Actions" в GitHub
3. Убедитесь, что workflow успешно выполнен

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).