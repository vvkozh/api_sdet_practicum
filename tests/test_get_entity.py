import allure

from helpers.api_requests import get_request


@allure.title('Тест создания сущности')
def test_create_entity(create_and_delete_entity):
    with allure.step('Подготовка к тесту'):
        payload, entity_id = create_and_delete_entity

    with allure.step('Запрос на получение данных сущности'):
        response = get_request(entity_id)
        response_data = response.json()

    with allure.step('Проверка статус кода'):
        assert response.status_code == 200

    with allure.step('Проверка данных сущности'):
        assert response_data['addition']['additional_info'] == payload['addition']['additional_info']
        assert response_data['addition']['additional_number'] == payload['addition']['additional_number']
        assert response_data['important_numbers'] == payload['important_numbers']
        assert response_data['title'] == payload['title']
        assert response_data['verified'] == payload['verified']
        assert 'id' in response.json()