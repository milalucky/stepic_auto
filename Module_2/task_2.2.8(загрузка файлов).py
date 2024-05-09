# Загрузка файлов
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

#заполнение полей
    name = browser.find_element(By.NAME, 'firstname')
    name.send_keys("Milana")
    last_name = browser.find_element(By.NAME,'lastname')
    last_name.send_keys('Zharkevich')
    email = browser.find_element(By.NAME,'email')
    email.send_keys('mz@mail.ru')

#загрузка файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

#отправляем форму нажав на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
