import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from dynamic.items import DynamicItem


class ElectsSpider(scrapy.Spider):
    name = 'elects'

    def start_requests(self):
        # Set up Selenium WebDriver
        options = ChromeOptions()
        options.headless = True  # Run in headless mode
        service = Service(executable_path="chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get("https://electrissima.dz/products/")
        
        # XPath to the product block links
        block_xpath = '//div[@class="product-img"]/a'  #new methode of configurate in selenium 
        product_blocks = driver.find_elements(By.XPATH, block_xpath)

        # Extract the links 
        for block in product_blocks:
            block_url = block.get_attribute("href")
            yield scrapy.Request(block_url, callback=self.parse_product_block)

        driver.quit()

    def parse_product_block(self, response):
        # Scrape the individual product details 
        products = response.css('div.product-info')  
        for product in products:
            item = DynamicItem()
            item['product_name'] = product.css('h2.product-title a::text').get()
            item['product_series'] = product.css('div.product-price span::text').get()
            yield item
