import pandas as pd
import json

json_file_path = "data/EC.d Export 2023_01_17_Visa_LEED [both].json"

# Read JSON file
with open(json_file_path) as f:
    data = json.load(f)

# Convert the JSON data to a DataFrame
df = pd.json_normalize(data['reference_results']['aps_stats'])


########### areas and volumes #############
# getting room sizes from data
area = df['sizes.area'].iloc[0]
volume = df['sizes.volume'].iloc[0]
rooms = df['sizes.rooms'].iloc[0]

sizes = " Area: {}\n Volume: {}\n Rooms: {}\n".format(area, volume, rooms)

print(sizes)
