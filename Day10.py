import sys
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
operations="""
+
-
*
/
"""

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    try:
        x=a/b
        return x
    except ZeroDivisionError:

       sys.exit( "did you put 0 as a divisor or forgot to put a value for 1 of the 2 values try running caculator again")

def main():
    print(logo)

    while True:
        try:
            num1 = float(input("Whats the next number ?: "))
            operation=input("Pick and operation : ")
            num2 = float(input("Whats the next number ?: "))
            ans=""
            if operation=="+":
                ans=add(num1,num2)
                print(f"{num1} {operation} {num2} = {ans}")
            elif operation == "-":
                ans=sub(num1,num2)
                print(f"{num1} {operation} {num2} = {ans}")
            elif operation == "*":
                ans=mul(num1,num2)
                print(f"{num1} {operation} {num2} = {ans}")
            elif operation =="/":
                ans=div(num1,num2)
                print(f"{num1} {operation} {num2} = {ans}")
            else:
                print("Try again with right operation symbol")

            contine=input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation:")
        except ValueError or ZeroDivisionError:
            print("did you put 0 as a divisor or forgot to put a value for 1 of the 2 values try again")
            while contine=='y':
                try :
                    operation = input("Pick and operation : ")
                    num2 = float(input("Whats the next number ?: "))
                    if operation == "+":
                        ansnew = add(ans, num2)
                        print(f"{ans} {operation} {num2} = {ansnew}")
                    elif operation == "-":
                        ansnew = sub(ans, num2)
                        print(f"{ans} {operation} {num2} = {ansnew}")
                    elif operation == "*":
                        ansnew = mul(ans, num2)
                        print(f"{ans} {operation} {num2} = {ansnew}")
                    elif operation == "/":
                        ansnew = div(ans, num2)
                        print(f"{ans} {operation} {num2} = {ansnew}")
                    else:
                        print("Try again with right operation symbol")

                    contine = input(f"Type 'y' to continue calculating with {ansnew}, or type 'n' to start a new calculation:")
                except ValueError or ZeroDivisionError:
                    print("did you put 0 as a divisor or forgot to put a value for 1 of the 2 values try again")




if __name__=="__main__":
    main()
