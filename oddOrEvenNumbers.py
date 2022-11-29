from timeit import default_timer as timer #imports a timer
underscores = "|________________________________________________________"#218
print("___________________________________________________________________________________________________________________________________")
print("| \n|  This program is a game where you will only count odd numbers or even \
numbers starting with 1 or 2 depending on what you choose.") #Introduction
highscore = 0
#the user can type in what they want to be called here
name = input("|  Type your name/username/nickname/something, here: ") 
while 0 == 0: #it will remain 0 unless the user choose to quit
    #these variables resets after a iteration 
    counting_user = 0
    counter = 0 
    average = 0
    rounds = 0 
    times = 0
    score = 0
    print(f"{underscores}\n|  \n|  1. Odd numbers. Start with the number 1")
    print("|  2. Even numbers. Starts with the number 2")
    #the user chooses between odd or even numbers 
    odd_or_even = input("|  Choose between odd or even numbers. (1/2): ") 
    if odd_or_even == "2": #the code below runs if the user typed "2"
        print(f"{underscores} \n|")
        while counter == counting_user: #this will loop as long as the user input is the same as "x" which is always two more then the previous round
            start = timer()
            try: #checks if the variable is an integer
                counting_user = int(input(f"|  {name}: ")) #here the user can input a number 
            except: #if the variable isn't an integer, this message will be printed to the screen
                print("|  You must type in a number") 
            else: #this will happend if the variable is an integer:
                end = timer() 
                time = end - start #calculates the time it takes between user inputs
                time = round(time, 2) #makes it so this number only has 2 decimals
                print(f"|  {time} seconds")
                times += time 
                rounds += 1 #this counts how many rounds has been played
                counter += 2       
    elif odd_or_even == "1": #the code below runs if the user typed "1" and does nearly the same as the "if" above
        counting_user -= 1 #because counter now is -1 at the, countingUser also has to start at -1 so the while condition is true
        counter -= 1 #because it's odd numbers, the counter must be set to -1 so it becomes 1 instead of two first
        print(f"{underscores} \n|")
        while counter == counting_user: 
            start = timer()
            try:
                counting_user = int(input(f"|  {name}: "))
            except:
                print("|  You must type a number")
            else:
                counter += 2
                end = timer()
                time = end - start
                time = round(time, 2) 
                print(f"|  {time} seconds")
                times += time 
                rounds += 1
    else:
        print("| \n|  You must type either the number 1 or 2")
    if odd_or_even == "1" or odd_or_even == "2": #if a round has passed, the user will be given a choice to play agian or quit.
        print(f"{underscores}\n\
| \n|  Wrong number. The next number was: {counter}") 
        average = round(times/rounds, 2) #makes it so this number only has 2 decimals
        print(f"|  Your average speed between numbers are: {average} seconds") 
        score = counter - 2 #the score is what number you got too
        if highscore < score:
            highscore = score #if the score is higher then the highscore, the score will be set as the new highscore
            print(f"|  Your new highscore is: {highscore} \n{underscores}")#
        else:
            print(f"|  Your highscore is: {highscore}\n{underscores}")#lets the user see what the current highscore is if they didn't get a new highscore   
        quit_or_again = input("| \n|  Enter 1 to play again, enter 2 to quit: ") 
        if quit_or_again == "1":
           print("|  You have choosen to play again") 
        elif quit_or_again == "2":
            print("|  You have choosen to quit")
            break #breaks out of the loop
        else:
            print("|  I don't understand what you are saying so I will just assume you said you wanted to play again")   
