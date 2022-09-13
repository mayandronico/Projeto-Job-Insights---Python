# from src.counter import count_ocurrences
from src.counter import count_ocurrences


def test_counter():
    result_py = count_ocurrences('src/jobs.csv', 'Python')
    result_js = count_ocurrences('src/jobs.csv', 'Javascript')
    assert result_py == 1639
    assert result_js == 122
