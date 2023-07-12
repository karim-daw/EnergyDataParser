import pandas as pd
import json
from convert_units import convert_kwh_to_gj

json_file_path = "data/EC.d Export Pfizer_LEED_R1 [both].json"


def get_gj_value(df: pd.DataFrame, column_header: str):
    value_kwh = df[column_header].iloc[0]
    value_gwh = convert_kwh_to_gj(value_kwh)
    return value_gwh


# Read JSON file
with open(json_file_path) as f:
    data = json.load(f)

# faltten aps_stats data
df = pd.json_normalize(data['proposed_results']['aps_stats'])

"""areas and volumes and rooms"""
area = df['sizes.area'].iloc[0]
volume = df['sizes.volume'].iloc[0]
rooms = df['sizes.rooms'].iloc[0]
sizes = " Area: {}\n Volume: {}\n Rooms: {}\n".format(area, volume, rooms)
print(sizes)

# flatten energy end use data
df = pd.json_normalize(data['proposed_results']['energy_uses'])

"""get interior lighitng"""
print(get_gj_value(df, "prm_interior_lighting.sources.elec.usage"))

"""get domestic hot water values"""
print(get_gj_value(df, "prm_services_water_heating.sources.elec.usage"))

"""get miscellaneous equipment values"""
print(get_gj_value(df, "prm_receptacle_equipment.sources.elec.usage"))

"""get pumping values"""
print(get_gj_value(df, "prm_pumps.sources.elec.usage"))

"""get space cooling values"""
print(get_gj_value(df, "prm_space_cooling.sources.elec.usage"))

"""get space heating values"""
print(get_gj_value(df, "prm_space_heating.sources.elec.usage"))

"""get fan values"""
fan_interior_local = get_gj_value(
    df, "prm_fans_interior_local.sources.elec.usage")
fan_interior_central = get_gj_value(
    df, "prm_fans_interior_central.sources.elec.usage")
fan_interior_exhaust = get_gj_value(df, "prm_fans_exhaust.sources.elec.usage")
sum = fan_interior_local+fan_interior_central+fan_interior_exhaust
print(sum)

# flatten building results data
df = pd.json_normalize(data['proposed_results']['building_results'])

"""get total electricty values"""
inW = get_gj_value(df, "Total electricity.total")
inKWH = inW * 0.001
print(inKWH)
