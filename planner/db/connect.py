import sqlite3 as sql
from pathlib import Path
from types import TracebackType

from planner.db import exceptions as exc


folder = Path.home() / '.expense-planner'
folder.mkdir(exist_ok=True)

file = folder / 'db.sqlite'


class _Connection:
    _connection: sql.Connection | None = None


    @property
    def connection(self) -> sql.Connection:
        if self._connection is None:
            raise exc.NoConnectionException
        return self._connection


    def __enter__(self) -> sql.Cursor:
        self._connection = sql.connect(file)
        return self.connection.cursor()


    def __exit__(
        self,
        type_: type[BaseException] | None,
        value: BaseException | None,
        traceback: TracebackType | None
    ) -> None:
        self.close()


    def commit(self) -> None:
        self.connection.commit()


    def close(self) -> None:
        self.connection.close()
        self._connection = None


connection = _Connection()
