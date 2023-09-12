from selenium.webdriver.chrome import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait



class SLBasePage:
    def __init__(self, headless=False):
        self.options = ChromeOptions()
        if headless == False:
            self.options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 5)

