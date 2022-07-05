from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


s=Service(ChromeDriverManager().install())
driver = Chrome(service=s)
url = 'http://lms.ue.edu.pk/LMS_LandingPage.aspx?id=095b29e1-e3e2-4431-b7b5-588859127803'
driver.get(url)
driver.maximize_window()
before = driver.window_handles
# find password field in the page source
forget_password = driver.find_element(by=By.ID,value='hpForgetPassword')
time.sleep(1)
forget_password.click()
time.sleep(1)
after = driver.window_handles
driver.switch_to.window(after[1])
print(driver.current_url)
driver.close()