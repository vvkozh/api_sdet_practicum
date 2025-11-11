import allure

from helpers import generators
from helpers.api_requests import post_request, get_request

@allure.title('Тест создания сущности')
def test_create_entity(delete_entity):
    with allure.step('Подготовка тестовых данных'):
        payload = generators.generate_data_entity()

    with allure.step('Отправка запроса на создание сущности'):
        response = post_request(payload)
        entity_id = response.json()
        delete_entity(entity_id)

    with allure.step('Проверка статус кода'):
        assert response.status_code == 200

    with allure.step('Проверка, что возвращается id сущности'):
        assert entity_id is not None
        assert isinstance(entity_id, int)
        assert entity_id > 0

    with allure.step('Проверка данных созданной сущности'):
        response_entity = get_request(entity_id)
        data_new_entity = response_entity.json()
        assert data_new_entity['addition']['additional_info'] == payload['addition']['additional_info']
        assert data_new_entity['addition']['additional_number'] == payload['addition']['additional_number']
        assert data_new_entity['important_numbers'] == payload['important_numbers']
        assert data_new_entity['title'] == payload['title']
        assert data_new_entity['verified'] == payload['verified']
        assert data_new_entity['id'] == entity_id
