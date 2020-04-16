from dataclasses import dataclass
import marshmallow_dataclass


@dataclass
class Column:
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

    class Meta:
        ordered = True

    def __str__(self):
        """ The string representation."""
        return "Column [columnName=" + str(self.columnName) + ", tableName=" + str(
            self.tableName) + ", typeName=" + str(self.typeName) + ", size=" + str(
            self.size) + ", decimalDigits=" + str(self.decimalDigits) + ", radix=" + str(
            self.radix) + ", nullable=" + str(self.nullable) + ", remarks=" + str(
            self.remarks) + ", defaultValue=" + str(self.defaultValue) + ", charOctetLength=" + str(
            self.charOctetLength) + ", ordinalPosition=" + str(self.ordinalPosition) + ", isNullable=" + str(
            self.isNullable) + ", scopeCatalog=" + str(self.scopeCatalog) + ", scopeSchema=" + str(
            self.scopeSchema) + ", scopeTable=" + str(self.scopeTable) + ", sourceDataType=" + str(
            self.sourceDataType) + ", isAutoincrement=" + str(self.isAutoincrement) + "]"
