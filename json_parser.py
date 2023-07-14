import pandas as pd
import json
from area_extractor import get_wall_construction_area_by_orientation
from gains_extractor import get_gains_source_amount, get_gains_source_name
from utilities import display_usage
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

# # get sizes of building
# print()
# print("Builing Information...")
# print(get_building_sizes(df))

# ################################################################################
# ################################# ENERGY #######################################
# ################################################################################

# # get energy uses categories
# energy_usage_categories = get_energy_uses_names(df)

# # get electricty values
# print()
# print("Getting Electricity Usages...")
# energy_usages_elec = []
# for energy_category in energy_usage_categories:
#     energy_usage = get_elec_energy_usage(df, energy_category)
#     energy_usages_elec.append(energy_usage)

#     # display
#     display_usage("elec", energy_category, energy_usage)

# # get natural gas values
# print()
# print("Getting Natural Gas Usages...")
# energy_usages_natGas = []
# for energy_category in energy_usage_categories:
#     energy_usage = get_natGas_energy_usage(df, energy_category)
#     energy_usages_natGas.append(energy_usage)
#     # display
#     display_usage("nat_gas", energy_category, energy_usage)

# #  totals
# print()
# print("Getting Total Usages...")

# # compute total electricty usage
# total_elec_usage = sum(energy_usages_elec)
# display_usage("elec", "total_electricity_usage", total_elec_usage)

# # compute total gas usage
# total_natGas_usage = sum(energy_usages_natGas)
# display_usage("nat_gas", "total_naturalGas_usage", total_natGas_usage)

# # compute totals
# total_energy = 0
# for energy_category in energy_usage_categories:

#     total_energy_usage = sum([
#         get_elec_energy_usage(df, energy_category),
#         get_natGas_energy_usage(df, energy_category)
#     ])

#     # sum total energy
#     total_energy += total_energy_usage

#     display_usage("combined", "total_"+energy_category,
#                   total_energy_usage)
# # output total energy
# display_usage("combined", "total_energy", total_energy)

# ################################################################################
# ################################# GAINS ########################################
# ################################################################################

# # get gains sources
# gains_sources = get_gains_source_name(df)

# # get gains values
# print()
# print("Getting Gains Values...")
# gains_amount = []
# for gain_source in gains_sources:
#     gain_amount = get_gains_source_amount(df, gain_source)
#     gains_amount.append(gain_amount)

#     # display
#     display_usage("gains", gain_source, gain_amount)

# # compute total gains
# total_gains = sum(gains_amount)

# # output total gains
# display_usage("gains", "total_gains", total_gains)


################################################################################
################################# AREAS ########################################
################################################################################

# get construction properties
pprint(get_wall_construction_area_by_orientation(df, "Wall", 0))
pprint(get_wall_construction_area_by_orientation(df, "Wall", 90))
pprint(get_wall_construction_area_by_orientation(df, "Wall", 180))
pprint(get_wall_construction_area_by_orientation(df, "Wall", 270))
