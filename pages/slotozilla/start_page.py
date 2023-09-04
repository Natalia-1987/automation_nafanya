from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.slotozilla.base_page import SLBasePage


class StartPageSL(SLBasePage):
    def __init__(self):
        super().__init__()

    def driver_current_url(self, url):
        self.driver.get(url)
        return self.driver.current_url

    def driver_get_text(self, url):
        self.driver.get(url)
        h3 = self.driver.find_element(By.XPATH, value=".//h3[contains(.,'Great Selection of Casino Games')]")
        h3_text = h3.text
        return h3_text

    def driver_get_tag(self, url):
        self.driver.get(url)
        tag_a = self.driver.find_element(By.TAG_NAME, value="a")
        href_value = tag_a.get_attribute("href")
        return href_value

    def driver_search(self, url):
        self.driver.get(url)
        sleep(1)
        search_button = self.driver.find_element(by=By.XPATH, value=".//div[@class='header-search-hide']")
        sleep(1)
        search_button.click()
        sleep(2)
        input_field = self.driver.find_element(By.XPATH, value=".//input[@class='header-search-input']")
        input_field.click()
        sleep(2)
        input_field.clear()
        input_field.send_keys("qwerty")
        sleep(2)
        input_field.send_keys(Keys.ENTER)
        sleep(1)
        nothing_found_message = self.driver.find_element(by=By.XPATH,
                                                         value=".//div[@class='nothing-found'][contains(.,'It seems we can’t find what you’re looking for. Perhaps you should try again with a different search term.')]")
        nothing_found_message_text = nothing_found_message.text
        return nothing_found_message_text
