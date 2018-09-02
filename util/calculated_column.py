# utility functions

import pandas as pd


def wfid_to_2digit_str(ser):
    assert isinstance(ser, pd.Series), 'ser should be Series type but {0}'.format(ser)

    convert_ser = ser.map('{:02d}'.format)

    return convert_ser













if __name__ == '__main__':

    df = pd.DataFrame(
        {
            'wf': [1, 2, 3, 11, 25],
        }
    )

    df['new'] = wfid_to_2digit_str(df['wf'])


    print(df)
