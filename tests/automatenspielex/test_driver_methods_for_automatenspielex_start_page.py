import platform

import pytest

from constants.automatenspielex.automatenspielex_start_page_constants import ASStartPageConstants
from constants.automatenspielex.automatenspielex_start_page_expected_results import StartPageASExpectedResults
from pages.automatenspielex.start_page_AS import StartPageAS

start_page = StartPageAS()
'''first tests'''


def test_compare_url():
    # assert = порівняння. Порівнюємо url, який отримали в результаті роботи методу driver_current_url(url)
    # із заданим нами очікуваним результатом "https://automatenspielex.com/"
    assert start_page.driver_current_url(ASStartPageConstants.URL) == StartPageASExpectedResults.EXPECTED_RESULT_URL


def test_h1_text():
    # Порівнюємо значення заголовка h1, який отримали в результаті роботи методу driver_get_text_h1
    # із заданим нами очікуваним результатом "AUTOMATENSPIELE KOSTENLOS SPIELEN"
    assert start_page.driver_get_text_h1(ASStartPageConstants.URL) == StartPageASExpectedResults.EXPECTED_RESULT_H1_TEXT


def test_up_to_top_button():
    assert start_page.driver_check_up_to_top_button(
        ASStartPageConstants.URL) == StartPageASExpectedResults.EXPECTED_RESULT_UP_TO_TOP_BUTTON


@pytest.mark.usefixtures("logger_fixture")
def test_href(logger_fixture):
    # Порівнюємо значення атрибуту href першого тега <a> на сторінці, який отримали в результаті роботи методу
    # driver_first_menu_item із заданим нами очікуваним
    # результатом "https://automatenspielex.com/kostenlos-spiele/ohne-anmeldung"
    assert start_page.driver_first_menu_item(
        ASStartPageConstants.URL) == StartPageASExpectedResults.EXPECTED_RESULT_HREF
    log = logger_fixture
    log.info("test_href був запущений")


def test_not_found_text(logger_fixture):
    # Порівнюємо на сторінці з результатами пошуку текст заголовка h2 із очікуваним результатом
    # (заданим в адмінці текстом для випадку, коли нічого по запиту не знайдено)
    assert start_page.driver_search(
        ASStartPageConstants.URL) == StartPageASExpectedResults.EXPECTED_RESULT_NOT_FOUND_TEXT
    log = logger_fixture
    log.info("test_href був запущений")


def test_amount_of_slots():
    assert start_page.driver_amount_of_slots(
        ASStartPageConstants.URL) == StartPageASExpectedResults.EXPECTED_RESULT_AMOUNT_OF_SLOTS


@pytest.mark.xfail(reason='Потім перероблю цей тест')
def test_following_link_to_page_casino():
    print("HELLLOOO")
    assert start_page.driver_following_link_to_page_casino(
        ASStartPageConstants.URL) == StartPageASExpectedResults.EXPECTED_RESULT_FOLLOWING_LINK_TO_PAGE_CASIN0
    print("GOOOOOODBYE")


@pytest.mark.skip(reason="bug 110")
def test_check_search_in_filter_block():
    assert start_page.driver_check_search_in_filter_block(
        ASStartPageConstants.URL) == StartPageASExpectedResults.EXPECTED_RESULT_SEARCH_IN_FILTER_BLOCK
