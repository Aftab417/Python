
###################-----------------   RegEx  (Regular Expression)   ------------------####################


# RegEx in python is a powerful tool for pattern matching text manipulation. It allows us to search, match, extract
#  and manipulate string based on specified pattern.
#  Python provide  're' module to work with RegEx.


#  HOW IT WORKS:
#       RegEx use a set of symbols and rules to define the pattern that can be used to match string.  You provide the 
#   pattren, python checks whether the given string follows that pattren or not.



# Example:

# import re

# pattern = r"\d"                # This pattren match any digits (0 - 9)
# txt = "hello123"

# if re.search(pattren, txt):
#     print("Text contain digits")








###################-----------------   RegEx  Metacharacters   ------------------####################

#  These are special characters with specific meaning to define a pattren.  


#  characters           -------->           Meanings

#   .                   -------->          all characters except newline character 
      
#   ^                   -------->           Start with  
     
#   $                   -------->           End with   
    
#   *                   -------->           0 or more occurence   
    
#   +                   -------->           1 or more occurence    
   
#   ?                   -------->           0 or 1 occurance    
   
#   {}                  -------->          specified number of occurance.  or between two specified characters  (e.g: {2}  or  {c, f}) 
     
#   []                   -------->          character set  (e.g: [a-z] matches lowercase letters)  
     
#   |                   -------->           or operator  (e.g: cat|dog,   matches  cat or dog)  
     
     
 





###################-----------------   RegEx  Special Sequences   ------------------####################


# Sequence              --------->              Meanings


#  \A                   --------->            return match if specified charcters are present at the begnning of string. (e.g:  r"\AThe) 

#  \Z                   --------->            return match if specified charcters are present at the end of string. (e.g:  r"school\Z) 
   
#  \b                   --------->            return match if specified charcters are present at begnning or at end of string. (e.g: r"\bain"  or  r"ain\b") 
 
#  \B                   --------->            return match if specified charcters are present no matter in start or at end of string. (e.g: r"\Bain"  or  r"ain\B")  

#  \d                   --------->            return match if any digit(0 - 9)  us present in string 

#  \D                   --------->            return match if there is non-digit  string

#  \s                   --------->            if Any whitespace (space, tab, newline) 

#  \S                   --------->            if Any non-whitespace 

#  \w                   --------->            if Any word character(letters, digits, underscores) 

#  \W                  --------->             if Any non-word character





#######################--------------  Some specific pattern groups -------------###########################


#   (?= ... )          it  is a positive lookahead, meaning it check ahead in the string for a required condition without consuming characters.

#       .*             Match any number of character.

# e.g:   (?=.*[A_Z])    this will check for capital letter in the string 






#   (?: ... )           This is non-capturing group. it group the pattern but does not store in the final match result.

# e.g:  (?:www\.)       This  will not capture the  "www."










#   ()               It is capturing group. Anything inside it is captured.   
# 
# 
#   e.g:     r"\b(\w+)\b"     This will capture the whole word.











###################-----------------   're'  module common methods   ------------------####################



###################-----------------   .group()   ------------------####################

# return the part of string where pattren match.




###################-----------------   re.search(pattern, string)   ------------------####################

# Search for the first match of pattern in the string.


# import re

# txt = "hello my number is 12345. Is this right."

# x = re.search(r"\d+", txt) 

# if x:
#     print(x.group())









 
###################-----------------   re.match(pattern, string)   ------------------####################

# checks if the pattern matches from the start of string.



# import re

# txt = "hello, world."

# x = re.match(r"hello", txt)

# if x:
#     print("Match found:", x.group())







# Alternative



# import re

# txt = "Say hello, world" 

# x = re.match(r"hello", txt)

# if x:
#     print(f"Match found: '{x.group()}'") 
# else:
#     print("Match not found.")
















###################-----------------   re.findall(pattern, string)   ------------------####################

# return the list of all matches of pattern in string



# import re

# txt = "my nubers are 123, 456, 678"

# x = re.findall(r"\d+", txt)

# if x:
#     print(x)











###################-----------------   re.finditr(pattern, string)   ------------------####################

# return the iterator of match objects.

# import re

# txt = "my number are 123, 456, 789 "

# x = re.finditer(r"\d+", txt)

# for match in x:
#     print(match.group())













###################-----------------   re.sub(pattern, replacement, string)   ------------------####################

# Replace matches with new string.



# import re

# txt = "I have apples, apples and more apples" 

# new_txt = re.sub(r"apples", "oranges", txt)

# print(new_txt)














###################-----------------   re.split(pattern, string)   ------------------####################

# Split the string at points where pattern matches





# import re

# txt = "mango:orange,banana|cherry"

# words = re.split(r"[:,|]", txt)

# print(words)













# Summary


# re.search(pattern, str)
# re.findall(pattern, str)
# re.finditr(pattern, str)
# re.match(pattern, str)
# re.sub(pattern, replacement, str)
# re.split(pattern, str)

# .group() 













