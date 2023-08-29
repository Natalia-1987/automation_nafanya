from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import time


class TestExample:
    def test_example(self):
        options = Options()
        options.headless = False
        options.add_argument("__incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

        driver.get("http://slotozilla.com")
        time.sleep(5)
        driver.quit()
