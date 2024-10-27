from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.chrome.options import Options
import unittest
import datetime

# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)

# driver = webdriver.Chrome(options=options)
# driver.get("http://www.bing.com")
# elem = driver.find_element(By.NAME , "q")
# elem.send_keys("Hello")
# WebDriverWait(driver , 12)
# elem.send_keys(Keys.RETURN)
test_link = "https://practice.expandtesting.com"
class Form_Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_delta(self):
        driver = self.driver
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get(f"{test_link}/inputs")
        num = driver.find_element(By.ID , "input-number")
        num.send_keys("24")
        driver.find_element(By.ID ,"btn-display-inputs").click()
        num_out = driver.find_element(By.ID , "output-number").text

        assert num_out == '24'

        txt = driver.find_element(By.ID , "input-text")
        txt.send_keys("ya Ali")
        driver.find_element(By.ID ,"btn-display-inputs").click()
        txt_out = driver.find_element(By.ID , "output-text").text

        assert txt_out == "ya Ali"

        password = driver.find_element(By.ID ,"input-password" )
        password.send_keys("moali")
        driver.find_element(By.ID ,"btn-display-inputs").click()
        password_out = driver.find_element(By.ID ,"output-password" ).text

        assert password_out == "moali"
        
        date = driver.find_element(By.ID ,"input-date" )
        mydate = "10/10/2000"
        date.send_keys(mydate)
        driver.find_element(By.ID ,"btn-display-inputs").click()
        date_out = driver.find_element(By.ID ,"output-date" ).text
        
        assert date_out == mydate



        

if __name__ == '__main__':
    unittest.main()

