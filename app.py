
import csv
from bs4 import BeautifulSoup, SoupStrainer
import lxml


def parse_html_table(file_path, table_name):
    with open(file_path) as file:
        # Parse only table tags and b tags
        parse_only = SoupStrainer(['table', 'b'])
        soup = BeautifulSoup(
            file, 'lxml', parse_only=parse_only)  # Use lxml parser

        values = {}
        table_tag = soup.find('b', string=table_name)
        if table_tag:
            # Find the table based on the table name
            table = table_tag.find_next('table')
            if table:
                # Find all row tags within the table
                rows = table.find_all('tr')

                # Find header cells in the first row
                header_cells = rows[0].find_all('td')
                headers = [cell.get_text(strip=True) for cell in header_cells]

                for row in rows:
                    cells = row.find_all('td')
                    row_values = [cell.get_text(strip=True) for cell in cells]
                    # Store the row values in the dictionary using the first cell as the key
                    values[row_values[0]] = row_values[1:]
        else:
            print("No b tag found")

        return values, headers


def write_table_to_csv(output_file, table_name, values, headers):
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Write table name as a header
        writer.writerow(['Table Name:', table_name])

        # Write header row
        writer.writerow(headers)

        # Write data rows
        for key, row_values in values.items():
            writer.writerow([key] + row_values)

    print(f"Table information written to '{output_file}'")


# Usage example
html_file_path = 'data/Energy Models_EnergyPlus.htm'
table_name = 'Site and Source Energy'
output_csv_file = 'output.csv'
parsed_values, header_row = parse_html_table(html_file_path, table_name)
write_table_to_csv(output_csv_file, table_name, parsed_values, header_row)
