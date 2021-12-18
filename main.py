# coding=utf-8
import random
from conf import MODEL
from faker import Faker
print(MODEL)


# digits = random.sample("1234567890", 4)  # 4 элемента без повторов из заданной коллекции
# number = int("".join(digits))  # соединяем в одно и конвертируем в число
# if number < 1000:  # если первая цифра была 0...
#     number = number * 10  # ...то добавляем его в конец
# print(number)
def year():
    print('"year":', random.randint(1900, 2021))

def author():
    faker = Faker("RU")
    for i in range(3):
        print('"author":', faker.name())


def title():
    filename = "books.txt"
    with open(filename) as f:  # менеджер контекста открывает файл в режиме чтения в текстовом формате "rt"
        for line in f:  # файл является итератором, который построчно возвращает свое содержимое
            print('"title":', line, end="")


if __name__ == "__main__":
    author()
    title()
