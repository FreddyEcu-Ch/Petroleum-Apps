#%%
import xlwings as xw
import pandas as pd
import numpy as np
from poes.model.utils import param_stoiip
from poes.model.poes import poes

#%% Call workbook
xb = xw.Book("poes/controller/poes.xlsm")
sheet = xb.sheets["Summary"]

#%% Call Dataframe
df_poes = sheet["A2"].options(pd.DataFrame, expand="table", index=False).value
df_poes["Distributions"] = np.array(
    ["Triangular", "Normal", "Lognormal", "Normal", "Exponential"]
)
df_poes["Loc"] = np.array([400, 30, 0, 0.4, 1])
df_poes["Scale"] = np.array([600, 90, 0.2, 0.2, 0.2])
df_poes["Sc"] = np.array([0.3, 0, 0.8, None, None])
df_poes["Lim min"] = np.array([50, 10, 0, 0, 1])
df_poes["Lim max"] = np.array([180, 80, 1, 1, 2])

#%% Test param_stoiip function
area_stoc = param_stoiip(
    df_poes, 0, "Distributions", "Loc", "Scale", 1000, "Sc", "Lim min", "Lim max"
)
thickess_stoc = param_stoiip(
    df_poes, 1, "Distributions", "Loc", "Scale", 1000, "Sc", "Lim min", "Lim max"
)
swi_stoc = param_stoiip(
    df_poes, 3, "Distributions", "Loc", "Scale", 1000, "Sc", "Lim min", "Lim max"
)
boi_stoc = param_stoiip(
    df_poes, 4, "Distributions", "Loc", "Scale", 1000, "Sc", "Lim min", "Lim max"
)
poro_stoc = param_stoiip(
    df_poes, 2, "Distributions", "Loc", "Scale", 1000, "Sc", "Lim min", "Lim max"
)
