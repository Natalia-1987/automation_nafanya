from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from constants.automatenspielex.automatenspielex_start_page_constants import ASStartPageConstants
from pages.automatenspielex.base_page_AS import ASBasePage
from selenium.webdriver.support import expected_conditions as EC


class StartPageAS(ASBasePage):
    def __init__(self):
        super().__init__()

    def driver_current_url(self, url):
        # перехід на вказаний URL
        self.driver.get(url)
        # повертає поточний урл
        return self.driver.current_url

    def driver_get_text_h1(self, url):
        # перехід на вказаний URL
        self.driver.get(url)
        # очікування, що елемент з вказаним локатором буде !видимий! на сторінці
        h1 = self.wait.until(EC.visibility_of_element_located((By.XPATH, ASStartPageConstants.HEADING_H1_XPATH)))
        # знаходження веб-елементу h1 за допомогою метода драйвера find_element по XPATHу
        # h1 = self.driver.find_element(By.XPATH, value=ASStartPageConstants.HEADING_H1_XPATH)
        # отримання текстового вмісту h1
        h1_text = h1.text
        # повернення тексту h1
        return h1_text

    def driver_first_menu_item(self, url):
        # перехід на вказаний URL
        self.driver.get(url)
        # очікування, що елемент з вказаним локатором буде !присутній! на сторінці
        first_menu_item = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, ASStartPageConstants.TAG_A)))
        # знаходження веб-елементу по тегу <a> (нас цікавить саме перше посилання з тегом <a> на сторінці) за допомогою метода драйвера find_element
        # first_menu_item = self.driver.find_element(By.TAG_NAME, value=ASStartPageConstants.TAG_A)
        # отримання значення атрибуту href тега <a>
        first_menu_item_value = first_menu_item.get_attribute(ASStartPageConstants.FIRST_MENU_ITEM_HREF)
        # повертає значення атрибуту href тега <a> - це буде посилання, куди веде (на яку сторінку) наш перший пункт хедер-меню
        return first_menu_item_value

    def driver_search(self, url):
        # перехід на вказаний URL
        self.driver.get(url)
        # очікування, що елемент з вказаним локатором буде видимий на сторінці
        search_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, ASStartPageConstants.HEADER_SEARCH_BUTTON_XPATH)))
        # знаходження елементу іконка пошуку за XPATH
        # search_button = self.driver.find_element(by=By.XPATH, value=ASStartPageConstants.HEADER_SEARCH_BUTTON_XPATH)
        # клік на лупу (іконку пошуку)
        search_button.click()
        # очікування, що елемент з вказаним локатором буде видимий на сторінці
        input_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, ASStartPageConstants.INPUT_FIELD_XPATH)))
        # знаходження елементу поля вводу, що з'являється після кліку на іконку пошуку
        # input_field = self.driver.find_element(By.XPATH, value=ASStartPageConstants.INPUT_FIELD_XPATH)
        # клік в полі пошуку, щоб можна було вводити текст
        input_field.click()
        # очищення тексту з поля вводу
        input_field.clear()
        # введення тексту "qwerty" в поле вводу
        input_field.send_keys(ASStartPageConstants.SEARCH_VALUE_TEXT)
        # натискання клавіши "Enter"
        input_field.send_keys(Keys.ENTER)
        # очікування, що елемент з вказаним локатором буде видимий на сторінці
        nothing_found_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, ASStartPageConstants.NOTHING_FOUND_XPATH)))
        # знаходження h2 по XPATHу
        # nothing_found_message = self.driver.find_element(By.XPATH, value=ASStartPageConstants.NOTHING_FOUND_XPATH)
        # отримання текстового вмісту тега <h2>
        nothing_found_message_text = nothing_found_message.text
        # повернення тексту заголовка h2
        return nothing_found_message_text

    def driver_amount_of_slots(self, url):
        # відкриває url
        self.driver.get(url)
        amount = self.driver.find_element(By.XPATH, value=ASStartPageConstants.AMOUNT_OF_SLOTS_XPATH)
        amount_of_slots = amount.text
        return amount_of_slots

    def driver_following_link_to_page_casino(self, url):
        # відкриває url
        self.driver.get(url)
        link_to_page_casino = self.driver.find_element(By.XPATH, value=ASStartPageConstants.LINK_TO_PAGE_CASINO_XPATH)
        link_to_page_casino.click()
        return self.driver.current_url

    def driver_check_search_in_filter_block(self, url):
        self.driver.get(url)
        search_field = self.driver.find_element(By.XPATH, value=ASStartPageConstants.SORT_SEARCH_BUTTON_XPATH)
        search_field.click()
        search_field.clear()
        search_field.send_keys(ASStartPageConstants.SEARCH_IN_FILTER_BLOCK_VALUE_TEXT)
        found_slot = self.driver.find_element(By.XPATH, value=ASStartPageConstants.FIND_SLOT_XPATH)
        slot_title = found_slot.text
        return slot_title

    def driver_check_up_to_top_button(self, url):
        self.driver.get(url)
        # цей блок кода я використала тільки для того, щоб змусити драйвер прокрутити сторінку вниз,
        # щоб ця кнопка "Up to top" з'явилась, бо спочатку на сторінці її немає.
        # Дуже примітивний звичайно ж спосіб, аде працює :)
        search_field = self.driver.find_element(By.XPATH, value=ASStartPageConstants.SORT_SEARCH_BUTTON_XPATH)
        search_field.click()
        # знаходимо елемент - а саме кнопку, яка прогортає сторінку на самий верх
        up_to_top_button = self.driver.find_element(By.XPATH, value=ASStartPageConstants.UP_TO_TOP_BUTTON_XPATH)
        # натискаємо на цю кнопку
        up_to_top_button.click()
        # після прогортання ми маємо знайти елемент - а саме тег h1
        up_text_h1 = self.driver.find_element(By.XPATH, value=ASStartPageConstants.HEADING_H1_XPATH)
        # отримуємо безпосередньо текстове значення з тега h1
        text_h1 = up_text_h1.text
        # повертаємо це текстове значення з тега h1
        return text_h1

