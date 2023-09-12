import pytest
from constants.slotozilla.start_page_sl_constants import StartPageSLConstants
from pages.slotozilla.start_page_SL import StartPageSL
from constants.slotozilla.start_page_sl_expected_results import StartPageSLExpectedResults

start_page = StartPageSL()


@pytest.mark.skip(reason="Не хочу")
def test_h1():
    assert start_page.driver_get_h1(StartPageSLConstants.URL) == "Find the Best Online Casinos at Slotozilla"


@pytest.mark.xfail(reason="xfail")
def test_h1():
    assert start_page.driver_get_h1(StartPageSLConstants.URL) == "Find the Best Online Casinos at Slotozilla"


@pytest.mark.parametrize("url", [StartPageSLConstants.URL, "https://www.google.com/"])
def test_compare_url(url):
    assert start_page.driver_current_url(url) == "https://www.slotozilla.com/"


# pytest test_failed.py --maxfail=2