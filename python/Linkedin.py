from selenium import webdriver


def login_to_linkedin():
    Username=browser.find_element_by_name("session_key")
    Username.send_keys("enter username")
    password=browser.find_element_by_name("session_password")
    password.send_keys("enter password")
    browser.find_element_by_xpath("//button[@type='submit']").click()

