import requests
from typing import Dict, Any

from data.urls import Urls

def post_request(payload: Dict[str, Any]) -> requests.Response:
    """Отправляет DELETE запрос для удаления сущности."""
    response = requests.post(Urls.CREATE_URL, json=payload)
    return response

def delete_request(id_entity: int) -> requests.Response:
    """Отправляет GET запрос для получения сущности по ID."""
    response = requests.delete(Urls.DELETE_URL + f'{id_entity}')
    return response

def get_request(id_entity: int) -> requests.Response:
    """Отправляет GET запрос для получения сущности по ID."""
    response = requests.get(Urls.GET_URL + f'{id_entity}')
    return response

def get_all_request(filtering: str = '') -> requests.Response:
    """Отправляет GET запрос для получения всех сущностей с возможностью фильтрации."""
    if filtering is not None :
        response = requests.get(Urls.GET_ALL_URL + f'{filtering}')
    else:
        response = requests.get(Urls.GET_ALL_URL )
    return response

def patch_request(id_entity, payload):
    """Отправляет PATCH запрос для обновления сущности."""
    response = requests.patch(Urls.PATCH_URL + f'{id_entity}', json=payload)
    return response
