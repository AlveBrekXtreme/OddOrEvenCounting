from timeit import default_timer as timer #imports a timer



print("This program is a game where you will only count odd numbers or even numbers starting with 1 or 2 depending on what you choose.") #Introduction
print("") #spacing for the user 
z = 0 #doesn't really matter what this is named
highscoreX = 0
highscoreY = 0 
scoreX = 0
scoreY = 0
name = input("Type your name/username/nickname/something, here: ") #the user can type in what they want to be called here
while z == 0: #it will remain 0 unless the user choose to quit, meaning the user can play this as long as they want
    #these are placed whithin the while loop so they reset after a round 
    rounds = 0 
    quitOrAgain = 0 
    times = 0
    average = 0
    countingEven = 0
    countingOdd = -1
    x = 0 
    y = -1 

    oddOrEven = input("Choose between odd or even numbers. (odd/even): ") #the user chooses between odd or even numbers here
    if oddOrEven == "even": #the code below runs if the user typed "even"

        while x == countingEven: #this will loop as long as the user input is the same as "x" which is always two more then the previous round
            start = timer()
            countingEven = int(input(name+": ")) #here the user can input a number 
            end = timer()
            time = end - start #calculates the time it takes between user inputs
            time = round(time, 2) #makes it so this number only has 2 decimals
            print(time, "seconds")
            times += time 
            rounds += 1 #this counts how many rounds has been played
            x += 2
        if x != countingEven: #lets the person know if they typed something wrong, this will also stop the loop because x is not equal to the number the user typed
            print("")
            print("Wrong number. The next number was:", x) 
            average = round(times/rounds, 2) #makes it so this number only has 2 decimals
            print("Your average speed between numbers are:", average, "seconds") 
            scoreX = x - 2 
            if highscoreX < scoreX:
                highscoreX = scoreX 
                print("Your new highscore for even numbers is:", highscoreX)
            else:
                print("Your highscore for even numbers is:", highscoreX)
            quitOrAgain = input("Enter 1 to play again, enter 2 to quit: ") #lets the user choose if they want to play another round or quit
            if quitOrAgain == "1":
                print("You have choosen to play again") 
            elif quitOrAgain == "2":
                print("You have choosen to quit")
                break
            else:
                print("I don't understand what you are saying so I will just assume you said you wanted to play again")
        
        

    elif oddOrEven == "odd": #the code below runs if the user typed "even"

        while y == countingOdd: #this loop does nearly the same as the while loop above, only differences is that it's for counting odd numbers and it has a diffrent variables than the other loop
            start = timer()
            countingOdd = int(input(name+": "))
            y += 2
            print("y",y)
            end = timer()
            time = end - start
            time = round(time, 2) 
            print(time, "seconds")
            times += time 
            rounds += 1
        if y != countingOdd:
            print("")
            print("Wrong number. The next number was:", y)
            average = round(times/rounds, 2)
            print("Your average speed between numbers are:", average, "seconds")
            scoreX = y - 2
            if highscoreX < scoreY:
                highscoreX = scoreY 
                print("Your new highscore for even numbers is:", highscoreY)
            else:
                print("Your highscore for even numbers is:", highscoreY)
        quitOrAgain = input("Enter 1 to play again, enter 2 to quit: ") #lets the user choose if they want to play another round or quit
        if quitOrAgain == "1":
            print("You have choosen to play again") 
        elif quitOrAgain == "2":
            print("You have choosen to quit")
            break
        else:
            print("I don't understand what you are saying so I will just assume you said you wanted to play again")

    else: #if the user typed neither odd, nor even, a message gets sent to the screen and the user can try again
        print("You typed something wrong, try again")
    

End = input("Press enter to stop the program: ")
