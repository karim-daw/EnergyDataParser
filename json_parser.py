import pandas as pd
import json
from convert_units import convert_kwh_to_gj
import typing

json_file_path = "data/EC.d Export Pfizer_LEED_R1 [both].json"


def get_gj_value(df: pd.DataFrame, column_header: str) -> float:
    value_kwh = df[column_header].iloc[0]
    value_gwh = convert_kwh_to_gj(value_kwh)
    return value_gwh


def get_energy_sources(df: pd.DataFrame, energy_use: str) -> typing.List[str]:
    energy_sources = df["proposed_results"]["energy_uses"][energy_use]["sources"]
    return list(energy_sources.keys())


def sources_filtering_function(pair):
    wanted_keys = ['name', 'usage']
    key, value = pair
    if key in wanted_keys:
        return True  # keep pair in the filtered dictionary
    else:
        return False  # filter pair out of the dictionary


def get_energy_usage(df: pd.DataFrame, energy_use_name: str, sourceFlag: int) -> float:
    """get the energy usage of the json file in gj\n
    The sourceFlag mapping is as follows:\n
    1 = Electricity
    2 = Natural Gas
    """
    # check flag
    energy_src = ""
    if sourceFlag == 1:
        energy_src = "elec"
    elif sourceFlag == 2:
        energy_src = "nat_gas"

    # get energy usage and convert from kwh to gj
    energy_usage = df["proposed_results"]["energy_uses"][energy_use_name]["sources"][energy_src]["usage"]
    energy_usage = convert_kwh_to_gj(energy_usage)

    return {"name": energy_use_name, "usage": energy_usage}


def get_building_sizes(df: pd.DataFrame) -> typing.List[str]:
    building_sizes = df["proposed_results"]["aps_stats"]["sizes"]
    return building_sizes


# Read JSON file
with open(json_file_path) as f:
    data = json.load(f)

# flatten aps_stats data
# df_aps_stat_flat = pd.json_normalize(data['proposed_results']['aps_stats'])
df = pd.read_json(json_file_path)


"""areas and volumes and rooms"""
print(get_building_sizes(df))

"""get interior lighitng"""
print(get_energy_usage(df, "prm_interior_lighting", 1))


"""get domestic hot water values"""
print(get_energy_usage(df, "prm_services_water_heating", 1))

"""get miscellaneous equipment values"""
print(get_energy_usage(df, "prm_receptacle_equipment", 1))

"""get pumping values"""
print(get_energy_usage(df, "prm_pumps", 1))

"""get space cooling values"""
print(get_energy_usage(df, "prm_space_cooling", 1))

"""get space heating values"""
print(get_energy_usage(df, "prm_space_heating", 1))


"""get fan values"""
fan_interior_local = get_energy_usage(df, "prm_fans_interior_local", 1)
fan_interior_central = get_energy_usage(df, "prm_fans_interior_central", 1)
fan_exhaust = get_energy_usage(df, "prm_fans_exhaust", 1)

total_fan_usage = fan_interior_local["usage"] + \
    fan_interior_central["usage"]+fan_exhaust["usage"]

fan_combined = {"name": "fan_total", "usage": total_fan_usage}
print(fan_combined)

# flatten building results data
df_building_results_flat = pd.json_normalize(
    data['proposed_results']['building_results'])

# """get total electricty values"""
# inW = get_gj_value(df_building_results_flat, "Total electricity.total")
# inKWH = inW * 0.001
# print(inKWH)

# # read data from from json (not flattened)
# df = pd.read_json(json_file_path)

# # get list of energy sources
# print(get_energy_sources(df, "prm_interior_lighting"))
