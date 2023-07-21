from collections import namedtuple
from typing import NamedTuple

TableTitle = NamedTuple(
    "TableTitle", [('start_title', str), ('end_title', str)])

# Sample named tuple instances
ELECTRICAL_ENERGY_ENDUSES = TableTitle(
    start_title="REPORT- PS-E Energy End-Use Summary for all Electric Meters                                 WEATHER FILE- Los Angeles  CA TMY2",
    end_title="REPORT- PS-E Energy End-Use Summary for all Fuel Meters                                     WEATHER FILE- Los Angeles  CA TMY2"
)

BUILDING_SIZE_TOTALS = TableTitle(
    start_title="BUILDING TOTALS",
    end_title="---------------------------------------------------------------------------------------------------------------------------------"
)
