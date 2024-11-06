import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from recentSearch import RecentSearch
from search_functionality import searchFunction
from filterBy import FilterBy
from add_Seat_Place import Place
from sorting_Airlines import SortingAirlines


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.expedia.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_search_Function(driver):
    search = searchFunction(driver)
    search.search_functionality("Ist")


def test_filter_functionality(driver):
    filter = FilterBy(driver)
    filter.navigate_to_first()
    initial_prices = filter.get_hotel_prices()
    print("Initial prices:", initial_prices)

    filter.click_sort_by_button()
    sorted_prices = filter.get_hotel_prices()
    print("Sorted prices:", sorted_prices)

    assert len(initial_prices) == len(sorted_prices), "Number of prices should not change after sorting!"
    for i in range(len(sorted_prices) - 1):
        assert sorted_prices[i] <= sorted_prices[
            i + 1], f"Prices are not sorted correctly at index "


def test_sort_functionality(driver):
    sort = SortingAirlines(driver)
    initial_count = sort.fetched_airlines()
    available_count = sort.fetched_airlines()
    if len(initial_count) != len(available_count):
        print("Success")


def test_recent_Search(driver):
    history = RecentSearch(driver)
    history.go_to_recent_search("Tashkent")

    carousel = driver.find_element(By.CLASS_NAME, 'uitk-carousel-item')
    text_div = carousel.find_element(By.XPATH,
                                     ".//div[contains(@class, 'uitk-text') and contains(@class, "
                                     "'uitk-type-400')]")

    text = text_div.text

    if "Tashkent" in text:
        print("The word 'Tashkent' is present in the text:", text)
    else:
        print("The word 'Tashkent' is not present in the text:", text)


def test_add_Seat_Place(driver):
    placing = Place(driver)
    placing.buy_Flight()
    initial_prices = placing.choose_place()
    print("Initial prices:", initial_prices)
    placing.choose_place()
    after_price = placing.choose_place()
    assert initial_prices != after_price, "Success"


