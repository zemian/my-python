from selenium.webdriver import Chrome
driver = Chrome()

while True:
    answer = input("Enter command: ")
    print("Answer: " + answer)
    if answer == 'quit':
        driver.quit()
        break

    with open('temp/test.py') as fh:
        exec(fh.read(), {'driver': driver})
