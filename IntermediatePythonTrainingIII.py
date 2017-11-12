#Customization
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv("C:/Users/celzhang/Desktop/gapminder.csv")
life_exp = df.life_exp.tolist()
gdp_cap = df.gdp_cap.tolist()
plt.scatter(gdp_cap,life_exp)
plt.ylabel('life expectancy[in years]')
plt.xlabel('GDP per Capita [in USD]')
plt.title('World Development in 2007')
#adding x ticks (optional 1)
tick_value = [1000, 10000,100000]
tick_lab = ['1k','10k','100k']
plt.xticks(tick_value,tick_lab)
#or you can adding/changing x ticks like this ( option 2)
#plt.xticks([10000,20000,30000,40000,50000],['10k', '20k','30k','40k','50k'])
#plt.xscale('log')
plt.show()
#Add more data
life_exp = [45, 80, 67]+life_exp
gdp_cap = [30000, 21000, 15000]+gdp_cap
plt.clf()
