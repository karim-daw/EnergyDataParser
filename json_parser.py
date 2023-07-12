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


def get_energy_usage(df: pd.DataFrame, energy_use_name: str) -> typing.List[str]:
    energy_usage = df["proposed_results"]["energy_uses"][energy_use_name]["sources"]["elec"]["usage"]
    energy_usage = convert_kwh_to_gj(energy_usage)
    return energy_usage


def get_building_sizes(df: pd.DataFrame) -> typing.List[str]:
    energy_usage = df["proposed_results"]["aps_stats"]["sizes"]
    return energy_usage


# Read JSON file
with open(json_file_path) as f:
    data = json.load(f)

# flatten aps_stats data
df_aps_stat_flat = pd.json_normalize(data['proposed_results']['aps_stats'])
df = pd.read_json(json_file_path)


"""areas and volumes and rooms"""
print(get_building_sizes(df))

# area = df_aps_stat_flat['sizes.area'].iloc[0]
# volume = df_aps_stat_flat['sizes.volume'].iloc[0]
# rooms = df_aps_stat_flat['sizes.rooms'].iloc[0]
# sizes = " Area: {}\n Volume: {}\n Rooms: {}\n".format(area, volume, rooms)
# print(sizes)


"""get interior lighitng"""
print(get_energy_usage(df, "prm_interior_lighting"))


# """get domestic hot water values"""
# print(get_gj_value(df_energy_uses_flat,
#       "prm_services_water_heating.sources.elec.usage"))

# """get miscellaneous equipment values"""
# print(get_gj_value(df_energy_uses_flat,
#       "prm_receptacle_equipment.sources.elec.usage"))

# """get pumping values"""
# print(get_gj_value(df_energy_uses_flat, "prm_pumps.sources.elec.usage"))

# """get space cooling values"""
# print(get_gj_value(df_energy_uses_flat, "prm_space_cooling.sources.elec.usage"))

# """get space heating values"""
# print(get_gj_value(df_energy_uses_flat, "prm_space_heating.sources.elec.usage"))

# """get fan values"""
# fan_interior_local = get_gj_value(
#     df_energy_uses_flat, "prm_fans_interior_local.sources.elec.usage")
# fan_interior_central = get_gj_value(
#     df_energy_uses_flat, "prm_fans_interior_central.sources.elec.usage")
# fan_interior_exhaust = get_gj_value(
#     df_energy_uses_flat, "prm_fans_exhaust.sources.elec.usage")
# sum = fan_interior_local+fan_interior_central+fan_interior_exhaust
# print(sum)

# # flatten building results data
# df_building_results_flat = pd.json_normalize(
#     data['proposed_results']['building_results'])

# """get total electricty values"""
# inW = get_gj_value(df_building_results_flat, "Total electricity.total")
# inKWH = inW * 0.001
# print(inKWH)

# # read data from from json (not flattened)
# df = pd.read_json(json_file_path)

# # get list of energy sources
# print(get_energy_sources(df, "prm_interior_lighting"))
