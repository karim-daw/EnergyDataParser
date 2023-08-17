from pprint import pprint
from sim_utilities import sim_table_extractor as te
from sim_utilities import sim_line_extractor as sle
from sim_utilities import sim_table_title_keys as sttks
from sim_utilities import sim_line_title_keys as ltk


def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def display_building_size_data(text):
    print("\nGetting building size data...")
    print(sle.extract_data_from_line(text, ltk.BUILDING_SIZE_TOTALS))
    print(sle.extract_data_from_line(text, ltk.BUILING_NUMBER_OF_SPACES))


def display_energy_data(text):
    print("\nGetting energy data...")
    te.get_data_from_table(text, sttks.TOTAL_ENERGY_ENDUSES_BY_FUELTYPE)
    te.get_data_from_table(text, sttks.TOTAL_ELECTRICTY_ENDUS_BY_SOURCE, source=sttks.LIGHTS)
    te.get_data_from_table(text, sttks.TOTAL_ELECTRICTY_ENDUS_BY_SOURCE, source=sttks.MISC_ELECTRIC)
    te.get_data_from_table(text, sttks.TOTAL_ELECTRICTY_ENDUS_BY_SOURCE, source=sttks.SPACE_HEATING)
    te.get_data_from_table(text, sttks.TOTAL_ELECTRICTY_ENDUS_BY_SOURCE, source=sttks.SPACE_COOLING)
    te.get_data_from_table(text, sttks.TOTAL_ELECTRICTY_ENDUS_BY_SOURCE, source=sttks.PUMPS)
    te.get_data_from_table(text, sttks.TOTAL_ELECTRICTY_ENDUS_BY_SOURCE, source=sttks.VENTS_FANS)
    te.get_data_from_table(text, sttks.TOTAL_ELECTRICTY_ENDUS_BY_SOURCE, source=sttks.DOMESTIC_HOT_WATER)
    te.get_data_from_table(text, sttks.TOTAL_ELECTRICTY_ENDUS_BY_SOURCE, source=sttks.EXTERNAL_EQUIPMENT)


def parse_sim_file(file_path):
    text = read_text_file(file_path)
    display_building_size_data(text)
    display_energy_data(text)
