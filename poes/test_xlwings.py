import xlwings as xw
import numpy as np

#%% Create a workbook
wb = xw.Book()
#%%
sheet = wb.sheets[0]

#%% Create a value from Python to MS Excel
sheet["C5"].value = "Barcelona"

#%% Call values from MS Excel to Python
values = sheet["E6:E9"].value
print(values)

#%% Create a numpy array from Python
sheet["G6"].options(np.array, transpose=True).value = np.array([1, 2, 3, 4, 5])
