# task 1

# You have a list of product descriptions. Your task is to tag each product based on keywords in 
# the description. For instance, tag products as 'Electronics', 'Apparel', or 'Home & Kitchen' 
# based on relevant keywords found in their descriptions.

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

# # Tag each product based on keywords in the description

# Efficiently tag each product with the appropriate category ('Electronics', 'Apparel', 'Home & Kitchen') 
# using regex to identify relevant keywords.
# Use regex to match specific product-related keywords in each description.

import re

def tag_products(descriptions):
    tagged = []

    electronics = r"(Smartphone|tv|laptop|headphones)"
    apparel = r"(t-shirt|dress|shorts|leggings|socks)"
    home_kitchen = r"(cutlery|spoon|cookware|knife)"

    # Iterate through each product description
    for word in descriptions:
        # Match keywords in the description using regex
        if re.search(electronics, word):
            
            tagged.append((word, "Electronics"))
            
        elif re.search(apparel, word):
            
            tagged.append((word, "Apparel"))
            
        elif re.search(home_kitchen, word):
            
            
            tagged.append((word, "Home & Kitchen"))
        

    return tagged

tagged_products = tag_products(descriptions)

for product, category in tagged_products:
    print(f"{product}: {category}")


# task 2

# You have a string containing various price formats from an 
# international e-commerce site. Standardize all prices to the 
# format 'USD XX.XX', converting from formats like '$XX.XX', 'XX.XX USD', and 'XX.XX$'.

price_data = "Items cost $15.99, 20.00 USD, and 7.50$."

# Convert all price formats in the string to a standardized 'USD XX.XX' format.
# Use re.sub() to perform the necessary replacements and format transformations.

def standard_pricing(price_data):
   
    pattern = r'\$?(\d+\.\d+)\s*(USD)?\s*\$?'

    data = re.sub(pattern, r'USD \1', price_data)

    return data

prices = standard_pricing(price_data)
print(prices)
