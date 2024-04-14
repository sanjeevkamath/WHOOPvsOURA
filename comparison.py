import pandas as pd
import matplotlib.pyplot as plt


# Step 1 - Load Data from CSV
oura_data = pd.read_csv('oura_sleep.csv')
whoop_data = pd.read_csv('whoop_sleep.csv')

# Step 2 - Data Cleaning
oura_data = oura_data[oura_data['type'] == 'long_sleep']
print(oura_data['day'])
whoop_data = whoop_data[whoop_data['Nap'] == False]
print(whoop_data['Cycle end time'])


