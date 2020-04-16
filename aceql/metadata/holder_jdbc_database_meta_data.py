from dataclasses import dataclass
import marshmallow_dataclass

from aceql.metadata.jdbc_database_meta_data import JdbcDatabaseMetaData


@dataclass
class HolderJdbcDatabaseMetaData(object):
    status: str
    jdbcDatabaseMetaData: JdbcDatabaseMetaData

    class Meta:
        ordered = True

    def __str__(self):
        """ The string representation."""
        return str(self.status) + ", " + str(self.jdbcDatabaseMetaData)

