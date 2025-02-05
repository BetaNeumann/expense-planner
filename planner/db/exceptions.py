class SqlException(Exception):
    pass


class NoConnectionException(SqlException):
    pass


class InvalidConfigurationException(SqlException):
    pass
