from dataclasses import dataclass
import marshmallow_dataclass


@dataclass
class Column:
    catalog: str
    schema: str
    columnName: str
    tableName: str
    typeName: str
    size: int
    decimalDigits: int
    radix: int
    nullable: str
    remarks: str
    defaultValue: str
    charOctetLength: int
    ordinalPosition: int
    isNullable: str
    scopeCatalog: str
    scopeSchema: str
    scopeTable: str
    sourceDataType: int
    isAutoincrement: str


def __str__(self):
    """ The string representation."""
    return str(self.columnName) + ", " + str(self.tableName) + ", " + str(self.typeName) + ", " + str(self.size) + ", " + str(self.decimalDigits) + ", " + str(self.radix) + ", " + str(self.nullable) + ", " + str(self.remarks) + ", " + str(self.defaultValue) + ", " + str(self.charOctetLength) + ", " + str(self.ordinalPosition) + ", " + str(self.isNullable) + ", " + str(self.scopeCatalog) + ", " + str(self.scopeSchema) + ", " + str(self.scopeTable) + ", " + str(self.sourceDataType) + ", " + str(self.isAutoincrement)
