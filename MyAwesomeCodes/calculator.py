

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b

def main():
    while True:
        try:
            o = input("operator: ")
            a = int(input("a: "))
            b = int(input("b: "))
    
            if o == "+":
                print(add(a, b))
            elif o == "-":
                print(sub(a, b))
            elif o == "*":
                print(mul(a, b))
            elif o == "/":
                print(div(a, b))
            elif o == "n":
                break
            else:
                print("Invalid operator")
        except ValueError:
            print("Invalid input for a or b")
        except ZeroDivisionError:
            print("You are dividing by zero idiot !")
        except:
            print("Some Error occured")

main()









