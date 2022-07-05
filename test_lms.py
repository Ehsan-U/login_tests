""" Test Cases for Lms.ue.edu.pk login page """

###### imports ######

from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
logging.getLogger('WDM').setLevel(logging.NOTSET)

#####################

@pytest.mark.login
def test_username_field():
    # webdriver setup
    s=Service(ChromeDriverManager().install())
    driver = Chrome(service=s)
    url = 'http://lms.ue.edu.pk/LMS_LandingPage.aspx?id=095b29e1-e3e2-4431-b7b5-588859127803'
    driver.get(url)
    driver.maximize_window()
    # find username field in the page source
    username_field = driver.find_element(by=By.ID,value='txtStudentID')
    # find submit button in the page source
    submit_btn = driver.find_element(by=By.ID,value='ibtnLogin')
    username_field.send_keys("Bsf1802224")
    time.sleep(1)
    submit_btn.click()
    assert driver.current_url == url
    driver.close()

@pytest.mark.login
def test_password_field():
    s=Service(ChromeDriverManager().install())
    driver = Chrome(service=s)
    url = 'http://lms.ue.edu.pk/LMS_LandingPage.aspx?id=095b29e1-e3e2-4431-b7b5-588859127803'
    driver.get(url)
    driver.maximize_window()
    # find password field in the page source
    password_field = driver.find_element(by=By.ID,value='txtPassword')
    # find submit button in the page source
    submit_btn = driver.find_element(by=By.ID,value='ibtnLogin')
    password_field.send_keys("Rumisays")
    time.sleep(1)
    submit_btn.click()
    assert driver.current_url == url
    driver.close()

@pytest.mark.login
def test_invalid_credentials():
    s=Service(ChromeDriverManager().install())
    driver = Chrome(service=s)
    url = 'http://lms.ue.edu.pk/LMS_LandingPage.aspx?id=095b29e1-e3e2-4431-b7b5-588859127803'
    driver.get(url)
    driver.maximize_window()
    # find username field in the page source
    username_field = driver.find_element(by=By.ID,value='txtStudentID')
    # find password field in the page source
    password_field = driver.find_element(by=By.ID,value='txtPassword')
    # find submit button in the page source
    submit_btn = driver.find_element(by=By.ID,value='ibtnLogin')
    username_field.send_keys("AAAAAAAAAA")
    time.sleep(1)
    password_field.send_keys("1111111111")
    time.sleep(1)
    submit_btn.click()
    assert driver.current_url == url
    driver.close()

@pytest.mark.login
def test_both_empty():
    s=Service(ChromeDriverManager().install())
    driver = Chrome(service=s)
    url = 'http://lms.ue.edu.pk/LMS_LandingPage.aspx?id=095b29e1-e3e2-4431-b7b5-588859127803'
    driver.get(url)
    driver.maximize_window()
    # find username field in the page source
    username_field = driver.find_element(by=By.ID,value='txtStudentID')
    # find password field in the page source
    password_field = driver.find_element(by=By.ID,value='txtPassword')
    # find submit button in the page source
    submit_btn = driver.find_element(by=By.ID,value='ibtnLogin')
    username_field.send_keys("")
    time.sleep(1)
    password_field.send_keys("")
    time.sleep(1)
    submit_btn.click()
    assert driver.current_url == url
    driver.close()

@pytest.mark.login
def test_valid_credentials():
    s=Service(ChromeDriverManager().install())
    driver = Chrome(service=s)
    url = 'http://lms.ue.edu.pk/LMS_LandingPage.aspx?id=095b29e1-e3e2-4431-b7b5-588859127803'
    driver.get(url)
    driver.maximize_window()
    # find username field in the page source
    username_field = driver.find_element(by=By.ID,value='txtStudentID')
    # find password field in the page source
    password_field = driver.find_element(by=By.ID,value='txtPassword')
    # find submit button in the page source
    submit_btn = driver.find_element(by=By.ID,value='ibtnLogin')
    username_field.send_keys("Bsf1802224")
    time.sleep(1)
    password_field.send_keys("Rumisays")
    time.sleep(1)
    submit_btn.click()
    time.sleep(2)
    assert driver.current_url != url
    driver.close()

@pytest.mark.login
def test_messages_on_invalid_attempt():
    s=Service(ChromeDriverManager().install())
    driver = Chrome(service=s)
    url = 'http://lms.ue.edu.pk/LMS_LandingPage.aspx?id=095b29e1-e3e2-4431-b7b5-588859127803'
    driver.get(url)
    driver.maximize_window()
    # find username field in the page source
    username_field = driver.find_element(by=By.ID,value='txtStudentID')
    # find password field in the page source
    password_field = driver.find_element(by=By.ID,value='txtPassword')
    # find submit button in the page source
    submit_btn = driver.find_element(by=By.ID,value='ibtnLogin')
    username_field.send_keys("Bsf1111111")
    time.sleep(1)
    password_field.send_keys("Rumisays")
    time.sleep(1)
    submit_btn.click()
    time.sleep(2)
    source = driver.page_source
    if "Invalid Student ID or Password".lower() in source.lower():
        flag = True
    else:
        flag = False
    assert flag == True
    driver.close()

@pytest.mark.login
def test_field_maxlength():
    s=Service(ChromeDriverManager().install())
    driver = Chrome(service=s)
    url = 'http://lms.ue.edu.pk/LMS_LandingPage.aspx?id=095b29e1-e3e2-4431-b7b5-588859127803'
    driver.get(url)
    driver.maximize_window()
    # find username field in the page source
    username_field = driver.find_element(by=By.ID,value='txtStudentID')
    # find password field in the page source
    password_field = driver.find_element(by=By.ID,value='txtPassword')
    # find submit button in the page source
    submit_btn = driver.find_element(by=By.ID,value='ibtnLogin')
    username_field.send_keys('A'*2000)
    time.sleep(1)
    password_field.send_keys('A'*2000)
    time.sleep(1)
    submit_btn.click()
    time.sleep(2)
    source = driver.page_source
    if "Invalid Student ID or Password".lower() in source.lower():
        flag = True
    else:
        flag = False
    assert flag == True
    driver.close()

@pytest.mark.login
def test_password_appearence():
    s=Service(ChromeDriverManager().install())
    driver = Chrome(service=s)
    url = 'http://lms.ue.edu.pk/LMS_LandingPage.aspx?id=095b29e1-e3e2-4431-b7b5-588859127803'
    driver.get(url)
    driver.maximize_window()
    # find password field in the page source
    password_field = driver.find_element(by=By.ID,value='txtPassword')
    time.sleep(1)
    password_field.send_keys('A'*2000)
    time.sleep(1)
    pswd_field_type = password_field.get_attribute('type')
    assert pswd_field_type.lower() == 'password'
    driver.close()

@pytest.mark.login
def test_forget_password():
    s=Service(ChromeDriverManager().install())
    driver = Chrome(service=s)
    url = 'http://lms.ue.edu.pk/LMS_LandingPage.aspx?id=095b29e1-e3e2-4431-b7b5-588859127803'
    driver.get(url)
    driver.maximize_window()
    # find password field in the page source
    forget_password = driver.find_element(by=By.ID,value='hpForgetPassword')
    time.sleep(1)
    forget_password.click()
    time.sleep(1)
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    assert driver.current_url != url
    driver.close()