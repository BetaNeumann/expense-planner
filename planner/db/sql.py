import re

from datetime import datetime, date
from decimal import Decimal

from planner.db import exceptions as exc


TYPE_MAP: dict[type, str] = {
    int: 'INTEGER',
    float: 'REAL',
    str: 'TEXT',
    bytes: 'BLOB',
    datetime: 'VARCHAR(19)',
    date: 'VARCHAR(10)',
    Decimal: 'DECIMAL(10,2)',
}

table_name_pattern = re.compile(r'CREATE TABLE (?:IF NOT EXISTS )?([\w_]+) \(')


class Table:
    name: str
    sql: str


    def __init__(self, sql: str) -> None:
        self.sql = sql
        
        match = table_name_pattern.search(self.sql)
        if match is None:
            raise exc.InvalidConfigurationException('Invalid table creation syntax')

        self.name = match.group(1)


    def __str__(self) -> str:
        return self.name
    
    
    def __repr__(self) -> str:
        return f'Table({self})'


    def __getattr__(self, name: str) -> str:
        return f'{self.name}.{name}'
