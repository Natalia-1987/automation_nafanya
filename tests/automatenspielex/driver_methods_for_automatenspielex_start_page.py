from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://automatenspielex.com/'


class ASConfigure:
    def driver_current_url(self, url):
        # відкриває сторінку браузера
        options = ChromeOptions()
        options.headless = False
        # відкриває в режимі інкогніто
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        # збільшуємо вікно браузера на весь екран
        driver.maximize_window()
        sleep(2)
        # перехід на вказаний URL
        driver.get(url)
        sleep(2)
        # повертає поточний урл
        return driver.current_url

    def driver_get_text_h1(self, url):
        # відкриває сторінку браузера
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(2)
        # перехід на вказаний URL
        driver.get(url)
        sleep(2)
        # знаходження h1 по XPATHу
        h1 = driver.find_element(By.XPATH, value=".//h1[contains(.,'Automatenspiele Kostenlos Spielen')]")
        # отримання текстового вмісту h1
        h1_text = h1.text
        sleep(2)
        # повернення тексту h1
        return h1_text

    def driver_first_menu_item(self, url):
        # відкриває сторінку браузера
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(2)
        # перехід на вказаний URL
        driver.get(url)
        sleep(2)
        # знаходження елементу по тегу <a> (буде знайдено перший)
        first_menu_item = driver.find_element(By.TAG_NAME, value="a")
        # отримання значення атрибуту href тега <a>
        first_menu_item_value = first_menu_item.get_attribute("href")
        # повертає значення атрибуту href тега <a> - це буде посилання, куди веде (на яку сторінку) наш перший пункт хедер-меню
        return first_menu_item_value

    def driver_search(self, url):
        # відкриває сторінку браузера
        options = ChromeOptions()
        options.headless = False
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        sleep(5)
        # перехід на вказаний URL
        driver.get(url)
        # знаходження елементу іконка пошуку за XPATH
        search_button = driver.find_element(by=By.XPATH, value=".//div[@class='search-btn']")
        sleep(1)
        # клік на лупу (іконку пошуку)
        search_button.click()
        sleep(2)
        # знаходження елементу поля вводу, що з'являється після кліку на іконку пошуку
        input_field = driver.find_element(By.XPATH, value=".//input[@class='searchform__input']")
        # клік в полі пошуку, щоб можна було вводити текст
        input_field.click()
        sleep(2)
        # очищення тексту з поля вводу
        input_field.clear()
        # введення тексту "qwerty" в поле вводу
        input_field.send_keys("qwerty")
        sleep(2)
        # натискання клавіши "Enter"
        input_field.send_keys(Keys.ENTER)
        sleep(1)
        # знаходження h2 по XPATHу
        nothing_found_message = driver.find_element(By.XPATH,
                                                    value=".//h2[@class='not_found']")
        # отримання текстового вмісту тега <h2>
        nothing_found_message_text = nothing_found_message.text
        # повернення тексту заголовка h2
        return nothing_found_message_text

    def driver_amount_of_slots(self, url):
        # відкриває сторінку браузера
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
        # відкриває сторінку браузера
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
        # відкриває сторінку браузера
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
        # відкриває сторінку браузера
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
        # знаходимо елемент - а саме кнопку, яка прогортає сторінку на самий верх
        up_to_top_button = driver.find_element(By.XPATH, value=".//div[@id='scroller']")
        # натискаємо на цю кнопку
        up_to_top_button.click()
        # після прогортання ми маємо знайти елемент - а саме тег h1
        up_text_h1 = driver.find_element(By.XPATH,
                                         value=".//h1[contains(.,'Automatenspiele Kostenlos Spielen')]")
        # отримуємо безпосередньо текстове значення з тега h1
        text_h1 = up_text_h1.text
        # повертаємо це текстове значення з тега h1
        return text_h1


conf = ASConfigure()
'''first tests'''


def test_compare_url():
    # assert = порівняння. Порівнюємо url, який отримали в результаті роботи методу driver_current_url(url)
    # із заданим нами очікуваним результатом "https://automatenspielex.com/"
    assert conf.driver_current_url(url) == "https://automatenspielex.com/"


def test_h1_text():
    # Порівнюємо значення заголовка h1, який отримали в результаті роботи методу driver_get_text_h1
    # із заданим нами очікуваним результатом "AUTOMATENSPIELE KOSTENLOS SPIELEN"
    assert conf.driver_get_text_h1(url) == "AUTOMATENSPIELE KOSTENLOS SPIELEN"


def test_href():
    # Порівнюємо значення атрибуту href першого тега <a> на сторінці, який отримали в результаті роботи методу
    # driver_first_menu_item із заданим нами очікуваним
    # результатом "https://automatenspielex.com/kostenlos-spiele/ohne-anmeldung"
    assert conf.driver_first_menu_item(url) == "https://automatenspielex.com/kostenlos-spiele/ohne-anmeldung"


def test_not_found_text():
    # Порівнюємо на сторінці з результатами пошуку текст заголовка h2 із очікуваним результатом
    # (заданим в адмінці текстом для випадку, коли нічого по запиту не знайдено)
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
