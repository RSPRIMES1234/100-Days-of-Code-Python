#prime number check fucntion
# def prime_check(user_input):
#     list=[]
#     for i in range(1,user_input):
#         if (user_input%i==0):
#             list.append(i)
#         else:
#             pass
#     if len(list)>2:
#         print(f"{user_input} is not a prime number")
#     elif len(list)<=2:
#         print(f"{user_input} is a prime number")
#
# prime_check(2)

#Ceaser Cypher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


def encode(text, shift):
    for i, alpha in enumerate(text):
        if alpha in alphabet:
            index_original = alphabet.index(alpha)
            if(index_original+shift<len(alphabet)):
                index_shifted = index_original + shift
                text[i] = alphabet[index_shifted]
            elif(index_original+shift>=len(alphabet)):
                index_shifted = index_original + shift-len(alphabet)
                text[i] = alphabet[index_shifted]

    print(f'The encoded text is {"".join(text)}')


def decode(text,key):
    for i, alpha in enumerate(text):
        if alpha in alphabet:
            index_original = alphabet.index(alpha)
            if(index_original-shift>0):
                index_shifted = index_original - shift
                text[i] = alphabet[index_shifted]
            elif(index_original-shift<=0):
                index_shifted = index_original - shift+len(alphabet)
                text[i] = alphabet[index_shifted]

    print(f'The decoded text is {"".join(text)}')


def ceaser_cypher(text,shift,direction):
    if direction == "decode":
        shift*=-1
    for i, alpha in enumerate(text):
        if alpha in alphabet:
            index_original = alphabet.index(alpha)
            if(index_original+shift<len(alphabet) and index_original+shift>0 ):
                index_shifted = index_original + shift
                text[i] = alphabet[index_shifted]
            elif(index_original+shift>=len(alphabet)):
                    index_shifted = index_original + shift%(-1*len(alphabet))
                    text[i] = alphabet[index_shifted]
            elif (index_original + shift < len(alphabet) and (index_original + shift < 0)):
                index_shifted = index_original + shift % (-1 * len(alphabet))
                text[i] = alphabet[index_shifted]

    print(f'The {direction}d text is {"".join(text)}')

def main():
    print(logo)

    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        text=list(text)
        # if direction=="encode":
        #     encode(text,shift)
        # elif direction=="decode":
        #     decode(text,shift)
        ceaser_cypher(text,shift,direction)
        restart=input("Do you want to restart the ceaser cypher for yes[y] or for no[n] ")
        if restart=="n":
            print("Goodbye")
            break



if __name__=="__main__":
    main()
