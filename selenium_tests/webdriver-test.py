import importlib
import selenium_tests
from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_argument('--user-data-dir=./temp')
driver = Chrome(options=options)

while True:
    answer = input("Enter command: ")
    print("Answer: " + answer)
    if answer == 'quit' or answer == 'x':
        driver.quit()
        break

    # selenium_tests = importlib.import_module('selenium_tests')
    importlib.reload(selenium_tests)
    selenium_tests.test_driver(driver)
