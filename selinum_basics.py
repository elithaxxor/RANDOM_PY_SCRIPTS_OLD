import os
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from selenium.webdriver.support.expected_conditions import presence_of_element_located



from selenium import webdriver
from selenium.webdriver.chrome.options import Options

## ORIGINAL CODE ###
# OS = os.name
# # s.environ['PATH'] += '/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/fileexteniontest.torrenttorrent.torrent'
# driver = webdriver.Chrome(r'/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/fileexteniontest.torrenttorrent.torrent/chromedriver')
# driver.get('https://1337x.to/')



## To Load Extensions::
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

try:
    search_box = driver.find_element_by_id('autocomplete')
    print(search_box.text)
    search_box.click()
    search_box.send_keys('chopper')
    click_search_box = driver.find_element_by_class_name('flaticon-search')
    #click_seach_box.click()
    #click_search_box.send_keys(Keys.ENTER)
    search_box.send_keys(Keys.ENTER)
    #driver.find_element_by_xpath("html/xxxxx").send_keys('keys.ENTER')
except Exception as e:
    print('Element not found CANNOT FIND SEARCH BOX ', str(e))


try:
    search_box01 = driver.find_element_by_id('autocomplete')
    print(search_box01.text)
    search_box01.click()
    search_box01.send_keys(Keys.CONTROL, "a")
    search_box01.clear()
    search_box01.send_keys('the titanic')
    search_box01.send_keys(Keys.ENTER)


except Exception as e:
    print('Element not found 2nd search', str(e))


### IMPLIMENT EXPLICIT WAIT
## SINCE THE WEBPAGE MAY TAKE LONG TO LOAD, AND TIME TO PARSE, SET UP AN EXPLICIT WAIT--> THIS WILL WAIT UNTIL THE DEFINED THING IS LOADED
## SET UP LOOP TO ITERATE THROUGH LIST OF ELEMENTS

try:
    body = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'table-list-wrap'))
        #EC.presence_of_all_elements_located((by.CLASS, 'table-list table table-responsive table-striped'))  ##
    )
    print(body.text)
    print(),print()
    print('1111111111')

    href_link = body.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]")
    print(href_link.text)

except Exception as e:
    print('Element not found body search', str(e))

try:
    click_link = driver.find_element_by_link_text('The Titanic Secret by Clive Cussler, Jack Du Brul EPUB')
    print(click_link.text)
    click_link.click()

except Exception as e:
    print('Element not found click test', str(e))

try:
  #  magnet = driver.find_element
    magnet_pull =WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l8680f3a1872d2d50e0908459a4bfa4dc04f0e610"))

    )
    print('magnetpull info')
    print(magnet_pull.text)
    magnet_link = driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[1]/ul[1]/li[1]/a")
    print(magnet_link.text)
    magnet_link.click()


except Exception as e:
    print('MAGNET PULL ERROR', str(e))
    driver.quit()




   ###### GOOOD CODE ######
    ##### TO LOOP THROUGH A LIST WHILE IN IMPLICIT WAIT
   #  sm_table = body.find_element_by_class_name('"table-list table table-responsive table-striped"')
   # # sm_table = body.find_element_by_class_name('coll-1 name')
   #  #sm_table = body.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]")
   #
   #  for cell in sm_table:
   #      href_link = cell.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]")
   #      print(href_link.text)





## ORIGINAL CODE ###
# OS = os.name
# # s.environ['PATH'] += '/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/fileexteniontest.torrenttorrent.torrent'
# driver = webdriver.Chrome(r'/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/fileexteniontest.torrenttorrent.torrent/chromedriver')
# driver.get('https://1337x.to/')




#################### EXPLICIT WAIT ###########################

###### USE WHEN DOWNLOAD COMPLETES ######### (23:00)
#### use when you want to wait some to for executution
## explicit wait -- waits until condition is returned true.
 ## driver, 30 --> how long to wait till true
