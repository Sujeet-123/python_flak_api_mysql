from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import google_sheet_api
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://www.zomato.com/pune")
time.sleep(5)


driver.maximize_window()
time.sleep(5)

links_list = []

main_link_list = []

def get_links():

    for i in range(30):
        
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(5)
        print(i)
        return("Done")
        if(i==15):
            driver.execute_script('scrollTo(0,700)')
            time.sleep(2)

    time.sleep(2)
    driver.execute_script('scrollTo(0,700)')
    time.sleep(3)
    links = driver.find_elements(By.CLASS_NAME,'jumbo-tracker a')
    time.sleep(3)    
    driver.minimize_window()
    print("total links : ",len(links))
    
    for n,i in enumerate(links):
        link = i.get_attribute("href")
        links_list.append(link)
        print("count : ",n)
      
    print("links_list : ",len(links_list))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    sub='order'

    for k in links_list:
        if (sub in k ) and (k not in main_link_list):
            main_link_list.append(k)
            print("done")  
            value1 = [k]
            google_sheet_api.append_googlesheet10(value1)
        else:
            continue

    print("main_link_list : ",len(main_link_list))


    print("Get link")


get_links()

print("main_link_list : ",len(main_link_list))
