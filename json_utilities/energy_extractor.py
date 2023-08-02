import pandas as pd
from typing import List, Dict

from general_utilities.convert_units import convert_kwh_to_gj, convert_wh_to_kwh


def get_energy_sources(df: pd.DataFrame, energy_use_name: str) -> List[str]:
    energy_sources = df["proposed_results"]["energy_uses"][energy_use_name]["sources"]
    return list(energy_sources.keys())


def get_energy_uses_names(df: pd.DataFrame) -> List[str]:
    energy_sources = df["proposed_results"]["energy_uses"]
    return list(energy_sources.keys())


def get_elec_energy_usage(df: pd.DataFrame, energy_use_name: str) -> float:
    """get the energy usage of the json file in gj\n
    """

    if "elec" in df["proposed_results"]["energy_uses"][energy_use_name]["sources"]:
        energy_usage = df["proposed_results"]["energy_uses"][energy_use_name]["sources"]["elec"]["usage"]
        # get energy usage and convert from kwh to gj
        energy_usage = convert_kwh_to_gj(energy_usage)
        return energy_usage
    else:
        return 0


def get_natGas_energy_usage(df: pd.DataFrame, energy_use_name: str) -> float:
    """check energy sources"""
    # if no natural gas return 0
    energy_sources = get_energy_sources(df, energy_use_name)
    if "nat_gas" not in energy_sources:
        return 0
    else:
        energy_usage_kwh = df["proposed_results"]["energy_uses"][energy_use_name]["sources"]["nat_gas"]["usage"]
        energy_usage_gj = convert_kwh_to_gj(energy_usage_kwh)
        return energy_usage_gj


def get_building_results(df: pd.DataFrame, desired_total) -> float:
    """Gets the total energy results and converts to GJ from the building results of the .json output \n
    Enter the desired header from the json in "desired_total" to retrieve the value"""

    total_wH = df["proposed_results"]["building_results"][desired_total]["total"]
    total_kWh = convert_wh_to_kwh(total_wH)
    total_gJ = convert_kwh_to_gj(total_kWh)

    return total_gJ


def get_building_sizes(df: pd.DataFrame) -> List[str]:
    building_sizes = df["proposed_results"]["aps_stats"]["sizes"]
    return building_sizes