#  ## use body class to find element
#  ## nest elements in a tuple
# print(f"my_element")
# WebDriverWait(driver, 30).until(
#     EC.text_to_b_present_in_element(
#         (by.CLASS_NAME, 'progress-label'),## element filtration (class name, class name vaue as a tuple
#          'complete'                      ## expected text as a string
#
#     )
#
# )



# my_element00 = driver.find_element_by_class_name('') ## <--- pass in class value  #-> class styling method
# print(my_element00)

#
#  #### DROP DOWN CLASSES FOR MAGNET / TORRENT DOWNLOAD ##
# <ul class="lfa750b508ad7d04e3fc96bae2ea94a5d121e6607 lcafae12a818cf41a5873ad374b98e79512c946c6">
# <li><a class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l8680f3a1872d2d50e0908459a4bfa4dc04f0e610" href="magnet:?xt=urn:btih:F5BC20E9AA709CFC32BE63B2F6BEE56882EB7BD2&amp;dn=The+Titanic+Secret+by+Clive+Cussler%2C+Jack+Du+Brul+EPUB&amp;tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&amp;tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.uw0.xyz%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fopen.demonii.si%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.nibba.trade%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Fopentracker.sktorrent.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fbt.xxx-tracker.com%3A2710%2Fannounce&amp;tr=udp%3A%2F%2Fzephir.monocul.us%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Famigacity.xyz%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce" onclick="javascript: count(this);"><span class="icon"><i class="flaticon-ld08a4206c278863eddc1bf813faa024ef55ce0ef"></i></span>Magnet Download</a> </li>
# <li class="dropdown">
# <a data-toggle="dropdown" class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c le41399670fcf7cac9ad72cbf1af20d76a1fa16ad" onclick="javascript: count(this);" href="#"><span class="icon"><i class="flaticon-le9f40194aef2ed76d8d0f7f1be7fe5aad6fce5e6"></i></span>Torrent Download</a>
# <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
# <li><a class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l13bf8e2d22d06c362f67b795686b16d022e80098" target="_blank" href="http://itorrents.org/torrent/F5BC20E9AA709CFC32BE63B2F6BEE56882EB7BD2.torrent"><span class="icon"><i class="flaticon-lbebff891414215bfc65d51afbd7677e45be19fad"></i></span>ITORRENTS MIRROR</a> </li>
# <li><a class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l13bf8e2d22d06c362f67b795686b16d022e80098" target="_blank" href="http://torrage.info/torrent.php?h=F5BC20E9AA709CFC32BE63B2F6BEE56882EB7BD2"><span class="icon"><i class="flaticon-lbebff891414215bfc65d51afbd7677e45be19fad"></i></span>TORRAGE MIRROR</a></li>
# <li><a class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l13bf8e2d22d06c362f67b795686b16d022e80098" target="_blank" href="http://btcache.me/torrent/F5BC20E9AA709CFC32BE63B2F6BEE56882EB7BD2"><span class="icon"><i class="flaticon-lbebff891414215bfc65d51afbd7677e45be19fad"></i></span>BTCACHE MIRROR</a></li>
# <li><a class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l8680f3a1872d2d50e0908459a4bfa4dc04f0e610" href="magnet:?xt=urn:btih:F5BC20E9AA709CFC32BE63B2F6BEE56882EB7BD2&amp;dn=The+Titanic+Secret+by+Clive+Cussler%2C+Jack+Du+Brul+EPUB&amp;tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&amp;tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.uw0.xyz%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fopen.demonii.si%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.nibba.trade%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Fopentracker.sktorrent.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fbt.xxx-tracker.com%3A2710%2Fannounce&amp;tr=udp%3A%2F%2Fzephir.monocul.us%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Famigacity.xyz%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce"><span class="icon"><i class="flaticon-ld08a4206c278863eddc1bf813faa024ef55ce0ef"></i></span>None Working? Use Magnet</a></li>
#
