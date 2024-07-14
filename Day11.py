import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards=[11,10,10,10,2,3,4,5,6,7,8,9,10]


def card_dealer(player):
    a=random.choice(cards)
    if a==11 and sum(player)+a>21:
        a=1
    player.append(a)
    return

def play_blackjack():
    while True:
        a=1
        user_cards=[]
        dealer_cards=[]
        card_dealer(user_cards)
        card_dealer(user_cards)
        card_dealer(dealer_cards)
        print(f"    Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {dealer_cards}")
        if sum(user_cards)==21:
            print("Win with a Blackjack 😎")
            break
        con_pass = input("Type 'y' to get another card, type 'n' to pass: ")
        while con_pass=='y' and sum(user_cards)<21:
            if sum(user_cards) == 21:
                print("Win with a Blackjack 😎")
                break
            card_dealer(user_cards)
            print(f"    Your cards: {user_cards}, current score: {sum(user_cards)}")
            print(f"Computer's first card: {dealer_cards}")
            if sum(user_cards) > 21:
                print(f"   Your final hand: {user_cards}, final score: {sum(user_cards)}")
                print(f"   Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
                print("You went over. You lose 😭")
                a=0
                break
            else:
                con_pass = input("Type 'y' to get another card, type 'n' to pass: ")
                a+=1

        if con_pass=="n":
            print(f"   Your final hand: {user_cards}, final score: {sum(user_cards)}")
            for _ in range(a):
                card_dealer(dealer_cards)
            print(f"   Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
            if sum(user_cards) > sum(dealer_cards) and sum(dealer_cards)<21:
                print("You win 😃")
                a=0
                break
            elif sum(dealer_cards)>21:
                print("Opponent went over. You win 😁")
                break
            elif sum(user_cards) ==sum(dealer_cards):
                print("Draw 🙃")
                break

        if a==0:
            break





def main():
    while True:
        start=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if start=='y':
            print(logo)
            play_blackjack()


        elif start=='n':
            pass




if __name__=="__main__":
    main()
