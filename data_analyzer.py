'''
Market Data Analyzer Module
Analyzes extracted data to provide insights and suggestions for negotiation.
'''
from datetime import datetime 
import logging

logging.basicConfig(level=logging.INFO)
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
    
    def analysis_vehicle_mileage(self, mileage: int):
        '''Analyze vehicle mileage against average UK mileage.'''
        vehicle_age = self.market_result['vehicle_age']
        
        mileage_average = round(mileage / vehicle_age)
        logger.info(f"Vehicle mileage analysis...")
    
        if mileage_average > 12000:
            '''High mileage'''
            #print("High mileage")
        elif mileage_average > 12000 and mileage_average < 10000:
            '''Average mileage'''
            #print("Average mileage")
        else:
            '''Low mileage'''
            
        self.market_result['mileage_analysis'] = mileage_average
     
    # def analyzed_data(self):
    #     self.vehicle_age()
    #     self.analysis_vehicle_mileage()
    #     return self.market_result

    #TODO: Add more analysis methods here as needed