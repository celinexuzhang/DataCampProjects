#Size
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#convern poplation from CSV file to a list
df = pd.read_csv("C:/Users/celzhang/Desktop/gapminder.csv")
life_exp = df.life_exp.tolist()
gdp_cap = df.gdp_cap.tolist()
pop = df.population.tolist()
continent = df.cont.tolist()
#convert population list to array using numpy
np_pop = np.array(pop)
#print(np_pop)
#time each element in the array by 2 in population array
np_pop = (np_pop *2)/100000
#update: set s arguement in the plt.scatter() method to be np_pop
#update: define c (color)
# step 1: define color using dictionary dict(), first define color based on continent
my_dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}
#step 2: map the color to each continent, using dictionaries
col_map =[my_dict[i] for i in continent]
#update: define alpha (Alpha can be set from zero to one, where zero is totally transparent, and one is not at all transparent.)
plt.scatter(gdp_cap, life_exp, c=col_map,alpha= 0.8, s= np_pop)
# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
#show the plot
plt.show()