import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FilterBy:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_first(self):
        wait = WebDriverWait(self.driver, 10)
        list = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'uitk-action-list')))

        list_items = list.find_elements(By.CLASS_NAME, 'uitk-action-list-item')
        if len(list_items) > 0:
            item = list_items[1]
            item.click()
            time.sleep(2)

        click_search = self.driver.find_element(By.ID, 'search_button')
        click_search.click()
        time.sleep(5)

    def click_sort_by_button(self):
        click_sort = self.driver.find_element(By.ID, 'sortTriggerPill')
        click_sort.click()
        time.sleep(4)

        radio_group = self.driver.find_element(By.CLASS_NAME, 'uitk-radio-button-group')

        radio_buttons = radio_group.find_elements(By.CLASS_NAME, 'uitk-radio-button')
        for radio_button in radio_buttons:
            label = radio_button.find_element(By.CLASS_NAME, 'uitk-radio-button-label-content')
            if label.text == "Price: low to high":
                label.click()
                time.sleep(4)

            button = self.driver.find_elements(By.TAG_NAME, 'button')

            for button in button:
                if button.text == "Done":
                    button.click()
                    break

    def get_hotel_prices(self):
        price_elements = self.driver.find_elements(By.CLASS_NAME, 'uitk-action-list no-bullet')
        prices = []
        for element in price_elements:
            price_text = element.text.strip('$')
            if price_text.isdigit():
                prices.append(int(price_text))
        return prices






