#first install matplotlib from Windows Commmend line "pip install matplotlib"
import matplotlib.pylab as plt
import xlrd
file_location = "C:/Users/celzhang/Desktop/Analytics/Python/IntermediatetoPython/DataSets/brics.xlsx"
workbook = xlrd.open_workbook(file_location)
brics_sheet = workbook.sheet_by_index(0)
#show a correlation between area and population
#first get list of area
area_list = brics_sheet.col_values(3,1)
#next get the population of that area
pop_list = brics_sheet.col_values(4,1)
#Plot the lists in a scatter plot
plt.scatter(area_list, pop_list)
plt.show()
