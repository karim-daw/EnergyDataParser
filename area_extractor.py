import pandas as pd
from typing import List, Dict
from pprint import pprint


def get_wall_construction_area_by_orientation(df: pd.DataFrame, construction_type: str, orientation: int):

    # this returns a list of dictionaries
    all_bodies = df["proposed_results"]["bodies"]["bodies"]

    total_wall_area = 0
    total_window_area = 0
    for body in all_bodies:
        # get the surfaces of the body
        surfaces = body["surfaces"]
        # for each surface, get the construction type
        for surface in surfaces:
            # get the properties of the surface
            properties = surface["properties"]
            areas = surface["areas"]

            # check if the key "o" is in the properties, if yes continue
            if "o" in properties:

                # add +- 10 degrees to the orientation for buffer

                if properties["ty"] == construction_type and properties["o"] < orientation+10 and properties["o"] > orientation-10:
                    # net wall area
                    wall_area = areas["en"]
                    total_wall_area += wall_area

                    # window area
                    if "ew" in areas:
                        window_area = areas["ew"]
                        total_window_area += window_area

    # mapping for different orientations to their labels
    if orientation == 0:
        orientation_label = "North"
    elif orientation == 90:
        orientation_label = "East"
    elif orientation == 180:
        orientation_label = "South"
    elif orientation == 270:
        orientation_label = "West"
    else:
        orientation_label = "Unknown"

    # dictionary containing the total area by orientation
    wall_construction_data = {"total_area": total_wall_area,
                              "orientation": orientation_label, "type": "Opaque Wall", "type_label": construction_type}
    window_construction_data = {"total_area": total_window_area,
                                "orientation": orientation_label, "type": "Window", "type_label": construction_type}
    sum_construction_data = {"total_area": total_wall_area+total_window_area,
                             "orientation": orientation_label, "type": "Window and Wall", "type_label": construction_type}
    return wall_construction_data, window_construction_data, sum_construction_data

# function that retrieves u values for walls by orientation


# def get_uVal_by_construction_category(df: pd.DataFrame, construction_category: str):

#  # check that construction category is correct
#     valid_categories = ["ext_glazing", "wall", "roof", "partition"]
#     if construction_category not in valid_categories:
#         raise ValueError(
#             "construction category must be one of the following: ext_glazing, wall, roof, partition. You entered: " + construction_category)

#     all_constructions = df["proposed_results"]["bodies"]["constructions"]

#     uValues_by_construction_category = []

#     # wall is the construction type and its lower case for some reason
#     construction_type = construction_category.lower()

#     # these are the construction names, this will be used to cross reference the different walls
#     # compared to their orienation in order to get a u value by oreintation
#     construction_names = all_constructions.keys()
#     for construction_name in construction_names:
#         construction_data = all_constructions[construction_name]
#         if construction_data["category"] == construction_category:
#             uVal = construction_data["u_value"]
#             reference_name = construction_data["reference"]
#             # create data dict with the value and construction type
#             uVal_data = {"construction_name": construction_name, "reference": reference_name,
#                          "u_value": uVal, "type": construction_category}
#             uValues_by_construction_category.append(uVal_data)

#     return uValues_by_construction_category


def get_uVal_by_construction_category(df: pd.DataFrame, construction_category: str):
    valid_categories = ["ext_glazing", "wall", "roof", "partition"]

    if construction_category not in valid_categories:
        raise ValueError(
            "Construction category must be one of the following: ext_glazing, wall, roof, partition. You entered: " + construction_category)

    all_constructions = df["proposed_results"]["bodies"]["constructions"]

    construction_category = construction_category.lower()

    # Create a DataFrame from the constructions dictionary
    # Transpose the DataFrame so that the construction names are the index
    # and the columns are the construction properties
    # This will make it easier to filter the DataFrame
    constructions_df = pd.DataFrame(all_constructions).T

    # Filter the DataFrame based on the construction category
    # This will return a new DataFrame with only the constructions
    # that match the construction category
    # The index of the DataFrame is the construction name
    # The columns of the DataFrame are the construction properties
    filtered_df = constructions_df[constructions_df["category"]
                                   == construction_category].copy()

    # Create a new DataFrame with the desired columns
    # This will make it easier to convert the DataFrame to a list of dictionaries
    # This will also make it easier to convert the DataFrame to a CSV file
    uValues_df = filtered_df[["u_value", "g_values", "reference"]].copy()
    uValues_df["construction_name"] = filtered_df.index
    uValues_df["type"] = construction_category

    # Convert the DataFrame to a list of dictionaries
    uValues_by_construction_category = uValues_df.to_dict("records")

    return uValues_by_construction_category
