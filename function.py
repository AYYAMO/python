# # # # # def sing_happy_birthday():
# # # # #     print("happy birthday to you")
# # # # #     print("happy birthday to you")
# # # # #     print("happy birthday to you")
# # # # #     print("happy birthday to you")
# # # # # sing_happy_birthday()


# # # # # def add(num1, num2):
# # # # #     return num1 + num2
# # # # # print(add(3, 5))
# # # # # print(add(70, 30))

# # # # def devide(num1, num2):
# # # #     return num1 / num2
# # # # print(devide(3, 5))
# # # # print(devide(70, 30))

# # # # def add(name, school):
# # # #     return name + " "+school
# # # # print(add("usman","buk" ))


# # # def add(*name):
# # #     print(name) 
# # # add("usman","buk" )


# # def passwordlenght(password):
# #     password=str(password)
# #     lenght=len(password)
# #     return lenght
# # password="bluehub"
# # print(passwordlenght(password))


def passwordcheck(password):
    if len(password)<7:
        print("the pasword has to be more than or equal to 7 digit")
    else:
        print("the account has been created")
password="ruuudjjdllll"
print(passwordcheck(password))


