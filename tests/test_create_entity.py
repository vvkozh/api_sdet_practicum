import allure
from typing import Any, Dict

from helpers import generators
from helpers.api_requests import post_request, get_request

@allure.title('Тест создания сущности')
def test_create_entity(delete_entity):
    with allure.step('Подготовка тестовых данных'):
        payload: Dict[str, Any] = generators.generate_data_entity()

    with allure.step('Отправка запроса на создание сущности'):
        response = post_request(payload)
        entity_id: int = response.json()
        delete_entity(entity_id)

    with allure.step('Проверка статус кода'):
        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"

    with allure.step('Проверка, что возвращается id сущности'):
        assert entity_id is not None, "ID сущности не должен быть None"
        assert isinstance(entity_id, int), "ID должен быть целым числом"
        assert entity_id > 0, "ID должен быть положительным числом"

    with allure.step('Проверка данных созданной сущности'):
        response_entity = get_request(entity_id)
        data_new_entity: Dict[str, Any] = response_entity.json()
        assert data_new_entity['addition']['additional_info'] == payload['addition']['additional_info'], "Additional_info не совпадает"
        assert data_new_entity['addition']['additional_number'] == payload['addition']['additional_number'], "Additional_number не совпадает"
        assert data_new_entity['important_numbers'] == payload['important_numbers'], "Important_numbers не совпадают"
        assert data_new_entity['title'] == payload['title'], "Title не совпадает"
        assert data_new_entity['verified'] == payload['verified'], "Verified не совпадает"
        assert data_new_entity['id'] == entity_id, "ID в ответе не совпадает с возвращенным ID"
