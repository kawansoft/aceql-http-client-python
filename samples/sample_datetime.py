from datetime import datetime, time

the_datetime = datetime.now()
the_date = the_datetime.date()
the_time = the_datetime.time()

print()
print("the_datetime: " + str(type(the_datetime)))
print("the_date    : " + str(type(the_date)))
print("the_time    : " + str(type(the_time)))
print()
print("the_datetime: " + str(the_datetime))
print("the_date    : " + str(the_date))
print("the_time    : " + str(the_time))
print()
print("the_time hour   : " + str(the_time.hour))
print("the_time minute : " + str(the_time.minute))
print("the_time second : " + str(the_time.second))
print("the_time micros : " + str(the_time.microsecond))