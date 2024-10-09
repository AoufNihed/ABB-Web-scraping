# Web Scraping Project

This project demonstrates web scraping for both static and dynamic pages using Scrapy and Selenium. It is split into two parts:
1. Scraping a static page.
2. Scraping a dynamic page using Selenium.

## Part 1️⃣: Scraping Static Pages

### Steps to Run the Project:

1. **Create a Virtual Environment**:
   ```bash
   python -m venv env

2. env\Scripts\activate
   
3.pip install scrapy

4.scrapy startproject disjoncteur

5.scrapy genspider disjoncteur disjoncteur

6.scrapy crawl disjoncteur -o output.csv

## Part2️⃣: Scraping Dynamic Pages
1.env\Scripts\activate

2.pip install selenium

3.scrapy startproject dynamic

4.scrapy genspider dynamic dynamic

5.scrapy crawl dynamic -o output.csv

Requirements
Python 3.x
Scrapy
Selenium
ChromeDriver (ensure it's compatible with your Chrome version)
