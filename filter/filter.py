# Filter Class for Path info

import pandas as pd


def read_path():
    return None



class Path(object):

    def __init__(self, option):
        self.option = option
        self.path = self.read()


    def read(self):
        self.path = read_path()
        self.path = self.path.query(option)


    def append_path(self, df):
        df = pd.merge(df, self.path, left_index=True, right_index=True) # index: lot_wf

        return df
