# # # # # # logical operators

# # # # # a=20
# # # # # b=100

# # # # # if b>a:
# # # # #     print("b is greater than a")
# # # # # else:
# # # # #     print("a is greater than b ")
  
# # # # # i=1

# # # # # while i>0:
# # # # #     print(i)
# # # # #     if (i==1000):
# # # # #         break
    
# # # # #     i+=1


# # # # state={"kano, jos, kaduna, lagos"}
# # # # for x in state:
# # # #     print(x)

# # # color=input("what is your favourite color?")
# # # if color=="purple":
# # #     print("excelent choice")
# # # elif color=="teal" :
# # #     print("not bad") 
# # # elif color=="green":
# # #     print("medicre") 
# # # elif color=="dark":
# # #     print("i like how you think ") 
# # # else:
# # #     print("you are monster")

# # from xml.sax.saxutils import prepare_input_source


# # username="usman"
# # password="12345"
# # print
# # if username=="usman"and password=="12345":
# #     print("well come to the app")
# # else:
# #     print("wrong username or password")
# current_blance=5000
# withdraw=2000
# check=current_blance - withdraw
# if check>=0:
#     print("withdrawal succeessfully")
# else:
#     print("balance is not ssufficient")

print("rock")
print("paper")
print("sccissors")
player1=input("player 1. make your move  ")
player2=input("player 2. make your move   ")

if player1=="rock"and player2=="paper":
    print("player1 wins")
elif player1=="rock" and player2=="scissors":
    print("player2 wins")
elif player1=="scissors" and player2=="paper":
    print("player1 wins")
elif player1=="paper" and player2=="rock":
    print("player1 wins")
elif player1=="paper" and player2=="rock":
    print("player1 wins")
elif player1==player2:
    print("it's tie")
else:
    print("something went wrong")

