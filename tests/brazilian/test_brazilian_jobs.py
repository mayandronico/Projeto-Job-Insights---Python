# from src.brazilian_jobs import read_brazilian_fil
from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result_py = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    for job in result_py:
        list_keys = job.keys()
    assert 'title' in list_keys
    assert 'salary' in list_keys
    assert 'type' in list_keys
