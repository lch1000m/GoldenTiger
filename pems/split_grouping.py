# mahanolobis distance test

import re

import pandas as pd
import goldentiger as gt


def grp_by_step(df):

    res = df.stack()
    res = res.reset_index()

    res.rename(columns={'level_1':'wf', 0:'ppid'}, inplace=True)

    res['n of split'] = res.groupby(['step'])['ppid'].transform(lambda x: x.nunique())

    temp = res[['step','ppid']].drop_duplicates(subset=['step','ppid'])
    temp['grp_by_step'] = temp.groupby(['step']).cumcount() + 1
    temp['grp_by_step'] = 'G' + temp['grp_by_step'].astype(str)

    res = pd.merge(res, temp, on=['step','ppid'], how='left')

    return res


def grp_by_wf(df):

    res = df.stack()
    res = res.reset_index()
    res.rename(columns={'level_1': 'wf', 0: 'ppid'}, inplace=True)

    pivot = pd.pivot_table(
        res,
        index=['wf'],
        columns=['step'],
        values='ppid',
        aggfunc='last',
    ).reset_index()

    check = pivot[['step1','step2','step3']].drop_duplicates()
    check['grp'] = ['G'+str(i+1) for i in range(len(check))]

    res = pd.merge(pivot,check, on=['step1','step2','step3'], how='left')

    return res


def main():

    df = pd.read_table(
    r'C:\Codes\Snippets\scientific\test\df_a.txt',
    index_col=['step'],
    )

    res1 = grp_by_step(df)

    res2 = grp_by_wf(df)

    print(res1)
    print(res2)



if __name__ == '__main__':

    main()
