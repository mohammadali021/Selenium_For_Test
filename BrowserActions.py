# first install webdriver-manager library
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path
import os
from selenium.webdriver.chrome.options import Options

# driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
chrome_op =Options()
chrome_op.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_op )

# Browser Action1 = Open Web
driver.get("http://www.google.com")
sleep(3)

# # Browser Action2 = title web
# window_title = driver.title
# print(window_title)

# # Browser Action3 = Back
# driver.get("http://www.python.org")
# sleep(2)
# driver.back()
# sleep(2)

# # Browser Action4 = Back
# driver.forward()

# # Browser Action5 = Back
# driver.refresh()

# # Browser Action6 = Open new window and switch to it
# driver.switch_to.new_window('window')
# sleep(2)
# print(driver.title)

# # Browser Action7 = Open new tab and switch to it
# driver.switch_to.new_window('tab')
# sleep(2)
# print(driver.title)

# # Browser Action8 = Open new window and go to web
# driver.switch_to.new_window('window')
# driver.get("https://toplearn.com/")
# web_window = driver.current_window_handle
# print('web handle' + str(web_window))

# # Browser Action9= Open new window and go to web and back to first web
# all_handel = driver.window_handles
# driver.switch_to.window(all_handel[0])

# # Browser Action10 = close tab
# driver.close()

# # Browser Action11 = session quit
# driver.quit()

# # Browser Action12 = window size
# window_site = driver.get_window_size()
# print(window_site)

# # Browser Action13 = set window size
# driver.set_window_size(500,500)
# sleep(3)

# # Browser Action14 = change window position
# current = driver.get_window_position()
# print(current)
# driver.set_window_position(400 , 500)
# sleep(3)


# # Browser Action15 = Maximize window
# driver.maximize_window()
# sleep(3)

# # Browser Action16 = Minimize window
# driver.minimize_window()
# sleep(3)

# # Browser Action17 = Fullsceen window
# driver.fullscreen_window()
# sleep(3)

# ---------------------------------------------------------------
# screenshot
# current_path = Path(__file__).parent#project folder
# file_name = os.path.join(str(current_path) , 'session2.png')

# driver.save_screenshot(file_name)





 











