from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

class Test_2link():
    def test_link_1(self):
        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first:required")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".second:required")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".third:required")
        input3.send_keys("Petrov@gmail.com")
        input4 = browser.find_element(By.CSS_SELECTOR, ".second_block .first_class .form-control.first")
        input4.send_keys("89994447788")
        input5 = browser.find_element(By.CSS_SELECTOR, ".second_block .second_class .form-control.second")
        input5.send_keys("Russia, Ufa")
        time.sleep(0.3)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert (welcome_text, "Congratulations! You have successfully registered!")

    def test_link_2(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first:required")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".second:required")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".third:required")
        input3.send_keys("Petrov@gmail.com")
        input4 = browser.find_element(By.CSS_SELECTOR, ".second_block .first_class .form-control.first")
        input4.send_keys("89994447788")
        input5 = browser.find_element(By.CSS_SELECTOR, ".second_block .second_class .form-control.second")
        input5.send_keys("Russia, Ufa")
        time.sleep(0.3)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert(welcome_text, "Congratulations! You have successfully registered!")

if __name__ == "__main__": unittest.main()