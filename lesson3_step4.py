from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time,math, os

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    

    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    prompt = browser.switch_to.alert
    prompt.accept()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    number = browser.find_element_by_id("input_value")

    y = calc(int(number.text))

    input = browser.find_element_by_id("answer").send_keys(y)

    button1 = browser.find_element_by_tag_name("button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла