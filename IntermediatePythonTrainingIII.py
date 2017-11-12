#Customization
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("C:/Users/celzhang/Desktop/gapminder.csv")
life_exp = df.life_exp.tolist()
gdp_cap = df.gdp_cap.tolist()
plt.scatter(life_exp,gdp_cap)
plt.xlabel('life expectancy[in years]')
plt.ylabel('GDP per Capita [in USD]')
plt.title('World Development in 2007')
#adding y ticks (optional step)
plt.yticks([10000,20000,30000,40000,50000],['10k', '20k','30k','40k','50k'])
plt.xscale('log')
plt.show()

#Add more data
life_exp = [45, 80, 67]+life_exp
gdp_cap = [30000, 21000, 15000]+gdp_cap

