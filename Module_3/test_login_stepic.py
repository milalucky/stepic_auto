import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


email = "******" #Введи почту
password = "******" #Введи пароль

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
])
def test_login(browser, url):
    link = f"{url}"
    browser.get(link)
    time.sleep(5)

    login = browser.find_element(By.ID, "ember459")
    login.click()
    email_el = browser.find_element(By.ID, "id_login_email")
    email_el.send_keys(email)
    password_el = browser.find_element(By.ID, "id_login_password")
    password_el.send_keys(password)
    button = browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn.button_with-loader')
    button.click()
    time.sleep(6)
    text_area = browser.find_element(By.CSS_SELECTOR, 'textarea.ember-text-area.ember-view.textarea.string-quiz__textarea')
    text_area.send_keys(str(math.log(int(time.time()))))
    time.sleep(2)
    button_send = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission')
    button_send.click()
    time.sleep(15)
    text_el = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
    text_1 = text_el.text
    if text_1 != "Correct!":
        print(f"Actual result for URL {url}: '{text_1}'")

    assert text_1 == "Correct!", f"Expected 'Correct!' but got '{text_1}'"





