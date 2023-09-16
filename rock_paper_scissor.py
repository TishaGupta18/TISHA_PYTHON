import random
rock='''
      🤛🏻
'''
paper='''
     👋
'''
scissor='''
     ✂
'''
user_choice=int(input("ENTER YOUR CHOICE: TYPE 0 FOR ROCK,1 FOR PAPER,2 FOR SCISSOR "))
images=[rock,paper,scissor]

if(user_choice>2 or user_choice<0):
    print("wrong choice... YOU LOSE")
else:
    print(images[user_choice])
    computer_choice=random.randint(0,2)
    print("computer chose:")
    print(images[computer_choice])
    if(user_choice==computer_choice):
        print("MATCH DRAW")
    elif(user_choice==0 and computer_choice==2):
        print("YOU WIN")
    elif(user_choice==2 and computer_choice==0):
        print("YOU LOSE")
    elif(user_choice<computer_choice):
        print("YOU LOSE")
    elif(user_choice>computer_choice):
        print("YOU WIN")
