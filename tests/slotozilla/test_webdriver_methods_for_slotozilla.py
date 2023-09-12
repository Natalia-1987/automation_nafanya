from constants.slotozilla.start_page_sl_constants import StartPageSLConstants
from pages.slotozilla.start_page_SL import StartPageSL
from constants.slotozilla.start_page_sl_expected_results import StartPageSLExpectedResults

'''tests'''
start_page = StartPageSL()


def test_compare_url():
    assert start_page.driver_current_url(StartPageSLConstants.URL) == StartPageSLExpectedResults.EXPECTED_RESULT_URL


def test_h1_text():
    assert start_page.driver_get_h1(StartPageSLConstants.URL) == StartPageSLExpectedResults.EXPECTED_RESULT_H1_TEXT


def test_a_href(logger_fixture, driver_google):
    assert start_page.driver_get_tag(StartPageSLConstants.URL) == StartPageSLExpectedResults.EXPECTED_RESULT_HREF
    log = logger_fixture
    log.info("test_a_href був запущений")


def test_search(logger_fixture):
    assert start_page.driver_search(
        StartPageSLConstants.URL) == StartPageSLExpectedResults.EXPECTED_RESULT_SEARCH
    log = logger_fixture
    log.info("test_search був запущений")


def test_search_list():
    start_page.search_list(StartPageSLConstants.URL)

# def test_switcher():
#     start_page.conf.driver_switcher(url)

# new_tab = driver.switch_to.window(driver.window_handles[1])
