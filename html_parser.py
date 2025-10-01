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
    def __init__(self, html_source: str, is_file: bool = True):
        if is_file:
            with open(html_source, 'r', encoding='utf-8') as f:
                html_content = f.read()
        else:
            html_content = html_source
            
        self.soup = BeautifulSoup(html_content, 'lxml')
        logger.info("="*40)
        logger.info("HTML content parsed successfully.")
 
    def extract_product_name(self):
        # Attempt to extract the product name from the <title> tag
        if self.soup.title and self.soup.title.string:
            logger.info("Extracting product name...")
            match = re.search(r'–\s*(.*?)\s*\|', self.soup.title.string)
            product_name = match.group(1).strip() if match else self.soup.title.string.strip()
        else:
            logger.warning("No <title> tag found in HTML.")
            product_name = None
        return product_name

    def extract_price(self):
        # Attempt to extract the price using regex
        logger.info("Extracting price...")
        price_string = self.soup.find(string=re.compile(r'\£\d+'))
        if price_string:
            match = re.search(r'\£([\d,\.]+)', price_string)
            if match:
                price_value = match.group(1).replace(',', '')
                try:
                    return float(price_value)
                except ValueError:
                    logger.error(f"Could not convert price '{price_value}' to float.")
                    return None
        logger.warning("Price not found or could not be parsed.")
        return None

    def extract_year(self):
        pass

    def extract_mileage(self):
        pass

    def extract_description(self):
        return None
    