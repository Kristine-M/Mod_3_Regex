# task 1

# You are given a piece of code that is intended to 
# extract email addresses from a given text. However, 
# the code contains errors and does not function as expected.
# Your task is to identify and correct these errors.


# Correct the regex pattern to capture email addresses effectively.
# Modify the code to handle different cases in email addresses.

import re

text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
print(emails)


# task 2

# Problem Statement: You have a log file represented as a string, 
# containing timestamps and messages. Write a script to reformat the 
# timestamps from 'MM-DD-YYYY' to 'YYYY-MM-DD' and anonymize any usernames 
# mentioned in the log (format: '@username').

# Code Example:

log_data = log_data = "12-25-2022: @john Logged in. 01-01-2023: @jane Accessed the dashboard."
# Correctly reformat the date in each log entry.
# Replace all instances of '@username' with '[ANONYMIZED USER]'.
# Use re.sub() effectively to achieve the desired text manipulations.


def reformat(log_data):

    new_log = re.sub(r'(\d{2}-\d{2})-(\d{4})', r'\2-\1', log_data)

    new_log = re.sub(r'@(\w+)', '[ANONYMIZED USER]', new_log)

    return new_log


reformatted = reformat(log_data)

print(reformatted)
