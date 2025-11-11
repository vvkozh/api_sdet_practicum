import pytest
from typing import Generator, Tuple, List, Any, Dict, Optional, Callable

from helpers import generators
from helpers.api_requests import post_request, delete_request


@pytest.fixture(scope="function")
def create_entity() -> Generator[int, None, None]:
    """Фикстура создает сущность для теста."""
    payload: Dict[str, Any] = generators.generate_data_entity()
    response = post_request(payload)
    yield response.json()

@pytest.fixture(scope="function")
def create_and_delete_entity() -> Generator[Tuple[Dict[str, Any], int], None, None]:
    """Фикстура создает сущность для теста и удаляет ее после завершения."""
    payload: Dict[str, Any] = generators.generate_data_entity()
    response = post_request(payload)
    entity_id: int = response.json()
    yield payload, entity_id
    delete_request(entity_id)

@pytest.fixture(scope="function")
def delete_entity() -> Generator[Callable[[int], int], None, None]:
    """Фикстура удаляет сущность после завершения теста."""
    entity_id_in_test: Optional[int] = None
    def save_entity_id(entity_id: int) -> int:
        """Сохраняет ID сущности для последующего удаления."""
        nonlocal entity_id_in_test
        entity_id_in_test = entity_id
        return entity_id_in_test
    yield save_entity_id
    if entity_id_in_test is not None:
        delete_request(entity_id_in_test)

@pytest.fixture(scope="session")
def create_entities() -> Generator[Tuple[List[Tuple[Dict[str, Any], int]], List[int]], None, None]:
    """Фикстура создает сущности для теста и удаляет их после завершения."""
    entities_data: List[Tuple[Dict[str, Any], int]] = []
    entities_ids: List[int] = []
    for i in range(10):
        payload: Dict[str, Any] = generators.generate_data_entity()
        response = post_request(payload)
        if response.status_code == 200:
            entity_id: int = response.json()
            entities_data.append((payload, entity_id))
            entities_ids.append(entity_id)
    yield entities_data, entities_ids
    for entity_id in entities_ids:
        delete_request(entity_id)

