import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def LoginLinkedin(driver,f_credential):
    
    credential=open(f_credential)
    line=credential.readlines()
    username=line[0]
    password=line[1]

    # Find id of the elements
    email_field=driver.find_element('id','username')

    email_field.send_keys(username)
    sleep(1)
    password_field=driver.find_element('name','session_password')

    password_field.send_keys(password)
    sleep(1)

    login_field=driver.find_element('xpath','//*[@id="organic-div"]/form/div[3]/button')
    login_field.click()
    sleep(1)