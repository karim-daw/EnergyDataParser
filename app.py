import os
from htm_utilities.html_parser import parse_html_table
from json_utilities.json_parser import *
from sim_utilities.sim_parser import *

from general_utilities.csv_writer import write_table_to_csv
from general_utilities.file_utils import generate_unique_filename


# get user input for file path
file_path = input("Enter the file path: ")

# check if file exists
if not os.path.isfile(file_path):
    print("File does not exist")
    exit()

# get file extension
file_extension = os.path.splitext(file_path)[1]

# parse file based on extension
if file_extension == ".json":
    parse_json_file(file_path)
elif file_extension == ".SIM":
    parse_sim_file(file_path)


# Usage example
# name of the html file to parse
# html_file_path = 'data/Energy Models_EnergyPlus.htm'

# # names of the tables to parse
# table_names = ['Site and Source Energy', 'Building Area', "End Uses", "Opaque Exterior", "Exterior Fenestration",]

# # output file path
# folder_path = 'out/'
# output_csv_file_name = 'output.csv'
# output_path = os.path.join(folder_path, output_csv_file_name)

# # Enumerate file if it exists
# output_csv_file = generate_unique_filename(folder_path, output_csv_file_name)

# # get table data
# table_data = parse_html_table(html_file_path, table_names)

# # output to csv
# write_table_to_csv(output_path, table_data)
