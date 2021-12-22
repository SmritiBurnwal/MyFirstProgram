#Faulty Calculator

a=int(input("A:"))

Operator=input("Operator:")

b=int(input("B:"))

if a==56 and b==6 and Operator=="+":

    print(77)

elif a==45 and b==7 and Operator=="/":

    print(9)

elif a==67 and b==5 and Operator=="*":

    print(555)

elif Operator=="+":

    print(a+b)

elif Operator=="/":

    print(a/b)

elif Operator=="*":

    print(a*b)

else:

    print(a-b)

print("Thanks for using calculator.")