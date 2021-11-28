from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

try: 
    link = "http://suninjuly.github.io/execute_script.html"

    browser = webdriver.Chrome(options=options)
    browser.get(link)
  
    x = browser.find_element_by_css_selector("#input_value")
    x = x.text
    z = calc(x)
    print(z)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys (z)
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()  
    button.click()
    
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

