import pandas as pd
import json
from json_utilities.envelope_extractor import *
from json_utilities.gains_extractor import *
from general_utilities.utilities import *
from json_utilities.energy_extractor import *
from pprint import pprint


def read_json_file(json_file_path):
    with open(json_file_path) as f:
        return json.load(f)


def display_building_information(df):
    print("Builing Information...")
    print(get_building_sizes(df))


def display_energy_usage(df):
    energy_usage_categories = get_energy_uses_names(df)

    print("\nGetting Electricity Usages...")
    energy_usages_elec = []
    for energy_category in energy_usage_categories:
        energy_usage = get_elec_energy_usage(df, energy_category)
        energy_usages_elec.append(energy_usage)
        display_usage("elec", energy_category, energy_usage)

    print("\nGetting Natural Gas Usages...")
    energy_usages_natGas = []
    for energy_category in energy_usage_categories:
        energy_usage = get_natGas_energy_usage(df, energy_category)
        energy_usages_natGas.append(energy_usage)
        display_usage("nat_gas", energy_category, energy_usage)

    total_elec_usage = sum(energy_usages_elec)
    display_usage("elec", "total_electricity_usage", total_elec_usage)

    total_natGas_usage = sum(energy_usages_natGas)
    display_usage("nat_gas", "total_naturalGas_usage", total_natGas_usage)

    total_energy = sum(
        [get_elec_energy_usage(df, category) + get_natGas_energy_usage(df, category)
         for category in energy_usage_categories])
    display_usage("combined", "total_energy", total_energy)


def display_gains(df):
    gains_sources = get_gains_source_name(df)

    print("\nGetting Gains Values...")
    gains_amount = []
    for gain_source in gains_sources:
        gain_amount = get_gains_source_amount(df, gain_source)
        gains_amount.append(gain_amount)
        display_usage("gains", gain_source, gain_amount)

    total_gains = sum(gains_amount)
    display_usage("gains", "total_gains", total_gains)


def display_areas_by_orientation(df):
    print("\nGetting Areas by Orientation...")
    constructions_by_area_east = get_wall_construction_area_by_orientation(df, "Wall", 90)
    constructions_by_area_west = get_wall_construction_area_by_orientation(df, "Wall", 270)
    constructions_by_area_north = get_wall_construction_area_by_orientation(df, "Wall", 0)
    constructions_by_area_south = get_wall_construction_area_by_orientation(df, "Wall", 180)
    display_named_tuple(constructions_by_area_east)
    display_named_tuple(constructions_by_area_west)
    display_named_tuple(constructions_by_area_north)
    display_named_tuple(constructions_by_area_south)


def display_u_values(df):
    print("\nGetting U-values by construction category...")
    uValues_wall = get_uVal_by_construction_category(df, "wall")
    uValues_roof = get_uVal_by_construction_category(df, "roof")
    uValues_ext_glazing = get_uVal_by_construction_category(df, "ext_glazing")
    uValues_partition = get_uVal_by_construction_category(df, "partition")
    display_named_tuples(uValues_wall)
    display_named_tuples(uValues_roof)
    display_named_tuples(uValues_ext_glazing)
    display_named_tuples(uValues_partition)

    # print("\nGetting U-values by construction name...")
    # pprint(get_uVal_by_construction_name(df, "STD_PART"))

    print("\nGetting U-values by orientation...")
    data = get_uVal_by_orientation(df, "Wall")
    pprint(get_uVal_by_orientation(df, "Wall"))

    print("\nCompute Weighted Average U-Values by Orientation...")
    weighted_average = compute_weighted_average(data)
    print("Weighted Average U-value:", weighted_average)


def display_area_by_construction_name_and_orientation(df):
    print("\nComputing area by construciton name and orientation...")

    # get construction names
    construction_names = get_construction_names(df)
    # get orientations
    orientations = [0, 90, 180, 270]

    # get area by construction name and orientation
    for construction_name in construction_names:
        # check if construction is vertical
        if is_vertical_wall(df, construction_name):
            for orientation in orientations:
                area = get_wall_area_by_construction_name_and_orientation(df, construction_name, orientation)
                display_tuple_as_dict(area)


def parse_json_file(json_file_path):
    data = read_json_file(json_file_path)
    df = pd.read_json(json_file_path)

    pprint(get_construction_names(df))

    display_building_information(df)
    display_energy_usage(df)
    display_gains(df)
    display_areas_by_orientation(df)
    display_u_values(df)
    display_area_by_construction_name_and_orientation(df)
