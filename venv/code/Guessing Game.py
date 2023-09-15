import pandas as pd
import time
import random

# Read the CSV into a DataFrame
df = pd.read_csv("venv/code/Assignment3CSV.csv")

# Create an empty list to hold the lists of pairs
all_data = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    pitcher_throws = row['PitcherThrows']
    answer_here = row['Answer Here:']
    spin_rate = row['SpinRate']
    tilt = row['Tilt']
    induced_vert_break = row['InducedVertBreak']
    horz_break = row['HorzBreak']
    velocity = row['RelSpeed']


    # Create a list with these two elements and append to all_data
    all_data.append([pitcher_throws, answer_here, spin_rate, tilt, induced_vert_break, horz_break, velocity])

random.shuffle(all_data)

total_guesses = 0
correct_guesses = 0

for i in all_data:
    print("---------------------------------------------")
    print("Pitch number : " + str(total_guesses + 1))
    print("")

    print("Pitcher Throws: " + i[0])
    print("Velocity: " + str(round(i[6], 1)) + " mph")
    print("Induced Vertical Break: " + str(round(i[4], 1)) + " inches")
    print("Horizontal Break: " + str(round(i[5], 1)) + " inches")
    print("Spin Rate: " + str(round(i[2], 0)))
    print("Tilt: " + str(i[3]))

    print("")
    #print(i) # Just for developement so I can see what pitch it is

    print("")
    print("Only enter: 'Fastball', 'Curve', 'Slider', 'Sinker', 'Change', 'Cutter', 'Splitter' or 'q'")
    user_guess = input("What do you think this pitch is? ")


    if user_guess == "q":
        print("")
        print("---------------------------------------------")
        print("")
        print("You guessed a total of " + str(total_guesses) + " times, " + str(correct_guesses) + " were correct and " + str(total_guesses - correct_guesses) + " were wrong.")
        print("You got " + str(round(correct_guesses/total_guesses*100,1)) + "% correct.")
        print("")
        print("---------------------------------------------")
        break
    else:
        total_guesses += 1
        if user_guess == i[1]:
           print("Correct!")
           correct_guesses += 1

        else:
            print("Wrong. It was a " + str(i[1]) + ".")
            temp = print(input("When you are ready to move on, press enter once."))

        time.sleep(1.5) # Pause for 1.5 seconds
        for _ in range(10):
           print("")



