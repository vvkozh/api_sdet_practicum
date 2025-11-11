import requests
from data.urls import Urls

def post_request(payload):
    response = requests.post(Urls.CREATE_URL, json=payload)
    return response

def delete_request(id_entity):
    response = requests.delete(Urls.DELETE_URL + f'{id_entity}')
    return response

def get_request(id_entity):
    response = requests.get(Urls.GET_URL + f'{id_entity}')
    return response

def get_all_request(filtering):
    if filtering is not None :
        response = requests.get(Urls.GET_ALL_URL + f'{filtering}')
    else:
        response = requests.get(Urls.GET_ALL_URL )
    return response

def patch_request(id_entity, payload):
    response = requests.patch(Urls.PATCH_URL + f'{id_entity}', json=payload)
    return response

for i in range(500):
    response_delete = delete_request(i)
