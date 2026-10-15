# TaskFlow – REST API менеджер задач

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

TaskFlow — это простой REST API для управления задачами, построенный на Flask. Позволяет создавать, читать, обновлять и удалять задачи через HTTP-запросы. Данные хранятся в SQLite-базе с помощью SQLAlchemy.

## Стек технологий

- **Язык:** Python
- **Фреймворк:** Flask
- **ORM:** SQLAlchemy
- **База данных:** SQLite

## Установка и запуск

### Требования
- Python 3.8 или выше

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Запуск приложения
```bash
python app.py
```

По умолчанию сервер запускается на `http://127.0.0.1:5000`.

### Инициализация базы данных
При первом запуске база данных создаётся автоматически. Если нужно создать БД вручную, запусти:
```bash
python init_db.py
```

## API

Документация по эндпоинтам и форматам запросов находится в файле [API.md](API.md).

Примеры базовых запросов:
- Получить все задачи: `GET /tasks`
- Создать задачу: `POST /tasks`
- Обновить задачу: `PUT /tasks/<id>`
- Удалить задачу: `DELETE /tasks/<id>`

## Лицензия

Проект распространяется под лицензией [MIT](LICENSE).
