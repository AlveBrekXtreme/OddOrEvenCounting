print("This program is a game where you will only count odd numbers or even numbers starting with 1 or 2 depending on what you choose.")
print("")
round = 0
name = input("Type your name/username/nickname/something: ")
while round == 0:
    quitOrAgain = 0
    even = 0
    odd = -1
    x = 0
    y = -1
    oddOrEven = input("Choose between odd or even numbers. (odd/even): ")
    if oddOrEven == "even":
        while x == even:
            even = int(input(name+": "))
            x += 2
        if x != even:
            print("")
            print("Wrong number. The next number was:", x)
            quitOrAgain = int(input("Enter 1 to play again, enter 2 to quit: "))
            if quitOrAgain == 1:
                print("You have choosen to play again")
            elif quitOrAgain == 2:
                print("You have choosen to quit")
                round = 1
            else:
                print("I don't understand what you are saying so I will just assume you said you wanted to play again")    
    elif oddOrEven == "odd":
        while y == odd:
            odd = int(input(name+": "))
            y += 2
        if y != odd:
            print("")
            print("Wrong number. The next number was:", y)
            quitOrAgain = input("Enter 1 to play again, enter 2 to quit: ")
            if quitOrAgain == "1":
                print("You have choosen to play again")
            elif quitOrAgain == "2":
                print("You have choosen to quit")
                round = 1
            else:
                print("I don't understand what you are saying so I will just assume you said you wanted to play again")
    else:
        print("You typed something wrong, try again")
    
End = input("Press enter to stop the program: ")
