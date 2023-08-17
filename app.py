import os
from json_utilities.json_parser import *
from sim_utilities.sim_parser import *
from htm_utilities.htm_parser import *

from general_utilities.csv_writer import write_table_to_csv
from general_utilities.file_utils import generate_unique_filename


# testing htm parser
# htm_file_path = 'data_in/Energy Models_EnergyPlus.htm'
# parse_htm_file(htm_file_path)


# while loop to get user input
while True:
    # get user input for file path
    file_path = input("Enter the file path: ")

    # check if file exists
    if not os.path.isfile(file_path):
        print("File does not exist")
    else:
        print("File exists")

        # get file extension
        file_extension = os.path.splitext(file_path)[1]

        # parse file based on extension
        if file_extension == ".json":
            parse_json_file(file_path)
        elif file_extension == ".SIM":
            parse_sim_file(file_path)
        elif file_extension == ".htm":
            print("Parsing htm file...")
            parse_htm_file(file_path)
        else:
            print("File type is not supported")


# # get file extension
# file_extension = os.path.splitext(file_path)[1]

# # parse file based on extension
# if file_extension == ".json":
#     parse_json_file(file_path)
# elif file_extension == ".SIM":
#     parse_sim_file(file_path)
# elif file_extension == ".htm":
#     parse_htm_file(file_path)


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
