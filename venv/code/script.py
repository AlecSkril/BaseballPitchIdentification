import pandas as pd
 
# reading CSV file
data = pd.read_csv("venv/code/Assignment3CSV.csv")
 
# converting column data to list
balls = data['Balls'].tolist()
#pitcherThrow = data['Pitcher Throw'].tolist()

 
# printing list data
#print('Balls:', balls)
#print('Pitcher Throw:', pitcherThrow)



pitcherThrows_column = pd.read_csv('venv/code/Assignment3CSV.csv', usecols=['PitcherThrows'])['PitcherThrows']
pitchGuess_column = pd.read_csv('venv/code/Assignment3CSV.csv', usecols=['Answer Here:'])['Answer Here:']
#print(pitcherThrows_column)
print(pitchGuess_column)
