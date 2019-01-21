# read yms il data

import goldentiger as gt
import pandas as pd

option = {
    'init': True,
}


def get_steps_from_prp(exp):

    steps = exp # extract step info from prp

    return steps


def query(_option):
    """
    query data to db
    """
    _option['step_seq'] = get_steps_from_prp(_option['expression'])
    option.update(_option)

    df = pd.DataFrame()

    return df


def rename_cols(df):
    """
    rename columns for appropriate form
    """
    return df


def read(option):
    """
    read il df from db
    """

    df = query(option)

    # rename columns of df
    df = rename_cols(df)

    # remove duplicated measure info
    df = gt.remove_duplicates(df)

    # add outlier info to df
    df = gt.add_outlier_info(df)

    # add calculated columns
    df = gt.add_lot_wf_info(df)

    if option['only_last_spec']:
        new_spec = pd.DataFrame()   # datafram w/ last spec information
        df = gt.merge(df, new_spec, on=['STEP_ITEM'], how='left', suffixes=['_rem',''])

    return df
