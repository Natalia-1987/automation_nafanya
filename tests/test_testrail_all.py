import requests
from pages.slotozilla.start_page_SL import SLBasePage
import pytest
import logging
from datetime import datetime
import pytz  # бібліотека для роботи з часовими поясами

# from decouple import config # для діставання токену з конфігу


"""Підготовка до початку:
1)	Документація testrail (для ознайомлення) https://support.testrail.com/h/en-us/articles/7077083596436-Introduction-to-the-TestRail-API
2)	Отримати в testrail apikey https://www.youtube.com/watch?v=nDPQ-5ce1pI
3)  Згенерувати token для testrail (я робив через postman)
4)	Зробити testrun в testrail (куди будемо відправляти результати)
5)	Ознайомитися з можливими статусами результатів виконання тесткейсу: get_statuses (Returns a list of available 
test statuses) - GET index.php?/api/v2/get_statuses
GET http://testrail01.slygods.top/index.php?/api/v2/get_statuses
"""

"""ЗМІННІ ЯКІ ПОТРІБНО ЗАПОВНИТИ!!!"""

# вказати токен з яким ви заходите в тестреіл.
# береться з Postman після GET запиту в консолі розкриваємо і там є Authorization
token_testrail = 'Basic Z29tZWhlMzg1M0BpbnRyb2FjZS5jb206Nm5oZDBtSEtwazc5R2NONlhXaXotcW1xNTF0T1RvWWVRMC5sMC5UaDc='
run_id = 6591  # потрібно вказати значення Test Run з тестреіл. наприклад  run_id = 6591 тут http://testrail01.slygods.top/index.php?/runs/view/6498

url_testrail = f'http://testrail01.slygods.top/index.php?/api/v2/add_results_for_cases/{run_id}'
result_tests = {"results": []}

"""Фікстура для логування виконання теста"""


@pytest.fixture
def logger_fixture():
    # Очищаємо попередній лог, якщо він існує
    logging.getLogger("Logs:").handlers = []
    # Отримуємо поточну дату та час по UTC
    current_time_utc = datetime.now(pytz.UTC)
    # Форматуємо поточний час у вигляді рядка
    time_utc = current_time_utc.strftime("%Y-%m-%d %H:%M:%S")
    # Створіть логер або отримайте існуючий логер
    log = logging.getLogger("Logs:")
    # Рівень логування (INFO)
    log.setLevel(logging.INFO)
    # Об'єкт для запису в файл
    log_file_handler = logging.FileHandler('test.log', encoding='utf-8')
    # Рівень логування для об'єкта запису в файл
    log_file_handler.setLevel(logging.INFO)
    # Фрматтер для логування в файл
    log_formatter = logging.Formatter(f'{time_utc} %(levelname)s %(name)s %(message)s (%(filename)s:%(lineno)s)')
    # Приєднаэ об'єкт запису в файл до логера
    log_file_handler.setFormatter(log_formatter)
    # Додаємо об'єкт запису в файл до логера
    log.addHandler(log_file_handler)
    # Повертаємо логер з фікстури
    return log


"""Фікстура повертає поточний час UTC"""


@pytest.fixture
def current_time_utc():
    # Отримуємо поточну дату та час по UTC
    current_time_utc = datetime.now(pytz.UTC)
    # Форматуємо поточний час у вигляді рядка
    time_utc = current_time_utc.strftime("%Y-%m-%d %H:%M:%S")
    return time_utc


"""Фікстура додає до запиту в testrail інформацію про виконання тесту"""


@pytest.fixture
def request_testrail(
        current_time_utc):  # використовуємо фікстуру current_time_utc для вказання в коментарях часу виконання тесту
    def inner(result, expected_result, case_id):  # функція необхідна щоб приймати аргументи які вказуються в тесті
        if result == expected_result:  # умова повторюється з assert самого тесту
            result_in_comment = 'passed'  # це коментар який передаємо в тестреіл
            status_id = 1  # це статус виконання для тестреіл. Статуси можна глянути тут гетом http://testrail01.slygods.top/index.php?/api/v2/get_statuses
        else:
            result_in_comment = 'failed'  # це коментар який передаємо в тестреіл в разі якщо умова не виконалася
            status_id = 5  # це статус виконання для тестреіл. Статуси можна глянути тут гетом http://testrail01.slygods.top/index.php?/api/v2/get_statuses
        result_tests["results"].append({  # формуємо масив результатів виконання тестів який буде передано в testrail
            "case_id": case_id,
            "status_id": status_id,
            "comment": f"Autotest {result_in_comment}\n run at {current_time_utc} UTC"
        })
        return result_in_comment  # повертаємо результат виконання теста

    return inner


"""post_result_testrail - відправляємо результати відпрацювання тестів в testrail"""


def post_result_testrail(result_tests):  # передаємо результати для відправки
    headers_testrail = {'Authorization': f'{token_testrail}', 'Content-Type': 'application/json'}
    body = result_tests  # передаємо в body запиту результати
    try:
        response_testrail = requests.post(url_testrail, json=body, headers=headers_testrail)
    except Exception as e:
        print(e)  # якщо виникне якийсь Exception то відображаю в консолі
    if response_testrail.status_code == 200:
        result_post_testrail = True  # якщо стату 200 то ставлю статус успішної відправки
        result_tests = {"results": []}  # після успішної відправки очищаю змінну
    else:
        result_post_testrail = False
    return result_post_testrail  # повертаю статус відправлення


"""test_login_page - перевірка завантаження сторінки логіна і перевіряємо поля та кнопку входу"""


def test_login_page(logger_fixture, request_testrail):  # використовую 2 фікстури
    log = logger_fixture
    expected_result = True  # задаю очікуваний результат для порівняння успішності виконання тесту
    case_id = 198559  # ID test case в testrail
    try:
        result = True  # записую результат виконання теста
        result_in_comment = request_testrail(result, expected_result,
                                             case_id)  # отримую статус виконання тесту (для відобораження результату в логах) та передаю в фікстуру необхідні параметри
        assert result == expected_result  # виконується порівняння
        log.info(f'Тест має статус виконання "{result_in_comment}", був запущений')  # логую результат виконання теста
    except Exception as e:  # якщо виник любий exception під час виконання тесту
        result = None  # обов'язкові дані для проставляння неуспішного результату в фікстурі для testrail
        result_in_comment = request_testrail(result, expected_result,
                                             case_id)  # отримую статус виконання тесту (для відобораження результату в логах) та передаю в фікстуру необхідні параметри
        log.info(
            f'Тест має статус виконання "{result_in_comment}", помилка {str(e)}, був запущений')  # в логи записую статус виконання та саму помилку
        pytest.fail(
            f'Тест не вдалося виконати через помилку: {str(e)}')  # позначаю що даний тест неуспішний та вивожу помилку


"""test_post_result_testrail - відправляємо результати в testrail"""


def test_post_result_testrail():
    print(result_tests)  # для себе вивожу в консоль результати які передаються в testrail
    assert post_result_testrail(result_tests) == True

# 6nhd0mHKpk79GcN6XWiz-qmq51tOToYeQ0.l0.Th7 - API Keys в testrail в My Settings у вкладці API Keys створити Add Key
# (при цьому логін gomehe3853@introace.com в Email Address в USER)
# 6591 - id TestRun (run_id)
# 198564 - ID test case в testrail
