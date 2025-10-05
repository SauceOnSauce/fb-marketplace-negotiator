from html_parser import FacebookMarketplaceParser
from data_analyzer import DataAnalyzer

file = "listings/ZX10R-listing.html"
product_data = FacebookMarketplaceParser(file)
info = product_data.extract_all_info()

def display_info(info):
    """Display the extracted product information."""
    print("="*40)
    print("EXTRACTED PRODUCT INFORMATION")
    print("="*40)
    print(f"Product Name: {info["product_name"]}")
    print(f"Price: £{info["price"]}")
    
    if info["mileage"]:
        print(f"Mileage: {info["mileage"]}")
    if info["year"]:
        print(f"Year: {info["year"]}")
        
    print(f"Description: {info["description"]}")
    print("="*40 + "\n")
        
display_info(info)


#print(info) #Testing purposes only
analyzer = DataAnalyzer()
year = info['year']
mileage = info['mileage']

analyzer.vehicle_age(int(year))
analyzer.analysis_vehicle_mileage(int(info['mileage']))

print(analyzer.market_result) #Testing purposes only