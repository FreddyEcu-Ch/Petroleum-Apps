# Define POES function

def poes(area, h, poro, swi, boi):
    """

    Parameters
    ----------
    area,
        area, acres
    h,
        Thickness, ft
    poro,
        Porosity, fraction
    swi,
        Water saturation, fraction
    boi,
        Oil bubble point, bbl/stb

    Returns
    -------
    POES
    """

    return 7758 * area * h * poro * (1 - swi) / boi