from timeit import default_timer as timer #imports a timer
underscores = "|________________________________________________________"
print("___________________________________________________________________________________________________________________________________")
print("| \n|  This program is a game where you will only count odd numbers or even numbers starting with 1 or 2 depending on what you choose.") #Introduction
highscores_and_avg_speed = {} 
num_of_deci = 2
num_counted = 0
time_limit = 99 
highscore = 0
name = input("|  Type your name/username/nickname/something, here: ") #the user can type in what they want to be called here
while 0 == 0: #it will remain 0 unless the user choose to quit
    #these variables resets after a iteration 
    counting_user = 0
    counter = 0 
    average = 0
    rounds = 0 
    times = 0
    score = 0
    time = 0
    print(f"{underscores}\n|\n|  1. Odd numbers. Start with counting the number 1")
    print("|  2. Even numbers. Start with counting the number 2")
    print("|  3. Statistics. See stats that are not shown after a round.")
    choice = input(f"|  Type one of these numbers(1/2/3): ") #the user makes a choice in the menu. 
    if choice == "1": #the code below runs if the user typed "1" 
        counting_user -= 1 #because counter now is -1 at the, countingUser also has to start at -1 so the while condition is true
        counter -= 1 #because it's odd numbers, the counter must be set to -1 so it becomes 1 instead of two first
        print(f"{underscores}\n|")
        while counter == counting_user and time < time_limit: #will loop as long as the user input is the same as "x" which is always two more then the previous round
          start = timer()
          try: #checks if the variable is an integer
            counting_user = int(input(f"|  {name}: ")) #here the user can input a number 
          except: #if the variable isn't an integer, this message will be printed to the scree
           print("|  You must type a number")
          else: #this will happend if the variable is an integer:
           counter += 2
           end = timer()
           time = end - start #calculates the time it takes between user inputs
           time = round(time, num_of_deci) #makes it so this number only has x number of decimals
           print(f"|  {time} seconds")
           times += time 
           rounds += 1 #this counts how many rounds has been played
           num_counted += 1 
    elif choice == "2": #the code below runs if the user typed "2" and does nearly the same as the "if" above
        print(f"{underscores}\n|")
        while counter == counting_user and time < time_limit: #will loop as long as the user input is the same as "x" which is always two more then the previous round
          start = timer()
          try: 
           counting_user = int(input(f"|  {name}: ")) 
          except: 
           print("|  You must type in a number") 
          else: 
           end = timer() 
           time = end - start 
           time = round(time, num_of_deci) 
           print(f"|  {time} seconds")
           times += time 
           rounds += 1 
           counter += 2     
           num_counted += 1   
    elif choice == "3":
        print(f"{underscores}\n|\n|")
        print(f"|  Total numbers counted: {num_counted} numbers\n|") 
        print(f"|  Total rounds played: {len(highscores_and_avg_speed)} rounds\n|") 
        print("|  Top 5 highest scores:\n|")
        highscores_and_avg_speed = dict(sorted(highscores_and_avg_speed.items())) #sorts the items by the value of the key
        sorted_keys = list(highscores_and_avg_speed.keys()) #puts all the dictionary keys in a list
        sorted_values = list(highscores_and_avg_speed.values()) #puts all the dictionary values in a list
        spot = 0 #spot is used to numerate which position the numbers is in
        for i in range(len(sorted_keys), 0, -1): #loops backwards with the lenght of the list 
          spot += 1 
          print(f"|  {spot}. Score of {sorted_keys[i-1]} with an average speed of {sorted_values[i-1]} seconds per number") 
          if spot == 5:
           break
        if len(sorted_keys) < 5: #if the length is less then the values in sorted_keys:
          for x in range(5-len(sorted_keys), 0, -1): #this loop makes sure it still numerates empty spots
           spot += 1
           print(f"|  {spot}.")
        print(f"|\n|  Total numbers counted: {num_counted} numbers\n|") 
        input("|\n  Press enter to exit statistics: ")  
        print("|")
    else:
        print("| \n|  You must type either 1, 2 or 3")
    if choice == "1" or choice == "2": 
        if time > time_limit: #Checks if the user ran out of time or counted the wrong number
          print(f"{underscores}\n|\n| You ran out of time, the time limit is set to {time_limit} seconds.")
        else:
          print(f"{underscores}\n|\n|  Wrong number. The next number was: {counter}") 
        num_counted -= 1
        average = round(times/rounds, 2) #makes it so this number only has 2 decimals
        score = counter - 2 #the score is what number you got too
        highscores_and_avg_speed[score] = average #adds the score and average speed to the dictionary
        if highscore < score:
          highscore = score #if the score is higher then the highscore, the score will be set as the new highscore
          print(f"|  Your new highscore is: {highscore}")#
        else:
          print(f"|  Your highscore is: {highscore}")#lets the user see what the current highscore is if they didn't get a new highscore 
        print(f"|  Your average speed per number is: {average} seconds\n{underscores}")   
        quit_or_again = input("| \n|  Enter 1 to play again, enter 2 to quit: ") 
        if quit_or_again == "1":
         print("|  You have choosen to play again") 
        elif quit_or_again == "2":
          print(f"|  You have choosen to quit\n{underscores}")
          break #breaks out of the loop
        else:
          print("|  I don't understand what you are saying so I will just assume you said you wanted to play again")  
