# Import Pyhton Libraries
import xlwings as xw
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from poes.model.poes import poes
from poes.model.utils import param_stoiip
import seaborn as sns
from matplotlib import ticker

# State names of all variables
# Create names for sheets
SHEET_SUMMARY = "Summary"
SHEET_RESULTS = "Results"

# Assing names to the whole columns of dataframe
VARIABLES = "Variables"
DISTRIBUTIONS = "Distributions"
LOC = "Loc"
SCALE = "Scale"
SC = "Sc"
LIM_MIN = "Lim min"
LIM_MAX = "Lim max"

# Create index for POES parameters
A_IDX, H_IDX, PORO_IDX, SWI_IDX, BOI_IDX = 0, 1, 2, 3, 4

# Call cells from MS Excel
DET_VALUES = "det_values"
DF_POES = "df_poes"
REALIZATIONS = "Realizations"
SEED = "Seed"

# Create names for outputs
DET_POES = "poes"
STOC_POES = "stoc_poes"
STOC_ARRAY = "stoc_array"


# Create main function to connect controller with fron-end (MS Excel)
def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[SHEET_SUMMARY]

    # Calculate deterministic STOIIP
    params = sheet[DET_VALUES].options(np.array, transpose=True).value
    sheet[DET_POES].value = poes(*params)

    # Calculate STOCHASTIC STOIIP
    df_poes = sheet[DET_POES].options(pd.DataFrame, expand="table", index=False).value

    # Call realizations cell
    realizations = int(sheet[REALIZATIONS].value)

    # Call seed cell
    seed = int(sheet[SEED].value)

    # Define random values for STOIIP Parameters
    input_col_names = df_poes[VARIABLES].to_list()
    area_col, h_col, poro_col, swi_col, boi_col = tuple(input_col_names)
    input_idx = [A_IDX, H_IDX, PORO_IDX, SWI_IDX, BOI_IDX]
    input_dict = dict(zip(input_col_names, input_idx))
    results_dict = {}

    for col, idx in input_dict.items():
        results_dict[col] = param_stoiip(
            df_poes,
            idx,
            DISTRIBUTIONS,
            LOC,
            SCALE,
            realizations,
            SC,
            LIM_MIN,
            LIM_MAX,
            seed,
        )

    # Calculate Stochastic Stoiip into results_dict
    results_dict[STOC_POES] = poes(
        results_dict[area_col],
        results_dict[h_col],
        results_dict[poro_col],
        results_dict[swi_col],
        results_dict[boi_col],
    )

    # Calculate mean, std, P90, 950, P10 from STOIIP
    summary_stoc_results = [
        results_dict[STOC_POES].mean(),
        results_dict[STOC_POES].std(),
        np.percentile(results_dict[STOC_POES], 90),
        np.percentile(results_dict[STOC_POES], 50),
        np.percentile(results_dict[STOC_POES], 10),
    ]

    # Send stochastic values to MS Excel
    sheet[STOC_POES].options(transpose=True).value = summary_stoc_results

    # Call sheet results
    sheet_re = wb.sheets[SHEET_RESULTS]

    # Create dataframe from results_dict
    df_results = pd.DataFrame(results_dict)

    # Send df_results to Results sheet in MS Excel
    sheet_re[STOC_ARRAY].options(
        pd.DataFrame, expand="table", index=False
    ).value = df_results

    # Create Histogram from stochastic STOIIP
    eng_formatter = ticker.EngFormatter()
    sns.set_style("white")
    fig = plt.figure(figsize=(8, 6))

    ax = sns.histplot(df_results[STOC_POES], color="lightgray", kde=True)

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
    plt.xlabel("STOIIP")
    plt.suptitle("Stochastic STOIIP")
    plt.legend(loc=0)

    # Send histogram to MS Excel
    sheet.pictures.add(fig, name="Histogram", update=True, left=sheet.range("J2").left)


if __name__ == "__main__":
    xw.Book("poes.xlsm").set_mock_caller()
    main()
