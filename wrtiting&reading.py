# f=open("new.txt","w")
# f.write("this is new file created through py")
# f.close()

# f = open("new.txt", "a")
# a= f.write("writing new line through program")
# print(a)


# f = open("new.txt", "r")
# a= f.read()
# print(a)


# def game():
#     return 60

# score = game()
# with open("score.txt") as f:
#     a = f.read()

# if int(a) == "":
#     with open("score.txt", "w") as f:
#         a = f.write(str(score))
# elif int(a)<score :
#     with open("score.txt", "w") as f:
#         a = f.write(str(score))

# print(score)

# for i in range(2, 20):
#     with open(f"table/table of {i}.txt", "w") as f:
#         for j in range(1, 12):
#             f.write(f"{i} x {j} = {i*j}")
#             f.write("\n")


# word = ["fuck", "bitch", "asshole", ]
# with open("sample.txt") as f:
#     content = f.read()
# for words in word:
#     content = content.replace(words, "@#!@#@")

# with open("sample.txt","w") as f:
#     f.write(content)

# num = 1
# while num <= 6:
#     if num % 3 == 0:
#         print(num)

# def add_five(num1, num2=5):
#     return num1 + 5
# print(add_five(1, 2))

# num = 10
# if num > 20 or num >= 10:
#     print("First")
# elif num <= 10:
#     print("Second")
# else:
#     print("Third")


# names = ['Alice', 'Bob', 'Lance', 'Mike']
# all_names = names
# names.remove('Bob')
# all_names + ['Kevin']
# print(all_names)

# names = ['Alice', 'Bob', 'Lance', 'Mike']
# names[:3]
# print(names)

# def hello(name, salutation):
#     print(salutation, name, sep=", ")

# hello(name="william", salutation="Howdy")

# names = ['Alice', 'Bob', 'Lance', 'Mike']
# names = names[::-1]
# print(names)

# num = input("Enter a float value: ")
# new_num = num // 100
# print(new_num)

# def fib(n):
#     a, b = 0, 1
#     for _ in range(1, n):
#         a, b = b, a + b
#         yield a
# fib_gen = fib(4)
# print(fib_gen)

# w = "la"
# print(w * 4)

# names = ['Alice', 'Lance', 'Bob', 'Mike']
# all_names = names
# names.append('Brock')
# sorted(all_names)
# print(all_names)

# pair1 = ('a', 'b', 'c')
# pair2 = ('d', 'e', 'f')
# index = 0

# while index < len(pair1):
#     for item in pair2:
#         print(pair1[index], item)
#     index += 1

# val = 1 or '2'
# val *= 3
# print(val)

# letter = 'a'
# if letter < 'b':
#     print("First")
# if letter == 'b' or letter > 'c':
#     print("Second")
# elif letter <= 'a':
#     print("Third")
# else:
#     print("Fourth")

# ages = {'Keith': 30, 'Levi': 25, 'John': 20}
# age = ages.get('Kevin')
# print(age)

# pair1 = ('a', 'b', 'c')
# pair2 = ('d', 'e', 'f')
# index = 0

# while index < len(pair1):
#     for item in pair2:
#         print(pair2[index], item)
#     index += 1

# def double_values(list1):
#     doubles = []
#     for num in list1:
#         doubles.append(str(num * 2))
#     return doubles

# first_list = [1, 2, 3, 4]
# print(" ".join(double_values(first_list)))

# num = 12
# num2 = num
# num = num + 1
# num2 = num2 / 2
# print(num2)

# num = 10
# if num > 20 or num > 10:
#     print("First")
# elif num < 10:
#     print("Second")
# else:
#     print("Third")