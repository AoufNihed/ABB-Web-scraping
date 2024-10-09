import scrapy


class DisjoncteurSpider(scrapy.Spider):
    name = "disjoncteur"
    start_urls = ["https://electrissima.dz/product-cat/13-disjoncteur-moteur/"]

    def parse(self, response):
        # Loop through each product section
        for product in response.css('div.product-info'):
            #  product name
            product_name = product.css('h2.product-title a::text').get()
            
            #  product series 
            product_series = product.css('div.product-price span::text').get()
            
            # Store the extracted data
            yield {
                'product_name': product_name,
                'product_series': product_series,
            }
