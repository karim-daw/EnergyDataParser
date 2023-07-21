import re
import pandas as pd
from pprint import pprint
from convert_units import convert_kwh_to_gj
from sim_utilities import table_extractor as te
from sim_utilities import table_title_keys as ttks
from sim_utilities import line_title_keys as ltk


sim_file_path = "data/JPL LEED Base 10 - Baseline Design.SIM"


# get the total electrical energy use from the table
# te.get_totals_from_table(sim_file_path, ttks.ELECTRICAL_ENERGY_ENDUSES)
print(te.extract_data_from_line_in_file(
    sim_file_path, ltk.BUILING_NUMBER_OF_SPACES))
print(te.extract_data_from_line_in_file(
    sim_file_path, ltk.BUILDING_SIZE_TOTALS))
