# ./helpers/mssql.py
from pyodbc import connect, Row # type: ignore
from typing import Any, Callable

# DATABASE parameters
DRIVER: str = "" # {SQL Server Native Client 11.0}
SERVER: str = "" # 192.168.11.19
DB: str = "" # w86md
USER: str = "" # sa
PASS: str = "" # z
Connection: str = f"Driver={DRIVER}; Server={SERVER}; Database={DB}; Uid={USER}; pwd={PASS}; Trusted_connection=Yes"

def mssql(function: Callable[..., str]) -> Callable[..., list[dict[str, Any]]]:
    # returning query with multiple row results
    def query(*args) -> list[dict[str, Any]]:
        command: str = function(*args)

        with connect(Connection).cursor() as mssql:
            mssql.execute(command)

            keys: list[str] = [row[0] for row in mssql.description]
            vals: list[Row] = [row for row in mssql.fetchall()]

            rslt: list[dict[str, Any]] = [{key: val for key, val in zip(keys, row)} for row in vals]
            
        return rslt
    return query

def msrow(function: Callable[..., str]) -> Callable[..., dict[str, Any]]:
    # returning query with only one row result
    def query(*args) -> dict[str, Any]:
        command: str = function(*args)

        with connect(Connection).cursor() as mssql:
            mssql.execute(command)

            keys: list[str] = [row[0] for row in mssql.description]
            vals: list[Row] = [row for row in mssql.fetchall()]

            rslt: list[dict[str, Any]] = [{key: val for key, val in zip(keys, row)} for row in vals]

        return rslt[0]
    return query