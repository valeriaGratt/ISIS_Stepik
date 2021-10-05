from selenium import webdriver
import os
import time
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
   
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys('My')
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys('My')
    input3 = browser.find_element_by_name("email")
    input3.send_keys('My')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'lol.txt')            
    file_btn = browser.find_element_by_id("file")
    file_btn.send_keys(file_path)
    
    button2 = browser.find_element_by_class_name("btn")
    button2.click()
    assert True

finally:
    time.sleep(10)
    browser.quit()