#first install matplotlib from Windows Commmend line "pip install matplotlib"
import matplotlib.pylab as plt
import xlrd
file_location = "C:/Users/celzhang/Desktop/Analytics/Python/IntermediatetoPython/DataSets/brics.xlsx"
workbook = xlrd.open_workbook(file_location)
brics = workbook.sheet_by_index(0)
#understanding the second column heading
brics.cell_value(0,1)
