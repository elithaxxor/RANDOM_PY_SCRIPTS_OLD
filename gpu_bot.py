
import os
import re
import time
import chromedriver_binary 
#import selenium
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import constants as const
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException



try:
    OS = os.name
    chrome_options = Options()
    chrome_options.add_extension('/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/Selenium_Project/ad_blocker.crx')
    driver = webdriver.Chrome(options=chrome_options, executable_path= r'/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/fileexteniontest.torrenttorrent.torrent/chromedriver')
    time.sleep(2)
    driver.get('https://1337x.to/')
    driver.implicitly_wait(25)  ### no need to call more than once
    print(OS)
    print(driver)
    #print(driver.text)

except Exception as e:
    print('ERROR IN PARSING CHROME EXTENSION', str(e))




wd = webdriver.Chrome()



try: 
pass 

except NoSuchElementException as e:
	print(str(e))
	
	pass



