

from typing import List, Dict


def sum_values_by_key(dict_list: List[Dict[str, float]], key: str) -> float:
    total_sum = 0
    for dictionary in dict_list:
        if key in dictionary:
            total_sum += dictionary[key]
    return total_sum


def display_usage(source: str, energy_category: str, usage: float):
    print({'source': source, 'energy_category': energy_category, "usage": usage})
