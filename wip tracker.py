# sample test

import pandas as pd
import goldentiger as gt


wip_info = pd.read_excel(
    gt.sample,
    sheetname='wip',
)

path = pd.read_excel(
    gt.sample,
    sheetname='wip_path',
)


res = pd.merge(wip_info, path, on=['desc'], how='left')


print(res)
