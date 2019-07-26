import pyranges as pr
import numpy as np
import pandas as pd


def _setattr(self, column_name, column):


    isiterable = isinstance(column, list) or isinstance(
        column, pd.Series) or isinstance(column, np.ndarray)
    isdict = isinstance(column, dict)

    if isiterable:
        if not len(self) == len(column):
            raise Exception("DataFrame and column must be same length.")

    already_exists = column_name in self.values()[0]

    if already_exists:
        pos = list(self.values()[0].columns).index(column_name)
    else:
        pos = self.values()[0].shape[1]

    start_length, end_length = 0, 0

    dfs = {}
    for k, df in self.items():

        end_length += len(df)

        if already_exists:
            df = df.drop(column_name, axis=1)

        if isiterable:
            df.insert(pos, column_name, column[start_length:end_length])
        elif isdict:
            df.insert(pos, column_name, column[k])
        else:
            df.insert(pos, column_name, column)

        start_length = end_length

        dfs[k] = df

    if column_name not in ["Chromosome", "Strand"]:

        self.__dict__["dfs"] = dfs
        # print(self)
        # raise
    else:
        self.__dict__["dfs"] = pr.PyRanges(pr.PyRanges(dfs).df).dfs


def _getattr(self, name):

    if name in self.columns:
        return pd.concat([df[name] for df in self.values()])
    else:
        raise Exception("PyRanges object has no attribute", name)
