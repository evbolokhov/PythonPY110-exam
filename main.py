# coding=utf-8
import random
from conf import MODEL
from faker import Faker
print(MODEL)


def year():
    print('"year":', random.randint(1900, 2021))


def pages():
    print('"pages":', random.randint(10, 500))


def isbn13():
    fake = Faker()
    for _ in range(10):
        print('"isbn13":', fake.numerify(text='%%%-%-%%%%%-%%%-%'))

def rating():
    print('"rating":', round(random.uniform(0, 5), 1))




def price():
    print('"price":', round(random.uniform(50, 50000), 1))

def author():
    faker = Faker("RU")
    for i in range(1):
        print((faker.name()))



#def task() -> list:
    # return [get_distance(point) for point in points]
   # return list(author)  # TODO записать через map




def title():
    filename = "books.txt"
    with open(filename) as f:  # менеджер контекста открывает файл в режиме чтения в текстовом формате "rt"
        for line in f:  # файл является итератором, который построчно возвращает свое содержимое
            print('"title":', line, end="")

if __name__ == "__main__":

    title()
    year()
    pages()
    isbn13()
    rating()
    price()
    print(author())
    #task()