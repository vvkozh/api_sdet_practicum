import pytest

from helpers import generators
from helpers.api_requests import post_request, delete_request


@pytest.fixture(scope="function")
def create_entity():
    payload = generators.generate_data_entity()
    response = post_request(payload)
    yield response.json()

@pytest.fixture(scope="function")
def create_and_delete_entity():
    payload = generators.generate_data_entity()
    response = post_request(payload)
    entity_id = response.json()
    yield payload, entity_id
    delete_request(entity_id)

@pytest.fixture(scope="function")
def delete_entity():
    entity_id_in_test = None
    def save_entity_id(entity_id):
        nonlocal entity_id_in_test
        entity_id_in_test = entity_id
        return entity_id_in_test
    yield save_entity_id
    if entity_id_in_test is not None:
        delete_request(entity_id_in_test)

@pytest.fixture(scope="session")
def create_entities():
    entities_data = []
    entities_ids = []
    for i in range(10):
        payload = generators.generate_data_entity()
        response = post_request(payload)
        if response.status_code == 200:
            entity_id = response.json()
            entities_data.append((payload, entity_id))
            entities_ids.append(entity_id)
    yield entities_data, entities_ids
    for entity_id in entities_ids:
        delete_request(entity_id)

