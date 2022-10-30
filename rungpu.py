from gpustealer import BestBuy_ripper, Prettify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#.add-to-cart-buttoon
# with Prettify() as pretty:

try:
    pretty = Prettify()
    pretty.display_header()
except Exception:
    print('Passing graphics commit')

print(),print()
print('X' * 50)


## chormium test
try:
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

   # driver = webdriver.Chrome(r"/Users/a-robot/Documents/CS/PROJECT/GPU_JACKER/")  # Optional argument, if not specified will search path.
    driver.get('http://www.google.com/');
    time.sleep(5)  # Let the user actually see something!
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)  # Let the user actually see something!
    driver.quit()
except Exception:
    print('Error in chromedriver loading ')




with BestBuy_ripper() as rip:
    # rip.install_plugins()
    rip.install_plugins()
    rip.login()
    rip.login_info()
    rip.first_page()
    flag = rip.iterate()
    print(flag)
    counter = 0
    while flag != 'True':
        print(f'Waiting.. [{counter + 2} Seconds]')
        print(f'This many recursions have been processed [{counter}]')
        flag = rip.iterate()
        counter += 2
        continue
    else:
        rip.send_email()
        rip.card_and_order()



    #rip.click_thru_page()

    print('Exiting..')

