res_p1=0
res_p2=0

print("Please Enter number from 1 to 6 otherwise your input will "
      "count as 0")


while(True):

    # Winner check
    if (res_p1 == 25):
        print("Player 1 wins")
        break
    if (res_p2 == 25):
        print("Player 2 wins")
        break

    #player1
    p1= int(input("Player 1:"))

    if(p1>6 or p1<0):
        print("invalid input , your input is set to 0")
        p1=0

    if (res_p1+p1>25):
        p1=0
    else:
        res_p1+=p1

    #print("P1 res",res_p1)


    #Winner check
    if (res_p1 == 25):
        print("Player 1 wins")
        break
    if (res_p2 == 25):
        print("Player 2 wins")
        break

    ##player 2
    p2 = int(input("Player 2:"))

    if (p2 > 6 or p2 < 0):
        print("invalid input , your input is set to 0")
        p2 = 0

    if (res_p2 + p2 > 25):
        p1 = 0
    else:
        res_p2 += p2

    #print("P2 res", res_p2)

