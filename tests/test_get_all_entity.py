import allure
import pytest

from helpers.api_requests import get_all_request

class TestGetAllEntity:
    @allure.title('Тест получения списка сущностей')
    def test_get_all(self, create_entities):
        with allure.step('Подготовка к тесту'):
            entities_data, entities_ids = create_entities

        with allure.step('Запрос на получение сущностей'):
            response = get_all_request('')
            response_data = response.json()

        with allure.step('Проверка статус кода'):
            assert response.status_code == 200

        with allure.step('Проверка что созданные сущности есть в списке'):
            response_ids = [entity['id'] for entity in response_data['entity']]
            for entity_id in entities_ids:
                assert entity_id in response_ids, f"Сущность {entity_id} не найдена в списке"

    @allure.title('Тест фильтрации по title')
    def test_filter_title(self, create_entities):
        with allure.step('Подготовка к тесту'):
            entities_data, entities_ids = create_entities
            sample_title = entities_data[0][0]['title']

        with allure.step(f'Запрос с фильтром по title: {sample_title}'):
            filtered = f'?title={sample_title}'
            response = get_all_request(filtered)

        with allure.step('Проверка статус кода'):
            assert response.status_code == 200

        with allure.step(f'Проверка, что найденные сущности содержат {sample_title}'):
            for entity in response.json()['entity']:
                assert sample_title in entity['title']

    @allure.title('Тест фильтрации по verified')
    @pytest.mark.parametrize('verified', [True, False])
    def test_filter_verified(self, create_entities, verified):
        with allure.step('Подготовка к тесту'):
            entities_data, entities_ids = create_entities

        with allure.step(f'Запрос с фильтром по verified = {verified}'):
            filtered = f'?verified={verified}'
            response = get_all_request(filtered)

        with allure.step('Проверка статус кода'):
            assert response.status_code == 200

        with allure.step(f'Проверка, что найдены сущности с verified = {verified}'):
            for entity in response.json()['entity']:
                assert verified == entity['verified']

    @allure.title('Тест базовой пагинации')
    def test_basic_pagination(self, create_entities):
        with allure.step('Подготовка к тесту'):
            entities_data, entities_ids = create_entities

        with allure.step(f'Запрос первых 5 элементов'):
            response = get_all_request('?page=1&perPage=5')
            assert response.status_code == 200

        with allure.step('Проверка, что на странице не более 5 элементов'):
            page_entities = response.json()['entity']
            assert len(page_entities) <= 5
        with allure.step('Проверка, что страница не пустая'):
            assert len(page_entities) > 0