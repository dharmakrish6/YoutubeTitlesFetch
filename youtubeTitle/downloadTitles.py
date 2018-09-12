
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys


print("********Automation Script started")

#code to fetch value from command prompt
os.environ['COUNT'] == 3
os.environ['KEYWORD'] == 'python'

count=int(os.environ['COUNT'])
keyword=os.environ['KEYWORD']
print(count,keyword)
chromedriver = "/PATH_TO_CHROMEDROVER/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://youtube.com")
driver.find_element_by_css_selector('[name="search_query"]').send_keys(os.environ['KEYWORD']+Keys.RETURN)
time.sleep(3)

#code for scroll to bottom of the page
for i in range(int(os.environ['COUNT'])):
    page = driver.find_element_by_tag_name("html")
    page.send_keys(Keys.END)
    time.sleep(2)

titles=driver.find_elements_by_css_selector('#contents #title-wrapper>h3 #video-title')
#code to fetch title of search results
list=[]

for each in titles:
    email = each.text
    try:
        print(email)
    except:
        pass
    list.append(email)
#store the list of values to CSV file with name of search keyword
try:
    resultFyle = open(keyword + ".csv", 'a')
    for r in list:
        resultFyle.write(r + "\n")

except:
    pass

list=[]
print(keyword+".csv file created !!")
time.sleep(2)
driver.quit()
print("********Automation Script Done !!")
