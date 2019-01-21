# debugging module

from pprint import pprint as pp


def pprint(**kwargs):
    """
    pretty print module
    """
    for key, val in kwargs.items():
        print('{0} : {1}'.format(key, val))
