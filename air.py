
# def add_user():

#     user_data = {
#         "name": input("Enter name: "),
#         "surname": input("Enter surname: "),
#         "age": input("Enter age: "),
#         "number": input("Enter number: ")
#     }
    
#     return user_data

# user_main = add_user()

# print(user_main)


# def nomi(a , b , amal):
#     if amal == "+":
#         print(a+b)
#     elif amal == "-":
#         print(a-b)
#     elif amal == "*":
#         print(a*b)
#     elif amal == "/":
#         print(a/b)
    
    
# a = int(input("Birinchi son kiriting:"))
# amal = input("Amalni kiriting:")
# c = int(input("IKkinchi son kiriting:"))

# nomi(a,amal,c)    

# def nums():
#     sonlar = [9, 32, 13, 46,73,2,32,3 ]
#     toq = []
#     main = sonlar

#     for item in main:
#         if item % 2 == 0:
#             a = "salom"
#         else:
#             toq.append(item)
#     print("toq sonlar:", toq)


# nums()


def nums(sonlar):
    toq = []

    for item in sonlar:
        if item % 2 != 0:  
            toq.append(item)
    print("Toq sonlar:", toq)

one = int(input("Enter one number: "))
two = int(input("Enter two number: "))
three = int(input("Enter three number: "))
four = int(input("Enter four number: "))
five = int(input("Enter five number: "))
six = int(input("Enter six number: "))
 
sonlar = [one, two, three, four, five, six]


nums(sonlar)






