
import goldentiger as gt

import pandas as pd


def union_list_all(a):
    """
    union all elements in the list like set property
    :param a: list of list
    :return:
    """
    assert isinstance(a, list), 'arg a should be list type but {0}'.format(type(a))

    res = []

    for it in a:
        if res == []:
            res = it
        else:
            res = union_from_list(res, it)

    return res


def union_from_list(a, b):
    assert isinstance(a, list), 'arg a should be list type but {0}'.format(type(a))
    assert isinstance(b, list), 'arg b should be list type but {0}'.format(type(b))

    return list(set(a) & set(b))


def get_wf_from_given_conditiob(df, condition=[]):
    assert isinstance(df, pd.DataFrame), 'arg df should be df type but {0}'.format(type(df))
    assert isinstance(condition, list), 'kwarg condition should be list type but {0}'.format(type(condition))

    res = []

    for exp in condition:
        temp = df.query(exp)

        res.append(temp['lot_wf'].values.tolist())

    result = union_list_all(res)

    return result
