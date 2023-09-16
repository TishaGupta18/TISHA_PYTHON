height=input("enter all heights separated by space:")
height_list=height.split()
print(height_list)
count=0
for i in height_list:
    count=count+1
#print(count)
for i in range(0,count):
    height_list[i]=int(height_list[i])
print(height_list)
total=0
for i in height_list:
    total=total+i
avg=total/count
print(round(avg))