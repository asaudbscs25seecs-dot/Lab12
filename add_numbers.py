# This program adds two numbers provided by the user and prints the result.
def add(a,b):
    return a+b



def main():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("The sum of", a, "and", b, "is", add(a,b))

main()