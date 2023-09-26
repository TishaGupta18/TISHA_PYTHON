import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['@','#', '$', '^', '&', '*', '(', ')', '_']
print("Welcome to password generator")
n_letters=int(input("How many letters do you want in your password?\n"))
n_numbers=int(input("How many numbers do you want in your password?\n"))
n_symbols=int(input("How many symbols do you want in your password?\n"))
password_list=[] #cresting an empty list
for i in range(1,n_letters+1):
    char = random.choice(letters)
    password_list=password_list+[char] #adding the char extracted to the list
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password_list=password_list+[char]
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password_list=password_list+[char]
random.shuffle(password_list)  #shuffling the list
#print(password_list)
#coverting the list to a string
password=""  #creating an empty string
for i in password_list:
    password=password+i
print(password)