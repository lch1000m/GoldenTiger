# utilities for goldentiger

import goldentiger as gt

import pandas as pd


def intersect_set(a, b):

    return list(set(a) & set(b))


def diff_set(a, b):
    return list(set(a) - set(b))


def union_set(a, b):
    return list(set(a) | set(b))
