num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

if num2==0:
    print("Error!:Division by zero is not allowed.")

else:
    print("Choose the type of division:1= '/', 2='//', 3='%'")
    choice=int(input("Enter your choice:"))
    if choice==1:
        result=num1/num2
        print("The result is:",result)
    elif choice==2:
       result=num1//num2
       print("The result is:",result)
    elif choice==3:
        result=num1%num2
        print("The result is:",result)
    else:
        print("Invalid Choice !")