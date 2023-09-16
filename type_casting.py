"""""
length=len("Tisha Gupta")
#print("your name has " +length+ " characters")
#this gives error as  you can only concatenate str (not "int") to str
print("your name has " +str(length)+ " characters")

new_length=str(length)
print(type(length))
print(type(new_length))


print(10+10)  #20
print("10"+"10") #1010
print(int("10")+int("10")) #20

#input from user and sum

x=input("enter first number :")
y=input("enter first number : ")
sum=int(x)+int(y)
print(sum)
"""

#sum of digits of a number

x=input("enter the number: ")
first=x[0]
second=x[1]
sum=int(first)+int(second)
print(sum)