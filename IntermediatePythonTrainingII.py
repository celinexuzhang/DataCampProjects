#Histogram
import matplotlib.pyplot as plt
help(plt.hist)
import pandas as pd
#Example
#Dataset
values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values, bins=3)
plt.show()

#read CSV file
#You can define the column name if you don't have column name in the file. This step is optional
columns = ['rank','country','year','population','cont','life_exp','gdp_cap']
#read in csv file in pandas
df = pd.read_csv("C:/Users/celzhang/Desktop/gapminder.csv")
#read column to a list in pandas (This is magic)
life_exp = df.life_exp.tolist()
print(life_exp)
#put the list into histogrom
plt.hist(life_exp,bins=3)
plt.show()






