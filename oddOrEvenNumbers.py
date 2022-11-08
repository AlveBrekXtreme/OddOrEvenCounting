from timeit import default_timer as timer #imports a timer

print("This program is a game where you will only count odd numbers or even numbers starting with 1 or 2 depending on what you choose.") #Introduction
highscoreX = 0
highscoreY = 0 
scoreX = 0
scoreY = 0
name = input("Type your name/username/nickname/something, here: ") #the user can type in what they want to be called here
while 0 == 0: #it will remain 0 unless the user choose to quit, meaning the user can play this as long as they want
    #these are placed whithin the while loop so they reset after a round 
    rounds = 0 
    quitOrAgain = 0 
    times = 0
    average = 0
    countingEven = 0
    countingOdd = -1
    even = 0 
    odd = -1 
    oddOrEven = input("\nChoose between odd or even numbers. (odd/even): ") #the user chooses between odd or even numbers here
    if oddOrEven == "even": #the code below runs if the user typed "even"
        while even == countingEven: #this will loop as long as the user input is the same as "x" which is always two more then the previous round
            start = timer()
            try: #checks if the variable is an integer
                countingEven = int(input(name+": ")) #here the user can input a number 
            except: #if the variable isn't an integer, this message will be printed to the screen
                print("You must type in a number") 
            else: #this will happend if the variable is an integer:
                end = timer() 
                time = end - start #calculates the time it takes between user inputs
                time = round(time, 2) #makes it so this number only has 2 decimals
                print(time, "seconds")
                times += time 
                rounds += 1 #this counts how many rounds has been played
                even += 2 
        if even != countingEven: #lets the person know if they typed something wrong, this will also stop the loop because x is not equal to the number the user typed
            print("\nWrong number. The next number was:", even) 
            average = round(times/rounds, 2) #makes it so this number only has 2 decimals
            print("Your average speed between numbers are:", average, "seconds") 
            scoreX = even - 2 #the score is what number you got too
            if highscoreX < scoreX: #if the score is higher then the highscore, the score will be set as the new highscore
                highscoreX = scoreX 
                print("Your new highscore for even numbers is:", highscoreX, "\n")
            else:
                print("Your highscore for even numbers is:", highscoreX, "\n") #lets the user see what the current highscore is if they didn't get a new highscore
            quitOrAgain = input("Enter 1 to play again, enter 2 to quit: ") #lets the user choose if they want to play another round or quit
            if quitOrAgain == "1":
                print("You have choosen to play again") 
            elif quitOrAgain == "2":
                print("You have choosen to quit")
                break #breaks out of the loop
            else:
                print("I don't understand what you are saying so I will just assume you said you wanted to play again")           
    elif oddOrEven == "odd": #the code below runs if the user typed "odd"
        while odd == countingOdd: #this loop does nearly the same as the while loop above, only differences is that it's for counting odd numbers and it uses some diffrent variables than the other loop
            start = timer()
            try:
                countingOdd = int(input(name+": "))
            except:
                print("You must type a number")
            else:
                odd += 2
                end = timer()
                time = end - start
                time = round(time, 2) 
                print(time, "seconds")
                times += time 
                rounds += 1
        if odd != countingOdd:
            print("\nWrong number. The next number was:", odd)
            average = round(times/rounds, 2)
            print("Your average speed between numbers are:", average, "seconds")
            scoreY = odd - 2
            if highscoreY < scoreY:
                highscoreY = scoreY 
                print("Your new highscore for odd numbers is:", highscoreY, "\n")
            else:
                print("Your highscore for odd numbers is:", highscoreY, "\n")
        quitOrAgain = input("Enter 1 to play again, enter 2 to quit: ") 
        if quitOrAgain == "1":
            print("You have choosen to play again") 
        elif quitOrAgain == "2":
            print("You have choosen to quit")
            break
        else:
            print("I don't understand what you are saying so I will just assume you said you wanted to play again")
    else: #if the user typed neither odd, nor even, a message gets sent to the screen and the user can try again
        print("You typed something wrong, try again")
