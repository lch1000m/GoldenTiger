
import pandas as pd

import goldentiger as gt


# df1 = pd.read_table(
#     r'C:\Codes\Snippets\scientific\test\df_a.txt',
# )
#
df1 = pd.read_table(
    r'C:\Codes\Snippets\scientific\test\df_b.txt',
)


df1['conv'] = df1['item'].map(gt.settings.yms_col_names_conversion)

print(df1)
