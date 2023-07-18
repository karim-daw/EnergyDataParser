# EnergyDataParser

This Python code provides functionality to parse an EnergyPlus HTML table, an IES .json file and an eQuest .SIM file extract data from it. The code consists of several modules for different tasks but the main files have \*\_parser.py as a postfix. The app.py will eventually be a kind of "client" where you can use the vairous parsers

## Installation

1. Clone the repository or download the code files.

2. Set up a virtual environment (optional but recommended):

   ```shell
   # Create a new virtual environment
   python -m venv energyplus-parser-venv

   # Activate the virtual environment
   # On Windows
   energyplus-parser-venv\Scripts\activate.bat
   # On macOS/Linux
   source energyplus-parser-venv/bin/activate
   ```

3. Install the dependencies from the provided requirements.txt file:
   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Place the EnergyPlus HTML file you want to parse in the same directory as the code files.

2. Open the `app.py` file and update the following variables:

   - `html_file_path`: Set this variable to the path of your EnergyPlus HTML file.
   - `table_name`: Set this variable to the name of the table you want to parse.
   - `folder_path`: Set this variable to the path of the folder where you want to save the CSV output file.
   - `output_csv_file_name`: Set this variable to the desired name of the CSV output file.

3. Run the app.py file if you want a preview on how to extract the .htm data:

   ```shell
   python app.py
   ```

   For now if you are testing, try running for the progress on the IES data extractor:

   ```shell
   python json_parser.py
   ```
