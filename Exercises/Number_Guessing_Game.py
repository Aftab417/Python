
# import random

# random_number = random.randint(1, 100)

# attempts = 5
# print("Welcome to the game.")
# print(f"You have {attempts} to Guess the right number between 1 and 100.")

# for attempt in range(1, attempts + 1):
#     guess = int(input(f"Attempt {attempt} Enter Your Guessed Number: "))
#     if guess == random_number:
#         print(f"Congratulation! You have guessed the right number.")
#         break
#     elif guess < random_number:
#         print(f"Too Low. Try some greater number.")
#     else:
#         print(f"Too High. Try a lowr number.")

#     if attempt == attempts:
#         print(f"Sorry You are Failed. The correct number is {random_number}")







####################---------------- NUmber Gussing Game in OOPS -------------#####################




# import random

# class NumberGuessingGame:
#     def __init__(self, attempts = 5):
#         self.random_number = random.randint(1, 100)
#         self.attempts = attempts

#     def play(self):
#         print(f"Welcome to the Game!\nYou have {self.attempts} attempts to guess the right number between 1 & 100.")

#         for attempt in range(1, self.attempts + 1 ):
#             guess = self.get_user_input(attempt)

#             if self.check_guess(guess):
#                 break
#         else:
#             print(f"Sorry you failed. The correct number was {self.random_number}")     


#     def get_user_input(self, attempt):
#         while True:
#             try:
#                 return int(input(f"Attempt {attempt}: Enter Your Guess Number:  "))
#             except ValueError:
#                 print(f"Invalid syntax! Please enter the correct value")


#     def check_guess(self, guess):
#         if guess == self.random_number:
#             print(f"Congratulation! You have guessed the right number.")
#             return True
#         elif guess > self.random_number:
#             print("Too Large. Try a smaller one")
#         elif guess < self.random_number:
#             print("Too Low. Try a greater one")
#         else:
#             return False
        

# game = NumberGuessingGame()

# game.play()  