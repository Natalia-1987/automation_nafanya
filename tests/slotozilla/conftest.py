import logging

import pytest

from selenium import webdriver

from pages.slotozilla.start_page_SL import StartPageSL


@pytest.fixture
def logger_fixture():
    # Створіть логер або отримайте існуючий логер
    log = logging.getLogger("Logs: ")

    # Рівень логування (INFO)
    log.setLevel(logging.INFO)

    # Об'єкт для запису в файл
    log_file_handler = logging.FileHandler('test.log', encoding='utf-8')

    # Рівень логування для об'єкта запису в файл
    log_file_handler.setLevel(logging.INFO)

    # Фрматтер для логування в файл
    log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s (%(filename)s:%(lineno)s)')

    # Приєднаэ об'єкт запису в файл до логера
    log_file_handler.setFormatter(log_formatter)

    # Додаємо об'єкт запису в файл до логера
    log.addHandler(log_file_handler)

    # Повертаємо логер з фікстури
    yield log

    # Необхідно очистити логер після використання, щоб уникнути конфліктів
    log.handlers.clear()


@pytest.fixture(scope="function")
def driver_google():
    # create driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    return driver.current_url


@pytest.fixture()
def search_field(driver_google):
    # create driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    return driver.current_url

@pytest.fixture()
def main_page():
    return StartPageSL()
