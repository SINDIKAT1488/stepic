from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time,math, os

link = "http://suninjuly.github.io/file_input.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    

    browser = webdriver.Chrome()
    browser.get(link)

    inputs = browser.find_elements_by_css_selector(".form-group input")
    for inp in inputs:
      inp.send_keys("text")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')   
    print(file_path)

    file = browser.find_element_by_id("file")
    file.send_keys(file_path)
    


    button = browser.find_element_by_tag_name("button")
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