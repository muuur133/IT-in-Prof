import requests


def get_tasks(page: int = 1, per_page: int = 10, token: str | None = None) -> dict:
    """
    Получить список задач из API TaskFlow с постраничной навигацией.

    Функция выполняет GET-запрос к эндпоинту ``/tasks`` сервиса TaskFlow
    и возвращает словарь с задачами и метаданными пагинации.

    Параметры
    ---------
    page : int, optional
        Номер страницы для выборки (по умолчанию ``1``).
    per_page : int, optional
        Количество задач на одной странице (по умолчанию ``10``).
    token : str | None, optional
        JWT-токен доступа. Если передан, добавляется в заголовок
        ``Authorization: Bearer <token>``. По умолчанию ``None``.

    Возвращаемое значение
    ---------------------
    dict
        Словарь вида::

            {
                "tasks": [
                    {
                        "id": 1,
                        "title": "Изучить Flask",
                        "description": "Прочитать документацию",
                        "completed": False,
                        "created_at": "2024-08-10T12:00:00",
                        "updated_at": "2024-08-10T12:00:00"
                    },
                    ...
                ],
                "total": 2,
                "page": 1,
                "per_page": 10
            }

    Исключения
    ----------
    requests.HTTPError
        Если сервер вернул код ответа, отличный от 2xx.
    requests.RequestException
        При сетевых ошибках (таймаут, недоступность сервера и т.п.).

    Примеры
    -------
    >>> tasks = get_tasks(page=1, per_page=5, token="eyJhbGciOi...")
    >>> tasks["total"]
    2
    >>> tasks["tasks"][0]["title"]
    'Изучить Flask'
    """
    # Базовый URL API TaskFlow (см. API.md)
    base_url = "http://127.0.0.1:5000"

    # Формируем параметры строки запроса для пагинации
    params = {
        "page": page,
        "per_page": per_page,
    }

    # Формируем заголовки запроса
    headers = {
        "Content-Type": "application/json",  # API работает с JSON
    }

    # Если передан токен — добавляем его в заголовок Authorization
    if token:
        headers["Authorization"] = f"Bearer {token}"

    # Выполняем GET-запрос к эндпоинту /tasks с параметрами и заголовками
    response = requests.get(
        f"{base_url}/tasks",
        params=params,
        headers=headers,
        timeout=10,  # защита от «зависания» запроса
    )

    # Вызываем исключение, если код ответа не 2xx (например, 400, 401, 500)
    response.raise_for_status()

    # Парсим JSON-ответ и возвращаем его как словарь
    return response.json()