### DESCRIBE METHODS TO BE CALLED
import os
import re
import time
import chromedriver_binary
# import selenium
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
import bbywebsite as BB

# driver = webdriver.Chrome()
timer = random.randrange(5.0, 15.0)
print('Random Wait Time', timer)
time.sleep(timer)
driver.implitently_wait(15)


class BestBuy_ripper(webdriver.Chrome):
    cart_wait = WebDriverWait

    def __init__(self,
                 executable_path=r"/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/Selenium_Project/chromedriver",
                 teardown=False):

        super(Booking, self).__init__()
        self.implicitly_wait(20)

        self.executable_path = executable_path
        os.environ['PATH'] += self.executable_path
        self.implicitly_wait(15)
        self.maximize_window()
        options = self.chrome_options()
        options.add_extension(
            "/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/Selenium_Project/ad_blocker.crx")

    def first_page(self):
            try:
                self.get(bbywebsite.URL)

                self.checkoutbutton = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
                )
                if
            except:
                self.refresh()
                continue


while True:
    try:
        OS = os.name
        BestBuy_ripper.add_extension(
            '/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/Selenium_Project/ad_blocker.crx')
        time.sleep(2)
        print(OS)

        cart = driver.find_element_by_xpath('')
        cart.click()

    except NoSuchElementException as e:
        print(str(e))
        print('Currently Out of Stock. ')
        time.sleep(90)





