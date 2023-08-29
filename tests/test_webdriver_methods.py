from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver

from selenium.webdriver.common.by import By

url = 'https://slotozilla.com'


def driver_current_url(url):
    options = ChromeOptions()
    options.headless = False
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    sleep(1)
    driver.get(url)
    sleep(1)
    return driver.current_url


def driver_get_text(url):
    options = ChromeOptions()
    options.headless = False
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    sleep(5)
    driver.get(url)
    sleep(5)
    h3 = driver.find_element(By.XPATH, value="//h3[contains.,'Great Selection of Casino Games']")
    print(h3)
    h3_text = h3.text
    sleep(2)
    return h3


def driver_get_tag(url):
    options = ChromeOptions()
    options.headless = False
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    sleep(5)
    driver.get(url)
    sleep(5)
    tag_a = driver.find_element(by=By.XPATH, value="")
    return tag_a


def test_compare_url():
    assert driver_current_url(url) == "https://www.slotozilla.com/"


def test_h3_text():
    assert driver_get_text(url) == "Great Selection of Casino Games"


def test_get_tag():
    assert driver_get_tag(url) == "https://www.slotozilla.com/"
