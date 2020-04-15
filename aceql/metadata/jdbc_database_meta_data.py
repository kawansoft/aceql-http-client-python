from dataclasses import dataclass
import marshmallow_dataclass


@dataclass
class JdbcDatabaseMetaData(object):
    getURL: str
    isReadOnly: bool
    allProceduresAreCallable: bool
    allTablesAreSelectable: bool
    getUserName: str
    nullsAreSortedHigh: bool
    nullsAreSortedLow: bool
    nullsAreSortedAtStart: bool
    nullsAreSortedAtEnd: bool
    getDatabaseProductName: str
    getDatabaseProductVersion: str
    getDriverName: str
    getDriverVersion: str
    getDriverMajorVersion: int
    getDriverMinorVersion: int
    usesLocalFiles: bool
    usesLocalFilePerTable: bool
    supportsMixedCaseIdentifiers: bool
    storesUpperCaseIdentifiers: bool
    storesLowerCaseIdentifiers: bool
    storesMixedCaseIdentifiers: bool
    supportsMixedCaseQuotedIdentifiers: bool
    storesUpperCaseQuotedIdentifiers: bool
    storesLowerCaseQuotedIdentifiers: bool
    storesMixedCaseQuotedIdentifiers: bool
    getIdentifierQuoteString: str
    getSQLKeywords: str
    getNumericFunctions: str
    getStringFunctions: str
    getSystemFunctions: str
    getTimeDateFunctions: str
    getSearchStringEscape: str
    getExtraNameCharacters: str
    supportsAlterTableWithAddColumn: bool
    supportsAlterTableWithDropColumn: bool
    supportsColumnAliasing: bool
    nullPlusNonNullIsNull: bool
    supportsConvert: bool
    supportsTableCorrelationNames: bool
    supportsDifferentTableCorrelationNames: bool
    supportsExpressionsInOrderBy: bool
    supportsOrderByUnrelated: bool
    supportsGroupBy: bool
    supportsGroupByUnrelated: bool
    supportsGroupByBeyondSelect: bool
    supportsLikeEscapeClause: bool
    supportsMultipleResultSets: bool
    supportsMultipleTransactions: bool
    supportsNonNullableColumns: bool
    supportsMinimumSQLGrammar: bool
    supportsCoreSQLGrammar: bool
    supportsExtendedSQLGrammar: bool
    supportsANSI92EntryLevelSQL: bool
    supportsANSI92IntermediateSQL: bool
    supportsANSI92FullSQL: bool
    supportsIntegrityEnhancementFacility: bool
    supportsOuterJoins: bool
    supportsFullOuterJoins: bool
    supportsLimitedOuterJoins: bool
    getSchemaTerm: str
    getProcedureTerm: str
    getCatalogTerm: str
    isCatalogAtStart: bool
    getCatalogSeparator: str
    supportsSchemasInDataManipulation: bool
    supportsSchemasInProcedureCalls: bool
    supportsSchemasInTableDefinitions: bool
    supportsSchemasInIndexDefinitions: bool
    supportsSchemasInPrivilegeDefinitions: bool
    supportsCatalogsInDataManipulation: bool
    supportsCatalogsInProcedureCalls: bool
    supportsCatalogsInTableDefinitions: bool
    supportsCatalogsInIndexDefinitions: bool
    supportsCatalogsInPrivilegeDefinitions: bool
    supportsPositionedDelete: bool
    supportsPositionedUpdate: bool
    supportsSelectForUpdate: bool
    supportsStoredProcedures: bool
    supportsSubqueriesInComparisons: bool
    supportsSubqueriesInExists: bool
    supportsSubqueriesInIns: bool
    supportsSubqueriesInQuantifieds: bool
    supportsCorrelatedSubqueries: bool
    supportsUnion: bool
    supportsUnionAll: bool
    supportsOpenCursorsAcrossCommit: bool
    supportsOpenCursorsAcrossRollback: bool
    supportsOpenStatementsAcrossCommit: bool
    supportsOpenStatementsAcrossRollback: bool
    getMaxBinaryLiteralLength: int
    getMaxCharLiteralLength: int
    getMaxColumnNameLength: int
    getMaxColumnsInGroupBy: int
    getMaxColumnsInIndex: int
    getMaxColumnsInOrderBy: int
    getMaxColumnsInSelect: int
    getMaxColumnsInTable: int
    getMaxConnections: int
    getMaxCursorNameLength: int
    getMaxIndexLength: int
    getMaxSchemaNameLength: int
    getMaxProcedureNameLength: int
    getMaxCatalogNameLength: int
    getMaxRowSize: int
    doesMaxRowSizeIncludeBlobs: bool
    getMaxStatementLength: int
    getMaxStatements: int
    getMaxTableNameLength: int
    getMaxTablesInSelect: int
    getMaxUserNameLength: int
    getDefaultTransactionIsolation: int
    supportsTransactions: bool
    supportsDataDefinitionAndDataManipulationTransactions: bool
    supportsDataManipulationTransactionsOnly: bool
    dataDefinitionCausesTransactionCommit: bool
    dataDefinitionIgnoredInTransactions: bool
    supportsBatchUpdates: bool
    supportsSavepoints: bool
    supportsNamedParameters: bool
    supportsMultipleOpenResults: bool
    supportsGetGeneratedKeys: bool
    getDatabaseMajorVersion: int
    getDatabaseMinorVersion: int
    getJDBCMajorVersion: int
    getJDBCMinorVersion: int
    getSQLStateType: int
    locatorsUpdateCopy: bool
    supportsStatementPooling: bool
    supportsStoredFunctionsUsingCallSyntax: bool
    autoCommitFailureClosesAllResultSets: bool
    getResultSetHoldability: int

    class Meta:
        ordered = True


