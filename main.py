from html_parser import FacebookMarketplaceParser
from data_analyzer import DataAnalyzer
import json


def display_info(info):
    """Display the extracted product information."""
    print("="*40)
    print("EXTRACTED PRODUCT INFORMATION")
    print("="*40)
    print(f"Product Name: {info['product_name']}")
    print(f"Price: £{info["price"]}")
    
    if info["mileage"]:
        print(f"Mileage: {info["mileage"]}")
    if info["year"]:
        print(f"Year: {info["year"]}")
        
    print(f"Description: {info["description"]}")
    print("="*40)
        
def display_analyzed_info(analyzed_data):
    """Display the extracted product information."""
    print("="*40)
    print("Analyzed PRODUCT INFORMATION")
    print("="*40)
    print(f"Vehicle Age: {analyzed_data['vehicle_age']}")
    print(f"Mileage Analysis: {analyzed_data['mileage_analysis']} miles/year")  
    print("="*40)  
    
      
file = "listings/Polo-listing.html"
product_data = FacebookMarketplaceParser(file)
product_data.extract_all_info()
#read product data from json
with open('listings/Product_data.json', 'r', encoding='utf-8') as json_file:
    info = json.load(json_file)
#print(info)testing purposes only

display_info(info)

#print(info) #Testing purposes only
analyzer = DataAnalyzer()

year = info['year']
mileage = info['mileage']

analyzer.vehicle_age(year)
analyzer.analysis_vehicle_mileage(mileage)
analyzed_data = analyzer.market_result

display_analyzed_info(analyzed_data)



#TODO List:
# Priority TODO's:
    #TODO: Create a function to save the extracted and analyzed data to a JSON or CSV file to handover to LLM message generator.
    #TODO: Implement negotiation message generation from extracted data using Local and/or API LLM.
    #TODO: Implement error handling in case the HTML structure changes or expected data is missing 
        #TODO: Add option to enter missing data manually before moving on.
    #TODO: Improve description clean up to remove unnecessary characters.
    #TODO: Refactor code for readability and maintainability.
    #TODO: Implement a web scraper to automatically download HTML files from Facebook Marketplace listings url.
        #visit url, save and rename html file, store locally, then parse it.
    #TODO: Create documentation for users on how to use the tool effectively.
    
    
# Other TODO's:
#TODO: Add support for additional marketplaces beyond Facebook Marketplace.   
#TODO: Add functionality to process multiple listings in a batch mode.
#TODO: Integrate with a database to store and query historical listing data.
#TODO: Add unit tests to ensure the reliability of the parsing and analysis functions.
#TODO: Create a simple GUI to allow users to upload HTML files and view extracted data easily.
    #TODO: Integrate with social media platforms to share extracted listings or negotiation messages. Discord/Whatsapp/Telegram.
#TODO: Add logging to track the flow of data and any issues encountered during parsing and analysis.
#TODO: Optimize performance for large HTML files or multiple listings.
#TODO: Implement a caching mechanism to avoid re-parsing unchanged HTML files.
#TODO: Explore machine learning techniques to predict fair prices based on historical data.
#TODO: Add functionality to compare multiple listings for similar products.
#TODO: Create a notification system to alert users of new listings matching their criteria.
#TODO: Explore the use of AI to enhance data extraction accuracy and handle complex HTML structures.
#TODO: Add a feature to track price changes over time for specific listings.
#TODO: Collaborate with other developers to expand the tool's capabilities and reach.
#TODO: Stay updated with changes in Facebook Marketplace's HTML structure to maintain parsing accuracy.
#TODO: Solicit user feedback to continuously improve the tool's usability and functionality.