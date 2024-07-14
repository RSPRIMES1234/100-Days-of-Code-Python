import os
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
x=0
print(logo)
auction_list={}
max=""
while True:
    name=input("What is your name? : ")
    bid=int(input("What's your bid? $"))
    auction_list[name]=bid
    countinue=input("Are there any more bidders? Type 'yes' or 'no'.")
    os.system('cls')
    if countinue=="no":
        break
    os.system('cls')

for _ in auction_list:
    if auction_list[_]>x:
        x=auction_list[_]
        max=_


print(f"The winner is {max} with a bid of ${x}.")
