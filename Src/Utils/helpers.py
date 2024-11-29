
def find_next_occurrence(string, char, start_index=0, return_invalid_value=None):
    try:
        return string.index(char, start_index)
    except ValueError:
        return return_invalid_value
