from collections import namedtuple
from typing import NamedTuple

TableTitle = NamedTuple(
    "TableTitle", [('start_title', str), ('end_title', str)])

# Sample named tuple instances
ENERGY_ENDUSES_BY_FUELTYPE = TableTitle(
    start_title="Utility and Fuel Use Summary",
    end_title="Equipment Loads and Energy Use"
)
