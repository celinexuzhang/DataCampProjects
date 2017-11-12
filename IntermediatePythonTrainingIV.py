#Size
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#convern poplation from CSV file to a list
df = pd.read_csv("C:/Users/celzhang/Desktop/gapminder.csv")
life_exp = df.life_exp.tolist()
gdp_cap = df.gdp_cap.tolist()
pop = df.population.tolist()
#convert population list to array using numpy
np_pop = np.array(pop)
#np_life_exp = np.array(life_exp)
#np_gdp_cap = np.array(gdp_cap)
#print(np_pop)
#time each element in the array by 2 in population array
np_pop = (np_pop *2)/100000
#update: set s arguement in the plt.scatter() method to be np_pop
plt.scatter(gdp_cap ,life_exp, s=np_pop)
# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
#show the plot
plt.show()