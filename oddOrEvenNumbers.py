from timeit import default_timer as timer #imports a timer


print("This program is a game where you will only count odd numbers or even numbers starting with 1 or 2 depending on what you choose.") #Introduction
print("")
z = 0 #doesn't really matter what this is named
highscore = 0 
name = input("Type your name/username/nickname/something: ")
while z == 0: #it will remain 0 unless the player choose to quit, meaning the user can play this as long as they want
    #these are placed whithin the while loop so they reset after a round
    times = 0 #This is used to keep count of how many times the player has played a round.
    quitOrAgain = 0 
    average = 0
    even = 0
    odd = -1
    x = 0 
    y = -1 
    oddOrEven = input("Choose between odd or even numbers. (odd/even): ") 
    if oddOrEven == "even":

        while x == even:
            start = timer()
            even = int(input(name+": ")) 
            end = timer()
            time = end - start
            print(time, "sec")
            average += time 
            times += 1 
            x += 2
        if x != even:
            print("")
            print("Wrong number. The next number was:", x)
            print("Your average speed between numbers are:", average/times, "sec") 
            quitOrAgain = int(input("Enter 1 to play again, enter 2 to quit: "))
            if quitOrAgain == 1:
                print("You have choosen to play again")
            elif quitOrAgain == 2:
                print("You have choosen to quit")
                z = 1
            else:
                print("I don't understand what you are saying so I will just assume you said you wanted to play again")  

    elif oddOrEven == "odd":

        while y == odd:
            start = timer()
            odd = int(input(name+": "))
            y += 2
            end = timer()
            time = end - start
            print(time, "sec")
            average += time 
            times += 1
        if y != odd:
            print("")
            print("Wrong number. The next number was:", y)
            print("Your average speed between numbers are:", average/times, "sec")
            quitOrAgain = input("Enter 1 to play again, enter 2 to quit: ")
            if quitOrAgain == "1":
                print("You have choosen to play again") 
            elif quitOrAgain == "2":
                print("You have choosen to quit")
                z = 1
            else:
                print("I don't understand what you are saying so I will just assume you said you wanted to play again")

    else:
        print("You typed something wrong, try again")
    

End = input("Press enter to stop the program: ")
