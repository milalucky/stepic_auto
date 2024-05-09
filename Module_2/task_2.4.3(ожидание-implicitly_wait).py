from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
# В Selenium WebDriver есть специальный способ организации такого ожидания, который позволяет задать ожидание
# при инициализации драйвера, чтобы применить его ко всем тестам. Ожидание называется неявным (Implicit wait),
# так как его не надо явно указывать каждый раз, когда мы выполняем поиск элементов,
# оно автоматически будет применяться при вызове каждой последующей команды.
browser.implicitly_wait(5)

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text