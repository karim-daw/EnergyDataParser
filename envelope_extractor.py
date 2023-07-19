from collections import namedtuple
import pandas as pd
from typing import List, Dict, NamedTuple
from pprint import pprint
from pandas import DataFrame
import numpy as np

#  named tuples
ConstructionAreas = namedtuple("ConstructionAreas", ["wall", "window", "sum"])
ConstructionAreasByNameAndOrientatoin = namedtuple("ConstructionAreasByNameAndOrientatoin", ["construction_category", "orientation", "total_area","construction_name"])
ConstructionUValues = namedtuple("ConstructionUValues", [
    "construction_name", "reference", "type", "u_value", "g_values"])


def get_wall_construction_area_by_orientation(df: pd.DataFrame, construction_type: str, orientation: int) -> ConstructionAreas:
    """ Get the wall area and window area for a given construction type 
        and orientation from the JSON file and return a ConstructionAreas namedtuple.
        The namedtuple contains the wall area, window area, and the sum of the wall 
        and window area.

    Args:
        df (pd.DataFrame): .json file converted to a DataFrame
        construction_type (str): The construction type to filter by.
        orientation (int): The orientation to filter by in degrees as an integer.

    Raises:
        ValueError: If the construction type is not one of the following:
        ext_glazing, wall, roof, partition. If the orientation is not one of the following:


    Returns:
        ConstructionAreas:  A namedtuple containing the wall area, window area,
        and the sum of the wall and window area.
    """

    # create a list of valid construction types
    valid_construction_types = ["Wall", "Partition"]

    # check if the construction type is valid
    if construction_type not in valid_construction_types:
        raise ValueError(
            "Construction type must be one of the following: Wall, Partition. You entered: " + construction_type)

    # create a list of valid orientations
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
    # if it is, it returns the value of the key "ew" if it is not, it returns 0
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

    # create a ConstructionAreas namedtuple
    construction_area = ConstructionAreas(
        wall={
            "name": "wall",
            "orientation": orientation_label,
            "total_area": wall_area,
            "type_label": construction_type
        },
        window={
            "name": "window",
            "orientation": orientation_label,
            "total_area": window_area,
            "type_label": construction_type
        },
        sum={
            "name": "sum",
            "orientation": orientation_label,
            "total_area": wall_area + window_area,
            "type_label": construction_type
        }
    )

    return construction_area


def get_wall_area_by_construction_name_and_orientation(df: pd.DataFrame, construction_name: str, orientation: int):
    
    all_constructions  = df["proposed_results"]["bodies"]["constructions"]
    
    construction_keys = all_constructions.keys()
    # the valid construction keys have valid categories below
    valid_categories = ["ext_glazing", "wall"]
    # filter construction keys by valid categories
    valid_construction_keys = [key for key in construction_keys if all_constructions[key]["category"] in valid_categories]


    # check if the construction type is valid
    if construction_name not in valid_construction_keys:
        raise ValueError("Construction name must be one of: " + str(valid_construction_keys) + "you entered " + construction_name)

    # create a list of valid orientations
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
        surfaces_df.apply(
            lambda row: "o" in row["properties"] 
            and row["properties"]["ty"] == "Wall" 
            and (row["properties"]["o"] >= orientation - 10)
            and (row["properties"]["o"] <= orientation + 10)
            and construction_name in row["constructions"], axis=1)
    ]

    # get the wall area and window area
    # by applying a lambda function to the areas column
    # the lambda function checks if the key "ew" is in the areas dictionary
    # if it is, it returns the value of the key "ew" if it is not, it returns 0
    # "en" means net envelope area
    # "ew" means window area
    construction_category = all_constructions[construction_name]["category"]
    
    if(construction_category == "wall"):
        area = filtered_df["areas"].apply(
            lambda x: x["en"]).sum()
    elif(construction_category == "ext_glazing"):
        area = filtered_df["areas"].apply(
            lambda x: x.get("ew", 0)).sum()
    else:
        raise ValueError("Construction category must be one of: " + str(valid_construction_keys) + "you entered " + construction_name)

    orientation_label = {
        0: "North",
        90: "East",
        180: "South",
        270: "West"
    }.get(orientation, "Unknown")

    # create a ConstructionAreas namedtuple
    construction_area_by_name_orientation = ConstructionAreasByNameAndOrientatoin(

            construction_category = construction_category,
            orientation = orientation_label,
            total_area = area,
            construction_name = construction_name

    )

    return construction_area_by_name_orientation

    

