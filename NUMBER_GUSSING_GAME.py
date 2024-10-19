import random
print("-----YOU CAN CHOOSE ONLY 1 TO 100-----")
i = 1
while i:
    a = 1
    upper = int(input("ENTER YOUR STARTING NUMBER : "))
    lower = int(input("ENTER YOUR ENDING NUMBER : "))
    rand = random.randint(upper,lower)

    count = 0
    while upper < lower:
        count = count+1
        upper+=1
    if count <= 1:
        turn = 0
    elif count <= 3:
        turn = 1
    elif count <= 5:
        turn = 2
    elif count > 5 and count <= 10:
        turn = 4
    elif count > 10 and count <= 20:
        turn = 5
    elif count > 20 and count <= 35:
        turn = 6
    elif (count > 35 and count <= 50) or (count > 50 and count <= 100):
        turn = 7

        
    print("YOU HAVE CHANCES FOR MATCH THE NUMBER : ",turn)
    while a <= turn:
        choice = int(input("ENTER THE CHOICE : "))
        if choice == rand:
            print("YOU ARE WINNER")
            print(rand)
            break
        else:
            print("YOUR NEXT TURN")
        a += 1
    again = int(input("IF YOU WANT TO PLAY AGAIN PRESS 1 OTHERWISE 0 : "))
    if again != 1:
        print("----THANK_YOU_FOR_PLAYING----")
        break
    i = i + again
