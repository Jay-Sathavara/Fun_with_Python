# JP0030

from selenium import webdriver

def login_to_linkedin():
    Username=browser.find_element_by_name("session_key")
    Username.send_keys("enter username")
    password=browser.find_element_by_name("session_password")
    password.send_keys("enter password")
    browser.find_element_by_xpath("//button[@type='submit']").click()

def navigate_to_network_and_connect():
   
    browser.find_element_by_xpath('//*[@id="ember21"]').click()

    browser.implicitly_wait(5)

    browser.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[2]/div/div/main/ul/li[1]/div/button/span').click()

    elements = browser.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/section/div/ul/li')
    for i in range(1,len(elements)+1):
        
        browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/section/div/ul/li[{}]/div/section/div[2]/footer/button/span'.format(str(i))).click()

        print('Connection request sent to person {}'.format(str(i)))

        browser.implicitly_wait(1)

browser = webdriver.Firefox(executable_path='/home/deepika/Downloads/internship/instagram/geckodriver')

browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

browser.implicitly_wait(5)

login_to_linkedin()
navigate_to_network_and_connect()
