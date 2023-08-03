from pprint import pprint
from sim_utilities import table_extractor as te
from sim_utilities import line_extractor as le
from sim_utilities import table_title_keys as ttks
from sim_utilities import line_title_keys as ltk


def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def display_building_size_data(text):
    print("\nGetting building size data...")
    print(le.extract_data_from_line(text, ltk.BUILDING_SIZE_TOTALS))
    print(le.extract_data_from_line(text, ltk.BUILING_NUMBER_OF_SPACES))


def display_energy_data(text):
    print("\nGetting energy data...")
    te.get_data(text, ttks.TOTAL_ENERGY_ENDUSES_BY_FUELTYPE)
    te.get_data(text, ttks.TOTAL_ELECTRICTY_ENDUS_BY_SOURCE, source=ttks.LIGHTS)
    te.get_data(text, ttks.TOTAL_ELECTRICTY_ENDUS_BY_SOURCE, source=ttks.MISC_ELECTRIC)
    te.get_data(text, ttks.TOTAL_ELECTRICTY_ENDUS_BY_SOURCE, source=ttks.SPACE_HEATING)
    te.get_data(text, ttks.TOTAL_ELECTRICTY_ENDUS_BY_SOURCE, source=ttks.SPACE_COOLING)
    te.get_data(text, ttks.TOTAL_ELECTRICTY_ENDUS_BY_SOURCE, source=ttks.PUMPS)
    te.get_data(text, ttks.TOTAL_ELECTRICTY_ENDUS_BY_SOURCE, source=ttks.VENTS_FANS)
    te.get_data(text, ttks.TOTAL_ELECTRICTY_ENDUS_BY_SOURCE, source=ttks.DOMESTIC_HOT_WATER)
    te.get_data(text, ttks.TOTAL_ELECTRICTY_ENDUS_BY_SOURCE, source=ttks.EXTERNAL_EQUIPMENT)


def parse_sim_file(file_path):
    text = read_text_file(file_path)
    display_building_size_data(text)
    display_energy_data(text)
