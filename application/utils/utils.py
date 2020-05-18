from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


def find_max_similarity(search, fields):
    max_ratio = 0.0
    for field_value in fields:
        field_value = str(field_value).lower()
        ratio = similarity(field_value, search)
        max_ratio = max(ratio, max_ratio)                 
    return max_ratio