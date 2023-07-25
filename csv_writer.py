import csv


def write_table_to_csv(output_file, table_data):
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        for table_name, data in table_data.items():
            # Write table name as a header
            writer.writerow(['Table Name:', table_name])

            # Write header row
            headers = list(data[list(data.keys())[0]].keys())
            writer.writerow([''] + headers)

            # Write data rows
            for key, row_values in data.items():
                writer.writerow([key] + list(row_values.values()))

    print(f"Table information written to '{output_file}'")
