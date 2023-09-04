from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://automatenspielex.com/'


class Configure:
    def driver_current_url(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(2)
        driver.get(url)
        sleep(2)
        return driver.current_url

    def driver_get_text_h1(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(2)
        driver.get(url)
        sleep(2)
        h1 = driver.find_element(By.XPATH, value=".//h1[contains(.,'Automatenspiele Kostenlos Spielen')]")
        h1_text = h1.text
        sleep(2)
        return h1_text

    def driver_first_menu_item(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(2)
        driver.get(url)
        sleep(2)
        first_menu_item = driver.find_element(By.TAG_NAME, value="a")
        first_menu_item_value = first_menu_item.get_attribute("href")
        return first_menu_item_value

    def driver_search(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(5)
        driver.get(url)
        search_button = driver.find_element(by=By.XPATH, value=".//div[@class='search-btn']")
        sleep(1)
        search_button.click()
        sleep(2)
        input_field = driver.find_element(By.XPATH, value=".//input[@class='searchform__input']")
        input_field.click()
        sleep(2)
        input_field.clear()
        input_field.send_keys("qwerty")
        sleep(2)
        input_field.send_keys(Keys.ENTER)
        sleep(1)
        nothing_found_message = driver.find_element(By.XPATH,
                                                    value=".//h2[@class='not_found']")
        nothing_found_message_text = nothing_found_message.text
        return nothing_found_message_text

    def driver_amount_of_slots(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(2)
        driver.get(url)
        sleep(2)
        amount = driver.find_element(By.XPATH, value=".//div[@id='slots-count']")
        amount_of_slots = amount.text
        sleep(2)
        return amount_of_slots

    def driver_following_link_to_page_casino(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(2)
        driver.get(url)
        sleep(2)
        link_to_page_casino = driver.find_element(By.XPATH,
                                                  value="//*[@id='sub-header-lg']/div/div[3]/div/div/ul/li[1]/figure/a")
        sleep(2)
        link_to_page_casino.click()
        sleep(2)
        return driver.current_url

    def driver_check_search_in_filter_block(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(2)
        driver.get(url)
        search_field = driver.find_element(By.XPATH, value=".//input[@id='slots-search-input']")
        sleep(2)
        search_field.click()
        sleep(2)
        search_field.clear()
        search_field.send_keys("Doom of Dead")
        sleep(2)
        found_slot = driver.find_element(By.XPATH,
                                         value="//*[@id='slots-container']/div/a/figure/figcaption/span")
        slot_title = found_slot.text
        print(slot_title)
        return slot_title

    def driver_check_up_to_top_button(self, url):
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(2)
        driver.get(url)
        sleep(2)
        # цей блок кода я використала тільки для того, щоб змусити драйвер прокрутити сторінку вниз,
        # щоб ця кнопка "Up to top" з'явилась, бо спочатку на сторінці її немає.
        # Дуже примітивний звичайно ж спосіб, аде працює :)
        search_field = driver.find_element(By.XPATH, value=".//input[@id='slots-search-input']")
        sleep(2)
        search_field.click()
        #
        up_to_top_button = driver.find_element(By.XPATH, value=".//div[@id='scroller']")
        up_to_top_button.click()
        up_text_h1 = driver.find_element(By.XPATH,
                                         value=".//h1[contains(.,'Automatenspiele Kostenlos Spielen')]")
        text_h1 = up_text_h1.text
        return text_h1


conf = Configure()
'''first tests'''


def test_compare_url():
    assert conf.driver_current_url(url) == "https://automatenspielex.com/"


def test_h1_text():
    assert conf.driver_get_text_h1(url) == "AUTOMATENSPIELE KOSTENLOS SPIELEN"


def test_href():
    assert conf.driver_first_menu_item(url) == "https://automatenspielex.com/kostenlos-spiele/ohne-anmeldung"


def test_not_found_text():
    assert conf.driver_search(
        url) == "Entschuldigung, Ihr Suchbegriff hat keinen Treffer ergeben. Versuchen Sie es bitte mit einem anderen Schlagwort erneut"


def test_amount_of_slots():
    assert conf.driver_amount_of_slots(url) == "1274"


def test_following_link_to_page_casino():
    assert conf.driver_following_link_to_page_casino(
        url) == "https://automatenspielex.com/online-casinos/syndicate-casino"


def test_check_search_in_filter_block():
    assert conf.driver_check_search_in_filter_block(url) == "Doom of Dead"


def test_up_to_top_button():
    assert conf.driver_check_up_to_top_button(url) == "AUTOMATENSPIELE KOSTENLOS SPIELEN"
