# Import Python Libraries
from scipy.stats import norm, lognorm, expon, triang, uniform
import numpy as np


def param_stoiip(
    df,
    row,
    dist_col,
    loc_col,
    scale_col,
    reali,
    sc_col=None,
    lim_min_col=None,
    lim_max_col=None,
    seed=None,
):
    """
    This function has a goal, return a numpy arrays of any stoiip variable like area,
    thickness, porosity, oil saturation, and Boi. Furthermore, this numpy array contains
    random variables from various continuous distributions.
    Parameters
    ----------
    df
        Pandas DataFrame
    row
        row index
    dist_col
        Stochastic distribution
    loc_col
        loc argument from scipy
    scale_col
        scale argument from scipy
    reali
        Number of random values
    sc_col
        c or s argument from scipy
    lim_min_col
        Minimum limit column
    lim_max_col
        Maximum limit column
    seed
        Specifies the seed number to create random number generator

    Returns
    -------
    Numpy arrays of any stoiip parameter

    """

    if seed is None:
        rng = np.random.default_rng()
    else:
        rng = np.random.default_rng(seed)

    if df.loc[row, dist_col] == "Lognormal" or df.loc[row, dist_col] == "Triangular":
        if df.loc[row, dist_col] == "Lognormal":
            param = lognorm.rvs(
                s=df.loc[row, sc_col],
                loc=df.loc[row, loc_col],
                scale=df.loc[row, scale_col],
                size=reali,
                random_state=rng,
            )
            param = np.where(
                param < df.loc[row, lim_min_col], df.loc[row, lim_min_col], param
            )
            param = np.where(
                param > df.loc[row, lim_max_col], df.loc[row, lim_max_col], param
            )

        elif df.loc[row, dist_col] == "Triangular":
            param = triang.rvs(
                c=df.loc[row, sc_col],
                loc=df.loc[row, loc_col],
                scale=df.loc[row, scale_col],
                size=reali,
                random_state=rng,
            )

    elif df.loc[row, dist_col] == "Normal":
        param = norm.rvs(
            loc=df.loc[row, loc_col],
            scale=df.loc[row, scale_col],
            size=reali,
            random_state=rng,
        )
        param = np.where(
            param < df.loc[row, lim_min_col], df.loc[row, lim_min_col], param
        )
        param = np.where(
            param > df.loc[row, lim_max_col], df.loc[row, lim_max_col], param
        )

    elif df.loc[row, dist_col] == "Exponential":
        param = expon.rvs(
            loc=df.loc[row, loc_col],
            scale=df.loc[row, scale_col],
            size=reali,
            random_state=rng,
        )
        param = np.where(
            param > df.loc[row, lim_max_col], df.loc[row, lim_max_col], param
        )

    elif df.loc[row, dist_col] == "Uniforme":
        param = uniform.rvs(
            loc=df.loc[row, loc_col],
            scale=df.loc[row, scale_col],
            size=reali,
            random_state=rng,
        )

    return param
