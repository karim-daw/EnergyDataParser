import re

# private function that given a string and a pattern, returns a list of values


def __extract_data_from_line(text, pattern):

    # Search for the pattern in the text
    match = re.search(pattern, text)

    if match:
        # Extract the captured groups (numbers) from the match
        values = [float(val) for val in match.groups()]
        return values
    else:
        # If no match is found, return None or handle it as you see fit.
        return None


def extract_data_from_line_in_file(file_path, desired_data):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Use the existing function to extract the values
    return __extract_data_from_line(text, desired_data)
