# Path Class for Path info

import pandas as pd



class Filter(object):

    def __init__(self, option):
        self.option = option


    def apply(self, df):
        assert isinstance(df, pd.DataFrame), 'input arg df should be df type but {0}'.format(type(df))

        _lot_wfs = df.query(self.option)['lot_wf'].unique()

        return df[df['lot_wf'].isin(_lot_wfs)]
