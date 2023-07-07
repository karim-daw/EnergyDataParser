import csv


def write_table_to_csv(output_file, table_names, values, headers):
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        for table_name in table_names:

            # Write table name as a header
            writer.writerow(['Table Name:', table_name])

            # Write header row
            writer.writerow(headers)

            # Write data rows
            for key, row_values in values.items():
                writer.writerow([key] + row_values)

    print(f"Table information written to '{output_file}'")
