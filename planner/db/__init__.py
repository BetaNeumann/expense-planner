from planner.db.connect import connection as connection
from planner.db.table import *


with connection as cur:
    for table in all:
        cur.execute(table.sql)

    connection.commit()
