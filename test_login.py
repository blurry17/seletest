
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLogin():  
  def test_login(self):
  	options = Options()
  	options.headless = True
  	options.add_argument("--no-sandbox")
  	options.add_argument("--disable-dev-shm-usage")
  	driver = webdriver.Firefox(options=options)
    vars = {}
    driver.get("http://testing-ground.scraping.pro/login")
    driver.set_window_size(636, 697)
    driver.find_element(By.ID, "pwd").click()
    driver.find_element(By.ID, "usr").click()
    driver.find_element(By.ID, "usr").send_keys("admin")
    driver.find_element(By.ID, "pwd").click()
    driver.find_element(By.ID, "pwd").send_keys("12345")
    driver.find_element(By.CSS_SELECTOR, "input:nth-child(5)").click()
    driver.find_element(By.CSS_SELECTOR, "#case_login > .success").click()
    driver.quit()