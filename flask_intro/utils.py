import string
import random
import requests
import csv
from faker import Faker


def generate_password(length: int = 10) -> str:

    chars = string.ascii_letters + string.digits
    password = ''

    for _ in range(length):
        password += random.choice(chars)

    return password


# task 1 --------------------------------------------------------------------
def read_txt(name: str = 'requirements.txt') -> str:
    with open(name, "r") as txt_file:
        return txt_file.read()


# task 2 --------------------------------------------------------------------
fake = Faker()


def generate_pref_name(min_len: int, max_len: int):
    return ''.join([random.choice(string.digits) for _ in range(random.randint(min_len, max_len))])


def generate_fake_user(user_num: int = 10, min_len: int = 2, max_len: int = 3):
    lname = []
    for _ in range(user_num):
        fk_name = [fname for fname in fake.name().split()]  # список - имя, фамилия пользователя
        pr_name = generate_pref_name(min_len, max_len)  # случайное число, для вставки в email
        i = 1 if '.' in fk_name[0] else 0  # проверка на наличие Mr. или Mrs. перед имнем, для фомроваия f строки

        lname.append(f"{fk_name[i]} {fk_name[i+1].lower()}.{fk_name[i][0].lower()}.{pr_name}@fakemail.fk")

    return ', '.join(lname)


# task 3 --------------------------------------------------------------------
def read_csv(name: str = "hw_2.csv"):
    with open(name, "r") as csv_file:
        data = []
        reader = csv.DictReader(csv_file)
        for row in reader:
            dct = {key.strip(): val.strip() for key, val in row.items()}
            data.append(dct)
    return data


# task 4 --------------------------------------------------------------------
def get_astros():
    return requests.get('http://api.open-notify.org/astros.json')
    # return url.json()['number']
