'''
Market Data Analyzer Module
Analyzes extracted data to provide insights and suggestions for negotiation.
'''
from datetime import datetime 
import logging
import json


logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class DataAnalyzer():
    '''Analyzes product data and generates negotiation suggestions.'''
     
    def __init__(self):
        '''Initialize the analyzer.'''
        logger.info("Data analyzer initialized.")
        
        self.market_result = {}
    
    def vehicle_age(self, year: int):
        '''Calculate vehicle age.'''
        current_year = datetime.now().year
        vehicle_age = current_year - year
        
        logger.info(f"Vehicle age calculation...")
        self.market_result['vehicle_age'] = vehicle_age
    
    def average_vehicle_mileage(self, mileage: int):
        '''Analyze vehicle mileage against average UK mileage.'''
        vehicle_age = self.market_result['vehicle_age']
        
        mileage_average = round(mileage / vehicle_age)
        logger.info(f"Vehicle mileage average...")
            
        self.market_result['mileage_average'] = mileage_average
        
    def append_to_json(self, data: dict, filename: str):
        '''Append analyzed data to product_data.json file.'''
        with open(filename, 'r+', encoding='utf-8') as json_file:
            existing_data = json.load(json_file)
            existing_data.update(data)
            json_file.seek(0)
            json.dump(existing_data, json_file, indent=4)
        logger.info(f"Appending analyzed data to {filename}...")
    