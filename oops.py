# class Programmer:
#     def __init__(self, name, product):
#         self.name = name    
#         self.product = product
    
#     def getinfo(self):
#         print(f"name of programmer is {self.name} working on product {self.product}")

# saad = Programmer("Saad", "Skype")
# annas = Programmer("Annas", "account")
# saad.getinfo()
 
# class number:
#     def __init__(self, num):
#         self.number = num
        
#     def square(self):
#         print(f"The value of number {self.number} is {self.number **2} ")
        
#     def multiplyby2(self):
#         print(f"The value of number {self.number} is {self.number *2} ")
    
# a = number(3)
# a.square()
# a.multiplyby2()

# class Train:
#     def __init__(self, name, fare, seats):
#         self.name = name
#         self.fare = fare
#         self.seats = seats
    
#     def getStatus(self):
#         print(f"the name of the train is {self.name}")
#         print(f"the number of seats are {self.seats}")
    
#     def fareinfo(self):
#         print(f" the fare is {self.fare}")
        
#     def bookTicket(self):
#         if (self.seats>0):
#             print(f"your ticket has been booked {self.seats}")
#             self.seats = self.seats - 1
#         else:
#             print("sorry no seats availalbe ")
            
#     def cxlTicket(self):
#         print(f"your ticket has been cancelled {self.seats + 1}  ")
    
# intercity = Train("Tezgamm", 2200, 5)
    
# intercity.fareinfo()    
# intercity.bookTicket()
# intercity.cxlTicket()
# intercity.bookTicket()
# intercity.bookTicket()
# intercity.bookTicket()
# intercity.bookTicket()
# intercity.bookTicket()

# intercity.getStatus()        
    
class Number:
     def __init__(self,num):
         self.num = num
         
     
     def __mul__(self,num1):
        return self.num * num1.num
     
     def __add__(self,num1):
        return self.num + num1.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1*n2
print(sum)
print(mul)     