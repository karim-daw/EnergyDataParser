from bs4 import BeautifulSoup, SoupStrainer
from typing import List, Union, Dict


# def parse_html_table(file_path, table_names):
#     with open(file_path) as file:
#         # Parse only table tags and b tags
#         parse_only = SoupStrainer(['table', 'b'])
#         soup = BeautifulSoup(file, 'lxml', parse_only=parse_only)  # Use lxml parser cause its faster

#         # Initialize dictionary to store all table data
#         all_table_data = {}

#         for table_name in table_names:
#             # Find all b tags that contain the table names
#             table_tags = soup.find_all('b', string=table_name)

#             for table_tag in table_tags:
#                 # Find the table based on the table name
#                 table = table_tag.find_next('table')
#                 if table:
#                     # Find all row tags within the table
#                     rows = table.find_all('tr')

#                     # Find header cells in the first row
#                     header_cells = rows[0].find_all('td')
#                     headers = [cell.get_text(strip=True) for cell in header_cells]

#                     # Initialize table-specific data
#                     data = {}

#                     for row in rows[1:]:  # Skip the first row as it contains the headers
#                         cells = row.find_all('td')
#                         row_values = [cell.get_text(strip=True) for cell in cells]
#                         # Store the row values in the dictionary using the first cell as the key
#                         data[row_values[0]] = dict(zip(headers, row_values[1:]))

#                     # Store the table-specific data in the main dictionary
#                     all_table_data[table_name] = data
#                 else:
#                     print(f"No table found for '{table_name}'")

#         return all_table_data


# def extract_tables_by_names(text, table_names):

#     parse_only = SoupStrainer(['table', 'b'])
#     soup = BeautifulSoup(text, 'lxml', parse_only=parse_only)  # Use lxml parser cause its faster

#     # Initialize dictionary to store all table data
#     all_table_data = {}

#     for table_name in table_names:
#         # Find all b tags that contain the table names
#         table_tags = soup.find_all('b', string=table_name)

#         for table_tag in table_tags:
#             # Find the table based on the table name
#             table = table_tag.find_next('table')
#             if table:
#                 # Find all row tags within the table
#                 rows = table.find_all('tr')

#                 # Find header cells in the first row
#                 header_cells = rows[0].find_all('td')
#                 headers = [cell.get_text(strip=True) for cell in header_cells]

#                 # Initialize table-specific data
#                 data = {}

#                 for row in rows[1:]:  # Skip the first row as it contains the headers
#                     cells = row.find_all('td')
#                     row_values = [cell.get_text(strip=True) for cell in cells]
#                     # Store the row values in the dictionary using the first cell as the key
#                     data[row_values[0]] = dict(zip(headers, row_values[1:]))

#                 # Store the table-specific data in the main dictionary
#                 all_table_data[table_name] = data
#             else:
#                 print(f"No table found for '{table_name}'")

#     return all_table_data


def extract_table_by_name(text: str, table_name: str) -> Dict[str, Dict[str, str]]:

    parse_only = SoupStrainer(['table', 'b'])
    soup = BeautifulSoup(text, 'lxml', parse_only=parse_only)  # Use lxml parser cause its faster

    # Initialize dictionary to store all table data
    all_table_data = {}

    table_tags = soup.find_all('b', string=table_name)

    for table_tag in table_tags:
        # Find the table based on the table name
        table = table_tag.find_next('table')
        if table:
            # Find all row tags within the table
            rows = table.find_all('tr')

            # Find header cells in the first row
            header_cells = rows[0].find_all('td')
            headers = [cell.get_text(strip=True) for cell in header_cells]
            print("These are the headers: ", headers)

            # Initialize table-specific data
            data = {}

            for row in rows[1:]:  # Skip the first row as it contains the headers
                cells = row.find_all('td')
                row_values = [cell.get_text(strip=True) for cell in cells]
                # Store the row values in the dictionary using the first cell as the key
                data[row_values[0]] = dict(zip(headers, row_values[1:]))

            # Store the table-specific data in the main dictionary
            all_table_data[table_name] = data
            print("this is the data: ", data)
        else:
            print(f"No table found for '{table_name}'")

    return all_table_data
