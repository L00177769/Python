"""
Script: my_for_dictionary_exercise.py
By: Martina Atkinson
Purpose: Teach 'for loop' with Dictionary item 
Prerequisites: None
Tested: 30/9/2022
"""

# create dictionary item (key:value)
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
# Answer - brings back the keys and not the values
for items in scan:
 # For each item, execute this code block
 print(items)
print()


# Exercise scan.items()
print("Exercise scan.items")
print("my_for Exercise")
# create dictionary item
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
# for each item in scan.items bring back the key and value
for ipv4, port in scan.items():
# item key and value printed 
 print(scan.items())
 # break to stop key and value been printed 3 times
 break
print()
"""
Answer scan.items brings back key and value, scan on its own just brings back keys
Put in break to stop printing the same informtion three times
"""

# Tuple example
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
for ipv4, port in scan.items():
 print(f"Found a service on {ipv4} at {port}")
 break