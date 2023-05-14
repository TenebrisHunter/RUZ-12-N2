from collections import OrderedDict


def sort_dict(dictionary):
    """
    Сортирует словарь и все его вложенные словари по ключам
    """
    if not isinstance(dictionary, dict):
        return dictionary
    sorted_dict = OrderedDict()
    for key in sorted(dictionary.keys()):
        sorted_dict[key] = sort_dict(dictionary[key])
    return sorted_dict