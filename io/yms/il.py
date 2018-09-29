# read yms il data

import pandas as pd


option = {
    'usecols': [],
}


def add_calculated_columns():
    return None


def remove_duplication():
    return None


def add_outlier_info():
    return None


def read():

    df = pd.DataFrame()

    df = remove_duplication(df)
    df = add_outlier_info(df)
    df = add_calculated_columns(df)

    return df
