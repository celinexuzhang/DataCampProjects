#first install matplotlib from Windows Commmend line "pip install matplotlib"
import matplotlib.pylab as plt
#read Excel file, first sheet
import xlrd
file_location = "C:/Users/celzhang/Desktop/Analytics/Python/IntermediatetoPython/DataSets/brics.xlsx"
workbook = xlrd.open_workbook(file_location)
brics_sheet = workbook.sheet_by_index(0)
#show a correlation between area and population
#first get list of area
area_list = brics_sheet.col_values(3)
#next get the population of that area
pop_list = brics_sheet.col_values(4)
NewAreaList = area_list[1:]
NewPopList = pop_list[1:]
#Plot the lists in a scatter plot
plt.scatter(NewPopList,NewAreaList)
plt.show()
#plot the lists in a line chart
plt.plot(NewPopList,NewAreaList)
plt.show()
#Put the x-axis on a Linear scale.
plt.xscale('linear')
plt.show()
#historgam
help(plt.hist)
plt.hist(NewPopList,bins = 5)
plt.show()