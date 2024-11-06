import time
from selenium.webdriver.common.by import By


class searchFunction:
    def __init__(self, driver):
        self.driver = driver

    def search_functionality(self, search_text):
        click = self.driver.find_element(By.CLASS_NAME, 'uitk-typeahead')
        time.sleep(2)
        click.click()

        sss = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Going to"]')
        # self.driver.implicitly_wait(10)
        time.sleep(3)
        sss.click()

        sss.send_keys(search_text)
        time.sleep(3)

        search_results = self.driver.find_elements(By.CSS_SELECTOR, '.uitk-typeahead-result-item '
                                                                    '.typeahead-custom-truncate-strong')
        found_categories = []
        for result in search_results:
            category_name = result.text
            if search_text in category_name.lower():
                found_categories.append(category_name)
        # assert len(found_categories) > 0, f"No categories containing '{search_text}' were found."
        print("Found categories:", found_categories)


