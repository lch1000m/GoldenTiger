# read yms il data

import goldentiger as gt
import pandas as pd


def rename_cols(df):
    """
    rename columns for appropriate form
    """
    return df


def read(df):
    """
    read il df from db
    """

    # rename columns of df
    df = rename_cols(df)

    # remove duplicated measure info
    df = gt.remove_duplicates(df)

    # add outlier info to df
    df = gt.add_outlier_info(df)

    # add calculated columns
    df = gt.add_lot_wf_info(df)

    return df


def apply(df, alias_option):
    for i, val in enumerate(alias_option['filter']):
        df.loc[eval(val), 'alias'] = alias_option['alias'][i]
    df.loc[df['alias'].isnull(), 'alias'] = alias_option['alias'][len(alias_option['alias']) - 1]

    return df


if __name__ == '__main__':

    alias = {
        'filter': [
            "df[df['ppid'] == 'A']",
            "df[df['ppid'] == 'C']",
        ],
        'alias': [
            'ppid is A',
            'ppid is C',
            'Other',
        ]
    }

    df = pd.read_table(r'C:\Codes\Snippets\sample data\alias.txt')

    res = apply(df, alias)

    print(res)
