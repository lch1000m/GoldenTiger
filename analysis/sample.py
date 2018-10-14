
import pandas as pd, numpy as np


df = pd.read_table(
    r'C:\Codes\Snippets\python\pandas\passrate.txt',
)


def get_passrate(df, grp=['step'], wf_grp=['step', 'lot_wf'], ul='', ll='', value=''):
    df.loc[(df[value] > df[ul]) | (df[value] < df[ll]), 'pass/fail'] = 1  # 1 measn fail
    df.loc[(df[value] <= df[ul]) & (df[value] >= df[ll]), 'pass/fail'] = 0  # 0 measn pass

    df['Pass/Fail'] = df['pass/fail'].map({0: 'Pass', 1: 'Fail'})
    df['fail sum'] = df.groupby(wf_grp)['pass/fail'].transform(lambda x: x.sum())

    # Pass/Fail by WF level
    df.loc[df['fail sum'] == 0, 'wf pass/fail'] = 'pass'
    df.loc[df['fail sum'] > 0, 'wf pass/fail'] = 'fail'

    # get grp pass rate[%]
    df_pivot = pd.pivot_table(
        df,
        index=grp,
        columns=['wf pass/fail'],
        values='lot_wf',
        aggfunc=lambda x: x.nunique(),
    ).reset_index()

    df_pivot['Pass Rate[%]'] = df_pivot['pass'] / (df_pivot['pass'] + df_pivot['fail']) * 100

    _join_cols = grp.copy()
    _join_cols.append('Pass Rate[%]')
    df = pd.merge(df, df_pivot[_join_cols], on=grp, how='left')

    # remove redundant columns
    for col in ['pass/fail', 'fail sum']:
        del df[col]

    return df


res = get_passrate(df, grp=['step'], wf_grp=['step', 'lot_wf'], ul='UL', ll='LL', value='value')


print(res)
