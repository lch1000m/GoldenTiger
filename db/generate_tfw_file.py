# generate extractor flow file objrct

import pandas as pd

# input parameters ########################
lid = ['KNBN']
prc = ['LN07LPP']
pids = ['KNGF','KNGG']

steps = ['KZ000000','KZ000100','KZ000200','KZ000300']
lots = ['AZ001','AZ002','AZ003']
###########################################



def main():

    res = pd.DataFrame(columns=['lid','prc','pids','steps','lots'])

    _index = 0

    for _lid in lid:
        for _prc in prc:
            for _pids in pids:
                for _st in steps:
                    for lot in lots:

                        res.set_value(_index, 'lid', _lid)
                        res.set_value(_index, 'prc', _prc)
                        res.set_value(_index, 'pids', _pids)
                        res.set_value(_index, 'steps', _st)
                        res.set_value(_index, 'lots', lot)

                        _index += 1

    return res


if __name__ == '__main__':

    res = main()

    print(res)
