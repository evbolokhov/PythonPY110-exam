# coding=utf-8
import random
import json
from conf import MODEL
from faker import Faker


def pk(value=1):
    """Функция счетчик"""
    while True:
        yield value
        value += 1


def title():
    """Функция возврта из файла рандомного наименования книги"""
    filename = "books.txt"
    with open(filename) as f:
        x = random.randint(0, len(f.readlines())-1)
    with open(filename) as f:
        return f.readlines()[x].replace("\n", "")


def year():
    """Функция возвращает рандомный год"""
    return random.randint(1900, 2021)


def pages():
    """Функция возвращает рандомные страницы"""
    return random.randint(10, 500)


def isbn13():
    """Функция возвращает рандомный ISDN"""
    fake = Faker()
    return fake.numerify(text='%%%-%-%%%%%-%%%-%')


def rating():
    """Функция возвращает рандомный рейтинг"""
    return round(random.uniform(0, 5), 1)


def price():
    """Функция возвращает рандомный прайс"""
    return round(random.uniform(50, 50000), 2)


def authors():
    """Функция возвращает авторов книг от 1 до 3х"""
    st = []
    fake = Faker("RU")
    for i in range(random.randint(1, 3)):
        st.append(fake.name())
    return st


def booklist():
    """Функция возвращает словарь"""
    yield {
            "model": MODEL,
            "pk": next(counter_),
            "fields": {
                       "title": title(),
                       "year": year(),
                       "pages": pages(),
                       "isbn13": isbn13(),
                       "rating": rating(),
                       "price": price(),
                       "author": [
                                  authors()
                                 ]
                       }
            }


def main():
    """Функция генератор списка книг и записи списка в фаил"""
    st = []
    for _ in range(100):
        st.append(next(booklist()))
        print(st)
    with open('UserList.json', 'w', encoding="utf-8") as f:
        json.dump(st, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    counter_ = pk()
    main()
