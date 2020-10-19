from src.exceptions import ExceptionCodes, VlanException
import pandas as pd


def check_not_empty(value):
    if value is None:
        raise VlanException(ExceptionCodes.NoneValue)
    
    if isinstance(value, str):
        if not value.strip():
            raise VlanException(ExceptionCodes.EmptyValue)

    if (type(value) is list) and (not value):
        raise VlanException(ExceptionCodes.NoRedundantVlans)

    return True


def validate_dataframe(value):
    if value is None:
        raise VlanException(ExceptionCodes.NoneValue, "vlan dataframe")
    
    if isinstance(value, pd.DataFrame) and value.empty:
        raise VlanException(ExceptionCodes.EmptyVlanDataframe)
    
    if isinstance(value, str):
        if not value.strip():
            raise VlanException(ExceptionCodes.EmptyValue, "vlan dataframe")

    if (type(value) is list) and (not value):
        raise VlanException(ExceptionCodes.EmptyList, "vlan dataframe")

    return True
