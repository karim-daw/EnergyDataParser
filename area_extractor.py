import pandas as pd
from typing import List, Dict


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


def get_wall_uVal_by_orientation(df: pd.DataFrame, construction_type: str, orientation: int):

    all_bodies = df["proposed_results"]["bodies"]
    total_wall_uVal = 0
    total_window_uVal = 0

    pass
