import importlib
import test
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

    # test = importlib.import_module('test')
    importlib.reload(test)
    test.test_driver(driver)
