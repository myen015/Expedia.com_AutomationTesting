# QA Automation Project – Expedia Website

This repository contains an automation project focused on testing the Expedia website's key functionalities. The project was built using Selenium WebDriver and PyTest, with the primary aim of ensuring the reliability and smooth functioning of critical web features.

## Project Overview

The main goal of this project was to automate the testing of various functionalities on the [Expedia](https://www.expedia.com) website. This includes testing user interactions such as searches, filters, sorting options, and booking workflows to identify any potential bugs or issues.

### Key Features:
- Automated UI testing using **Selenium WebDriver**.
- Structured test cases executed with **PyTest**.
- API testing implemented with **Postman**.
- Debugging and web analysis using **Chrome DevTools**.

## Tools & Technologies Used

- **Programming Language**: Python
- **Frameworks & Libraries**: Selenium, PyTest
- **API Testing**: Postman, Swagger
- **Debugging Tools**: Chrome DevTools
- **Version Control**: Git
- **IDE**: Visual Studio Code

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/myen015/Expedia.com_AutomationTesting.git
   cd expedia-automation-project

Explanation of Test Cases
test_search_Function:

Purpose: Tests the search functionality by entering a search term (e.g., "Ist") and verifying that results populate correctly.
Class Used: searchFunction
Method: search.search_functionality("Ist")
test_filter_functionality:

Purpose: Tests the filter feature by capturing initial hotel prices, applying sorting, and validating that the prices are sorted correctly.
Class Used: FilterBy
Methods:
filter.navigate_to_first(): Navigates to the initial filter view.
filter.get_hotel_prices(): Retrieves prices for comparison.
filter.click_sort_by_button(): Applies the sorting operation.
Assertions: Ensures that the list of hotel prices remains consistent in length and verifies proper sorting order.
test_sort_functionality:

Purpose: Tests airline sorting to confirm that the total number of airlines fetched before and after sorting is consistent.
Class Used: SortingAirlines
Method: sort.fetched_airlines()
Logic: Compares initial and available counts; prints "Success" if the counts differ.
test_recent_Search:

Purpose: Verifies if a recent search (e.g., for "Tashkent") is present in the carousel of recent searches.
Class Used: RecentSearch
Method: history.go_to_recent_search("Tashkent")
Logic:
Locates the carousel item.
Searches for the text "Tashkent" and prints whether it is found.
test_add_Seat_Place:

Purpose: Simulates selecting a seat on a flight and ensures that prices update correctly after selecting a seat.
Class Used: Place
Methods:
placing.buy_Flight(): Initiates the flight purchase process.
placing.choose_place(): Chooses a seat and returns the updated price.
Assertion: Compares the initial and updated prices to confirm that they change after selecting a seat.
