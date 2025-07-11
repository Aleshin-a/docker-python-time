# docker-python-time

Это простое приложение на Python, отображающее текущее время и дату, контейнеризованное с помощью Docker и управляемое Docker Compose.

## Технологии

*   Python 3.9
*   Docker
*   Docker Compose

## Установка

1.  **Prerequisites:**Убедитесь, что в вашей системе установлены Docker и Docker Compose.
2.  **Клонировать репозиторий:**

    ```bash
    git clone <your_repository_url>
    cd <your_project_directory>
    ```

3.  **Создайте и запустите приложение с помощью Docker Compose:**

    ```bash
    docker compose up --build
    ```

## Использование

Приложение выведет текущее время и дату на консоль. Вы можете просмотреть журналы:

    ```bash
    docker compose logs app
    ```

Чтобы остановить работу приложения:

    ```bash
    docker compose down
    ```

## Файлы

*   `app.py`: Приложение на Python.
*   `Dockerfile`: Инструкции по созданию образа Docker.
*   `docker-compose.yml`:Конфигурация для запуска приложения с помощью Docker Compose.

