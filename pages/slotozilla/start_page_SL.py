from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from constants.slotozilla.start_page_sl_constants import StartPageSLConstants
from pages.slotozilla.base_page_SL import SLBasePage
from selenium.webdriver.support import expected_conditions as EC


class StartPageSL(SLBasePage):
    def __init__(self):
        super().__init__()
        self.constants = StartPageSLConstants

    def driver_current_url(self, url):
        self.driver.get(url)
        return self.driver.current_url

    def driver_get_h1(self, url):
        self.driver.get(url)
        # h1 = self.driver.find_element(By.XPATH, value=StartPageSLConstants.H1_XPATH)
        h1 = self.wait.until(EC.visibility_of_element_located(StartPageSLConstants.H1_XPATH))
        return h1.text

    def driver_get_tag(self, url):
        self.driver.get(url)
        tag_a = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))
        href_value = tag_a.get_attribute("href")
        return href_value

    def driver_search(self, url):
        self.driver.get(url)
        search_button = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, StartPageSLConstants.HEADER_SEARCH_BUTTON_XPATH)))
        search_button.click()
        input_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, StartPageSLConstants.INPUT_FIELD_XPATH)))
        input_field.click()
        input_field.clear()
        input_field.send_keys(StartPageSLConstants.SEARCH_VALUE_TEXT)
        input_field.send_keys(Keys.ENTER)
        nothing_found_message = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, StartPageSLConstants.NOTHING_FOUND_XPATH)))
        nothing_found_message_text = nothing_found_message.text
        return nothing_found_message_text

    def search_list(self, url):
        self.driver.get(url)
        search_button = self.driver.find_element(By.XPATH, StartPageSLConstants.HEADER_SEARCH_BUTTON_XPATH)
        search_button.click()
        input_field = self.driver.find_element(By.XPATH, StartPageSLConstants.INPUT_FIELD_XPATH)
        input_field.click()
        input_field.clear()
        input_field.send_keys(StartPageSLConstants.SEARCH_VALUE_TEXT)
        search_list = self.driver.find_element(By.XPATH, "//div[contains(@class,'autocomplete-group-cover software')]")
        input_field.send_keys(Keys.ENTER)
        nothing_found_message = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, StartPageSLConstants.NOTHING_FOUND_XPATH)))
        nothing_found_message_text = nothing_found_message.text
        return nothing_found_message_text

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
