from random import randint
print("welcome to rock paper sissors")
s1=0
s2=0
#s1 is score of user
#s2 is  score of computer
for i in range(0,5):
    com=randint(1,3)
    u=int(input("INPUT 1-ROCK,2-PAPER,3-SCISSOR........"))
    if (com==u):
        print(".........its  a TIE.......... ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        s1=s1+1
        s2=s2+1
        print("SCORE IS USER:COMPUTER.....", s1, " : ", s2)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif (com==1 and u==2):
        print(".....you won this round.....!!!!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        s1=s1+1
        print("SCORE IS USER:COMPUTER.....",s1," : ",s2)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif (com==1 and u==3):
        print("you lost this round.....")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        s2 = s2 + 1
        print("SCORE IS USER:COMPUTER.....", s1, " : ", s2)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif (com == 2 and u == 3):
        print("......you won this round.....!!!!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        s1 = s1 + 1
        print("SCORE IS USER:COMPUTER.....", s1, " : ", s2)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif (com ==2 and u == 1):
        print("you lost this round.....")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        s2 = s2 + 1
        print("SCORE IS USER:COMPUTER.....", s1, " : ", s2)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif (com == 3 and u == 1):
        print("....you won this round.....!!!!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        s1 = s1 + 1
        print("SCORE IS USER : COMPUTER.....", s1, " : ", s2)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif (com == 3 and u == 2):
        print("you lost this round.....")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        s2 = s2 + 1
        print("SCORE IS USER : COMPUTER.....", s1, " : ", s2)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("invalid input........You lose")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        s2=s2+1
        print("SCORE IS USER : COMPUTER.....", s1, " : ", s2)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("------------------------------------")
if(s1>s2):
    print("!!!!!!!YOU WON YHE GAME!!!!!!!")
elif(s2>s1):
    print("......YOU LOST THE GAME.......")
else:
    print("^^^^^^^ITS A TIE^^^^^^^")
print("------------------------------------")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("GOODBYE")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")





