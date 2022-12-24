from ast import main
from tkinter.tix import MAIN


def greet(name):
    print(f"Good Morning , {name}")


# print(__name__)  - name of the common file is __main__ 
if __name__ == "__main__":
    n = input("Enter a name")
    greet(n)
              
                