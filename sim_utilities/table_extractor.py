import re
from typing import NamedTuple
import pandas as pd
from pprint import pprint
from convert_units import convert_kwh_to_gj
from . import table_title_keys as ttks


# function that given a .sim file and a table title, returns a list of values
def get_totals_from_table(file: str, table: ttks.TableTitle):
    # Read the .SIM file
    with open(file, 'r') as file:
        sim_data = file.read()

    # Find the start and end indices of the desired table
    start_index = sim_data.find(table.start_title)
    end_index = sim_data.find(table.end_title)

    print("start index: ", start_index)
    print("end index: ", end_index)

    # Extract the table data between the start and end indices
    if start_index != -1 and end_index != -1:
        table_data = sim_data[start_index +
                              len(table.start_title):end_index].strip()
    else:
        table_data = ''

    # Initialize the list of dictionaries
    table_list = []
    print("hello")
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
