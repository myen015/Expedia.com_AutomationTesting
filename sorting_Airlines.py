import time
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SortingAirlines:
    def __init__(self, driver):
        self.driver = driver

    def go_to_accordion(self):
        click = self.driver.find_element(By.CSS_SELECTOR, '#primary-navigation > div > button')
        click.click()
        time.sleep(3)

        menu_locator = (By.CLASS_NAME, "uitk-menu-container")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(menu_locator))

        flights_link = self.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Flights']")
        flights_link.click()
        time.sleep(2)

        one_way_button = self.driver.find_element(By.CLASS_NAME, 'uitk-tab-anchor')
        one_way_button.click()
        time.sleep(2)

        first_country = self.driver.find_element(By.CLASS_NAME, 'uitk-input-swapper-start-input')
        first_country.click()
        first_country.send_keys("Istanbul")
        first_country.send_keys(Keys.ENTER)
        time.sleep(2)

        second_country = self.driver.find_element(By.CLASS_NAME, 'uitk-input-swapper-end-input')
        second_country.click()
        second_country.send_keys("New York")
        second_country.send_keys(Keys.ENTER)
        time.sleep(2)

        button = self.driver.find_elements(By.TAG_NAME, 'button')

        for button in button:
            if button.text == "Search":
                button.click()
                break

    def fetch_list_airlines(self):
        fieldset = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "fieldset[data-test-id='filter-container']")))

        nonstop_checkbox = fieldset.find_element(By.XPATH,
                                                 ".//label[contains(text(), 'Nonstop')]/preceding-sibling::input["
                                                 "@type='checkbox']")
        nonstop_checkbox.click()
        self.driver.implicitly_wait(1)
        nonstop_count_element = self.driver.find_element(By.XPATH, "//label[contains(text(), 'Nonstop')]")
        nonstop_count = nonstop_count_element.text.strip().split()[1]

        return nonstop_count

    def fetched_airlines(self):
        list_airlines = self.driver.find_elements(By.XPATH, '//*[@data-test-id="offer-listing"]')
        available_count = len(list_airlines)
        return available_count
