from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time,math, os

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:

  browser = webdriver.Chrome()
  # говорим WebDriver искать каждый элемент в течение 5 секунд
  browser.implicitly_wait(5)

  browser.get("http://suninjuly.github.io/wait1.html")

  button = browser.find_element_by_id("verify")
  button.click()
  message = browser.find_element_by_id("verify_message")

  assert "successful" in message.text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла