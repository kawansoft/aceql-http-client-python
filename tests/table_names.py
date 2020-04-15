class TableNames(object):
    def __init__(self, status, tableNames):
        self.status = status
        self.tableNames = tableNames

    def __repr__(self):
        """ The string representation."""
        return self.status + ", " + str(self.tableNames)