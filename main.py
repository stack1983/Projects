import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# creae insurance dataframe from csv file
insurance_data = pd.read_csv('insurance.csv')

#find average age of insured
avg_age_of_insured = round(np.average(insurance_data['age']),0)

print('Average age of insured is: ' + str(avg_age_of_insured))

#find youngest and oldest person insured for range of data
min_age_insured = np.min(insurance_data['age'])
max_age_insured = np.max(insurance_data['age'])

#create bins for age group data
bins = [18, 30, 40, 50, 60, 70]
labels = ['Twenties', 'Thirties', 'Fourties', 'Fifties', 'Sixties']

#create AgeGroup column with category values in dataframe
insurance_data['AgeGroup'] = pd.cut(insurance_data['age'], bins=bins, labels=labels, right=False)
print(insurance_data.head())
#print details of insurance data
print(insurance_data.describe())

#creat histogram to display ages insured
plt.hist(insurance_data['age'], bins=bins)
plt.xlabel('Ages')
plt.ylabel('Number of Insured')
plt.title("Ages of Insured")
plt.show()




