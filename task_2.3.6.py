import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

# решаем уравнение
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
# открываем браузер
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

# клик на кнопку
    button_1 = browser.find_element(By.XPATH, '//button')
    button_1.click()

# переключаемся на новую вкладку
    new_window = browser.window_handles[1]  # получили массив имен вкладок
    browser.switch_to.window(new_window)  # переключились на нужную вкладку

# ищем x
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

# вводим ответ
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

# отправляем форму
    button_1 =  browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button_1.click()
    time.sleep(10)

finally:
    browser.quit()