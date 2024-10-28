from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("https://www.toplearn.com")
sleep(2)
# use script console code 
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
sleep(6)