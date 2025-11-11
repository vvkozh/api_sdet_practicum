from faker import Faker

faker = Faker('ru_RU')

def generate_data_entity():
    data_entity = {
        "addition": {
            "additional_info": faker.sentence(),
            "additional_number": faker.random_int(0, 999)
        },
        "important_numbers": [faker.random_int(1, 999) for _ in range(faker.random_int(3, 5))],
        "title": faker.sentence(),
        "verified": faker.boolean()
    }
    return data_entity

def generate_random_sense():
    return faker.sentence()

def generate_random_int():
    return faker.random_int(0, 999)

def generate_random_list_int():
    return [faker.random_int(1, 999) for _ in range(faker.random_int(1, 2))]