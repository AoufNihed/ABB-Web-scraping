from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Setup the ChromeDriver service
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# ABB website!!
driver.get("https://electrissima.dz/products/")

#  product links 
xpath = '//div[@class="product-img"]/a'  
link_elements = driver.find_elements('xpath', xpath)

# Extract 
links = []
for link_el in link_elements:
    href = link_el.get_attribute("href")
    print(href)  
    links.append(href)

# Close the driver
driver.quit()
