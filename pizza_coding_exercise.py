size=input("enter what size pizza do you want (S/M/l)")
bill=0
if(size=='l'or size=='L'):
    bill=bill+300
elif(size=='m'or size=='M'):
    bill=bill+200
else:
    bill=bill+100

pepperoni=input("do you want pepperoni?(y/n)")
if(pepperoni=='y'or pepperoni=='Y'):
    if (size == 's' or size == 's'):
        bill = bill + 30
    else:
        bill=bill+50
cheese=input("do you want cheese?(y/n)")
if(cheese=='y'or cheese=='Y'):
    bill=bill+20

print(f"your bill is {bill}")
