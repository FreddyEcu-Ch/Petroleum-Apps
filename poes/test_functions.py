#%%
import xlwings as xw
import pandas as pd
import numpy as np
from poes.model.utils import param_stoiip
from poes.model.poes import poes
import matplotlib.pyplot as plt
from matplotlib import ticker
import seaborn as sns

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

#%%
# Define random values for STOIIP Parameters
input_col_names = df_poes["Variables"].to_list()
area_col, h_col, poro_col, swi_col, boi_col = tuple(input_col_names)
input_idx = [0, 1, 2, 3, 4]
input_dict = dict(zip(input_col_names, input_idx))
results_dict = {}

#%%
for col, idx in input_dict.items():
    results_dict[col] = param_stoiip(
        df_poes, idx, "Distributions", "Loc", "Scale", 1000, "Sc", "Lim min", "Lim max"
    )

#%%
# Calculate Stochastic Stoiip into results_dict
results_dict["stoc_poes"] = poes(
    results_dict[area_col],
    results_dict[h_col],
    results_dict[poro_col],
    results_dict[swi_col],
    results_dict[boi_col],
)

#%%
# Calculte mean, std, P90, 950, P10 from STOIIP
summary_stoc_results = [
    results_dict["stoc_poes"].mean(),
    results_dict["stoc_poes"].std(),
    np.percentile(results_dict["stoc_poes"], 90),
    np.percentile(results_dict["stoc_poes"], 50),
    np.percentile(results_dict["stoc_poes"], 10),
]

#%%
# Send stochastic values to MS Excel
sheet["H11"].options(transpose=True).value = summary_stoc_results

#%%
# Call sheet results
sheet_re = xb.sheets["Results"]

# Create dataframe from results_dict
df_results = pd.DataFrame(results_dict)

#%%
# Send df_results to Results sheet in MS Excel
sheet_re["A1"].options(pd.DataFrame, expand="table", index=False).value = df_results

#%%
# Create Histogram from stochastic STOIIP
eng_formatter = ticker.EngFormatter()
sns.set_style("white")
fig = plt.figure(figsize=(8, 6))

ax = sns.histplot(df_results["stoc_poes"], color="lightgray", kde=True)

plt.axvline(
    summary_stoc_results[2],
    ymax=0.85,
    color="darkorange",
    linewidth=1.5,
    linestyle="--",
    label="P90",
)

plt.axvline(
    summary_stoc_results[3],
    ymax=0.85,
    color="gold",
    linewidth=1.5,
    linestyle="--",
    label="P50",
)

plt.axvline(
    summary_stoc_results[4],
    ymax=0.85,
    color="green",
    linewidth=1.5,
    linestyle="--",
    label="P10",
)

ax.xaxis.set_major_formatter(eng_formatter)
plt.xlabel("STOIIP (STB)")
plt.suptitle("Stochastic STOIIP")
plt.legend(loc=0)
plt.show()

#%%
# Send histogram to MS Excel
sheet.pictures.add(fig, name="Histogram", update=True, left=sheet.range("J2").left)