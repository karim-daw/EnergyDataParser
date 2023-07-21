from collections import namedtuple
from typing import NamedTuple

TableTitle = NamedTuple(
    "TableTitle", [('start_title', str), ('end_title', str)])

EnergyUsageHeader = NamedTuple(
    "EnergyUsageHeader", [('header_name', str), ('header_index', int)])

# Sample named tuple instances
TOTAL_ENERGY_ENDUSES_BY_FUELTYPE = TableTitle(
    start_title="Utility and Fuel Use Summary",
    end_title="Equipment Loads and Energy Use"
)
# Sample named tuple instances

TOTAL_ELECTRICTY_ENDUS_BY_SOURCE = TableTitle(
    start_title="Energy End-Use Summary for all Electric Meters",
    end_title="Energy End-Use Summary for all Fuel Meters"
)

# header indexes
LIGHTS = EnergyUsageHeader(header_name="LIGHTS", header_index=1)
MISC_ELECTRIC = EnergyUsageHeader(header_name="MISC_ELECTRIC", header_index=3)
SPACE_HEATING = EnergyUsageHeader(header_name="SPACE_HEATING", header_index=4)
SPACE_COOLING = EnergyUsageHeader(header_name="SPACE_COOLING", header_index=5)
PUMPS = EnergyUsageHeader(header_name="PUMPS", header_index=7)
VENTS_FANS = EnergyUsageHeader(header_name="VENTS_FANS", header_index=7)
DOMESTIC_HOT_WATER = EnergyUsageHeader(header_name="DOMESTIC_HOT_WATER", header_index=11)
EXTERNAL_EQUIPMENT = EnergyUsageHeader(header_name="EXTERNAL_EQUIPMENT", header_index=12)
