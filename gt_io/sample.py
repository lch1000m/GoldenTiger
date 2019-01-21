# sample code for efficient query

import goldentiger as gt


query = {   # query statement uses only lower case
    'db': 'il',
    'process_id': ['kngf','kngg'],

    'query': '^9.5.+tk.+adi+.CD1$',

    'outlier':{'apply': True, 'remain': True},
    'only_last_spec': {'apply': True, 'pid':'kngf'},
}


df = gt.db.DB().read() # data you want
