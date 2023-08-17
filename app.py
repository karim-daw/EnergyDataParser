import os
from json_utilities.json_parser import *
from sim_utilities.sim_parser import *
from htm_utilities.htm_parser import *

from general_utilities.csv_writer import write_table_to_csv
from general_utilities.file_utils import generate_unique_filename


# # testing htm parser
# htm_file_path = 'data_in/Energy Models_EnergyPlus.htm'
# parse_htm_file(htm_file_path)

# # testing json parser
# json_file_path = 'data_in/EC.d Export Pfizer_LEED_R1 [both].json'
# parse_json_file(json_file_path)

# testing sim parser
# sim_file_path = 'data_in/JPL LEED Base 10 - Baseline Design.SIM'
# parse_sim_file(sim_file_path)

# create menu with pile path selection or cancel
# if cancel, exit program
# if file path, check if file exists
# if file exists, check file extension
# if file extension is json, parse json file
# if file extension is sim, parse sim file
# if file extension is htm, parse htm file
# if file extension is not supported, display error message


# while loop to get user input
while True:

    # welcome message
    print()
    print("==================================================")
    print("Welcome to the Energy Model Parser!")
    print("==================================================")
    print()

    # menu for going to file path or exiting program
    print("1. Proceed to the parser")
    print("2. Exit program")
    print()

    # get user input for menu
    menu_input = input("Enter menu option: ")

    # check if user input is 1
    if menu_input == "1":
        print()
        print("Proceeding to the parser...")
        print("==================================================")
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
                print("Parsing json file...")
                parse_json_file(file_path)
            elif file_extension == ".SIM":
                print("Parsing sim file...")
                parse_sim_file(file_path)
            elif file_extension == ".htm":
                print("Parsing htm file...")
                parse_htm_file(file_path)
            else:
                print("File type is not supported")

    # check if user input is 2
    elif menu_input == "2":
        print()
        print("Exiting program")
        break
