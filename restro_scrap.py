from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager
import google_sheet_api

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://www.zomato.com/pune")
time.sleep(5)


driver.maximize_window()
time.sleep(5)






def Data():

    try:
        name = driver.find_element(By.CLASS_NAME,'sc-7kepeu-0.sc-eilVRo.eAhpQG').text
        print("Name => ",name)
    except:
        name = None

    try:
        address = driver.find_element(By.CLASS_NAME,'sc-cpmLhU.fDVcNc').text
    except:
        address = None


    try:
        times = driver.find_element(By.CLASS_NAME,'sc-fhYwyz.fRKkxr').text.split('(')
    
        time2 = times[0]
    except:
        time2 = None

    try:
        dining_reviews = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/section[3]/section/section/div/div/div/section/div[1]/div[1]/div/div/div[1]').text
    except:
        dining_reviews = None


    try:
        delivery_reviews = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/section[3]/section/section/div/div/div/section/div[3]/div[1]/div/div/div[1]').text
    except:
        delivery_reviews = None



    driver.execute_script('scrollTo(0,1000)')
    time.sleep(5)
    read_k=driver.find_elements(By.CLASS_NAME,'sc-ya2zuu-0.SWRrQ')
    for i in read_k:
        try:
            i.click()
            time.sleep(2)
        except:
            print("except")
            pass
    m=[]
    D_Name = []
    divs = driver.find_elements(By.CLASS_NAME,'sc-1s0saks-17.bGrnCu')
    for div in divs:
        Down_list = []
        try:
            Dname = div.find_element(By.CLASS_NAME,'sc-1s0saks-15.iSmBPS').text
            Down_list.append(Dname)
            print("Dname => ",Dname)
        except:
            Dname = None

        try:
            Dvotes = div.find_element(By.CLASS_NAME,'sc-z30xqq-4.hTgtKb').text
            Down_list.append(Dvotes)
        except:
            Dvotes = None

        try:
            Dprice = div.find_element(By.CLASS_NAME,'sc-17hyc2s-1.cCiQWA').text
            Down_list.append(Dprice)
        except:
            Dprice = None

        try:
            Ddiscrib = div.find_element(By.CLASS_NAME,'sc-1s0saks-12.hcROsL').text
            Down_list.append(Ddiscrib)
            print("Ddiscrib => ",Ddiscrib)
        except:
            Ddiscrib = None
            Down_list.append(Ddiscrib)
        D_Name.append(Down_list)


    for i, n in enumerate(D_Name):
        if n not in m:
            m.append(n)

    
    if len(m)>=100:
        F_D_data=[m[0:99]]
        L_D_data=[m[99:]]
    else:
        L_D_data = None
        F_D_data=[m]

    value1 = [name, address, time2, dining_reviews, delivery_reviews, str(F_D_data), str(L_D_data)]
    google_sheet_api.append_googlesheet1(value1)




# def click():

#     for i in :
#         print("In click function")
#         driver.get(i)
#         time.sleep(5)
       
#         Data()

# click()