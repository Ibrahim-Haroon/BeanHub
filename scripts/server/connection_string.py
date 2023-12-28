import pandas as pd
from os import path


def connection_string() -> str:
    """

    @rtype: str
    @return: connection string for PostgreSQL
    """
    db_info_file_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other", "database-info.csv")

    df = pd.read_csv(db_info_file_path)
    row = df.iloc[0]

    dsn = f"dbname={row['dbname']} user={row['user']} password={row['password']} host={row['host']} port={row['port']}"

    return dsn
