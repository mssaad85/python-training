import random

def gameWin(comp, you):
    if comp == you:
        return None

    if comp == "r":
        if you == "p":
            return True
    
    if comp == "r":
        if you == "s":
            return False
    
    if comp == "p":
        if you == "r":
            return False
    
    if comp == "p":
        if you == "s":
            return True
    
    if comp == "s":
        if you == "r":
            return True
    
    if comp == "s":
        if you == "p":
            return False
    
print("computer turn: Choose Rock(r) Paper(p), Scissor(s)")
randNo = random.randint(1,3)
if randNo == 1:
    comp = "r"

if randNo == 2:
    comp = "p"

if randNo == 3:
    comp = "s"

you = input("your turn: Choose Rock(r) Paper(p), Scissor(s)")

a= gameWin(comp, you)

print(f"compuetr chose {comp}")
print(f"you chose {you}")

if a == None:
    print("Tie")

elif a == True:
    print("You win")

else:
    print("You lose")

