from bs4 import BeautifulSoup, SoupStrainer


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