def get_getResultSetHoldability(self):
    return self.getResultSetHoldability

@dataclass
class HolderJdbcDatabaseMetaData(object):
    status: str
    jdbcDatabaseMetaData: JdbcDatabaseMetaData

    class Meta:
        ordered = True


def __str__(self):
    """ The string representation."""
    return str(self.status) + ", " + str(self.getURL) + ", " + str(self.isReadOnly) + ", " + str(self.allProceduresAreCallable) + ", " + str(
        self.allTablesAreSelectable) + ", " + str(self.getUserName) + ", " + str(self.nullsAreSortedHigh) + ", " + str(
        self.nullsAreSortedLow) + ", " + str(self.nullsAreSortedAtStart) + ", " + str(
        self.nullsAreSortedAtEnd) + ", " + str(self.getDatabaseProductName) + ", " + str(
        self.getDatabaseProductVersion) + ", " + str(self.getDriverName) + ", " + str(
        self.getDriverVersion) + ", " + str(self.getDriverMajorVersion) + ", " + str(
        self.getDriverMinorVersion) + ", " + str(self.usesLocalFiles) + ", " + str(
        self.usesLocalFilePerTable) + ", " + str(self.supportsMixedCaseIdentifiers) + ", " + str(
        self.storesUpperCaseIdentifiers) + ", " + str(self.storesLowerCaseIdentifiers) + ", " + str(
        self.storesMixedCaseIdentifiers) + ", " + str(self.supportsMixedCaseQuotedIdentifiers) + ", " + str(
        self.storesUpperCaseQuotedIdentifiers) + ", " + str(self.storesLowerCaseQuotedIdentifiers) + ", " + str(
        self.storesMixedCaseQuotedIdentifiers) + ", " + str(self.getIdentifierQuoteString) + ", " + str(
        self.getSQLKeywords) + ", " + str(self.getNumericFunctions) + ", " + str(self.getStringFunctions) + ", " + str(
        self.getSystemFunctions) + ", " + str(self.getTimeDateFunctions) + ", " + str(
        self.getSearchStringEscape) + ", " + str(self.getExtraNameCharacters) + ", " + str(
        self.supportsAlterTableWithAddColumn) + ", " + str(self.supportsAlterTableWithDropColumn) + ", " + str(
        self.supportsColumnAliasing) + ", " + str(self.nullPlusNonNullIsNull) + ", " + str(
        self.supportsConvert) + ", " + str(self.supportsTableCorrelationNames) + ", " + str(
        self.supportsDifferentTableCorrelationNames) + ", " + str(self.supportsExpressionsInOrderBy) + ", " + str(
        self.supportsOrderByUnrelated) + ", " + str(self.supportsGroupBy) + ", " + str(
        self.supportsGroupByUnrelated) + ", " + str(self.supportsGroupByBeyondSelect) + ", " + str(
        self.supportsLikeEscapeClause) + ", " + str(self.supportsMultipleResultSets) + ", " + str(
        self.supportsMultipleTransactions) + ", " + str(self.supportsNonNullableColumns) + ", " + str(
        self.supportsMinimumSQLGrammar) + ", " + str(self.supportsCoreSQLGrammar) + ", " + str(
        self.supportsExtendedSQLGrammar) + ", " + str(self.supportsANSI92EntryLevelSQL) + ", " + str(
        self.supportsANSI92IntermediateSQL) + ", " + str(self.supportsANSI92FullSQL) + ", " + str(
        self.supportsIntegrityEnhancementFacility) + ", " + str(self.supportsOuterJoins) + ", " + str(
        self.supportsFullOuterJoins) + ", " + str(self.supportsLimitedOuterJoins) + ", " + str(
        self.getSchemaTerm) + ", " + str(self.getProcedureTerm) + ", " + str(self.getCatalogTerm) + ", " + str(
        self.isCatalogAtStart) + ", " + str(self.getCatalogSeparator) + ", " + str(
        self.supportsSchemasInDataManipulation) + ", " + str(self.supportsSchemasInProcedureCalls) + ", " + str(
        self.supportsSchemasInTableDefinitions) + ", " + str(self.supportsSchemasInIndexDefinitions) + ", " + str(
        self.supportsSchemasInPrivilegeDefinitions) + ", " + str(self.supportsCatalogsInDataManipulation) + ", " + str(
        self.supportsCatalogsInProcedureCalls) + ", " + str(self.supportsCatalogsInTableDefinitions) + ", " + str(
        self.supportsCatalogsInIndexDefinitions) + ", " + str(self.supportsCatalogsInPrivilegeDefinitions) + ", " + str(
        self.supportsPositionedDelete) + ", " + str(self.supportsPositionedUpdate) + ", " + str(
        self.supportsSelectForUpdate) + ", " + str(self.supportsStoredProcedures) + ", " + str(
        self.supportsSubqueriesInComparisons) + ", " + str(self.supportsSubqueriesInExists) + ", " + str(
        self.supportsSubqueriesInIns) + ", " + str(self.supportsSubqueriesInQuantifieds) + ", " + str(
        self.supportsCorrelatedSubqueries) + ", " + str(self.supportsUnion) + ", " + str(
        self.supportsUnionAll) + ", " + str(self.supportsOpenCursorsAcrossCommit) + ", " + str(
        self.supportsOpenCursorsAcrossRollback) + ", " + str(self.supportsOpenStatementsAcrossCommit) + ", " + str(
        self.supportsOpenStatementsAcrossRollback) + ", " + str(self.getMaxBinaryLiteralLength) + ", " + str(
        self.getMaxCharLiteralLength) + ", " + str(self.getMaxColumnNameLength) + ", " + str(
        self.getMaxColumnsInGroupBy) + ", " + str(self.getMaxColumnsInIndex) + ", " + str(
        self.getMaxColumnsInOrderBy) + ", " + str(self.getMaxColumnsInSelect) + ", " + str(
        self.getMaxColumnsInTable) + ", " + str(self.getMaxConnections) + ", " + str(
        self.getMaxCursorNameLength) + ", " + str(self.getMaxIndexLength) + ", " + str(
        self.getMaxSchemaNameLength) + ", " + str(self.getMaxProcedureNameLength) + ", " + str(
        self.getMaxCatalogNameLength) + ", " + str(self.getMaxRowSize) + ", " + str(
        self.doesMaxRowSizeIncludeBlobs) + ", " + str(self.getMaxStatementLength) + ", " + str(
        self.getMaxStatements) + ", " + str(self.getMaxTableNameLength) + ", " + str(
        self.getMaxTablesInSelect) + ", " + str(self.getMaxUserNameLength) + ", " + str(
        self.getDefaultTransactionIsolation) + ", " + str(self.supportsTransactions) + ", " + str(
        self.supportsDataDefinitionAndDataManipulationTransactions) + ", " + str(
        self.supportsDataManipulationTransactionsOnly) + ", " + str(
        self.dataDefinitionCausesTransactionCommit) + ", " + str(self.dataDefinitionIgnoredInTransactions) + ", " + str(
        self.supportsBatchUpdates) + ", " + str(self.supportsSavepoints) + ", " + str(
        self.supportsNamedParameters) + ", " + str(self.supportsMultipleOpenResults) + ", " + str(
        self.supportsGetGeneratedKeys) + ", " + str(self.getDatabaseMajorVersion) + ", " + str(
        self.getDatabaseMinorVersion) + ", " + str(self.getJDBCMajorVersion) + ", " + str(
        self.getJDBCMinorVersion) + ", " + str(self.getSQLStateType) + ", " + str(self.locatorsUpdateCopy) + ", " + str(
        self.supportsStatementPooling) + ", " + str(self.supportsStoredFunctionsUsingCallSyntax) + ", " + str(
        self.autoCommitFailureClosesAllResultSets) + ", " + str(self.getResultSetHoldability)
