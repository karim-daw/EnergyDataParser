import re
from typing import NamedTuple
import pandas as pd
from pprint import pprint
from convert_units import convert_kwh_to_gj
from . import table_title_keys as ttks


# function that given a .sim file and a table title, returns a list of values
def get_totals_from_table(text, table: ttks.TableTitle):

    # Find the start and end indices of the desired table
    start_index = text.find(table.start_title)
    end_index = text.find(table.end_title)

    print("start index: ", start_index)
    print("end index: ", end_index)

    # Extract the table data between the start and end indices
    if start_index != -1 and end_index != -1:
        table_data = text[start_index +
                          len(table.start_title):end_index].strip()
    else:
        table_data = ''

    # Initialize the list of dictionaries
    table_list = []
    print(table_data)

    # delimit string by new line
    rows = table_data.split('\n')
    # strip empty lines
    rows = [row for row in rows if row.strip()]

    for i in range(len(rows)-10, len(rows)):
        row = rows[i]
        # check if he row contains the word "KWH"
        if "KWH" in row:
            # delimit by spaces
            values = row.split()
            # print the first two values

            # convert the last value from kwh to gj
            usage_elec_light = convert_kwh_to_gj(float(values[1]))
            usage_elec_misc = convert_kwh_to_gj(float(values[3]))
            usage_elec_total = convert_kwh_to_gj(float(values[-1]))
            print("Lighting: ", usage_elec_light)
            print("Misc: ", usage_elec_misc)
            print("Total: ", usage_elec_total)


def extract_table_between_keywords(text, table_pattern: ttks.TableTitle) -> str:
    # Define the regex patterns for the start and end keywords
    start_pattern = re.escape(table_pattern.start_title)
    end_pattern = re.escape(table_pattern.end_title)

    # Construct the combined regex pattern with optional whitespace characters
    combined_pattern = rf'{start_pattern}\s*(.*?)\s*{end_pattern}'

    # Use re.DOTALL flag to allow matching across multiple lines
    match = re.search(combined_pattern, text, re.DOTALL)

    if match:
        # Extract the matched table_pattern content
        table = match.group(1)
        table.strip()
        # delimit string by new line
        return table

    else:
        # If either or both keywords are not found, return None or handle it as you see fit.
        return None


# find the total usage by fuel type from a table represented as a string
def find_total_usage_by_fuel_type(table: str):
    rows = table.split('\n')
    # strip empty lines
    rows = [row for row in rows if row.strip()]

    for i in range(len(rows)-10, len(rows)):
        row = rows[i]
        # check if he row contains the word "KWH"
        if "KWH" in row:
            # delimit by spaces
            values = row.split()
            # print the first two values

            usage_elec_total = convert_kwh_to_gj(float(values[-1]))
            print("Total Electricy Usage [kWH]: ", usage_elec_total)
            continue

        if "THERM" in row:
            # delimit by spaces
            values = row.split()
            # print the first two values

            usage_nat_gas_total = convert_kwh_to_gj(float(values[-1]))
            print("Total Natural Gas Usage [kWH]: ", usage_nat_gas_total)
            break


# get the total usage by fuel type from a table represented as a string
def get_total_usage_by_fuel_type(text, desired_data):
    table = extract_table_between_keywords(text, desired_data)
    find_total_usage_by_fuel_type(table)


def get_data(text, desired_data):
    print("desired data: ", desired_data)
    if desired_data == ttks.ENERGY_ENDUSES_BY_FUELTYPE:
        get_total_usage_by_fuel_type(text, desired_data)
