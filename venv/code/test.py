import pandas as pd
import time
import random

# Read the CSV into a DataFrame
df = pd.read_csv("Assignment3CSV.csv")




# # Shuffle the DataFrame rows
# df = df.sample(frac=1).reset_index(drop=True)

# total_guesses = 0
# correct_guesses = 0

# for _, row in df.iterrows():
#     print("---------------------------------------------")
#     print(f"Pitch number : {total_guesses + 1}\n")

#     pitcher_throws = row['PitcherThrows']
#     answer_here = row['Answer Here:']
#     velocity = round(row['RelSpeed'], 1)
#     induced_vert_break = round(row['InducedVertBreak'], 1)
#     horz_break = round(row['HorzBreak'], 1)
#     spin_rate = round(row['SpinRate'], 0)
#     tilt = row['Tilt']

#     print(f"Pitcher Throws: {pitcher_throws}")
#     print(f"Velocity: {velocity} mph")
#     print(f"Induced Vertical Break: {induced_vert_break} inches")
#     print(f"Horizontal Break: {horz_break} inches")
#     print(f"Spin Rate: {spin_rate}")
#     print(f"Tilt: {tilt}\n")

#     user_guess = input("What do you think this pitch is? (Only enter: 'Fastball', 'Curve', 'Slider', 'Sinker', 'Change', 'Cutter', 'Splitter' or 'q'): ")

#     if user_guess == "q":
#         accuracy = round(correct_guesses / total_guesses * 100, 1) if total_guesses > 0 else 0
#         print(f"\n---------------------------------------------\n")
#         print(f"You guessed a total of {total_guesses} times, {correct_guesses} were correct and {total_guesses - correct_guesses} were wrong.")
#         print(f"You got {accuracy}% correct.\n")
#         print("---------------------------------------------")
#         break
#     else:
#         total_guesses += 1
#         if user_guess == answer_here:
#             print("Correct!")
#             correct_guesses += 1
#         else:
#             print(f"Wrong. It was a {answer_here}.")
#             input("When you are ready to move on, press enter once.")

#     time.sleep(1.5)
#     print("\n" * 10)
