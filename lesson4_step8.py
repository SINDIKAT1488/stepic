from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,math, os

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    
  browser = webdriver.Chrome()
  browser.get(link)

  # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

  button = browser.find_element_by_id("book")

  price = WebDriverWait(browser, 5).until(
          EC.text_to_be_present_in_element((By.ID, "price"),"$100")
      )
  button.click()
  number = browser.find_element_by_id("input_value")

  y = calc(int(number.text))

  input = browser.find_element_by_id("answer").send_keys(y)

  button1 = browser.find_element_by_id("solve").click()

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()

# не забываем оставить пустую строку в конце файла