
#######################------- Logical and Operator -----------##########################

# Logical and :  It return True answer if both statements are True. And False if both or one of the statements is False.

# print((5>2) and (5<10)) # True
# print((5<2) and (5<10)) # False
# print((5<2) and (5>10)) # False


# x = 5>2           # True
# y = 5<10          # True
# print(x and y)    # True => Because both statements are true.

# a = 5 < 2         # False
# b = 5 > 2         # True
# print(a and b)    # False => Because "and" operators gives true only when both statements are tue, in above situation one of statements is false so the answer is false.

# a = 5 < 2         # False
# b = 5 > 10        # False
# print(a and b)    # False => Because both statements are false 



#######################------- Logical or Operator -----------##########################

# Logical or : It return True if both or one of the statements is true. And only return False if both statements are False.

# print((5>2) or (5<10))   # True
# print((5<2) or (5<10))   # True
# print((5<2) or (5>10))   # False


# x = 5>2            # True
# y = 5<10           # True
# print(x or y)      # True


# a = 5>2           # True
# b = 5>10          # False
# print(a or b)     # True   => Because one of the statement is True.


# a = 5<2           # False
# b = 5>10          # False
# print(a or b)     # False  => Because both statements are False.



#######################------- Logical not Operator -----------##########################


# Logical not : It reverse the Final answer. If the answer is True it will return False and return True if the answer is False.

# print(not (5>2) and (5<10) ) # False => Because the Final answer of statements is true and not operater reverse the answer.
# print(not (5<2) and (5<10) ) # True 

# a = 5>2                      # True
# b = 5<10                     # True
# print(not(a and b))          # False  => Because both statements are true, "and" operater will return True, but "not" operater reverse the final option of "and" into False.
# print(not(a or b))           # False  => Because "or" operator will return True and "not" operator will reverse the answer of "or" into False. 

# a = 5>2                      # True
# b = 5>10                     # False  
# print(not(a and b))          # True   => Because one of the statements is False "and" operator will return False, but "not" operater wil reverse the answer into True.
# print(not(a or b))           # False  => Because one of the statements is True "or" operator will return True, but "not" operator will reverse it into False.

# a = 5<2                      # False 
# b = 5>10                     # False 
# print(not(a and b))          # True   => Because both statement are False "and" will return False, but "not" will change it into True.
# print(not(a or b))           # True   => Because both Statement are False "or" will return False, but "not" will change it into True.



