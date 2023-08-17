from htm_utilities import htm_table_extractor as hte
from htm_utilities import htm_table_title_keys as httks
from pprint import pprint


def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def display_building_size_data(text):
    print("\nGetting building size data...")
    pprint(hte.extract_table_by_name(text, httks.BUILDING_AREA))


def display_energy_data(text):
    print("\nGetting energy data...")
    pprint(hte.extract_table_by_name(text, httks.SITE_AND_SOURCE_ENERGY))


def display_envelope_data(text):
    print("\nGetting envelope data...")
    pprint(hte.extract_table_by_name(text, httks.OPAQUE_EXTERIOR))
    pprint(hte.extract_table_by_name(text, httks.EXTERIOR_FENESTRATION))


def parse_htm_file(file_path):
    text = read_text_file(file_path)
    display_building_size_data(text)
    display_energy_data(text)
    display_envelope_data(text)
