import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json


class LaixuatnganhangSpider(scrapy.Spider):
    name = "laixuatnganhang"
    allowed_domains = ["s.cafef.vn"]
    start_urls = ["https://s.cafef.vn/lai-suat-ngan-hang.chn#data"]

    def __init__(self, *args, **kwargs):
        super(LaixuatnganhangSpider, self).__init__(*args, **kwargs)
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def parse(self, response):
        self.driver.get(response.url)
        # Selenium waits for a certain time to allow the page to load fully
        self.driver.implicitly_wait(10)

        # Now that the page is fully loaded, you can extract data using Selenium
        # In this example, we use XPath to extract the table header
        header_xpath = '/html/body/form/div[3]/div[3]/div[1]/div[3]/div[1]/table/thead'
        header_element = self.driver.find_element(By.XPATH, header_xpath)

        # Get the text content of each column in the table header
        header_columns = [column.text.strip() for column in header_element.find_elements(By.TAG_NAME, 'th')]
        tbody_xpath = '/html/body/form/div[3]/div[3]/div[1]/div[3]/div[1]/table/tbody'
        tbody_element = self.driver.find_element(By.XPATH, tbody_xpath)

        # Get the text content of each row in the table body
        rows = []
        rows.append(header_columns)
        for row in tbody_element.find_elements(By.TAG_NAME, 'tr'):
            row_data = [cell.text.strip() for cell in row.find_elements(By.TAG_NAME, 'td')]
            rows.append(row_data)
        # Save the header columns to a JSON file with UTF-8 encoding

        with open('result.txt', 'w', encoding='utf-8') as file:
            json.dump(rows, file, ensure_ascii=False)

    def closed(self, reason):
        self.driver.quit()
