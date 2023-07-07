import os
from html_parser import parse_html_table
from csv_writer import write_table_to_csv
from file_utils import generate_unique_filename

# Usage example
html_file_path = 'data/Energy Models_EnergyPlus.htm'
table_name = 'Site and Source Energy'
folder_path = 'out/'
output_csv_file_name = 'output.csv'

# Enumerate file if it exists
output_csv_file = generate_unique_filename(folder_path, output_csv_file_name)

parsed_values, header_row = parse_html_table(html_file_path, table_name)
write_table_to_csv(os.path.join(folder_path, output_csv_file),
                   table_name, parsed_values, header_row)
