from html_parser import FacebookMarketplaceParser
import json
  
      
file = "listings/2018_GSXR.html"
product_data = FacebookMarketplaceParser(file)
product_data.extract_all_info()
filename = file.replace('.html', '_data.json')

try:
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(product_data.result, json_file, indent=4)
    print(f"{"="*80}\nProduct data extracted and saved to {filename}\n{"="*80}")
    
except Exception as e:
    print(f"Error saving content to JSON: {e}")

with open(filename, 'r', encoding='utf-8') as json_file:
    info = json.load(json_file)
    
    