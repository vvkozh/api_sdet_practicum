import allure
import pytest
from typing import Any, Dict

from helpers.api_requests import get_request, patch_request
from helpers.generators import generate_random_int, generate_random_sense, generate_random_list_int


class TestPatchEntity:
    @allure.title('Тест изменения addition')
    @pytest.mark.parametrize('modified_param, not_modified_param, generate_method',
                             [('additional_info', 'additional_number', generate_random_sense),
                              ('additional_number', 'additional_info', generate_random_int)])
    def test_patch_addition(self, create_and_delete_entity, modified_param, not_modified_param, generate_method):
        with allure.step('Подготовка к тесту'):
            payload: Dict[str, Any]
            entity_id: int
            payload, entity_id = create_and_delete_entity

        with allure.step(f'Меняем {modified_param}'):
            payload['addition'][modified_param] = generate_method()

        with allure.step(f'Запрос на изменение {modified_param}'):
            response = patch_request(entity_id, payload)

        with allure.step('Проверка статус кода'):
            assert response.status_code == 204, f"Ожидался статус 204, получен {response.status_code}"

        with allure.step(f'Проверка, что изменился {modified_param}'):
            response_patch_entity = get_request(entity_id)
            response_data: Dict[str, Any] = response_patch_entity.json()
            response_data['addition'].pop('id')
            response_data.pop('id')
            assert response_data == payload,  "Структура сущности не соответствует ожидаемой после обновления"


    @allure.title('Тест изменения important_numbers')
    def test_patch_important_numbers(self, create_and_delete_entity):
        with allure.step('Подготовка к тесту'):
            payload: Dict[str, Any]
            entity_id: int
            payload, entity_id = create_and_delete_entity

        with allure.step('Меняем important_numbers'):
            payload['important_numbers'] = generate_random_list_int()

        with allure.step('Запрос на изменение important_numbers'):
            response = patch_request(entity_id, payload)

        with allure.step('Проверка статус кода'):
            assert response.status_code == 204, f"Ожидался статус 204, получен {response.status_code}"

        with allure.step(f'Проверка изменения important_numbers'):
            response_patch_entity = get_request(entity_id)
            response_data: Dict[str, Any] = response_patch_entity.json()
            response_data['addition'].pop('id')
            response_data.pop('id')
            assert response_data == payload, "Структура сущности не соответствует ожидаемой после обновления"


    @allure.title('Тест изменения title')
    def test_patch_title(self, create_and_delete_entity):
        with allure.step('Подготовка к тесту'):
            payload: Dict[str, Any]
            entity_id: int
            payload, entity_id = create_and_delete_entity

        with allure.step('Меняем title'):
            payload['title'] = generate_random_sense()

        with allure.step('Запрос на изменение title'):
            response = patch_request(entity_id, payload)

        with allure.step('Проверка статус кода'):
            assert response.status_code == 204, f"Ожидался статус 204, получен {response.status_code}"

        with allure.step(f'Проверка изменения title'):
            response_patch_entity = get_request(entity_id)
            response_data: Dict[str, Any] = response_patch_entity.json()
            response_data['addition'].pop('id')
            response_data.pop('id')
            assert response_data == payload, "Структура сущности не соответствует ожидаемой после обновления"

    @allure.title('Тест изменения verified')
    def test_patch_verified(self, create_and_delete_entity):
        with allure.step('Подготовка к тесту'):
            payload: Dict[str, Any]
            entity_id: int
            payload, entity_id = create_and_delete_entity

        with allure.step(f'Меняем verified'):
            if payload['verified'] is True:
                payload['verified'] = False
            else:
                payload['verified'] = True

        with allure.step('Запрос на изменение verified'):
            response = patch_request(entity_id, payload)

        with allure.step('Проверка статус кода'):
            assert response.status_code == 204, f"Ожидался статус 204, получен {response.status_code}"

        with allure.step(f'Проверка изменения verified'):
            response_patch_entity = get_request(entity_id)
            response_data: Dict[str, Any] = response_patch_entity.json()
            response_data['addition'].pop('id')
            response_data.pop('id')
            assert response_data == payload, "Структура сущности не соответствует ожидаемой после обновления"