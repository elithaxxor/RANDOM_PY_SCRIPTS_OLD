import os
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





OS = os.name
# s.environ['PATH'] += '/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/fileexteniontest.torrenttorrent.torrent'
driver = webdriver.Chrome(r'/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/fileexteniontest.torrenttorrent.torrent/chromedriver')
driver.get('https://1337x.to/')
driver.implicitly_wait(25) ### no need to call more than once
print(OS)
print(driver)


#print(dir(selenium))


try:
    search_box = driver.find_element_by_id('autocomplete')
    search_box.click()
    search_box.send_keys('chopper')
    click_search_box = driver.find_element_by_class_name('flaticon-search')
    #click_seach_box.click()
    #click_search_box.send_keys(Keys.ENTER)
    search_box.send_keys(Keys.ENTER)
    #driver.find_element_by_xpath("html/xxxxx").send_keys('keys.ENTER')
except Exception as e:
    print('Element not found', str(e))

try:
 	url04 = driver.find_element_by_class_name('btn btn-search')
	
	#url04.click()
	url04.send_keys(Keys.ENTER)
	
	
#     url03 = driver.find_element_by_css_selector("button[submit]")
#     url03.click()
#     url03.send_keys(Keys.ENTER)


except Exception as e:
    print('Element not found', str(e))


	## button type="submit"

# 	url04= driver.find_element_by_css_selector(
# 	a[href]text=
# 	
	#)

#     url01 = driver.find_element_by_class_name('box-info-detail inner-table')   #  ("coll-1 name")
#     url01.click()
#     url01.send_keys(Keys.ENTER)
# 
# 
#     url02 = driver.find_element_by_tag_name('a')
#     url02.click()
#     url02.send_keys(Keys.ENTER)
# 
#     #.class1.class2 ## this is for search box on chopper page 
#     





# msg01 = driver.find_element_by_id('search-index-form')





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


