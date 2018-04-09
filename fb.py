from selenium import webdriver
from getpass import getpass

login_ids = ['u_0_6', 'u_0_2', 'u_0_4']

usr = 'abhilash4317@gmail.com'
#usr = input('enter your facebook email address or mobile number ')
pwd = getpass('enter password')

driver = webdriver.Chrome('I:\downloads\chrome\chromedriver.exe')
driver.get('https://www.facebook.com/')

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)

try:
    login_btn = driver.find_element_by_id('u_0_2')
except:
    try:
        login_btn = driver.find_element_by_id('u_0_6')
    except:
        try:
            login_btn = driver.find_element_by_id('u_0_4')
        except:
            pass
            
login_btn.submit()

