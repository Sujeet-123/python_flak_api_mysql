# from ast import IsNot/
# from unicodedata import name
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import google_sheet_api
# import links

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://www.zomato.com/pune")
time.sleep(5)
driver.maximize_window()
time.sleep(10)

def see_more():

    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(5)


    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_UP)
    time.sleep(5)
                                            
    divs = driver.find_elements(By.CLASS_NAME,'sc-rbbb40-0.iwHbVQ')
    print("=========================")
    n = 1
    for i in divs:
        print("in for loop")
        print(n)
        if n==6:
            i.click()
            print("clicked")
            time.sleep(10)
            break
        n = n+1



def city_links():

    get_links()

    time.sleep(5)
    see_more()


    city_links = []


    div1 = driver.find_elements(By.CLASS_NAME,'sc-bke1zw-1.gLbmAn a')

    for i in div1:
        hrf = i.get_attribute('href')
        city_links.append(hrf)
        print(hrf)


    div1 = driver.find_elements(By.CLASS_NAME,'sc-bke1zw-1.gGzIKR a')

    for i in div1:
        hrf = i.get_attribute('href')
        city_links.append(hrf)
        print(hrf)



    div1 = driver.find_elements(By.CLASS_NAME,'sc-bke1zw-1.jdRPl a')

    for i in div1:
        hrf = i.get_attribute('href')
        city_links.append(hrf)
        print(hrf)

    print("city_links_len = > ",len(city_links))
    # n = 1
    for i in city_links:
        # if n==4:
        #     break
        driver.get(i)
        time.sleep(5)
        get_links()
        # n = n+1



# ===========================================================================================================================================
main_resto_links = []

links_list = []

main_link_list = []

def get_links():

    for i in range(30):

        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(10)

        print(i)

    

        if(i==5 or i==10 or i==15 or i==20 or i==25):
            driver.execute_script('scrollTo(0,700)')
            time.sleep(5)


    time.sleep(5)
    driver.execute_script('scrollTo(0,700)')
    
    time.sleep(8)
    links = driver.find_elements(By.CLASS_NAME,'jumbo-tracker a')
    print(len(links))
    num = 1
    for i in links:
        link = i.get_attribute("href")
        links_list.append(link)
        print(num)
        num = num+1
        print(link)
    print(len(links_list))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    sub='order'

    for k in links_list:
        if (sub in k ) and (k not in main_link_list):
            main_link_list.append(k)  
        else:
            continue

    # print(main_link_list) 
    main_resto_links.append(main_link_list)           
    print("main_link_list => ",len(main_link_list))
    print("Get link")
    
    # click()

 

def Data():

    try:
        name = driver.find_element(By.CLASS_NAME,'sc-7kepeu-0.sc-eilVRo.eAhpQG').text
        print("Name => ",name)
    except:
        name = None

    try:
        address = driver.find_element(By.CLASS_NAME,'sc-cpmLhU.fDVcNc').text
        print("Address name => ",address)
    except:
        address = None


    try:
        times = driver.find_element(By.CLASS_NAME,'sc-fhYwyz.fRKkxr').text.split('(')
    
        print("Time => ",times[0])
        time2 = times[0]
    except:
        time2 = None

    try:
        dining_reviews = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/section[3]/section/section/div/div/div/section/div[1]/div[1]/div/div/div[1]').text
        print("dining_reviews => ",dining_reviews)
    except:
        dining_reviews = None


    try:
        delivery_reviews = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/section[3]/section/section/div/div/div/section/div[3]/div[1]/div/div/div[1]').text
        print("delivery_reviews => ",delivery_reviews)
    except:
        delivery_reviews = None



    driver.execute_script('scrollTo(0,1000)')
    time.sleep(5)
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
            Down_list.append(Dname)

        try:
            Dvotes = div.find_element(By.CLASS_NAME,'sc-z30xqq-4.hTgtKb').text
            Down_list.append(Dvotes)
            print("votes => ",Dvotes)
        except:
            Dvotes = None
            Down_list.append(Dvotes)

        try:
            Dprice = div.find_element(By.CLASS_NAME,'sc-17hyc2s-1.cCiQWA').text
            Down_list.append(Dprice)
            print("Dprice => ",Dprice)
        except:
            Dprice = None
            Down_list.append(Dprice)

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
    # print(m)  
    value1 = [name, address, time2, dining_reviews, delivery_reviews, str(F_D_data), str(L_D_data)]
    google_sheet_api.append_googlesheet1(value1)

def click():

    for i in main_link_list:
        print("In click function")
        driver.get(i)
        time.sleep(5)
       
        # Data()


   
city_links()
   
print("----------------------------------------------------------")

# print(main_resto_links)
print("main_resto_links => ",len(main_resto_links))
count = 0
for k in main_resto_links:
    count+=len(k)



restro_links = []

for i in main_resto_links:
    for j in i:
        if j not in restro_links:
            restro_links.append(j)
            links_list.append(j)

print(count)
print("===========================================")
print("restro_links => ",len(restro_links))

