# A Simple Code By ThisMahdi | Telegram : @Thisismahdi

import random

def GuessNumberGame():
  while(True):
      number_range = int(input("how many digit you want to guess the number?"))
      if number_range < 2:
          first_number = 0
          second_range = 9
          break
      elif number_range == 2:
          first_number = 10
          second_range = 99
          break
      elif number_range == 3:
          first_number = 100
          second_range = 999
          break
      elif number_range == 4:
          first_number = 1000
          second_range = 9999
          break
      else:
          print("range number is invalid, Please enter between 1 and 4")

  random_number = random.randint(first_number,second_range)
  print("Ok! we have created a number for you, let's guess it :)")
  user_input = int(input("You guess here : "))

  while(True):
      if user_input == random_number:
          print(f"You Won! the number was {random_number} ;)")
          break
      elif user_input > random_number:
          print("your guss is higher than the number! Try again.")
          user_input = int(input("You guess here : "))
      elif user_input < random_number:
          print("your guess is lower than the number! Try again.")
          user_input = int(input("You guess here : "))
      else:
          print("Error")
          break

if "__name__ == "__main__":
  GuessNumberGame()
  
# A Simple Code By ThisMahdi | Telegram : @Thisismahdi
