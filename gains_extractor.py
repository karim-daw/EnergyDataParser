import pandas as pd
from typing import List, Dict
from convert_units import convert_kwh_to_gj, convert_wh_to_kwh


def get_gains_source_name(df: pd.DataFrame) -> List[str]:
    gains_source_name = df["proposed_results"]["gains"]
    return list(gains_source_name.keys())


def get_gains_source_amount(df: pd.DataFrame, gain_name: str) -> float:
    """get the gains source of the json file in gj\n"""

    if gain_name not in get_gains_source_name(df):
        return 0

    return df["proposed_results"]["gains"][gain_name]
