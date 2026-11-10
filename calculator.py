#A simple calculator program for performing simple operations
while True:
    try:
        num1=float(input("Enter a number: "))
        num2=float(input("Enter the second number: "))
    except ValueError:
        print("Invalid! Enter only numbers")
        continue
    operation=input("Choose an operation to use +,-,/,* : ").lower().strip()
# + for addition  - for subtraction  / for divisio  * for multiplication 
    if operation not in ["+", "-", "/","*"]:
        print("Invalid! Select an operation from the choices")
        continue
    if operation=="+":
        answer=num1+num2
    elif operation=="-":
        answer=num1-num2
    elif operation=="*":
        answer=num1*num2
    elif operation=="/":
        try:
            answer=num1/num2
        except ZeroDivisionError:
            print("Invalid! Cannot divide by zero")
    print(answer)
    continue_choice=input("Do you want to perform another operation: Yes/No ").lower().strip()
    if continue_choice!="yes":
        print("Thank You!")
        break
