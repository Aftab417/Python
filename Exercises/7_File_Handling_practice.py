
# Write a Python program to read the contents of a file named example.txt and display it on the console.

# with open("example.txt", "w") as f:
#     f.write("Hello world!")


# with open("example.txt", "r") as f:
#     print(f.read())









# Write a Python program to create a file named output.txt and write the text "Hello, File Handling!" into it.

# with open("output.txt", "w") as f:
#     f.write("Hello, File Handling!")





# Modify the file output.txt to add the text "This is an appended line." without overwriting the existing content.

# with open("output.txt", "a") as f:
#     f.write("\nThis is appended line.")








# Write a Python program to count and print the number of lines in a file named output.txt.

# with open("output.txt", "r") as f:
#     line_count = 0
#     for x in f:
#         line_count += 1
# print(line_count)



# Alternative: 

# def line_count():
#     with open("output.txt", "r") as f:
#         return sum(1 for x in f)
# print(line_count()) 

    








# Write a Python program to read the first 3 lines of a file named output.txt.
 
# with open("output.txt", "r") as f:
#     for i in range(3):
#         lines = f.readline()
#         if lines:
#             print(lines.strip())
#         else:
#             break
      
  










# Write a Python program to copy the contents of output.txt into a new file named destination.txt.

# with open("output.txt", "r") as f:
#     data = f.read()
# with open("destination.txt", "w") as f:
#     f.write(data)



# Alternative:

# with open("output.txt", "r") as source_file, open("destination.txt", "w") as destination_file:
#     content = source_file.read()
#     destination_file.write(content)
# print("The content of output.txt is copied to destination.txt")










# Write a Python program to check if the word "want" exists in a file named sample.txt and display its frequency.

# with open("sample.txt", "r") as f:
#     data = True
#     frequency = 0
#     while data:
#         data = f.readline()
#         if "want" in data:
#             frequency += 1
#     print(frequency)




# Alternative: 

# def check_frequency():
#     with open("sample.txt", "r") as f:
#         return sum(1 for x in f if "want" in x)
# print(check_frequency())
         
 

# Alternative:

# with open("sample.txt", "r") as f:
#     content = f.read()
#     frequency = content.count("want")

# if frequency > 0:
#     print(f"The word 'want' exist and appear {frequency} times in the file.")
# else:
#     print("The word 'want' does not exist in the file.")










# Write a Python program that writes a list of numbers [1, 2, 3, 4, 5] to a file numbers.txt. Then read the file and calculate their sum.

# with open("numbers.txt", "w") as f:
#     numbers = [1, 2, 3, 4, 5]
#     for number in numbers:
#         f.write(f"{number}\n")

# def sum_numbers():
#     with open("numbers.txt", "r") as f:
#         return sum(int(line.strip()) for line in f)
# print(sum_numbers())












# Write a Python program to read a large file (largefile.txt) line by line without loading the entire file into memory.

# with open("large_file.txt", "w") as f:
#     f.write("Hi, I am Aftab Ahmad\nI am 18 year old\nI like to play fooball\nCurrently i am working in a Tech company\nas a devops engineer.")



# def read_large_file():
#     with open("large_file.txt", "r") as file:
#         for line in file:
#             print(line.strip())
# read_large_file()






















