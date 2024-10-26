from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

# driver = Chrome(executable_path = "C:/chromedriver.exe")
# driver = webdriver.Chrome()
# chrome_options=Options
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incongnito")
# global driver
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get("http://www.bing.com")
elem = driver.find_element(By.NAME , "q")
elem.send_keys("Hello")
WebDriverWait(driver , 12)
elem.send_keys(Keys.RETURN)
