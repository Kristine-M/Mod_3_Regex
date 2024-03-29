# task 1

# Develop a script to extract specific information from a formatted text. 
# The text contains data entries delimited by semicolons and formatted as 'Key: Value'. 
# Extract the value corresponding to a specific key.

import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"

# Successfully extract the 'Occupation' value from the text.
# Implement a regex pattern that accurately targets and captures the desired data.


pattern_to_find = r"\b" + "Occupation" + r":\s*([^;]+)"

found = re.search(pattern_to_find, text)



if found:
    occupation = found.group(1).strip()
    print("occupation:", occupation)
else:
    print("Key not found")
    
    
# task 2

# Write a Python program to validate a list of URLs. 
# A valid URL should start with 'http://' or 'https://', followed by a domain name.

urls = ["https://example.com", "www.example.com", "http://test.com"]


# Correctly identify and categorize valid and invalid URLs from the list.
# Use regex to validate the format of each URL.


def validate(urls):
    valid = []
    invalid = []

    
    pattern = r'^(https?://)?(?:www\.)?\w+\.\w+$'

    for website in urls:
        
        if re.match(pattern, website):
            
            valid.append(website)
            
        else:
            
            invalid.append(website)

    return valid, invalid

valid_urls, invalid_urls = validate(urls)

print("valid url:", valid_urls)
print("invalid url:", invalid_urls)
