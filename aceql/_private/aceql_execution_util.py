class AceQLExecutionUtil(object):
    """Utilities for SQL execution """

    @staticmethod
    def check_values(is_prepared_statement: bool, sql: str):
        if sql is None:
            raise TypeError("sql is null!")
        if is_prepared_statement is None:
            raise TypeError("isPreparedStatement is null!")