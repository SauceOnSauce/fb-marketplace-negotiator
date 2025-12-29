from html_parser import FacebookMarketplaceParser
from data_analyzer import DataAnalyzer
import json
  
      
file = "listings/ZX6R-listing.html"
product_data = FacebookMarketplaceParser(file)
product_data.extract_all_info()
filename = file.replace('.html', '_data.json')

try:
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(product_data.result, json_file, indent=4)
    print(f"""
          {"="*40}
          Product data extracted and saved to {filename}
          {"="*40}
          """)
except Exception as e:
    print(f"Error saving content to JSON: {e}")

with open(filename, 'r', encoding='utf-8') as json_file:
    info = json.load(json_file)

analyzer = DataAnalyzer()
analyzer.vehicle_age(info['year'])
analyzer.average_vehicle_mileage(info['mileage'])
analyzed_data = analyzer.market_result

analyzer.append_to_json(analyzed_data, filename)

#TODO List:
# Priority TODO's:
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
#TODO: Implement a caching mechanism to avoid re-parsing unchanged HTML files.
#TODO: Explore machine learning techniques to predict fair prices based on historical data.
#TODO: Add functionality to compare multiple listings for similar products.
#TODO: Create a notification system to alert users of new listings matching their criteria.
#TODO: Add a feature to track price changes over time for specific listings.