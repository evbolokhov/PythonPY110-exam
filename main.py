from faker import Faker
faker = Faker("RU")
for i in range(3):
        print('name:', faker.name())