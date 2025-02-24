# Following are the list methods in python.


################--------------- append method -----------------#################
# append method : This method add an item to the last of list.

# name = ["ali", "ahmad", "zakria", "haider",]
# name.append("taha")
# print(name)

# fruites = ["apple", "mango", "orange", ]
# fruites.append("banana")
# print(fruites)

# num = [1, 2, 3, 4, 5]
# num.append(6)
# print(num)


################--------------- extend method -----------------#################

# extend method : This method is use to add one list into another.

# num = [1,3,4,3]
# letters = ["a", "b", "c"]
# num.extend(letters)

# letters.extend(num)
# print(letters)

################--------------- insert method -----------------#################

# insert method : We can add an item in list at any index using insert mathod. in this method first we define the index where we want to add and then the item we want to add

# name = ["ali", "ahmad", "taha", "zakria", "haider"]
# name.insert(1, "zakria")
# print(name)

# name.insert(2, "mesum")
# print(name)



################--------------- remove method -----------------#################

# remove method : This method is use to remove the specified item from the list.

# name = ["ali", "ahmad", "haider", "taha",]
# name.remove("haider")
# print(name)

# name.remove("ali")
# print(name)




################--------------- pop method -----------------#################

# pop method : This method is use to remove specified index in the list.

# name = ["ali", "ahmad", "zakria", "haider",]
# name.pop(2)
# print(name)

# name.pop(0)
# print(name)


#####################--------------- sort method --------------------#####################

# Sort method : This method is use to sort a string in ascending and decending orders.

# num = [1, 2, 4, 5,7, 3]
# num.sort()
# print(num)

# num.sort(reverse= True)
# print(num)

# letters = ["a", "d", "c", "b"]
# letters.sort()
# print(letters)

# letters.sort(reverse= True)
# print(letters)

# letters = ["a", "b", "A", "C"]
# letters.sort()
# print(letters)

# name = ["Ali", "Ahmad", "Haider", "aftab"]
# name.sort()
# print(name)

# name.sort(reverse= True)
# print(name)



#####################--------------- reverse method --------------------#####################

# reverse method : This method is use to reverse all the items of list.

# num = [1, 2, 3, 4, 5, 6]
# num.reverse()
# print(num)

# letters = ["a", "b", "c"]
# letters.reverse()
# print(letters)



#####################--------------- copy method --------------------#####################

# copy method : This method is use to copy the items of one list into an other.

# list1 = [1, 2, 5, 6]
# mylist = list1.copy()
# print(mylist)


#####################--------------- count method --------------------#####################

# count method : This method is use to count the specified value in the list.

# name = ["aftab", "ali", "ahmad", "aftab", "taha", "aftab", "haider"]
# x = name.count("aftab")
# print(x)

#####################--------------- clear method --------------------#####################

# clear method : This method is use to clear all the items of list.

# name = ["ali", "haider", "aftab", "khan", "zain"]
# name.clear()
# print(name)