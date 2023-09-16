#arithmetic operators + _ * / ** ^

#CALCULATE BMI
# height=input("enter height in metres: ")
# weight=input("enter weight in kgs: ")
# bmi=float(weight)/(float(height)**2)
# print(bmi)

#assignment operators = += -= /=
#comparison or assignment operators = <= >= < > !=
#logical operators and or not
#bitwise operator  & | ^ ~ << >>
#identity operator  is   is not

a=5
b=6
print(id(a)) #2333308840368
print(id(b)) #2333308840400
print(a is b) #false

x=7
y=7
print(id(x))    #2333308840432
print(id(y))    #2333308840432
print(x is y) #true 

p=2
print(id(p))  #2333308840272
p=3
print(id(p))  #2333308840272
print(p is p)  #True

#membership  operators  in   not in
str="Tisha"
print('s' in str)
print('Tis' not in str)
print('A' in str)
l1=[1,2,3,4,5]
print(3 in l1)