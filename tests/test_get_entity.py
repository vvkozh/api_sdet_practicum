import allure
from typing import Any, Dict

from helpers.api_requests import get_request


@allure.title('Тест создания сущности')
def test_create_entity(create_and_delete_entity):
    with allure.step('Подготовка к тесту'):
        payload: Dict[str, Any]
        entity_id: int
        payload, entity_id = create_and_delete_entity

    with allure.step('Запрос на получение данных сущности'):
        response = get_request(entity_id)
        response_data: Dict[str, Any] = response.json()

    with allure.step('Проверка статус кода'):
        assert response.status_code == 200, f"Ожидался статус 200 OK, получен {response.status_code}"

    with allure.step('Проверка данных сущности'):
        assert response_data['addition']['additional_info'] == payload['addition']['additional_info'], "Additional info не совпадает"
        assert response_data['addition']['additional_number'] == payload['addition']['additional_number'], "Additional number не совпадает"
        assert response_data['important_numbers'] == payload['important_numbers'], "Important numbers не совпадают"
        assert response_data['title'] == payload['title'], "Title не совпадает"
        assert response_data['verified'] == payload['verified'], "Verified не совпадает"
        assert 'id' in response.json(), "Поле 'id' отсутствует в ответе"