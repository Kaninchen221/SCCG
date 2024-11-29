from Utils.helpers import find_next_occurrence


def test_find_next_occurrence():
    strings_list = ["a", "b", " ", "a", "b"]
    result = find_next_occurrence(strings_list, 'a', 0)
    assert result == 0

    result = find_next_occurrence(strings_list, 'c')
    assert not result

    result = find_next_occurrence(strings_list, 'c', 0, -1)
    assert result == -1
