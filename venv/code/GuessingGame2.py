import pandas as pd
import time
import random

all_data = []
total_guesses = 0  # total amount of guesses
correct_guesses = 0  # amount of correct guesses


def import_CSV(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"CSV file could not be imported correctly: {e}")
        return None


def get_Data(df):
    for _, row in df.iterrows():
        all_data.append([
            row['PitcherThrows'], row['Answer Here:'], row['SpinRate'], row['Tilt'],
            row['InducedVertBreak'], row['HorzBreak'], row['RelSpeed']
        ])
    random.shuffle(all_data)
    return all_data


def new_Pitch(i):
    print("---------------------------------------------")
    print(f"Pitch number: {total_guesses + 1}")
    print(f"Pitcher Throws: {i[0]}")
    print(f"Velocity: {round(i[6], 1)} mph")
    print(f"Induced Vertical Break: {round(i[4], 1)} inches")
    print(f"Horizontal Break: {round(i[5], 1)} inches")
    print(f"Spin Rate: {round(i[2], 0)}")
    print(f"Tilt: {i[3]}")
    print("")
    print("Only enter: 'Fastball', 'Curve', 'Slider', 'Sinker', 'Change', 'Cutter', 'Splitter' or 'q'")


def check_Guess(correct_Pitch, user_Guess):
    global total_guesses, correct_guesses
    total_guesses += 1

    if correct_Pitch.lower() == user_Guess.lower():
        correct_guesses += 1
        return True
    else:
        print(f"Wrong! It was {correct_Pitch}")
        return False


def end_Game():
    print("---------------------------------------------")
    print(f"You guessed a total of {total_guesses} times, {correct_guesses} were correct and {total_guesses - correct_guesses} were wrong.")
    print(f"You got {round((correct_guesses / total_guesses) * 100, 1)}% correct.")
    print("---------------------------------------------")


csv_file = import_CSV('Assignment3CSV.csv')

if csv_file is not None:
    all_data = get_Data(csv_file)

    for i in all_data:
        new_Pitch(i)
        user_guess = input("What do you think this pitch is? ")

        if user_guess == 'q':
            end_Game()
            break
        else:
            check_Guess(i[1], user_guess)
