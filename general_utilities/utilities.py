

from typing import List, Dict, NamedTuple
from pprint import pprint
from numpy import average


def sum_values_by_key(dict_list: List[Dict[str, float]], key: str) -> float:
    total_sum = 0
    for dictionary in dict_list:
        if key in dictionary:
            total_sum += dictionary[key]
    return total_sum


def display_usage(source: str, energy_category: str, usage: float):
    print({'source': source, 'energy_category': energy_category, "usage": usage})


def display_named_tuples(named_tuples: List[NamedTuple]):
    for named_tuple in named_tuples:
        print(named_tuple._asdict())


def display_named_tuple(named_tuple: NamedTuple):
    for entry in named_tuple:
        # print(type(entry))
        print(entry)


def display_tuple_as_dict(named_tuple: NamedTuple):
    print(named_tuple._asdict())
# compute weighted average of a list of named tuples using numpy
