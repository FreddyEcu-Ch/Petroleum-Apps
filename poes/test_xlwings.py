import xlwings as xw
import numpy as np
import pandas as pd

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

#%% Call a numpy array from MS Excel to Python
values = sheet["G6:K6"].value
print(values)

#%% Create a DataFrame from Python to MS Excel
sheet["D13"].options(pd.DataFrame, expand="table", index=False).value = pd.DataFrame(
    {
        "Oilfield": np.array(["Auca", "Sacha", "Sushufindi"]),
        "Wells": np.array(["Auc-001", "Sa-006", "Shu-009"]),
        "Oil_production (bpd)": np.array([300, 1000, 1500]),
    }
)

#%% Call a DataFrame form MS Excel to Python
df = sheet["D13"].options(pd.DataFrame, expand="table", index=False).value
