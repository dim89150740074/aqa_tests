import sqlite3
from collections import namedtuple
from selenium import webdriver
import pytest
from faker import Faker # Позволяет генерировать данные, pip3 install faker

fake = Faker() # Через этот обьект будет генерировать данные


@pytest.fixture(name='db_con')
def db_connection():
    connection = sqlite3.connect("test.db")
    print("Соединение с БД установлено")
    yield connection
    connection.close()
    print("Соединение с БД закрыто")

@pytest.fixture
def db_connection2(request):
    connection = sqlite3.connect("test.db")
    request.cls.connection = connection


@pytest.fixture
def generate_data():
    login = fake.email()
    password = fake.password()
    yield login, password
    print("Тест выполнен")

@pytest.fixture
def generate_data2():
    login = fake.email()
    password = fake.password()
    GenLogPass = namedtuple("_", ["login", "password"])
    return GenLogPass(login, password)

class LoginPasswordGen:
    login: str = fake.email()
    password: str = fake.password()

@pytest.fixture
def generate_data3():
    return LoginPasswordGen()

@pytest.fixture
def generate_data4(request):
    request.cls.login = fake.email()
    request.cls.password = fake.password()

@pytest.fixture(name="db_conn3")
def db_connection3(request):
    request.cls.connection = sqlite3.connect("test.db")
    print("Соединение с БД установлено")
    yield
    request.cls.connection.close()
    print("Соединение с БД закрыто")

@pytest.fixture(name="browser")
def get_chrome_driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless=new")
    options.page_load_strategy = "eager"
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    print("драйвер создан")
    yield
    driver.quit()
    print("драйвер закрыт")





@pytest.fixture
def upper_param(request):
    res = request.param
    return res.upper()

@pytest.mark.parametrize('upper_param', ['one', 'two', 'three', 'four'], indirect=True)
def test_parampampam(upper_param):
    print(upper_param)































