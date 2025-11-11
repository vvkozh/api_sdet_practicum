"""Базовый URL для API."""
BASIC_URL: str = 'http://localhost:8080'

class Urls:
    """Класс для хранения URL endpoints API."""
    CREATE_URL: str = f'{BASIC_URL}/api/create'
    DELETE_URL: str = f'{BASIC_URL}/api/delete/'
    GET_URL: str = f'{BASIC_URL}/api/get/'
    GET_ALL_URL: str = f'{BASIC_URL}/api/getAll'
    PATCH_URL: str = f'{BASIC_URL}/api/patch/'