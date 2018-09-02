import pandas as pd

if __name__ == '__main__':

    df = pd.read_table(
        r'C:\Codes\Snippets\scientific\test\df_a.txt',
    )

    pivot = pd.pivot_table(
        df,
        index=['id'],
        columns=['step'],
        values='ppid',
        aggfunc='last',
    )

    """
    start here!
    """

    merge_step = ['a', 'b', 'c']

    for i, col in enumerate(merge_step):
        if i == 0:
            pivot['new'] = pivot[col]
            title = col
        else:
            pivot['new'] = pivot['new'] + '_' + pivot[col]
            title += '_' + col

    # rename cols
    pivot.rename(columns={'new': title}, inplace=True)

    print(pivot)

    import pdb;

    pdb.set_trace()
