from html_parser import FacebookMarketplaceParser, ProductData



def display_product_info(product_data: ProductData):
    """Display the extracted product information."""
    print("="*40)
    print("EXTRACTED PRODUCT INFORMATION")
    print("="*40)
    print(f"Product Name: {product_data.product_name}")
    print(f"Price: £{product_data.price}")
    
    if product_data.mileage:
        print(f"Mileage: {product_data.mileage}")
    if product_data.year:
        print(f"Year: {product_data.year}")
        
    print(f"Description: {product_data.description}")
    print("="*40 + "\n")


file = "listings/ZX10R-listing.html"
html = FacebookMarketplaceParser(file)

display_product_info(html.parse())