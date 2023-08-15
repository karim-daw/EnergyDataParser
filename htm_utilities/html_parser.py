import htm_table_title_keys as httks


def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def get_building_size_data(text):
    pass
    # return httks.get_data_from_table(text, httks.BUILDING_AREA)
