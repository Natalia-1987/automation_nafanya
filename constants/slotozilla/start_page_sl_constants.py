from selenium.webdriver.common.by import By


class StartPageSLConstants:
    URL = "https://www.slotozilla.com/"
    H1_XPATH = (By.XPATH, "//h1[contains(., 'Find the Best Online Casinos at Slotozilla')]")
    GG_BET_GET_BONUS_XPATH = ".//div[@data-pid='ggbet-casino-wb-en']"
    HEADER_SEARCH_BUTTON_XPATH = ".//div[@id='header-search-hide']"
    LOGIN_VALUE_ADMIN = "QWERTY12345"
    INPUT_FIELD_XPATH = ".//input[@class='header-search-input']"
    NOTHING_FOUND_XPATH = ".//div[@class='nothing-found'][contains(.,'It seems we can’t find what you’re looking for. Perhaps you should try again with a different search term.')]"
    SEARCH_VALUE_TEXT = "slotozilla_1111"

