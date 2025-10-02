from html_parser import FacebookMarketplaceParser


def display_product_info(product_name, price, year, mileage, description):
    """Display the extracted product information."""
    print("="*40)
    print("EXTRACTED PRODUCT INFORMATION")
    print("="*40)
    print(f"Product Name: {product_name}")
    print(f"Price: £{price}")
    
    if mileage:
        print(f"Mileage: {mileage}")
    if year:
        print(f"Year: {year}")
        
    print(f"Description: {description}")
    print("="*40 + "\n")


file = "listings/Astra-listing.html"
product_data = FacebookMarketplaceParser(file)

product_name = product_data.extract_product_name()
price = product_data.extract_price()
year = product_data.extract_year()
mileage = product_data.extract_mileage()
description = product_data.extract_description()

display_product_info(product_name, price, year, mileage, description)
