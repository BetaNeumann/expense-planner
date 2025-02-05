from planner.db.sql import Table


expense_type = Table("""--sql
    CREATE TABLE IF NOT EXISTS expense_type (
        id           INTEGER  PRIMARY KEY,
        description  TEXT     NOT NULL
    );
""")


expense = Table(f"""--sql
    CREATE TABLE IF NOT EXISTS expense (
        id       INTEGER        PRIMARY KEY,
        value    DECIMAL(10,2)  NOT NULL,
        type_id  INTEGER        NOT NULL,
        start    DATE           NOT NULL,
        end      DATE,

        FOREIGN KEY(type_id) REFERENCES {expense_type}(id)
    );
""")


all = [obj for obj in locals().values() if isinstance(obj, Table)]
