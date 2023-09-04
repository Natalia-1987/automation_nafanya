from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://slotozilla.com'


class SLConfigure:

    # def driver_switcher(self, url):
    #     options = ChromeOptions()
    #     options.headless = False
    #     options.add_argument("--incognito")
    #     driver = webdriver.Chrome(options=options)
    #     driver.maximize_window()
    #     sleep(5)
    #     driver.get(url)
    #     ref_button = driver.find_element(by=By.XPATH,
    #                                      value=".//span[@class='sloto-button sloto-button__yellow'][contains(.,'Play')][3]")
    #     ref_button.click()
    #     sleep(1)


conf = SLConfigure()
'''tests'''


def test_compare_url():
    assert conf.driver_current_url(url) == "https://www.slotozilla.com/"


def test_h3_text():
    assert conf.driver_get_text(url) == "Great Selection of Casino Games"


def test_href():
    assert conf.driver_get_tag(url) == "https://www.slotozilla.com/au/"


def test_search():
    assert conf.driver_search(
        url) == "It seems we can’t find what you’re looking for. Perhaps you should try again with a different search term."


def test_switcher():
    conf.driver_switcher(url)

# new_tab = driver.switch_to.window(driver.window_handles[1])
