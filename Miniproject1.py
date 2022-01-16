#Miniproject: rock, paper, scissors game




#Getting user input
n=int(input("How many games do you want to play?"))


for i in range(n):
    b=input("Please indicate your choice")

    if b=="rock" or b=="paper" or b=="scissor":
        print("it is a valid choice")
    else:
        print("please enter a valid choice")



#Creating system imput

    Li1=["rock", "paper", "scissor"]
    import random
    a=random.choice(Li1)
    print(a)

#Game rules

    if b=="rock" and a=="rock":
        print("draw")
    elif b=="rock" and a=="paper":
        print("loss")
    elif b=="rock" and a=="scissor":
        print("win")
    
    if b=="paper" and a=="paper":
        print("draw")
    elif b=="paper" and a=="scissor":
        print("loss")
    elif b=="paper" and a=="rock":
        print("win")
    
    if b=="scissor" and a=="scissor":
        print("draw")
    elif b=="scissor" and a=="rock":
        print("loss")
    elif b=="scissor" and a=="paper":
        print("win")


#Making the game loop




