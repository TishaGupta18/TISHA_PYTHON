n=int(input("enter the number upto which you want to print:"))
for number in range(1,n+1):
    if(number%3==0 and number%5==0):
        print("FIZZ BUZZ")
    elif(number%3==0):
        print("BUZZ")
    elif (number % 5 == 0):
        print("FIZZ")
    else:
        print(number)
