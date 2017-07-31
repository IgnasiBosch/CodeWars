def binary_search_recursive(_list, item, min_index=None, max_index=None):
    if min_index is None:
        min_index = 0
    if max_index is None:
        max_index = len(_list) - 1

    if min_index == max_index:
        return False
    midpoint = (min_index + max_index) // 2

    if _list[midpoint] == item:
        return True

    if item < _list[midpoint]:
        return binary_search_recursive(_list, item, min_index, midpoint)
    return binary_search_recursive(_list, item, midpoint + 1, max_index)
