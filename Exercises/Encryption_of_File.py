

# ASCII (American Standard Code for Information Interchange) is a character encoding standard
#  that represents text in computers, communication equipment, and other devices.
#  Each character (letters, digits, punctuation, etc.) is assigned a unique number in the ASCII table,
#  which ranges from 0 to 127.
#  For example:

# The character 'A' has an ASCII value of 65.
# The character 'a' has an ASCII value of 97.
# The character '1' has an ASCII value of 49.




# ord(char) :  This is the built in function in python  that takes the character and gives its ASCII Value.

# print(ord("a"))
# print(ord("A"))
# print(ord("k"))
# print(ord("C"))
# print(ord(","))
# print(ord("."))
# print(ord("4"))
# print(ord("#"))
# print(ord("@"))
# print(ord("K") + 5)






# chr(ord(char)) :  This is the built in function in python that takes the ASCII value and change it into corresponding character.

# print(ord("a"))
# print(chr(ord("a") + 3))
# print(ord("d"))


# print(ord("$"))
# print(chr(ord("$") + 3))
# print(ord("'"))







# Write a programe to encrypt the word "Hello".

# word = "Hello"
# encrypted_word = ''.join(chr(ord(char) + 3) for char in word)
# print(encrypted_word)


# Alternative:

# def encrypt_word(word):
#     return ''.join(chr(ord(char) + 5) for char in word)
# print(encrypt_word(input("Enter a word: ")))














# Write a Python program to encrypt the contents of a file plain.txt by shifting each character by 3 ASCII values and save it to encrypted.txt. # Then write a program to decrypt it back to the original file.


# def encrypt_file(input_file, output_file):
#     with open(input_file, "r") as infile, open(output_file, "w") as outfile:
#         for line in infile:
#             encrypted_line = ''.join(chr(ord(char) + 3) for char in line)
#             outfile.write(encrypted_line)

# encrypt_file("output.txt", "ecrypted.txt")
# print("File encrypted successfully")
            
# def decrypt_file(input_file, output_file):
#     with open(input_file, "r") as infile, open(output_file, "w") as outfile:
#         for line in infile:
#             decrypted_line = ''.join(chr(ord(char) - 3) for char in line)
#             outfile.write(decrypted_line)
# decrypt_file("ecrypted.txt", "decrypted.txt")
# print("File decrypted successfully!")


 




















