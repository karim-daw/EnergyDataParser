# EnergyDataParser

This Python code provides functionality to parse an EnergyPlus HTML table, extract data from it, and write the data to a CSV file. The code consists of several modules for different tasks.

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

3. Run the app.py file:
   ```shell
   python app.py
   ```
