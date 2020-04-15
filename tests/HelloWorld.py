from aceql._private.result_set_info import *
import json

print("Ok")

result_set_info = ResultSetInfo("my_file.txt", 2)
print(result_set_info.get_filename())
print(result_set_info.get_row_count())

json.loads()


