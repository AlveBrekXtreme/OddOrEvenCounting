from timeit import default_timer as timer 
underscores = "|________________________________________________________"
print("___________________________________________________________________________________________________________________________________")
print("| \n|  This program is a game where you will only count odd numbers or even numbers starting with 1 or 2 depending on what you choose.") #Introduction
highscores_and_avg_speed = {} 
num_of_decimals = 2
num_counted = 0
time_limit = 99 
highscore = 0
name = input("|  Type your username here: ") 

def number_numeric_test(inputs, text):
    inputs = input(f"|  {text}: ") 
    while not inputs.isnumeric(): 
        print("|  You must type in a number")
        inputs = input(f"|  {text}: ")
    inputs = int(inputs)
    return inputs

while 0 == 0: 
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
    print("|  4. Settings")
    choice = input(f"|  Type one of these numbers(1/2/3/4): ") 

    if choice == "1": 
      counting_user -= 1 
      counter -= 1 
    if choice == "1" or choice == "2": 
      print(f"{underscores}\n|")
      while counter == counting_user and time < time_limit: 
        start_num_count = timer()
        counting_user = number_numeric_test(counting_user, name) 
        end_num_counted = timer() 
        time = end_num_counted - start_num_count 
        time = round(time, num_of_decimals) 
        print(f"|  {time} seconds")
        times += time 
        rounds += 1 
        counter += 2   
        num_counted += 1  

      else: 
        if time > time_limit: 
          print(f"{underscores}\n|\n|  You ran out of time, the time limit is set to {time_limit} seconds.")
        else:
          print(f"{underscores}\n|\n|  Wrong number. The next number was: {counter}") 
        num_counted -= 1
        average = round(times/rounds, 2) 
        score = counter - 2 
        highscores_and_avg_speed[score] = average 
        if highscore < score:
          highscore = score 
          print(f"|  Your new highscore is: {highscore}")
        else:
          print(f"|  Your highscore is: {highscore}")
        print(f"|  Your average speed per number is: {average} seconds\n{underscores}")  
        quit_or_again = input("| \n|  Enter 1 to play again, enter 2 to quit: ")
        if quit_or_again == "1":
          print("|  You have choosen to play again")
        elif quit_or_again == "2":
          print(f"|  You have choosen to quit\n{underscores}")
          break
        else:
          print("|  I don't understand what you are saying so I will just assume you said you wanted to play again") 

    elif choice == "3":
      print(f"{underscores}\n|\n|")
      print(f"|  Total numbers counted: {num_counted} numbers") 
      print(f"|  Total rounds played: {len(highscores_and_avg_speed)} rounds\n|") 
      print("|  Top 5 highest scores:\n|")
      highscores_and_avg_speed = dict(sorted(highscores_and_avg_speed.items())) 
      sorted_keys = list(highscores_and_avg_speed.keys()) 
      sorted_values = list(highscores_and_avg_speed.values()) 
      spot = 0 #
      for i in range(len(sorted_keys), 0, -1): 
        spot += 1 
        print(f"|  {spot}. Score of {sorted_keys[i-1]} with an average speed of {sorted_values[i-1]} seconds per number")
        if spot == 5:
         break
      if len(sorted_keys) < 5: 
        for x in range(5-len(sorted_keys), 0, -1): 
         spot += 1
         print(f"|  {spot}.")
      input("|\n|  Press enter to exit statistics: ")  
      print("|")

    elif choice == "4":

      print(f"{underscores}\n|\n|")
      print(f"|  Your current number of decimals is {num_of_decimals}")
      num_of_decimals = str(num_of_decimals)
      change_num_of_decimals = "Change numbers of decimals here"
      num_of_decimals = number_numeric_test(num_of_decimals, change_num_of_decimals)
      
      print(f"\n|  Your current timelimit is {time_limit}")
      time_limit = str(time_limit)
      change_time_limit = "Change the time limit here"
      time_limit = number_numeric_test(time_limit, change_time_limit)

      input("|\n|  Press enter to exit settings: ")  
      print("|")

    else:
        print("| \n|  You must type either 1, 2 or 3")
