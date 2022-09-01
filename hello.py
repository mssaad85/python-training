# myDict = {
#     "balla" : "Bat",
#     "Pankha" : "Fan",
#     "palang" : "Bed"
# }

# print("Options are : ", myDict.keys())
# a= input("Enter you option : ")
# print("your answer is :", myDict.get(a))

# a = input("Enter Fruit NAme : ")
# b = input("Enter Fruit NAme : ")
# c = input("Enter Fruit NAme : ")
# d = input("Enter Fruit NAme : ")

# s = [a,b,c,d]
# print(s)

# n1 = int(input("enter Num : "))
# n2 = int(input("enter Num : "))
# n3 = int(input("enter Num : "))
# n4 = int(input("enter Num : "))
# n5 = int(input("enter Num : "))
# n6 = int(input("enter Num : "))
# n7 = int(input("enter Num : "))
# n8 = int(input("enter Num : "))

# s= {n1,n2,n3,n4,n5,n6,n7,n8}
# print(s)

# lang = {}
# a = input ("Enter you fav lang : ")
# b= input ("Enter you fav lang : ")
# c= input ("Enter you fav lang : ")
# d= input ("Enter you fav lang : ")
# lang["Saad"] = a
# lang["Annas"] = b
# lang["Ali"] = c
# lang["Moin"] = d
# print(lang)


# sub1= int(input("enter marks in english out of 100 : "))
# sub2= int(input("enter marks in maths out of 100 : "))
# sub3= int(input("enter marks in urdu out of 100: "))
# sub4= int(input("enter marks in sst out of 100 : "))

# per1 = sub1/100*100
# per2 = sub2/100*100
# per3 = sub3/100*100
# per4 = sub4/100*100

# if(per1<=33):
#     print("Fail")
# else:
#     print("you have pass")

# if(per2<=33):
#     print("Fail")
# else:
#     print("you have pass")
# if(per3<=33):
#     print("Fail")
# else:
#     print("you have pass")
# if(per4<=33):
#     print("Fail")
# else:
#     print("you have pass")




# text = input("Enter comment : ")

# if("buy now" in text):
#     spam = true
#     print("this is spam")
# elif("subscribe now" in text):
#     print("this is spam")
# elif("make money" in text):
#     print("this is spam")
# else:
#     print("not spam")


# a = input("Enter user name :")
# if(len(a) <10):
#     print("User name is less than 10 ")
# else:
#     print("USesr name is ok")


# a = ["saad", "annas", "ali", "moin"]
# if("saad" in a):
#     print("name is present")

# fruits = ["apple", "Mango", "banana", "grapes"]
# i=0
# while i < len(fruits):
#     print(fruits[i])
#     i +=1

# for items in fruits : 
#     print(items)


# for i in range(8):
#     # print(i)


# for i in range(1, 8):
#     print(i)

# num = int(input("Enter you number for multiplication : "))
# print("Table")
# for i in range(1 , 12) :
    
#     print(f"{num} x {i} = {num*i}")

# li = ["Saad" , "Annas", "Ali", "Moin"]
# for name in li:
#     if name.startswith("S"):
#         print("Hello" + name)
 

# from multiprocessing.sharedctypes import Value


# student_grade = {
#     "saad" : 72,
#     "madiha" : 82,
#     "ali" : 72,
#     "annas" : 80 
# }

# for key, value in student_grade.items():
#     print(f"Mr.{key} has got marks {value}")

# username = " "

# while username != "Saad" :
#     username = input("enter user name : ")

# while True:
#     username = input("enter user name :")
#     if username == "Saad":
#         print("you have loggedin")
#         break
#     else:
#         continue 


# data = []
# while True:
#     a = input("Say some this : ")
#     if a == "end":
#         break
#     else:
#        data.append(a)

# print(' '.join(data))





# def sentence_maker(phrase):
#     interogatives = ("how", "when","where","what","how",)
#     capitalize = phrase.capitalize()
#     if phrase.startswith(interogatives):
#        return "{}?".format(capitalize)
#     else:
#        return "{}.".format(capitalize)

# result = []
# while True:
#     a = input("say something :")
#     if a == "end":
#         break
#     else:
#         result.append(sentence_maker(a))

# print(" ".join(result))



# def sentence_maker(phrase):
#     capitalize = phrase.capitalize()
#     interpgatives = ("when", "where", "why", "what")
#     if phrase.startswith(interpgatives):
#         return "{}?".format(capitalize)
#     else:
#         return "{}.".format(capitalize)

# word = []
# while True:
#     inp = input("say something : ")
#     if inp == "end":
#         break
#     else:
#         word.append(sentence_maker(inp))

# print(" ".join(word))


# temps = [221, 234, 340, -9999, 230]
# new_temp = [temp/10  if temp != -9999 else 0 for temp in temps]
# print(new_temp)


# array=[99, 'no data', 95, 94, 'no data']
# def foo(array):
#     return [i  if not isinstance(i, str) else 0 for i in array ]

# print(foo(array))

# array = ['1.2', '2.6', '3.3']
# def response (array):
#    return sum(float(i) for i in array)

# print(response(array), type(array))

# file = open("python.docx")
# print(file.read())

# with open("myfile.txt") as myfile:
#     content = myfile.read()

# print(content)

# def occur(char,filepath="bear.txt"):
#     file = open(filepath)
#     content = file.read()
#     return content.count(char)

# print(occur("bear.txt"))
    
# a= input("enter number :")
# b= input("enter number :")
# c= input("enter number :")

# def high(a,b,c):
     
#      return max(a,b,c)

# print(high(a,b,c))

        
# n=1
# for i in range(6):
#     print("*" * (n+i))
    

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
    

print("computers turn choose Rock(r), Paper(p), Scissor(s)")
randNo = random.randint(1,3)
if randNo == 1:
    comp = "r"
elif randNo == 2:
    comp = "p"
elif randNo == 3:
    comp = "s" 

you = input("your turn choose Rock(r), Paper(p), Scissor(s)")

a= gameWin(comp, you)
print(f"compuer choose {comp}")
print(f"you choose {you}")

if a == None:
    print("Tie")

elif a == True:
    print("You win")

else:
    print("You lose")

