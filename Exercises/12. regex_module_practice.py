

#################------------------   RegEx (re)  Module  --------------------####################



# Match a Pattern:
# Write a regex to match any email address in a given text.
# Example: "Contact us at support@example.com" → Match: "support@example.com"



# Solution:


# import re

# txt = "Contact us at aftabkhan1567ss@gmail.com or at aftabdevops0@gmail.com"

# pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}"


# check_mail = re.findall(pattern, txt) 
# print(f"Match Emails: {check_mail}")







 






# Find All Occurrences:
# Extract all words that start with a capital letter from a string.
# Example: "Hello from Python and Regex World!" → Match: ["Hello", "Python", "Regex", "World"]


# Solution:



# import re

# txt = "Hello from Python and Regex World!"

# pattern = r"\b[A-Z][a-z]*\b"


# Capital_words = re.findall(pattern, txt) 


# print(f"Capital words in string: {Capital_words} ")






 








# Check a Valid Phone Number:
# Write a regex to check if a string is a valid phone number in the format +92-300-1234567 (Pakistan number format).



# Solution:

# import re

# def phone_number_validation(number):

#     pattern = r"^\+92-[3][0-9]{2}-[0-9]{7,}$"

#     return bool(re.match(pattern, number))

# numbers = [
#     "+92-300-1234567",  # Valid
#     "+92-315-7654321",  # Valid
#     "92-300-1234567",   # Invalid (missing '+')
#     "+92-400-1234567",  # Invalid (400 is not a valid mobile code)
#     "+92-30-1234567",   # Invalid (missing one digit in mobile code)
#     "+92-300-123456"    # Invalid (missing one digit in number)

# ]

# for num in numbers:
#     print(f"{num}: {'Valid' if phone_number_validation(num) else "Invalid"}")



 




 








# Replace Text:
# Replace all occurrences of "color" with "colour" in a given text. "This color is very beautiful. I like this color"  



# import re

# txt = "This color is very beautiful. I like this color"

# new_txt = re.sub(r"color", "colour", txt)

# print(new_txt)















# Extract Numbers:
# Write a regex to extract all numbers (including decimals) from a string.
# Example: "The price is 123.50 and the discount is 20%" → Match: ["123.50", "20"]



# import re

# txt =  "The price is 123.50 and the discount is 20%"

# numbers = re.findall(r"\d+", txt)

# print(numbers)



















# Validate a Password:
# Write a regex to check if a password is valid. A valid password:
# Has at least 8 characters
# Contains at least one uppercase letter
# Contains at least one lowercase letter
# Contains at least one digit
# Contains at least one special character (e.g., @, #, $, %, -, _)



# Solution:


# import re

# def validate_password(password):
#     pattren = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%\.\-_])[A-Za-z0-9.@#$%\-_]{8,}"

#     if re.match(pattren, password):
#         print(f"Correct Password")
#     else:
#         print("Incorrect Password")


# validate_password(input("Enter Your Password: "))











 





# Extract Domain from URLs:
# Write a regex to extract domain names from URLs.
# Example: "https://www.google.com, http://example.org" → Match: ["google.com", "example.org"]



# Solution:

 
# import re

# txt = "https://www.google.com, http://example.org" 

# pattern = r"https?://(?:www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"

# domains = re.findall(pattern, txt)

# print(f"Domains: {domains}")



 




 






# Split a Sentence into Words:
# Use re.split() to split a sentence into words, considering spaces, commas, and periods as delimiters.
# Example: "Hello, how are you? I am fine." → ["Hello", "how", "are", "you", "I", "am", "fine"]




# Solution:



# import re


# txt = "Hello, how are you? I am fine."

# pattern = r"[,?\.\s]"


# word = re.split(pattern, txt)

# words = list(filter(None, word))

# print(words)




















# Find Duplicate Words:
# Write a regex to detect duplicate words in a sentence.
# Example: "This is is a test test sentence." → Match: ["is", "test"]


# Solution:


# import re

# sentence = "This is is a test test sentence."

# pattern = r"\b(\w+)\b\s+\b\1\b"

# duplicates = re.findall(pattern, sentence, re.IGNORECASE)

# print(duplicates)



 














# Validate an IPv4 Address:
# Write a regex to check if a string is a valid IPv4 address (e.g., "192.168.1.1", "255.255.255.0", etc.).





# import re


# def ip_address_validation(address):

#     pattern = r"^(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)$" 

#     is_valid = re.match(pattern, address)

#     if is_valid:
#         print(f"'{address}' is a valid IP")
#     else:
#         print(f"'{address}' is not a valid IP")
     
#     return

# ip_address_validation(input(f"Enter Your IP address: ").strip())         


