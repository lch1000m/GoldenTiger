# utility function

import pandas as pd


def merge(*args, **kwargs):
    """
    pandas merge compatible
    """
    res = pd.merge(*args, **kwargs)

    return res


def remove_duplicates(df):
    """
    remove duplicates from df
    """
    return df


def add_lot_wf_info(df):
    """
    add lot_wf column to df
    """
    return df


def add_outlier_info(df):
    """
    add outlier info to df
    """
    return df
