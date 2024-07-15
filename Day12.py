import random

logo=r"""
  ________                                 __  .__                                  ___.                 
 /  _____/ __ __   ____   ______ ______  _/  |_|  |__   ____      ____  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/  \   __\  |  \_/ __ \    /    \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |  | |   Y  \  ___/   |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |__| |___|  /\___  >  |___|  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/              \/     \/        \/            \/    \/     \/       


"""
def random_gen():
    global random_num
    random_num=random.randint(1,100)

random_num=0
guess_left=0
print(logo)
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
random_gen()
level=input("Choose a difficulty. Type 'easy' or 'hard': ")
if level=="easy":
    guess_left=10
elif level=="hard":
    guess_left=5

while guess_left>0:
    guess=int(input(f"""You have {guess_left} attempts remaining to guess the number.
Make a guess: 
"""))
    if guess>random_num:
        print("""Too high.
Guess again.""")
        guess_left -= 1
    elif guess<random_num:
        print("""Too low.
Guess again.""")
        guess_left-=1
    elif guess==random_num:
        print(f"You got it! The answer was {random_num}.")
        break

if guess_left==0:
    print("You've run out of guesses, you lose.")

