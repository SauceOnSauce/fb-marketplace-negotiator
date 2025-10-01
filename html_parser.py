'''
Facebook Marketplace Negotiator - HTML Parser Module
This module provides functions to extract HTML content from Facebook Marketplace listings from .html file.
'''

from bs4 import BeautifulSoup
from pydantic import BaseModel, field_validator
from typing import Optional
import logging
import re
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProductData(BaseModel):
    """Validate product data structure."""
    product_name: str
    price: float
    description: str
    year: Optional[int] = None
    mileage: Optional[int] = None
    
    @field_validator("price")
    def price_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("Price must be a positive number.")
        return v
    
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
        logger.info("Extracting description...")
        match = re.search(r'"redacted_description":\{"text":"(.*?)"\}', self.soup.get_text(), re.DOTALL)
        if match:
            description = match.group(1).replace('\\n', '\n').strip()
            if description:
                return str(description)
        logger.warning("Description not found.")
        return None
    
    def parse(self) -> ProductData:
        """Extract and validate all product data."""
        title = self.extract_product_name()
        price = self.extract_price()
        year = self.extract_year()
        mileage = self.extract_mileage()
        description = self.extract_description()
        
        if title is None:
            raise TypeError("Product name could not be extracted from HTML.")
        if price is None:
            raise ValueError("Price could not be extracted from HTML.")
        if description is None:
            raise TypeError("Description could not be extracted from HTML.")
        product_data = ProductData(
            product_name=title,
            price=price,
            year=year,
            mileage=mileage,
            description=description
        )
        
        logger.info("Product data extracted and validated successfully.")
        return product_data
    
   