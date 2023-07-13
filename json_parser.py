import pandas as pd
import json
from utilities import display_usage
from energy_extractor import *

json_file_path = "data/EC.d Export Pfizer_LEED_R1 [both].json"


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
