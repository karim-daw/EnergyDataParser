# EnergyDataParser

This Python code provides functionality to parse an EnergyPlus HTML table, an IES .json file and an eQuest .SIM file extract data from it. The code consists of several modules for different tasks but the main files have \*\_parser.py as a postfix. The app.py will eventually be a kind of "client" where you can use the vairous parsers

## Installation

1. Clone the repository or download the code files.

2. Set up a virtual environment (optional but recommended):

   ```shell
   # Create a new virtual environment
   python -m venv energydataparser-venv

   # Activate the virtual environment
   # On Windows
   energydataparser-venv\Scripts\activate.bat
   # On macOS/Linux
   source energydataparser-venv/bin/activate
   ```

3. Install the dependencies from the provided requirements.txt file:
   ```shell
   pip install -r requirements.txt
   ```

## Usage STILL WIP

1. Place the EnergyPlus .htm, IES .json, and/or eQuest .SIM file you want to parse in the the `data_in` folder as thats where the scripts will be pointed to to recieve the input files.

2. Run the app.py file if you want a preview on how to extract the .htm data:

   ```shell
   python app.py
   ```

This will display a simple menu where you can enter the file path to the the file you want to parse. The output will be printed in your console.

```
==================================================
Welcome to the Energy Model Parser!
==================================================

1. Proceed to the parser
2. Exit program

```

```
Enter menu option: 1

Proceeding to the parser...
==================================================
Enter the file path:
```

```
Enter the file path: C:\Users\43310\source\repos\EnergyDataParser\data_in\JPL LEED Base 10 - Baseline Design.SIM
File exists
Parsing sim file...

Getting building size data...
[994.2, 85981.9, 1514489.2]
[109.0, 76.0, 33.0]

Getting energy data...
Total Electricy Usage [KWH]:  4041652.0
Total Electricy Usage [GJ]:  14549.947199999999
Total Natural Gas Usage [KWH]:  1379448.708
Total Natural Gas Usage [GJ]:  4966.0153488000005
Total Electricity Usage for LIGHTS [KWH]: 377708.0
Total Electricity Usage for LIGHTS [GJ]: 1359.7488
Total Electricity Usage for MISC_ELECTRIC [KWH]: 1435014.0
Total Electricity Usage for MISC_ELECTRIC [GJ]: 5166.0504
Total Electricity Usage for SPACE_HEATING [KWH]: 2718.0
Total Electricity Usage for SPACE_HEATING [GJ]: 9.7848
Total Electricity Usage for SPACE_COOLING [KWH]: 743543.0
Total Electricity Usage for SPACE_COOLING [GJ]: 2676.7547999999997
Total Electricity Usage for PUMPS [KWH]: 199356.0
Total Electricity Usage for PUMPS [GJ]: 717.6816
Total Electricity Usage for VENTS_FANS [KWH]: 199356.0
Total Electricity Usage for VENTS_FANS [GJ]: 717.6816
Total Electricity Usage for DOMESTIC_HOT_WATER [KWH]: 0.0
Total Electricity Usage for DOMESTIC_HOT_WATER [GJ]: 0.0
Total Electricity Usage for EXTERNAL_EQUIPMENT [KWH]: 22516.0
Total Electricity Usage for EXTERNAL_EQUIPMENT [GJ]: 81.0576

==================================================
Welcome to the Energy Model Parser!
==================================================

1. Proceed to the parser
2. Exit program

Enter menu option:

```
