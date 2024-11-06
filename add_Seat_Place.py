import time
from selenium.webdriver.common.by import By


class Place:
    def __init__(self, driver):
        self.driver = driver

    def buy_Flight(self):
        self.driver.execute_script("window.scrollBy(0, 200);")
        first_element = self.driver.find_element(By.CSS_SELECTOR, "li[data-test-id='offer-listing']")
        first_element.click()
        time.sleep(2)

        select = self.driver.find_element(By.CSS_SELECTOR, 'div.uitk-layout-flex > div.uitk-spacing > button')
        select.click()
        time.sleep(2)

        no_click = self.driver.find_elements(By.TAG_NAME, 'a')

        for button in no_click:
            if button.text == "No thanks":
                button.click()
                break

    def seat_place(self):
        checkOut_price = self.driver.find_element(By.CLASS_NAME, 'uitk-heading uitk-heading-5')
        price_text = checkOut_price.text.strip('$')
        price = int(price_text)
        return price

    def choose_place(self):
        click_place = self.driver.find_elements(By.TAG_NAME, 'button')

        for button in click_place:
            if button.text == "Choose your seat":
                button.click()
                break

        seat = self.driver.find_element(By.CLASS_NAME, 'uitk-seat-map-button')
        seat.click()
        time.sleep(2)

        selectPlace = self.driver.find_elements(By.TAG_NAME, 'button')

        for button in selectPlace:
            if button.text == "Select seat":
                button.click()
                break

        returnTo = self.driver.find_element(By.CLASS_NAME, 'uitk-icon')
        returnTo.click()
        time.sleep(2)

        returnPlace = self.driver.find_elements(By.TAG_NAME, 'button')

        for button in returnPlace:
            if button.text == "Save & close":
                button.click()
                break

