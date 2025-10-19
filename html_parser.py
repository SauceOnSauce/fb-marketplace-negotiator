'''
Facebook Marketplace Negotiator - HTML Parser Module
This module provides functions to extract HTML content from Facebook Marketplace listings from .html file.
'''

from bs4 import BeautifulSoup
import logging
import re


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
  
class FacebookMarketplaceParser:
    """
    Parses HTML content from Facebook Marketplace listings to extract product information.
    """
    def __init__(self, html_source: str):
        with open(html_source, 'r', encoding='utf-8') as f:
            self.html_content = f.read()
        self.soup = BeautifulSoup(self.html_content, 'lxml')
        logger.info("HTML content reloaded from file.")
        
        self.result = {}
            
    def extract_product_name(self):
        # Attempt to extract the product name from the <title> tag
        if self.soup.title and self.soup.title.string:
            logger.info("Extracting name...")
            match = re.search(r'–\s*(.*?)\s*\|', self.soup.title.string)
            product_name = match.group(1).strip() if match else self.soup.title.string.strip()
            self.result['product_name'] = product_name   
        else:
            logger.warning("No <title> tag found in HTML.")
            self.result['product_name'] = None
        
    def extract_price(self):
        # Attempt to extract the price using regex
        logger.info("Extracting price...")
        price_text = self.soup.find(string=re.compile(r'\£\d+'))
        if price_text:
            match = re.search(r'\£([\d,\.]+)', price_text)
            if match:
                try:
                    self.result['price'] = float(match.group(1).replace(',', ''))
                    return self.result['price']
                except ValueError:
                    pass
        self.result['price'] = None        
        logger.warning("Price not found or could not be parsed.")
        
    def extract_year(self):
        # Extract year from product name
        logger.info("Extracting year...")
        name = self.result['product_name']
        match = re.search(r'\b(19\d{2}|20\d{2})\b', name)
        self.result['year'] = int(match.group(1)) if match else None
        if not match:
            logger.warning("Year not found in product name.")
            self.result['year'] = None

    def extract_mileage(self):
        logger.info("Extracting mileage...")
        mileage_tag = self.soup.find('span', text=re.compile(r'Driven.*km'))
        if mileage_tag:
            mileage = mileage_tag.get_text(strip=True)
            # Extract just the number
            mileage_match = re.search(r'([\d,]+)\s*km', mileage)
            if mileage_match:
                mileage_num = mileage_match.group(1)
                self.result['mileage'] = int(mileage_num.replace(',', ''))
            else:
                logger.warning("Mileage format not recognized.")
                self.result['mileage'] = None
        else:
            logger.warning("Mileage not found in the HTML content.")
            self.result['mileage'] = None

    def extract_description(self):
        logger.info("Extracting description...")
        for script in self.soup.find_all('script'):
            if script.string and 'redacted_description' in script.string:
                # Use regex to extract the description text
                match = re.search(r'"redacted_description":\s*\{\s*"text"\s*:\s*"([^"]*(?:\\.[^"]*)*)"', script.string)
                if match:
                    description = match.group(1)
                    # Unescape newlines and other escaped characters
                    description = description.replace('\\n', '\n').replace('\\"', '"')
                    self.result['description'] = description
                else:
                    logger.warning("Description not found in the HTML content.")
                    self.result['description'] = None
    
    def extract_all_info(self):
        self.extract_product_name()
        self.extract_price()
        self.extract_year()
        self.extract_mileage()
        self.extract_description()
        return self.result      
    