from selenium import webdriver
#from selenium.webdriver.support.ui import Select
import time
import os



  
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

try: 
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome(options=options)
    browser.get(link)  
    Fname = browser.find_element_by_xpath("/html/body/div/form/div/input[1]")
    Fname.send_keys ("Stas")
    Lname = browser.find_element_by_xpath("/html/body/div/form/div/input[2]")
    Lname.send_keys ("Volkov")
    mail = browser.find_element_by_xpath("/html/body/div/form/div/input[3]")
    mail.send_keys ("volk@mail.ru")
    
    #file = browser.find_element_by_css_selector("#file")
    #directory = "D/"
    #file_name = "stepik.txt"
    #file_path = os.path.join(directory, file_name)
    #file.send_keys(file_path)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "stepik.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_css_selector("#file")
    element.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()
    
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

