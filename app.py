
import csv
from bs4 import BeautifulSoup, SoupStrainer
import lxml
import os


def parseHtmlTable(filePath, table_name):
    with open(filePath) as file:
        # Parse only table tags and b tags
        parseOnly = SoupStrainer(['table', 'b'])
        soup = BeautifulSoup(
            file, 'lxml', parse_only=parseOnly)  # Use lxml parser

        values = {}
        tableTag = soup.find('b', string=table_name)
        if tableTag:
            # Find the table based on the table name
            table = tableTag.find_next('table')
            if table:
                # Find all row tags within the table
                rows = table.find_all('tr')

                # Find header cells in the first row
                headerCells = rows[0].find_all('td')
                headers = [cell.get_text(strip=True) for cell in headerCells]

                for row in rows:
                    cells = row.find_all('td')
                    rowValues = [cell.get_text(strip=True) for cell in cells]
                    # Store the row values in the dictionary using the first cell as the key
                    values[rowValues[0]] = rowValues[1:]
        else:
            print("No b tag found")

        return values, headers


def writeTableToCsv(output_file, table_name, values, headers):
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


def generateUniqueFilename(folderPath, baseFilename):
    suffix = 1
    fileName = baseFilename
    fileExt = os.path.splitext(baseFilename)[1]

    # If a file with the same name already exists in the folder, generate a new filename with a numeric suffix
    while os.path.exists(os.path.join(folderPath, fileName)):
        fileName = f"{os.path.splitext(baseFilename)[0]}_{suffix}{fileExt}"
        suffix += 1
    return fileName


# Usage example
htmlFilePath = 'data/Energy Models_EnergyPlus.htm'
tableName = 'Site and Source Energy'
folderPath = 'out/'
outputCSVFileName = 'output.csv'

# enumerate file if it exists
outputCSVFile = generateUniqueFilename(folderPath, outputCSVFileName)

parsedValues, headerRow = parseHtmlTable(htmlFilePath, tableName)
writeTableToCsv(folderPath+outputCSVFile, tableName, parsedValues, headerRow)
