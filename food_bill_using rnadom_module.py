import random
names=input("enter the names of the people separated by a space: ")
names_list=names.split(" ")
print(names_list)

#calculte length of list

length=len(names_list)
a=random.randint(0,length-1)
print(f"{names_list[a]} will pay the bill")