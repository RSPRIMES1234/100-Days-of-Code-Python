print(r""""
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`""")

choice_1=input('Welcome to Treasure Island.Your mission is to find the treasure. Where do you want to go? Type "left" or "right"')
if(choice_1=="right"):
    print("gameover u fell off a cliff")
elif(choice_1=="left"):
    choice_2=input('You reached a lake .There is a island in the middle of the lake.Type "wait" to wait for a boat or type "swim" to swin across')
    if(choice_2=="swim"):
        print("Gameover you were eaten alive by a shark.")
    elif(choice_2=="wait"):
        choice_3=input('You arrive at the island unharmed. There are 3 doors . One red,one yellow and one blue.Which colour do you choose?')
        if(choice_3=="red"):
            print("Gameover u fell into a trap")
        elif (choice_3 == "yellow"):
            print("Gameover u fell into a trap")
        elif(choice_3=="blue"):
            print("Congratulation you found the treasure")
        else:
            print("Gameover undefined door choosen.")
    else:
        print("Gameover as you choose a undefined input.")
else:
    print("Gameover you choose a direction which doesnt exsist.")
