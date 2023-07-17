from collections import namedtuple
import pandas as pd
from typing import List, Dict
from pprint import pprint

# def get_wall_construction_area_by_orientation(df: pd.DataFrame, construction_type: str, orientation: int):

#     # this returns a list of dictionaries
#     all_bodies = df["proposed_results"]["bodies"]["bodies"]

#     total_wall_area = 0
#     total_window_area = 0
#     for body in all_bodies:
#         # get the surfaces of the body
#         surfaces = body["surfaces"]
#         # for each surface, get the construction type
#         for surface in surfaces:
#             # get the properties of the surface
#             properties = surface["properties"]
#             areas = surface["areas"]

#             # check if the key "o" is in the properties, if yes continue
#             if "o" in properties:

#                 # add +- 10 degrees to the orientation for buffer

#                 if properties["ty"] == construction_type and properties["o"] < orientation+10 and properties["o"] > orientation-10:
#                     # net wall area
#                     wall_area = areas["en"]
#                     total_wall_area += wall_area

#                     # window area
#                     if "ew" in areas:
#                         window_area = areas["ew"]
#                         total_window_area += window_area

#     # mapping for different orientations to their labels
#     if orientation == 0:
#         orientation_label = "North"
#     elif orientation == 90:
#         orientation_label = "East"
#     elif orientation == 180:
#         orientation_label = "South"
#     elif orientation == 270:
#         orientation_label = "West"
#     else:
#         orientation_label = "Unknown"

#     # dictionary containing the total area by orientation
#     wall_construction_data = {"total_area": total_wall_area,
#                               "orientation": orientation_label, "type": "Opaque Wall", "type_label": construction_type}
#     window_construction_data = {"total_area": total_window_area,
#                                 "orientation": orientation_label, "type": "Window", "type_label": construction_type}
#     sum_construction_data = {"total_area": total_wall_area+total_window_area,
#                              "orientation": orientation_label, "type": "Window and Wall", "type_label": construction_type}
#     return wall_construction_data, window_construction_data, sum_construction_data


# def get_wall_construction_area_by_orientation(df: pd.DataFrame, construction_type: str, orientation: int):
#     valid_orientations = [0, 90, 180, 270]

#     if orientation not in valid_orientations:
#         raise ValueError(
#             "Orientation must be one of the following: 0, 90, 180, 270. You entered: " + str(orientation))

#     all_bodies = df["proposed_results"]["bodies"]["bodies"]

#     wall_areas = []
#     window_areas = []

#     for body in all_bodies:
#         surfaces = body["surfaces"]
#         for surface in surfaces:
#             properties = surface["properties"]
#             areas = surface["areas"]

#             if "o" in properties:
#                 if properties["ty"] == construction_type and properties["o"] < orientation + 10 and properties["o"] > orientation - 10:
#                     wall_areas.append(areas["en"])

#                     if "ew" in areas:
#                         window_areas.append(areas["ew"])

#     orientation_label = {
#         0: "North",
#         90: "East",
#         180: "South",
#         270: "West"
#     }.get(orientation, "Unknown")

#     wall_area = sum(wall_areas)
#     window_area = sum(window_areas)

#     wall_construction_data = {"total_area": wall_area,
#                               "orientation": orientation_label, "type": "Opaque Wall", "type_label": construction_type}
#     window_construction_data = {"total_area": window_area,
#                                 "orientation": orientation_label, "type": "Window", "type_label": construction_type}
#     sum_construction_data = {"total_area": wall_area + window_area,
#                              "orientation": orientation_label, "type": "Window and Wall", "type_label": construction_type}

#     return wall_construction_data, window_construction_data, sum_construction_data


ConstructionData = namedtuple("ConstructionData", ["wall", "window", "sum"])


def get_wall_construction_area_by_orientation(df: pd.DataFrame, construction_type: str, orientation: int) -> ConstructionData:
    valid_orientations = [0, 90, 180, 270]

    # check if the orientation is valid
    if orientation not in valid_orientations:
        raise ValueError(
            "Orientation must be one of the following: 0, 90, 180, 270. You entered: " + str(orientation))

    #   this returns a list of dictionaries of all the bodies
    all_bodies = df["proposed_results"]["bodies"]["bodies"]

    surfaces = []
    for body in all_bodies:
        surfaces.extend(body["surfaces"])

    # create a DataFrame from the surfaces list
    surfaces_df = pd.DataFrame(surfaces)

    # filter the DataFrame based on the construction type and orientation
    # this will return a new DataFrame with only the surfaces that match the construction type and orientation
    # it first checks if the key "o" is in the properties
    # then it checks if the construction type matches the construction type argument
    # then it checks if the orientation is within +- 10 degrees of the orientation argument
    filtered_df = surfaces_df[
        surfaces_df["properties"].apply(lambda x: "o" in x and x["ty"] == construction_type and (
            x["o"] >= orientation - 10) and (x["o"] <= orientation + 10))
    ]

    # get the wall area and window area
    # by applying a lambda function to the areas column
    # the lambda function checks if the key "ew" is in the areas dictionary
    # if it is, it returns the value of the key "ew"
    # if it is not, it returns 0
    # "en" means net envelope area
    # "ew" means window area
    wall_area = filtered_df["areas"].apply(lambda x: x["en"]).sum()
    window_area = filtered_df["areas"].apply(lambda x: x.get("ew", 0)).sum()

    orientation_label = {
        0: "North",
        90: "East",
        180: "South",
        270: "West"
    }.get(orientation, "Unknown")

    # create a ConstructionData namedtuple
    construction_data = ConstructionData(
        wall={
            "total_area": wall_area,
            "orientation": orientation_label,
            "type_label": construction_type
        },
        window={
            "total_area": window_area,
            "orientation": orientation_label,
            "type_label": construction_type
        },
        sum={
            "total_area": wall_area + window_area,
            "orientation": orientation_label,
            "type_label": construction_type
        }
    )

    return construction_data


def get_uVal_by_construction_category(df: pd.DataFrame, construction_category: str) -> List[Dict]:
    """ Get the U-Values for a given construction category from the JSON
        file and return a list of dictionaries. 
    Args:
        df (pd.DataFrame): .json file converted to a DataFrame
        construction_category (str): The construction category to filter by.

    Raises:
        ValueError: If the construction category is not one of the following:
        ext_glazing, wall, roof, partition.

    Returns:
        List[Dict]: A list of dictionaries containing the U-Values for the
        given construction category.
    """
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
