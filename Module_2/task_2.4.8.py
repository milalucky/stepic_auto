from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# ищем кнопку
button = browser.find_element(By.ID, 'book')
# ждем пока снизится цена до 100$
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button.click()
#скролл страницы
button_1 = browser.find_element(By.ID, 'solve')
browser.execute_script("return arguments[0].scrollIntoView(true);", button_1)
#находим x
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)
#вводим ответ
input_1 = browser.find_element(By.ID, 'answer')
input_1.send_keys(y)
#отправляем форму
button_1.click()
time.sleep(5)