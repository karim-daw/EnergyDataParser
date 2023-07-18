import pandas as pd
import json
from envelope_extractor import get_uVal_by_construction_category, get_uVal_by_construction_name, get_uVal_by_orientation, get_wall_construction_area_by_orientation
from gains_extractor import get_gains_source_amount, get_gains_source_name
from utilities import display_named_tuples, display_usage, display_named_tuple
from energy_extractor import *
from pprint import pprint

json_file_path = "data/EC.d Export Pfizer_LEED_R1 [both].json"
# json_file_path = "data\EC.d Export 2023_01_17_Visa_LEED [both].json"


# Read JSON file
with open(json_file_path) as f:
    data = json.load(f)

# put json in dataframe
df = pd.read_json(json_file_path)


################################################################################
############################### BUILDING DATA ##################################
################################################################################

# get sizes of building
print()
print("Builing Information...")
print(get_building_sizes(df))

# ################################################################################
# ################################# ENERGY #######################################
# ################################################################################

# get energy uses categories
energy_usage_categories = get_energy_uses_names(df)

# get electricty values
print()
print("Getting Electricity Usages...")
energy_usages_elec = []
for energy_category in energy_usage_categories:
    energy_usage = get_elec_energy_usage(df, energy_category)
    energy_usages_elec.append(energy_usage)

    # display
    display_usage("elec", energy_category, energy_usage)

# get natural gas values
print()
print("Getting Natural Gas Usages...")
energy_usages_natGas = []
for energy_category in energy_usage_categories:
    energy_usage = get_natGas_energy_usage(df, energy_category)
    energy_usages_natGas.append(energy_usage)
    # display
    display_usage("nat_gas", energy_category, energy_usage)

#  totals
print()
print("Getting Total Usages...")

# compute total electricty usage
total_elec_usage = sum(energy_usages_elec)
display_usage("elec", "total_electricity_usage", total_elec_usage)

# compute total gas usage
total_natGas_usage = sum(energy_usages_natGas)
display_usage("nat_gas", "total_naturalGas_usage", total_natGas_usage)

# compute totals
total_energy = 0
for energy_category in energy_usage_categories:

    total_energy_usage = sum([
        get_elec_energy_usage(df, energy_category),
        get_natGas_energy_usage(df, energy_category)
    ])

    # sum total energy
    total_energy += total_energy_usage

    display_usage("combined", "total_"+energy_category,
                  total_energy_usage)
# output total energy
display_usage("combined", "total_energy", total_energy)

# ################################################################################
# ################################# GAINS ########################################
# ################################################################################

# get gains sources
gains_sources = get_gains_source_name(df)

# get gains values
print()
print("Getting Gains Values...")
gains_amount = []
for gain_source in gains_sources:
    gain_amount = get_gains_source_amount(df, gain_source)
    gains_amount.append(gain_amount)

    # display
    display_usage("gains", gain_source, gain_amount)

# compute total gains
total_gains = sum(gains_amount)

# output total gains
display_usage("gains", "total_gains", total_gains)


################################################################################
################################# AREAS ########################################
################################################################################

# get construction properties
# constructionData_0 = get_wall_construction_area_by_orientation(df, "Wall", 0)
print()
print("Getting Areas by Orientation...")
constructions_by_area_east = get_wall_construction_area_by_orientation(
    df, "Wall", 90)
constructions_by_area_west = get_wall_construction_area_by_orientation(
    df, "Wall", 270)
constructions_by_area_north = get_wall_construction_area_by_orientation(
    df, "Wall", 0)
constructions_by_area_south = get_wall_construction_area_by_orientation(
    df, "Wall", 180)

display_named_tuple(constructions_by_area_east)
display_named_tuple(constructions_by_area_west)
display_named_tuple(constructions_by_area_north)
display_named_tuple(constructions_by_area_south)


# get construction properties
print()
print("Getting U-values by construction category...")
# uValues_wall = get_uVal_by_construction_category(df, "wall")
# uValues_roof = get_uVal_by_construction_category(df, "roof")
# uValues_ext_glazing = get_uVal_by_construction_category(df, "ext_glazing")
# uValues_partition = get_uVal_by_construction_category(df, "partition")

# display_named_tuples(uValues_wall)
# display_named_tuples(uValues_roof)
# display_named_tuples(uValues_ext_glazing)
# display_named_tuples(uValues_partition)

# pprint(get_uVal_by_cosntruction_name(df, "STD_PART"))
pprint(get_uVal_by_orientation(df, "Wall"))
