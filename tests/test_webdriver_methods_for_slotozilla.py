from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://slotozilla.com'


class Configure:
    def driver_current_url(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(1)
        driver.get(url)
        sleep(1)
        return driver.current_url

    def driver_get_text(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(5)
        driver.get(url)
        sleep(5)
        h3 = driver.find_element(By.XPATH, value=".//h3[contains(.,'Great Selection of Casino Games')]")
        print(h3)
        h3_text = h3.text
        sleep(2)
        return h3_text

    def driver_get_tag(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(5)
        driver.get(url)
        sleep(5)
        tag_a = driver.find_element(By.TAG_NAME, value="a")
        href_value = tag_a.get_attribute("href")
        return href_value

    def driver_search(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(5)
        driver.get(url)
        search_button = driver.find_element(by=By.XPATH, value=".//div[@class='header-search-hide']")
        sleep(1)
        search_button.click()
        sleep(2)
        input_field = driver.find_element(By.XPATH, value=".//input[@class='header-search-input']")
        input_field.click()
        sleep(2)
        input_field.clear()
        input_field.send_keys("qwerty")
        sleep(2)
        input_field.send_keys(Keys.ENTER)
        sleep(1)
        nothing_found_message = driver.find_element(by=By.XPATH,
                                                    value=".//div[@class='nothing-found'][contains(.,'It seems we can’t find what you’re looking for. Perhaps you should try again with a different search term.')]")
        nothing_found_message_text = nothing_found_message.text
        return nothing_found_message_text

    def driver_switcher(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(5)
        driver.get(url)
        ref_button = driver.find_element(by=By.XPATH,
                                         value=".//span[@class='sloto-button sloto-button__yellow'][contains(.,'Play')][3]")
        ref_button.click()
        sleep(1)


conf = Configure()
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
