from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time,math

link = "http://suninjuly.github.io/selects1.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    

    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element_by_id("num1")
    num1 = int(first.text)

    second = browser.find_element_by_id("num2")
    num2 = int(second.text)

    sum = num1+num2

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(sum)) # ищем элемент с текстом "Python"


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла