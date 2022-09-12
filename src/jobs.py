from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as csv_file:
        dict_list = csv.DictReader(csv_file)
        list_jobs = list(dict_list)
    return list_jobs
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