def get_uVal_by_construction_category(df: pd.DataFrame, construction_category: str) -> List[NamedTuple]:
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

    # create a ConstructionUValues namedtuple
    uValues_by_construction_category = []
    for row in uValues_df.itertuples(index=False):
        construction_uValues = ConstructionUValues(
            construction_name=row.construction_name,
            reference=row.reference,
            type=row.type,
            u_value=row.u_value,
            g_values=row.g_values  # this is a dictionary
        )

        uValues_by_construction_category.append(construction_uValues)

    return uValues_by_construction_category


def get_uVal_by_construction_name(df: pd.DataFrame, construction_name: str) -> Dict:
    all_constructions  = df["proposed_results"]["bodies"]["constructions"]
    
    construction_keys = all_constructions.keys()
    
    construction_uValue = {}
    
    # for each construction get the u value
    for construction_key in construction_keys:
        # if the construction name matches the construction name argument
        if construction_key == construction_name:
            # get the u value
            construction_data = all_constructions[construction_key]
            u_value = construction_data["u_value"]
            construction_category = construction_data["category"]

            # create a ConstructionUValues dict
            construction_uValue = {
                "construction_name": construction_name,
                "construction_category":construction_category,
                "u_value": u_value}
            break


    return construction_uValue
        
        



def get_uVal_by_orientation(df: pd.DataFrame, construction_type: str):
    construction_areas = {}  # Dictionary to accumulate the total area by identifier

    all_bodies = df["proposed_results"]["bodies"]["bodies"]

    orientation_mapping = {
        (0, 10): 0,
        (80, 100): 90,
        (170, 190): 180,
        (260, 280): 270
    }

    for body in all_bodies:
        body_surfaces = body["surfaces"]

        for surface in body_surfaces:
            properties = surface.get("properties", {})
            areas = surface.get("areas", {})
            if "o" in properties and properties["ty"] == construction_type:
                construction_names = surface["constructions"]
                orientation = properties["o"]

                for construction_name in construction_names:
                    for orientation_range, mapped_orientation in orientation_mapping.items():
                        if orientation_range[0] <= orientation <= orientation_range[1]:
                            orientation = mapped_orientation
                            break
                    else:
                        orientation = "Orientation not found"

                    combination = (construction_type, construction_name, orientation)
                    uVal_data = get_uVal_by_construction_name(df, construction_name)
                    uVal = uVal_data["u_value"]
                    construction_category = uVal_data["construction_category"]

                    # Getting area by construction name and orientation
                    if construction_category == "wall":
                        area = areas.get("en", 0)
                    elif construction_category == "ext_glazing":
                        area = areas.get("ew", 0)

                    # Combine dictionaries with the same identifier and accumulate the area
                    if combination in construction_areas:
                        construction_areas[combination]["total_area"] += area
                    else:
                        orientation_labels = {
                            0: "North",
                            90: "East",
                            180: "South",
                            270: "West"
                        }
                        orientation_label = orientation_labels.get(orientation, "Unknown")

                        construction_uValue_by_orientation = {
                            "construction_name": construction_name,
                            "construction_category": construction_category,
                            "u_value": uVal,
                            "orientation": orientation_label,
                            "total_area": area
                        }
                        construction_areas[combination] = construction_uValue_by_orientation

    # Retrieve the combined dictionaries from the lookup table
    all_constructions_uValues_by_orientation = list(construction_areas.values())

    return all_constructions_uValues_by_orientation



def compute_weighted_average(data):
    orientation_u_values = {}
    orientations = np.array([entry['orientation'] for entry in data if entry['construction_category'] not in ['partition', 'int_glazing']])
    areas = np.array([entry['total_area'] for entry in data if entry['construction_category'] not in ['partition', 'int_glazing']])
    u_values = np.array([entry['u_value'] for entry in data if entry['construction_category'] not in ['partition', 'int_glazing']])

    unique_orientations = np.unique(orientations)

    for orientation in unique_orientations:
        mask = orientations == orientation
        orientation_areas = areas[mask]
        orientation_u_vals = u_values[mask]
        weighted_avg = np.average(orientation_u_vals, weights=orientation_areas)
        orientation_u_values[orientation] = weighted_avg

    return orientation_u_values







                
                
