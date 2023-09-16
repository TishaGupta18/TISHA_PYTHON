numbers=input("enter all heights separated by space:")
numbers_list=numbers.split()
print(numbers_list)
count=0
for i in numbers_list:
    count=count+1
#print(count)
for i in range(0,count):
    numbers_list[i]=int(numbers_list[i])
print(numbers_list)
max_no=numbers_list[0]
for i in numbers_list:
    if i>max_no:
        max_no=i
print(f"max number is {max_no}")