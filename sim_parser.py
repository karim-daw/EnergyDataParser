import re
import pandas as pd
from pprint import pprint
from convert_units import convert_kwh_to_gj

sim_file_path = "data/JPL LEED Base 10 - Baseline Design.SIM"

# Read the .SIM file
with open(sim_file_path, 'r') as file:
    sim_data = file.read()

# Find the start and end indices of the desired table
start_title = "REPORT- PS-E Energy End-Use Summary for all Electric Meters                                 WEATHER FILE- Los Angeles  CA TMY2"

end_title = "REPORT- PS-E Energy End-Use Summary for all Fuel Meters                                     WEATHER FILE- Los Angeles  CA TMY2"

# Find the start and end indices of the desired table
start_index = sim_data.find(start_title)
end_index = sim_data.find(end_title)

# Extract the table data between the start and end indices
if start_index != -1 and end_index != -1:
    table_data = sim_data[start_index + len(start_title):end_index].strip()
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


# # Extract table values
# rows = table_data.split('\n')
# for row in rows:
#     values = re.findall(r'[\d.]+', row)
#     if values:
#         table_dict = {i: float(value) for i, value in enumerate(values)}
#         table_list.append(table_dict)

# # Create a DataFrame from the list of dictionaries
# df = pd.DataFrame(table_list)

# # Print the DataFrame
# print(df.head())
