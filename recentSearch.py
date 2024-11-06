import time
from selenium.webdriver.common.by import By


class RecentSearch:
    def __init__(self, driver):
        self.driver = driver

    def go_to_home_page(self):
        click = self.driver.find_element(By.CLASS_NAME, 'uitk-header-brand-logo')
        time.sleep(2)
        click.click()

    def go_to_recent_search(self, search_text):
        self.go_to_home_page()

        sss = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Going to"]')
        sss.click()
        time.sleep(3)

        sss.send_keys(search_text)
        time.sleep(3)

        searchButton = self.driver.find_element(By.ID, 'search_button')
        searchButton.click()
        time.sleep(2)

        self.go_to_home_page()


