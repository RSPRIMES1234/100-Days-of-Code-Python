# #FIZZBUZZ GAME CODE
# for _ in range(1, 101):
#     if (_ % 3 == 0 and _ % 5 == 0):
#         print("FizzBuzz")
#     elif (_ % 3 == 0):
#         print("Fizz")
#         elif (_ % 5 == 0):
#         print("Buzz")
#     else:
#         print(_)


#password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")

pass_len=int(input("What is the length of your password"))
symbols_count=int(input("How many symbols do you need"))
numeric_count=int(input("How many number of numeric characters do you need"))

alphabet_li=[]
numeric_li=[]
symbol_li=[]

for _ in range(0,symbols_count):
    x=random.choice(symbols)
    symbol_li.append(x)
for _ in range(0,numeric_count):
    x=random.choice(numbers)
    numeric_li.append(x)
for _ in range(0,pass_len-symbols_count-numeric_count):
    x=random.choice(letters)
    alphabet_li.append(x)
pass_li="".join(alphabet_li+numeric_li+symbol_li)
new_pass=[]
for _ in range(len(pass_li)):
    new_pass.append(pass_li[_])

random.shuffle(new_pass)
new_pass="".join(new_pass)
print(f"Here is your password :{new_pass}")







