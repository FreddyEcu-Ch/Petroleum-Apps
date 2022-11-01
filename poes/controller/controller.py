# Import Pyhton Libraries
import xlwings as xw
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from poes.model.poes import poes

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


if __name__ == "__main__":
    xw.Book("poes.xlsm").set_mock_caller()
    main()
