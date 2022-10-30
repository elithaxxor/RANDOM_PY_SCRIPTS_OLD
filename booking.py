### DESCRIBE METHODS TO BE CALLED
import os
import re
import time
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



class Booking(webdriver.Chrome): # use webdriver .chrome methods and designed methods in bookings
    PATH = r"/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/Selenium_Project/chromedriver"
    chrome_options = Options
    #chrome_options.add_extension(r"/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/Selenium_Project/ad_blocker.crx")
    url_frame = WebDriverWait
    chrome_options = Options
    #Options.add_extension(r"/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/Selenium_Project/ad_blocker.crx")
    keys00 = Keys
    #ad_blocker = '/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/Selenium_Project/ad_blocker.crx'
    options = webdriver.ChromeOptions


    def __init__(self, executable_path= r"/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/Selenium_Project/chromedriver",
                 teardown = False
                 ):

        super(Booking, self).__init__()
        self.implicitly_wait(20)

        self.executable_path = executable_path
        os.environ['PATH'] += self.executable_path
        self.implicitly_wait(15)
        self.maximize_window()
        options = self.chrome_options()
        options.add_extension("/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/Selenium_Project/ad_blocker.crx")
        #self.chrome_options.


        keys00 = Keys()


    def first_page(self):
        self.get(const.BASE_URL)

    def install_plugins(self):
        self.implicitly_wait(15)
        #chrome_options = self.chrome_options


      #  options.add_extension('/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/Selenium_Project/ad_blocker.crx')


    def searchbox(self, box_message):  ### to click box on webpage using css selector
        self.implicitly_wait(20)
        box00 = self.find_element_by_id('query')
        print(box00.text)
        box00.click()
        box00.send_keys(Keys.CONTROL + "a")
        box00.clear()
        box00.click()
        box00.send_keys(box_message)
        box00.send_keys(Keys.ENTER)

        box00.click()
        time.sleep(2)
        box00.send_keys(Keys.COMMAND, '_')
        box00.click()
        box00.send_keys(Keys.CONTROL, '-')
        box00.click()
        box00.send_keys(Keys.CONTROL, '-')
        box00.click()




    def select_link(self, val):
        print('select link modoule')
        url_frame = self.url_frame(self, 15).until(
            EC.presence_of_element_located((By.ID,
                                            "search-results"))

        )

        print(url_frame.text)
        print(type(url_frame.text))

        ## to resive window frame
        #self.execute_script("$('#values').css('zoom', -5);")
        #keys00(Keys.COMMAND, '-')

    def take_screenshots(self):
        # options00 = self.options
        # options00.headless = True
        self.implicitly_wait(20)

        scrolls = 35
        while True:
            scrolls -= 1
            self.execute_script("window.scrollBy(0, 250)")
            #ime.sleep(2)
            self.save_screenshot('computer_pics/f"scrolls{scrolls}.png"')
            
           # time.sleep(.5)
            if scrolls < 0:
                break


        #
        # for i in range(20):  # adjust integer value for need
        #     # you can change right side number for scroll convenience or destination
        #     # you can change time integer to float or remove
        #     time.sleep(1)



        time.sleep(1)
        S = lambda X: self.execute_script('return document.body.parentNode.scroll' + X)
        self.set_window_size(S('Width'), S('Height'))
        self.find_element_by_id('search-results').screenshot('FINALFRESHIT111.png')
        time.sleep(2)



        self.save_screenshot("FREESHIT02.png")
        time.sleep(3)



        self.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        self.save_screenshot("FREESHIT03.png")
        time.sleep(3)
        self.execute_script("document.body.style.zoom='-50'")
        time.sleep(3)
        self.save_screenshot("FREESHIT04.png")
        time.sleep(5)




        #
        # url_link = self.find_element_by_id('result-row')
        # print(url_link.text)
        # prnt(type(url_link))
        # url_link.click()
        # #print(url_frame)
        #
        #
        #





