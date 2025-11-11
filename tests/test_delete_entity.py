import allure

from data.data import ResponseData
from helpers.api_requests import delete_request, get_request


@allure.title('Тест создания сущности')
def test_create_entity(create_entity):
    with allure.step('Запрос на удаление сущности'):
        response = delete_request(create_entity)

    with allure.step('Проверка статус кода'):
        assert response.status_code == 204

    with allure.step('Проверка, что сущность удалена'):
        response_entity = get_request(create_entity)
        assert response_entity.status_code == 500
        assert response_entity.json() == ResponseData.GET_RESPONSE_500