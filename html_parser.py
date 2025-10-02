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
        print("="*40)
        print("HTML content loaded successfully.")
        print("="*40)
        
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
        logger.info("Extracting product price...")
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
        product_name = self.extract_product_name()
        # Extract year from product name
        logger.info("Extracting product year...")
        if product_name is not None:
            year_match = re.search(r'\b(19\d{2}|20\d{2})\b', product_name)
            if year_match:
                year = year_match.group(1)
                return year
            else:
                logger.warning("Year not found in product name.")
                return None
        else:
            logger.warning("Year not found in product name.")
            return None

    def extract_mileage(self):
        logger.info("Extracting product mileage...")
        mileage_tag = self.soup.find('span', text=re.compile(r'Driven.*km'))
        if mileage_tag:
            mileage = mileage_tag.get_text(strip=True)
            # Extract just the number
            mileage_match = re.search(r'([\d,]+)\s*km', mileage)
            if mileage_match:
                mileage_num = mileage_match.group(1)
                return mileage_num.replace(',', '')
            else:
                logger.warning("Mileage format not recognized.")
                return None
        logger.warning("Mileage not found in the HTML content.")
        return None

    def extract_description(self):
        logger.info("Extracting product description...")
        for script in self.soup.find_all('script'):
            if script.string and 'redacted_description' in script.string:
                # Use regex to extract the description text
                match = re.search(r'"redacted_description":\s*\{\s*"text"\s*:\s*"([^"]*(?:\\.[^"]*)*)"', script.string)
                if match:
                    description = match.group(1)
                    # Unescape newlines and other escaped characters
                    description = description.replace('\\n', '\n').replace('\\"', '"')
                    return description
        logger.warning("Description not found in the HTML content.")
        return None
    
    