from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
logging.getLogger('WDM').setLevel(logging.NOTSET)


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
def test_login():
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

