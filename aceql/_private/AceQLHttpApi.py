#
# This file is part of AceQL Python Client SDK.
# AceQL Python Client SDK: Remote SQL access over HTTP with AceQL HTTP.
# Copyright (C) 2017,  KawanSoft SAS
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

import requests
from aceql._private.ResultAnalyzer import *
from aceql._private.ResultSetInfo import *
from aceql._private.RowCounter import *
from aceql._private.StreamResultAnalyzer import *
from requests_toolbelt.multipart import encoder

from aceql.Error import *
from aceql._private.FileUtil import *
from aceql._private.VersionValues import *


# from builtins import int


class AceQLHttpApi(object):
    """ AceQL HTTP wrapper for all apis. Takes care of all
	HTTP calls and operations."""

    __trace_on = False
    __stateless = False
    __timeout = 0

    def __init__(self, serverUrl, database, username, password, proxies=None):

        if serverUrl is None:
            raise TypeError("serverUrl is null!")
        if database is None:
            raise TypeError("database is null!")
        if username is None:
            raise TypeError("username is null!")
        if password is None:
            raise TypeError("password is null!")

        self.__database = database
        self.__username = username
        self.__password = password
        self.__proxies = proxies

        self.__http_status_code = requests.codes.ok

        # Other self for other methods
        self._prettyPrinting = True
        self._gzipResult = False
        self._temp_length = 0
        self.__total_length = 0

        url = serverUrl + "/database/" + database + "/username/" \
              + username + "/connect" + "?password=" \
              + password + "&stateless=" + str(AceQLHttpApi.__stateless)

        try:
            result = self.callWithGetUrl(url)
            resultAnalyzer = ResultAnalyzer(result, self.__http_status_code)
            if not resultAnalyzer.isStatusOk():
                raise Error(resultAnalyzer.getErrorMessage(),
                            resultAnalyzer.getErrorId(), None, None, self.__http_status_code)

            sessionId = resultAnalyzer.getValue("session_id")
            self._url = serverUrl + "/session/" + sessionId + "/"

        except Exception as e:
            if type(e) == Error:
                raise
            else:
                raise Error(str(e), 0, e, None, self.__http_status_code)

    # *
    # * Says if session is stateless.
    # *
    # * @return {@code true} if session is stateless, else {@code false}.
    #
    def isStateless():
        return AceQLHttpApi.__stateless

    isStateless = staticmethod(isStateless)

    # *
    # * Sets the session mode
    # *
    # * @param stateless
    # * if true, the session will be stateless, else stateful.
    #
    def setStateless(theStateless):
        if theStateless is None:
            raise TypeError("stateless is null!")
        if str(theStateless) == "True":
            AceQLHttpApi.__stateless = True
        else:
            AceQLHttpApi.__stateless = False

    setStateless = staticmethod(setStateless)

    # *
    # * Sets the timeout.
    #
    def setTimeout(timeout):
        if timeout is None:
            raise TypeError("timeout is null!")

        if isinstance(timeout, int):
            __timeout = timeout
        else:
            raise Exception("timeout is not numeric!")

    setTimeout = staticmethod(setTimeout)

    def setProgressIndicator(self, progressIndicator):
        self.__progressIndicator = progressIndicator

    def getProgressIndicator(self):
        return self.__progressIndicator

    def callWithGetUrl(self, url):

        if AceQLHttpApi.__timeout == 0:
            response = requests.get(url, self.__proxies)
        else:
            response = requests.get(url, self.__proxies, timeout=AceQLHttpApi.__timeout)

        self._http_status = response.status_code

        return response.text

    def callWithGetAction(self, action, actionParameter):
        urlWithaction = self._url + action

        if not actionParameter is None and len(actionParameter) > 1:
            urlWithaction += "/" + actionParameter

        return self.callWithGetUrl(urlWithaction)

    def callApiWithResult(self, commandName, commandOption):
        if commandName is None:
            raise TypeError("commandName is null!")

        try:
            result = self.callWithGetAction(commandName, commandOption)

            resultAnalyzer = ResultAnalyzer(result, self.__http_status_code)
            if not resultAnalyzer.isStatusOk():
                raise Error(resultAnalyzer.getErrorMessage(),
                            resultAnalyzer.getErrorId(), None, None, self.__http_status_code)

            return resultAnalyzer.getResult()

        except Exception as e:
            if type(e) == Error:
                raise
            else:
                raise Error(str(e), 0, e, None, self.__http_status_code)

    def callApiNoResult(self, commandName, commandOption):
        if commandName is None:
            raise TypeError("commandName is null!")

        try:
            result = self.callWithGetAction(commandName, commandOption)

            resultAnalyzer = ResultAnalyzer(result, self.__http_status_code)
            if not resultAnalyzer.isStatusOk():
                raise Error(resultAnalyzer.getErrorMessage(),
                            resultAnalyzer.getErrorId(), None, None, self.__http_status_code)

        except Exception as e:
            if type(e) == Error:
                raise
            else:
                raise Error(str(e), 0, e, None, self.__http_status_code)

    def setAutoCommit(self, autoCommit):
        autoCommitStr = str(autoCommit)

        if autoCommitStr == "True":
            autoCommitStr = "true"
        else:
            autoCommitStr = "false"

        self.callApiNoResult("set_auto_commit", autoCommitStr)

    def getAutoCommit(self):
        isAutoCommitStr = self.callApiWithResult("get_auto_commit", None)
        if isAutoCommitStr == "true":
            return True
        else:
            return False

    def commit(self):
        self.callApiNoResult("commit", None)

    def rollback(self):
        self.callApiNoResult("rollback", None)

    def trace(self):
        if AceQLHttpApi.__trace_on:
            print()

    def trace(self, s):
        if AceQLHttpApi.__trace_on:
            print(s)

    # *
    # * Says if trace is on
    # *
    # * @return true if trace is on
    #
    def isTraceOn():
        return AceQLHttpApi.__trace_on

    isTraceOn = staticmethod(isTraceOn)

    # *
    # * Sets the trace on/off
    # *
    # * @param TRACE_ON
    # * if true, trace will be on
    #
    def setTraceOn(traceOn):
        AceQLHttpApi.__trace_on = traceOn

    setTraceOn = staticmethod(setTraceOn)

    # *
    # * @return the prettyPrinting
    #
    def isPrettyPrinting(self):
        return self._prettyPrinting

    # *
    # * Says the query result is returned compressed with the GZIP file format.
    # *
    # * @return the gzipResult
    #
    def isGzipResult(self):
        return self._gzipResult

    # *
    # * Says if JSON contents are to be pretty printed.  Defaults to false.
    # *
    # * @param prettyPrinting
    # * if true, JSON contents are to be pretty printed
    #
    def setPrettyPrinting(self, prettyPrinting):
        self._prettyPrinting = prettyPrinting

    # *
    # * Define if result sets are compressed before download.  Defaults to true.
    # *
    # * @param gzipResult
    # * if true, sets are compressed before download
    #
    def setGzipResult(self, gzipResult):

        if str(gzipResult) == 'True':
            self._gzipResult = True
        else:
            self._gzipResult = False

    # *
    # * Calls /get_version API
    # *
    # * @
    # * if any Exception occurs
    #
    def getServerVersion(self):
        theVersion = self.callApiWithResult("get_version", None)
        return theVersion

    # *
    # * Gets the SDK version
    # *
    # * @
    # * if any Exception occurs
    #
    def getClientVersion(self):
        return VersionValues.NAME + " - " + VersionValues.VERSION + " - " + VersionValues.DATE

    # *
    # * Calls /disconnect API
    # *
    # * @
    # * if any Exception occurs
    #
    def disconnect(self):
        self.callApiNoResult("disconnect", None)

    # *
    # * Calls /get_transaction_isolation_level API
    # *
    # * @return the current transaction isolation level, which will be one of the
    # * following constants: <code>transaction_read_uncommitted</code>,
    # * <code>transaction_read_committed</code>,
    # * <code>transaction_repeatable_read</code>,
    # * <code>transaction_serializable</code>, or
    # * <code>transaction_none</code>.
    # * @
    # * if any Exception occurs
    #
    def get_transaction_isolation(self):
        transactionIsolation = self.callApiWithResult("get_transaction_isolation_level", None)
        return transactionIsolation

    # *
    # * Calls /set_transaction_isolation_level API
    # *
    # * @param level
    # * the isolation level
    # * @
    # * if any Exception occurs
    #
    def set_transaction_isolation(self, level):
        self.callApiNoResult("set_transaction_isolation_level", level)

    #
    # * Calls /get_holdability API
    # *
    # * @return the holdability, one of <code>hold_cursors_over_commit</code> or
    # * <code>close_cursors_at_commit</code>
    # * @throws Error
    # * if any Exception occurs
    #
    def get_holdability(self):
        holdability = self.callApiWithResult("get_holdability", None)
        return holdability

    # *
    # * Calls /set_holdability API
    # *
    # * @param holdability
    # * the holdability
    # * @
    # * if any Exception occurs
    #
    def set_holdability(self, holdability):
        self.callApiNoResult("set_holdability", holdability)

    # *
    # * Calls /get_auto_commit API
    # *
    # * @return <code>true</code> if this <code>Connection</code> object is
    # * read-only; <code>false</code> otherwise
    # * @
    # * if any Exception occurs
    #
    def is_read_only(self):
        isReadOnlyStr = self.callApiWithResult("is_read_only", None)
        if isReadOnlyStr == "true":
            return True
        else:
            return False

    # *
    # * Calls /set_read_only API
    # *
    # * @param readOnly
    # * {@code true} enables read-only mode; {@code false} disables it
    # * @
    # * if any Exception occurs
    #
    def set_read_only(self, readOnly):
        if readOnly is None:
            raise TypeError("readOnly is null!")

        readOnlyStr = "false"

        if str(readOnly) == "True":
            readOnlyStr = "true"

        self.callApiNoResult("set_read_only", readOnlyStr)

    # *
    # * @return the httpStatus
    #
    def getHttpStatusCode(self):
        return self.__http_status_code

    # *
    # * @return the httpStatusMessage
    #
    def getHttpStatusMessage(self):
        statusMessages = requests.status_codes._codes[self.__http_status_code]
        return statusMessages[0]

    # *
    # * Calls /execute_update API
    # *
    # * @param sql
    # * an SQL <code>INSERT</code>, <code>UPDATE</code> or
    # * <code>DELETE</code> statement or an SQL statement that returns
    # * nothing
    # * @param isPreparedStatement
    # * if true, the server will generate a prepared statement, else a
    # * simple statement
    # * @param statementParameters
    # * the statement parameters in JSON format.  Maybe null for simple
    # * statement call.
    # * @return either the row count for <code>INSERT</code>, <code>UPDATE</code>
    # * or <code>DELETE</code> statements, or <code>0</code> for SQL
    # * statements that return nothing
    # * @
    # * if any Exception occurs
    #
    def execute_update(self, sql, isPreparedStatement, statementParameters):

        try:

            action = "execute_update"

            if sql is None:
                raise TypeError("sql is null!")
            if isPreparedStatement is None:
                raise TypeError("isPreparedStatement is null!")

            dictParams = {}
            dictParams["sql"] = sql

            if str(isPreparedStatement) == 'True':
                dictParams["prepared_statement"] = "true"
            else:
                dictParams["prepared_statement"] = "false"

            urlWithaction = self._url + action

            AceQLDebug.debug("urlWithaction: " + urlWithaction)
            AceQLDebug.debug("dictParams 1: " + str(dictParams))

            if statementParameters is not None:
                if not isinstance(statementParameters, dict):
                    raise TypeError("statementParameters is not a dictionnary!")

                dictParams.update(statementParameters)

            AceQLDebug.debug("dictParams 2: " + str(dictParams))

            # r = requests.post('http://httpbin.org/post', data = {'key':'value'})

            if AceQLHttpApi.__timeout == 0:
                response = requests.post(urlWithaction, data=dictParams, proxies=self.__proxies)
            else:
                response = requests.post(urlWithaction, data=dictParams, proxies=self.__proxies,
                                         timeout=AceQLHttpApi.__timeout)

            self._http_status = response.status_code
            result = response.text

            AceQLDebug.debug("result: " + result)

            resultAnalyzer = ResultAnalyzer(result, self.__http_status_code)
            if not resultAnalyzer.isStatusOk():
                raise Error(resultAnalyzer.getErrorMessage(),
                            resultAnalyzer.getErrorId(), None, None, self.__http_status_code)

            rowCount = resultAnalyzer.getIntvalue("row_count")
            return rowCount

        except Exception as e:
            if type(e) == Error:
                raise
            else:
                raise Error(str(e), 0, e, None, self.__http_status_code)

    # *
    # * Calls /execute_query API
    # *
    # * @param sql
    # * an SQL <code>INSERT</code>, <code>UPDATE</code> or
    # * <code>DELETE</code> statement or an SQL statement that returns
    # * nothing
    # * @param isPreparedStatement
    # * if true, the server will generate a prepared statement, else a
    # * simple statement
    # * @param statementParameters
    # * the statement parameters in JSON format.  Maybe null for simple
    # * statement call.
    # * @return the input stream containing either an error, or the result set in
    # * JSON format.  See user documentation.
    # * @
    # * if any Exception occurs
    #
    def execute_query(self, sql, isPreparedStatement, statementParameters):

        try:

            action = "execute_query"

            if sql is None:
                raise TypeError("sql is null!")
            if isPreparedStatement is None:
                raise TypeError("isPreparedStatement is null!")

            dictParams = {}
            dictParams["sql"] = sql

            if str(isPreparedStatement) == 'True':
                dictParams["prepared_statement"] = "true"
            else:
                dictParams["prepared_statement"] = "false"

            urlWithaction = self._url + action

            AceQLDebug.debug("urlWithaction: " + urlWithaction)
            AceQLDebug.debug("dictParams 1: " + str(dictParams))

            if statementParameters is not None:
                if not isinstance(statementParameters, dict):
                    raise TypeError("statementParameters is not a dictionnary!")

                dictParams.update(statementParameters)

            if self._gzipResult:
                dictParams["gzip_result"] = "true"
            if self._prettyPrinting:
                dictParams["pretty_printing"] = "true"

            # Force pretty printing to True because parser needs it
            dictParams["pretty_printing"] = "true"

            # We need the types
            dictParams["column_types"] = "true"

            AceQLDebug.debug("dictParams 2: " + str(dictParams))

            # r = requests.post('http://httpbin.org/post', data = {'key':'value'})

            if AceQLHttpApi.__timeout == 0:
                response = requests.post(urlWithaction, data=dictParams, proxies=self.__proxies)
            else:
                response = requests.post(urlWithaction, data=dictParams, proxies=self.__proxies,
                                         timeout=AceQLHttpApi.__timeout)

            self._http_status = response.status_code

            filename = FileUtil.build_result_set_file()
            AceQLDebug.debug("filename1: " + filename)

            # We dump the JSon stream into user.home/.kawansoft/tmp
            with open(filename, 'wb') as fd:
                for chunk in response.iter_content(chunk_size=2048):
                    fd.write(chunk)

            AceQLDebug.debug("after open filename")

            file_out = None

            if self.isGzipResult():
                file_out = filename[0: len(filename) - 4] + ".ungzipped.txt"
                FileUtil.decompress(filename, file_out)
                if Parms.DELETE_FILES:
                    os.remove(filename)
            else:
                file_out = filename

            AceQLDebug.debug("Before StreamResultAnalyzer")

            resultAnalyzer = StreamResultAnalyzer(file_out, self.__http_status_code)
            if not resultAnalyzer.is_status_ok():
                if Parms.DELETE_FILES:
                    os.remove(filename)
                raise Error(resultAnalyzer.get_error_message(),
                            resultAnalyzer.get_error_type(), None, None, self.__http_status_code)

            rowCounter = RowCounter(file_out)
            row_count = rowCounter.count()

            resultSetInfo = ResultSetInfo(file_out, row_count)
            AceQLDebug.debug("Before resultSetInfo")

            return resultSetInfo

        except Exception as e:
            if type(e) == Error:
                raise
            else:
                raise Error(str(e), 0, e, None, self.__http_status_code)

    def get_blob_stream(self, blob_id):
        """ returns a BLOB stream as a Requests response """
        try:

            if blob_id is None:
                raise TypeError("blob_id is null!")

            theUrl = self._url + "/blob_download?blob_id=" + blob_id

            if AceQLHttpApi.__timeout == 0:
                response = requests.get(theUrl, proxies=self.__proxies)
            else:
                response = requests.get(theUrl, proxies=self.__proxies, timeout=AceQLHttpApi.__timeout)

            self._http_status = response.status_code

            return response

        except Exception as e:
            if type(e) == Error:
                raise
            else:
                raise Error(str(e), 0, e, None, self.__http_status_code)

    # def blob_download(self, blob_id, filename, total_length=0,
    # progress_holder=None):
    #	""" Allows to download a blob.  """

    #	try:

    #		if blob_id is None:
    #			raise TypeError("blob_id is null!")

    #		if filename is None:
    #			raise TypeError("filename is null!")

    #		theUrl = self._url + "/blob_download?blob_id=" + blob_id

    #		#Stream input = await CallWithGetReturnStreamAsync(theUrl);
    #		#return input;
    #		if (AceQLHttpApi.__timeout == 0):
    #			response = requests.get(theUrl, proxies = self.__proxies)
    #		else:
    #			response = requests.get(urlWithaction, proxies = self.__proxies,
    #			timeout=AceQLHttpApi.__timeout)

    #		self._http_status = response.status_code

    #		# We dump the blob into file
    #		with open(filename, 'wb') as fd:

    #			the_chunk_size = 2048

    #			if total_length == 0 or progress_holder == None:
    #				for chunk in response.iter_content(chunk_size=the_chunk_size):
    #					fd.write(chunk)
    #			else:
    #				temp_length = 0
    #				for chunk in response.iter_content(chunk_size=the_chunk_size):
    #					if progress_holder.is_cancelled():
    #						break
    #					fd.write(chunk)
    #					temp_length += the_chunk_size
    #					if temp_length > total_length / 100:
    #						progress_holder.increment()
    #						temp_length = 0

    #				progress_holder.set_complete()

    #	except Exception as e:
    #		if type(e) == Error:
    #			raise
    #		else:
    #			raise Error(str(e), 0, e, None, self.__http_status_code)


    def get_blob_length(self, blob_id):
        """ Gets the blob length. """
        try:

            if blob_id is None:
                raise TypeError("blob_id is null!")

            action = "get_blob_length"

            dictParams = {}
            dictParams["blob_id"] = blob_id

            urlWithaction = self._url + action

            AceQLDebug.debug("urlWithaction: " + urlWithaction)
            AceQLDebug.debug("dictParams   : " + str(dictParams))

            # r = requests.post('http://httpbin.org/post', data = {'key':'value'})

            if AceQLHttpApi.__timeout == 0:
                response = requests.post(urlWithaction, data=dictParams, proxies=self.__proxies)
            else:
                response = requests.post(urlWithaction, data=dictParams, proxies=self.__proxies,
                                         timeout=AceQLHttpApi.__timeout)

            self._http_status = response.status_code
            result = response.text

            AceQLDebug.debug("result: " + result)

            resultAnalyzer = ResultAnalyzer(result, self.__http_status_code)
            if not resultAnalyzer.isStatusOk():
                raise Error(resultAnalyzer.getErrorMessage(),
                            resultAnalyzer.getErrorId(), None, None, self.__http_status_code)

            length_str = resultAnalyzer.getValue("length")
            AceQLDebug.debug("result: " + length_str + ":")
            return int(length_str)

        except Exception as e:
            if type(e) == Error:
                raise
            else:
                raise Error(str(e), 0, e, None, self.__http_status_code)

    def my_callback(self, monitor):
        """ The callback function when uploading a BLOB """
        try:
            if self.__total_length == 0 or self.__progressIndicator == None:
                return

            the_read = monitor.bytes_read

            self._temp_length += the_read
            if self._temp_length >= self.__total_length / 100:
                self._temp_length = 0
                self.__progressIndicator._increment()

        except Exception as e:
            print(str(e))
            pass

    def blob_upload(self, blob_id, fd, total_length):
        """ Upload the BLOB and use a callback function for progress indicator. """

        self.__total_length = total_length

        # fields={'field0': 'value', 'field1': 'value',
        #		'field2': ('filename', open('file.py', 'rb'), 'text/plain')}

        theFields = {}
        theFields["blob_id"] = blob_id
        theFields["file"] = ("filename", fd, "application/octet-stream")

        e = encoder.MultipartEncoder(fields=theFields)

        m = encoder.MultipartEncoderMonitor(e, self.my_callback)

        theUrl = self._url + "blob_upload"

        r = requests.post(theUrl, data=m,
                          headers={'Content-Type': m.content_type})
