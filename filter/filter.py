# path data reading class

import pandas as pd


def add_step_desc(df):
    """
    add step_desc to path df
    """

    return df


def read_path(option):
    """
    read path function
    """
    df = pd.DataFrame(option)

    df = add_step_desc(df)

    return df



class Path(object):

    def __init__(self, option):
        self.option = option
        self.path = read_path()


    def get_low_wfs(self):
        """
        :return: unique lot_wfs
        """

        try:
            return self.path['lot_wf'].unique().tolist()
        except:
            print('path data is not prepared yet!')


    def append_path(self, df, direction='vertical'):
        """
        append path info to df in given direction
        :param direction: vertical or horizontal
        """
        if direction == 'vertical':
            pivot_vertical = pd.pivot_table(
                self.path,
                index=['lot_wf'],
                columns=['step'],
                values='ppid',
                aggfunc='last',
            )
            df = pd.merge(df, pivot_vertical, left_index=True, right_index=True) # index: lot_wf
        elif direction == 'horizontal':
            df = pd.merge(df, self.path, left_index=True, right_index=True)  # index: lot_wf

        return df


def aliasing(df, alias_option):
    """
    alias = {
        'filter':[
            "(df['ppid'].isin(['a','c'])) & (df['lot_wf'].isin([1,3]))",
        ],
        'alias':[
            'ppid is A or C',
            'Other',
        ],
    }
    """

    assert len(alias_option['filter']) == len(alias_option['alias']) - 1, 'filter & alias length matching failed! filter: {0} - alias: {1}'.format(len(alias_option['filter']), len(alias_option['alias']))

    for i, val in enumerate(alias_option['filter']):
        df.loc[eval(val), 'alias'] = alias_option['alias'][i]

    df.loc[df['alias'].isnull(), 'alias'] = alias_option['alias'][len(alias_option['alias']) - 1]

    return df



class Alias(object):

    def __init__(self, option):
        self.path = Path(option)


    def apply_alias(self, alias_option):
        df = aliasing(alias_option)

        return df
