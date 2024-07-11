# #DAY 4 - TREASURE MAP
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input("Where do you want to put the treasure?")
#
# letter=position[0]
# abc=["A"A,"B","C"]
# posx=abc.index(letter)
# posy=int(position[1])-1
# map[posx][posy]="X"
#
# print(f"{line1}\n{line2}\n{line3}")

#DAY4 ROCK,PAPER,SCISSORS
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice=int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors."))
list=[rock,paper,scissors]


computer_choice=random.randint(0,int(len(list)-1))
if(user_choice==0):
    print(list[user_choice])
    print("Computer chose:")
    if(computer_choice==0):
        print(list[computer_choice])
        print("Draw")
    elif(computer_choice==1):
        print(list[computer_choice])
        print("You lose")
    elif(computer_choice==2):
        print(list[computer_choice])
        print("You Win")
    else:
        print("You choose a invalid number You loose!")
elif(user_choice==1):
    print(list[user_choice])
    print("Computer chose:")
    if (computer_choice == 0):
        print(list[computer_choice])
        print("You Win")
    elif (computer_choice == 1):
        print(list[computer_choice])
        print("Draw")
    elif (computer_choice == 2):
        print(list[computer_choice])
        print("You loose")
    else:
        print("You choose a invalid number You loose!")
elif(user_choice==2):
    print(list[user_choice])
    print("Computer chose:")
    if (computer_choice == 0):
        print(list[computer_choice])
        print("You Lose")
    elif (computer_choice == 1):
        print(list[computer_choice])
        print("You Win")
    elif (computer_choice == 2):
        print(list[computer_choice])
        print("Draw")
    else:
        print("You choose a invalid number You loose!")
else:
    print("You choose a invalid number You loose!")
