#
# This file is part of AceQL Python Client SDK.
# AceQL Python Client SDK: Remote SQL access over HTTP with AceQL HTTP.
# Copyright (C) 2021,  KawanSoft SAS
# (http://www.kawansoft.com). All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##

from dataclasses import dataclass
from typing import Optional


@dataclass
class JdbcDatabaseMetaData:

    """
    Contains main SQL meta info sent by remote JDBC Driver. The info matches the DatabaseMetaData Java class [1] main values.
    [1]: https://docs.oracle.com/javase/8/docs/api/java/sql/DatabaseMetaData.html
    """
    getURL: Optional[str]
    isReadOnly: Optional[bool]
    allProceduresAreCallable: Optional[bool]
    allTablesAreSelectable: Optional[bool]
    getUserName: Optional[str]
    nullsAreSortedHigh: Optional[bool]
    nullsAreSortedLow: Optional[bool]
    nullsAreSortedAtStart: Optional[bool]
    nullsAreSortedAtEnd: Optional[bool]
    getDatabaseProductName: Optional[str]
    getDatabaseProductVersion: Optional[str]
    getDriverName: Optional[str]
    getDriverVersion: Optional[str]
    getDriverMajorVersion: Optional[int]
    getDriverMinorVersion: Optional[int]
    usesLocalFiles: Optional[bool]
    usesLocalFilePerTable: Optional[bool]
    supportsMixedCaseIdentifiers: Optional[bool]
    storesUpperCaseIdentifiers: Optional[bool]
    storesLowerCaseIdentifiers: Optional[bool]
    storesMixedCaseIdentifiers: Optional[bool]
    supportsMixedCaseQuotedIdentifiers: Optional[bool]
    storesUpperCaseQuotedIdentifiers: Optional[bool]
    storesLowerCaseQuotedIdentifiers: Optional[bool]
    storesMixedCaseQuotedIdentifiers: Optional[bool]
    getIdentifierQuoteString: Optional[str]
    getSQLKeywords: Optional[str]
    getNumericFunctions: Optional[str]
    getStringFunctions: Optional[str]
    getSystemFunctions: Optional[str]
    getTimeDateFunctions: Optional[str]
    getSearchStringEscape: Optional[str]
    getExtraNameCharacters: Optional[str]
    supportsAlterTableWithAddColumn: Optional[bool]
    supportsAlterTableWithDropColumn: Optional[bool]
    supportsColumnAliasing: Optional[bool]
    nullPlusNonNullIsNull: Optional[bool]
    supportsConvert: Optional[bool]
    supportsTableCorrelationNames: Optional[bool]
    supportsDifferentTableCorrelationNames: Optional[bool]
    supportsExpressionsInOrderBy: Optional[bool]
    supportsOrderByUnrelated: Optional[bool]
    supportsGroupBy: Optional[bool]
    supportsGroupByUnrelated: Optional[bool]
    supportsGroupByBeyondSelect: Optional[bool]
    supportsLikeEscapeClause: Optional[bool]
    supportsMultipleResultSets: Optional[bool]
    supportsMultipleTransactions: Optional[bool]
    supportsNonNullableColumns: Optional[bool]
    supportsMinimumSQLGrammar: Optional[bool]
    supportsCoreSQLGrammar: Optional[bool]
    supportsExtendedSQLGrammar: Optional[bool]
    supportsANSI92EntryLevelSQL: Optional[bool]
    supportsANSI92IntermediateSQL: Optional[bool]
    supportsANSI92FullSQL: Optional[bool]
    supportsIntegrityEnhancementFacility: Optional[bool]
    supportsOuterJoins: Optional[bool]
    supportsFullOuterJoins: Optional[bool]
    supportsLimitedOuterJoins: Optional[bool]
    getSchemaTerm: Optional[str]
    getProcedureTerm: Optional[str]
    getCatalogTerm: Optional[str]
    isCatalogAtStart: Optional[bool]
    getCatalogSeparator: Optional[str]
    supportsSchemasInDataManipulation: Optional[bool]
    supportsSchemasInProcedureCalls: Optional[bool]
    supportsSchemasInTableDefinitions: Optional[bool]
    supportsSchemasInIndexDefinitions: Optional[bool]
    supportsSchemasInPrivilegeDefinitions: Optional[bool]
    supportsCatalogsInDataManipulation: Optional[bool]
    supportsCatalogsInProcedureCalls: Optional[bool]
    supportsCatalogsInTableDefinitions: Optional[bool]
    supportsCatalogsInIndexDefinitions: Optional[bool]
    supportsCatalogsInPrivilegeDefinitions: Optional[bool]
    supportsPositionedDelete: Optional[bool]
    supportsPositionedUpdate: Optional[bool]
    supportsSelectForUpdate: Optional[bool]
    supportsStoredProcedures: Optional[bool]
    supportsSubqueriesInComparisons: Optional[bool]
    supportsSubqueriesInExists: Optional[bool]
    supportsSubqueriesInIns: Optional[bool]
    supportsSubqueriesInQuantifieds: Optional[bool]
    supportsCorrelatedSubqueries: Optional[bool]
    supportsUnion: Optional[bool]
    supportsUnionAll: Optional[bool]
    supportsOpenCursorsAcrossCommit: Optional[bool]
    supportsOpenCursorsAcrossRollback: Optional[bool]
    supportsOpenStatementsAcrossCommit: Optional[bool]
    supportsOpenStatementsAcrossRollback: Optional[bool]
    getMaxBinaryLiteralLength: Optional[int]
    getMaxCharLiteralLength: Optional[int]
    getMaxColumnNameLength: Optional[int]
    getMaxColumnsInGroupBy: Optional[int]
    getMaxColumnsInIndex: Optional[int]
    getMaxColumnsInOrderBy: Optional[int]
    getMaxColumnsInSelect: Optional[int]
    getMaxColumnsInTable: Optional[int]
    getMaxConnections: Optional[int]
    getMaxCursorNameLength: Optional[int]
    getMaxIndexLength: Optional[int]
    getMaxSchemaNameLength: Optional[int]
    getMaxProcedureNameLength: Optional[int]
    getMaxCatalogNameLength: Optional[int]
    getMaxRowSize: Optional[int]
    doesMaxRowSizeIncludeBlobs: Optional[bool]
    getMaxStatementLength: Optional[int]
    getMaxStatements: Optional[int]
    getMaxTableNameLength: Optional[int]
    getMaxTablesInSelect: Optional[int]
    getMaxUserNameLength: Optional[int]
    getDefaultTransactionIsolation: Optional[int]
    supportsTransactions: Optional[bool]
    supportsDataDefinitionAndDataManipulationTransactions: Optional[bool]
    supportsDataManipulationTransactionsOnly: Optional[bool]
    dataDefinitionCausesTransactionCommit: Optional[bool]
    dataDefinitionIgnoredInTransactions: Optional[bool]
    supportsBatchUpdates: Optional[bool]
    supportsSavepoints: Optional[bool]
    supportsNamedParameters: Optional[bool]
    supportsMultipleOpenResults: Optional[bool]
    supportsGetGeneratedKeys: Optional[bool]
    getDatabaseMajorVersion: Optional[int]
    getDatabaseMinorVersion: Optional[int]
    getJDBCMajorVersion: Optional[int]
    getJDBCMinorVersion: Optional[int]
    getSQLStateType: Optional[int]
    locatorsUpdateCopy: Optional[bool]
    supportsStatementPooling: Optional[bool]
    supportsStoredFunctionsUsingCallSyntax: Optional[bool]
    autoCommitFailureClosesAllResultSets: Optional[bool]
    getResultSetHoldability: Optional[int]

    class Meta:
        ordered = True

    def __str__(self):
        """ The string representation."""
        return "JdbcDatabaseMetaData [getURL=" + str(self.getURL) + ", isReadOnly=" + str(
            self.isReadOnly) + ", allProceduresAreCallable=" + str(
            self.allProceduresAreCallable) + ", allTablesAreSelectable=" + str(
            self.allTablesAreSelectable) + ", getUserName=" + str(self.getUserName) + ", nullsAreSortedHigh=" + str(
            self.nullsAreSortedHigh) + ", nullsAreSortedLow=" + str(
            self.nullsAreSortedLow) + ", nullsAreSortedAtStart=" + str(
            self.nullsAreSortedAtStart) + ", nullsAreSortedAtEnd=" + str(
            self.nullsAreSortedAtEnd) + ", getDatabaseProductName=" + str(
            self.getDatabaseProductName) + ", getDatabaseProductVersion=" + str(
            self.getDatabaseProductVersion) + ", getDriverName=" + str(
            self.getDriverName) + ", getDriverVersion=" + str(self.getDriverVersion) + ", getDriverMajorVersion=" + str(
            self.getDriverMajorVersion) + ", getDriverMinorVersion=" + str(
            self.getDriverMinorVersion) + ", usesLocalFiles=" + str(
            self.usesLocalFiles) + ", usesLocalFilePerTable=" + str(
            self.usesLocalFilePerTable) + ", supportsMixedCaseIdentifiers=" + str(
            self.supportsMixedCaseIdentifiers) + ", storesUpperCaseIdentifiers=" + str(
            self.storesUpperCaseIdentifiers) + ", storesLowerCaseIdentifiers=" + str(
            self.storesLowerCaseIdentifiers) + ", storesMixedCaseIdentifiers=" + str(
            self.storesMixedCaseIdentifiers) + ", supportsMixedCaseQuotedIdentifiers=" + str(
            self.supportsMixedCaseQuotedIdentifiers) + ", storesUpperCaseQuotedIdentifiers=" + str(
            self.storesUpperCaseQuotedIdentifiers) + ", storesLowerCaseQuotedIdentifiers=" + str(
            self.storesLowerCaseQuotedIdentifiers) + ", storesMixedCaseQuotedIdentifiers=" + str(
            self.storesMixedCaseQuotedIdentifiers) + ", getIdentifierQuoteString=" + str(
            self.getIdentifierQuoteString) + ", getSQLKeywords=" + str(
            self.getSQLKeywords) + ", getNumericFunctions=" + str(
            self.getNumericFunctions) + ", getStringFunctions=" + str(
            self.getStringFunctions) + ", getSystemFunctions=" + str(
            self.getSystemFunctions) + ", getTimeDateFunctions=" + str(
            self.getTimeDateFunctions) + ", getSearchStringEscape=" + str(
            self.getSearchStringEscape) + ", getExtraNameCharacters=" + str(
            self.getExtraNameCharacters) + ", supportsAlterTableWithAddColumn=" + str(
            self.supportsAlterTableWithAddColumn) + ", supportsAlterTableWithDropColumn=" + str(
            self.supportsAlterTableWithDropColumn) + ", supportsColumnAliasing=" + str(
            self.supportsColumnAliasing) + ", nullPlusNonNullIsNull=" + str(
            self.nullPlusNonNullIsNull) + ", supportsConvert=" + str(
            self.supportsConvert) + ", supportsTableCorrelationNames=" + str(
            self.supportsTableCorrelationNames) + ", supportsDifferentTableCorrelationNames=" + str(
            self.supportsDifferentTableCorrelationNames) + ", supportsExpressionsInOrderBy=" + str(
            self.supportsExpressionsInOrderBy) + ", supportsOrderByUnrelated=" + str(
            self.supportsOrderByUnrelated) + ", supportsGroupBy=" + str(
            self.supportsGroupBy) + ", supportsGroupByUnrelated=" + str(
            self.supportsGroupByUnrelated) + ", supportsGroupByBeyondSelect=" + str(
            self.supportsGroupByBeyondSelect) + ", supportsLikeEscapeClause=" + str(
            self.supportsLikeEscapeClause) + ", supportsMultipleResultSets=" + str(
            self.supportsMultipleResultSets) + ", supportsMultipleTransactions=" + str(
            self.supportsMultipleTransactions) + ", supportsNonNullableColumns=" + str(
            self.supportsNonNullableColumns) + ", supportsMinimumSQLGrammar=" + str(
            self.supportsMinimumSQLGrammar) + ", supportsCoreSQLGrammar=" + str(
            self.supportsCoreSQLGrammar) + ", supportsExtendedSQLGrammar=" + str(
            self.supportsExtendedSQLGrammar) + ", supportsANSI92EntryLevelSQL=" + str(
            self.supportsANSI92EntryLevelSQL) + ", supportsANSI92IntermediateSQL=" + str(
            self.supportsANSI92IntermediateSQL) + ", supportsANSI92FullSQL=" + str(
            self.supportsANSI92FullSQL) + ", supportsIntegrityEnhancementFacility=" + str(
            self.supportsIntegrityEnhancementFacility) + ", supportsOuterJoins=" + str(
            self.supportsOuterJoins) + ", supportsFullOuterJoins=" + str(
            self.supportsFullOuterJoins) + ", supportsLimitedOuterJoins=" + str(
            self.supportsLimitedOuterJoins) + ", getSchemaTerm=" + str(
            self.getSchemaTerm) + ", getProcedureTerm=" + str(self.getProcedureTerm) + ", getCatalogTerm=" + str(
            self.getCatalogTerm) + ", isCatalogAtStart=" + str(self.isCatalogAtStart) + ", getCatalogSeparator=" + str(
            self.getCatalogSeparator) + ", supportsSchemasInDataManipulation=" + str(
            self.supportsSchemasInDataManipulation) + ", supportsSchemasInProcedureCalls=" + str(
            self.supportsSchemasInProcedureCalls) + ", supportsSchemasInTableDefinitions=" + str(
            self.supportsSchemasInTableDefinitions) + ", supportsSchemasInIndexDefinitions=" + str(
            self.supportsSchemasInIndexDefinitions) + ", supportsSchemasInPrivilegeDefinitions=" + str(
            self.supportsSchemasInPrivilegeDefinitions) + ", supportsCatalogsInDataManipulation=" + str(
            self.supportsCatalogsInDataManipulation) + ", supportsCatalogsInProcedureCalls=" + str(
            self.supportsCatalogsInProcedureCalls) + ", supportsCatalogsInTableDefinitions=" + str(
            self.supportsCatalogsInTableDefinitions) + ", supportsCatalogsInIndexDefinitions=" + str(
            self.supportsCatalogsInIndexDefinitions) + ", supportsCatalogsInPrivilegeDefinitions=" + str(
            self.supportsCatalogsInPrivilegeDefinitions) + ", supportsPositionedDelete=" + str(
            self.supportsPositionedDelete) + ", supportsPositionedUpdate=" + str(
            self.supportsPositionedUpdate) + ", supportsSelectForUpdate=" + str(
            self.supportsSelectForUpdate) + ", supportsStoredProcedures=" + str(
            self.supportsStoredProcedures) + ", supportsSubqueriesInComparisons=" + str(
            self.supportsSubqueriesInComparisons) + ", supportsSubqueriesInExists=" + str(
            self.supportsSubqueriesInExists) + ", supportsSubqueriesInIns=" + str(
            self.supportsSubqueriesInIns) + ", supportsSubqueriesInQuantifieds=" + str(
            self.supportsSubqueriesInQuantifieds) + ", supportsCorrelatedSubqueries=" + str(
            self.supportsCorrelatedSubqueries) + ", supportsUnion=" + str(
            self.supportsUnion) + ", supportsUnionAll=" + str(
            self.supportsUnionAll) + ", supportsOpenCursorsAcrossCommit=" + str(
            self.supportsOpenCursorsAcrossCommit) + ", supportsOpenCursorsAcrossRollback=" + str(
            self.supportsOpenCursorsAcrossRollback) + ", supportsOpenStatementsAcrossCommit=" + str(
            self.supportsOpenStatementsAcrossCommit) + ", supportsOpenStatementsAcrossRollback=" + str(
            self.supportsOpenStatementsAcrossRollback) + ", getMaxBinaryLiteralLength=" + str(
            self.getMaxBinaryLiteralLength) + ", getMaxCharLiteralLength=" + str(
            self.getMaxCharLiteralLength) + ", getMaxColumnNameLength=" + str(
            self.getMaxColumnNameLength) + ", getMaxColumnsInGroupBy=" + str(
            self.getMaxColumnsInGroupBy) + ", getMaxColumnsInIndex=" + str(
            self.getMaxColumnsInIndex) + ", getMaxColumnsInOrderBy=" + str(
            self.getMaxColumnsInOrderBy) + ", getMaxColumnsInSelect=" + str(
            self.getMaxColumnsInSelect) + ", getMaxColumnsInTable=" + str(
            self.getMaxColumnsInTable) + ", getMaxConnections=" + str(
            self.getMaxConnections) + ", getMaxCursorNameLength=" + str(
            self.getMaxCursorNameLength) + ", getMaxIndexLength=" + str(
            self.getMaxIndexLength) + ", getMaxSchemaNameLength=" + str(
            self.getMaxSchemaNameLength) + ", getMaxProcedureNameLength=" + str(
            self.getMaxProcedureNameLength) + ", getMaxCatalogNameLength=" + str(
            self.getMaxCatalogNameLength) + ", getMaxRowSize=" + str(
            self.getMaxRowSize) + ", doesMaxRowSizeIncludeBlobs=" + str(
            self.doesMaxRowSizeIncludeBlobs) + ", getMaxStatementLength=" + str(
            self.getMaxStatementLength) + ", getMaxStatements=" + str(
            self.getMaxStatements) + ", getMaxTableNameLength=" + str(
            self.getMaxTableNameLength) + ", getMaxTablesInSelect=" + str(
            self.getMaxTablesInSelect) + ", getMaxUserNameLength=" + str(
            self.getMaxUserNameLength) + ", getDefaultTransactionIsolation=" + str(
            self.getDefaultTransactionIsolation) + ", supportsTransactions=" + str(
            self.supportsTransactions) + ", supportsDataDefinitionAndDataManipulationTransactions=" + str(
            self.supportsDataDefinitionAndDataManipulationTransactions) + ", supportsDataManipulationTransactionsOnly=" + str(
            self.supportsDataManipulationTransactionsOnly) + ", dataDefinitionCausesTransactionCommit=" + str(
            self.dataDefinitionCausesTransactionCommit) + ", dataDefinitionIgnoredInTransactions=" + str(
            self.dataDefinitionIgnoredInTransactions) + ", supportsBatchUpdates=" + str(
            self.supportsBatchUpdates) + ", supportsSavepoints=" + str(
            self.supportsSavepoints) + ", supportsNamedParameters=" + str(
            self.supportsNamedParameters) + ", supportsMultipleOpenResults=" + str(
            self.supportsMultipleOpenResults) + ", supportsGetGeneratedKeys=" + str(
            self.supportsGetGeneratedKeys) + ", getDatabaseMajorVersion=" + str(
            self.getDatabaseMajorVersion) + ", getDatabaseMinorVersion=" + str(
            self.getDatabaseMinorVersion) + ", getJDBCMajorVersion=" + str(
            self.getJDBCMajorVersion) + ", getJDBCMinorVersion=" + str(
            self.getJDBCMinorVersion) + ", getSQLStateType=" + str(
            self.getSQLStateType) + ", locatorsUpdateCopy=" + str(
            self.locatorsUpdateCopy) + ", supportsStatementPooling=" + str(
            self.supportsStatementPooling) + ", supportsStoredFunctionsUsingCallSyntax=" + str(
            self.supportsStoredFunctionsUsingCallSyntax) + ", autoCommitFailureClosesAllResultSets=" + str(
            self.autoCommitFailureClosesAllResultSets) + ", getResultSetHoldability=" + str(
            self.getResultSetHoldability) + "]"
