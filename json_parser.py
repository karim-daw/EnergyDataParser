import pandas as pd
import json
from convert_units import convert_kwh_to_gj, convert_wh_to_kwh
from typing import List, Dict
from utilities import sum_values_by_key

json_file_path = "data/EC.d Export Pfizer_LEED_R1 [both].json"


def get_gj_value(df: pd.DataFrame, column_header: str) -> float:
    value_kwh = df[column_header].iloc[0]
    value_gwh = convert_kwh_to_gj(value_kwh)
    return value_gwh


def get_energy_sources(df: pd.DataFrame, energy_use_name: str) -> List[str]:
    energy_sources = df["proposed_results"]["energy_uses"][energy_use_name]["sources"]
    return list(energy_sources.keys())


def get_energy_uses(df: pd.DataFrame) -> List[str]:
    energy_sources = df["proposed_results"]["energy_uses"]
    return list(energy_sources.keys())


def get_elec_energy_usage(df: pd.DataFrame, energy_use_name: str) -> Dict[str, float]:
    """get the energy usage of the json file in gj\n
    The sourceFlag mapping is as follows:\n
    1 = Electricity
    2 = Natural Gas
    """

    if "elec" in df["proposed_results"]["energy_uses"][energy_use_name]["sources"]:
        energy_usage = df["proposed_results"]["energy_uses"][energy_use_name]["sources"]["elec"]["usage"]
        # get energy usage and convert from kwh to gj
        energy_usage = convert_kwh_to_gj(energy_usage)
        return {"source": "elec", "name": energy_use_name, "usage": energy_usage}
    else:
        return {"source": "elec", "name": energy_use_name, "usage": 0}


def get_natGas_energy_usage(df: pd.DataFrame, energy_use_name: str) -> Dict[str, float]:
    """check energy sources"""
    # if no natural gas return 0
    energy_sources = get_energy_sources(df, energy_use_name)
    if "nat_gas" not in energy_sources:
        return {"source": "nat_gas", "name": energy_use_name, "usage": 0}
    else:
        energy_usage_kwh = df["proposed_results"]["energy_uses"][energy_use_name]["sources"]["nat_gas"]["usage"]
        energy_usage_gj = convert_kwh_to_gj(energy_usage_kwh)
        return {"source": "nat_gas", "name": energy_use_name, "usage": energy_usage_gj}


def get_building_results(df: pd.DataFrame, desired_total) -> Dict[str, float]:
    """Gets the total energy results and converts to GJ from the building results of the .json output \n
    Enter the desired header from the json in "desired_total" to retrieve the value"""

    total_wH = df["proposed_results"]["building_results"][desired_total]["total"]
    total_kWh = convert_wh_to_kwh(total_wH)
    total_gJ = convert_kwh_to_gj(total_kWh)

    return {"source": "elec", "name": desired_total, "usage": total_gJ}


def get_building_sizes(df: pd.DataFrame) -> List[str]:
    building_sizes = df["proposed_results"]["aps_stats"]["sizes"]
    return building_sizes


# Read JSON file
with open(json_file_path) as f:
    data = json.load(f)

# put json in dataframe
df = pd.read_json(json_file_path)

# get energy uses categories
energy_usage_categories = get_energy_uses(df)

# get sizes of building
print()
print("Builing Information...")
print(get_building_sizes(df))


# get electricty values
print()
print("Getting Electricity Usages...")
energy_usages_elec = []
for energy_category in energy_usage_categories:
    energy_usage = get_elec_energy_usage(df, energy_category)
    energy_usages_elec.append(energy_usage)
    print(get_elec_energy_usage(df, energy_category))

# compute total electricty usage
total_elec_usage = sum_values_by_key(energy_usages_elec, "usage")
print(total_elec_usage)

# get natural gas values
print()
print("Getting Natural Gas Usages...")
energy_usages_natGas = []
for energy_category in energy_usage_categories:
    energy_usage = get_natGas_energy_usage(df, energy_category)
    energy_usages_natGas.append(energy_usage)
    print(get_natGas_energy_usage(df, energy_category))

# compute total nat gas usage
total_natGas_usage = sum_values_by_key(energy_usages_natGas, "usage")
print(total_natGas_usage)
