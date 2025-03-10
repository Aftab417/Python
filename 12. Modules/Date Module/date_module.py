
#####################-----------------  Datetime Module  --------------------##########################

# datetime module in python provides classes for working with date and time.


# Common Classes in datetime:

# datetime  ----->   Represents date and time  (year, month, day, Hour, Minute, second, microsecond)

# date     ------>   Represents only the date  (year, month, day)

# time     ------->  Represents only the time  (Hour, Munutes, Seconds, microseconds)

# timedelta ------>  Represents the difference between two dates/times.

# tzinfo   ------->  Handles the timezone information.


  



#  Common  methods  and  function in datetime module


################## ---------  Get current datetime  ----------------###################

# from datetime import datetime

# now = datetime.now()

# print(now)






################## ---------  Get current date  ----------------###################


# from datetime import date

# today = date.today()

# print(today)







################## ---------  Extract components of date/time  ----------------###################


# from datetime import datetime

# now = datetime.now()

# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)








################## ---------  Formate datetime  (strftime) ----------------###################

# strftime  method is used to formate a datetime object into a string.


# from datetime import datetime

# now = datetime.now()

# formated_date = now.strftime("%d-%m-%Y  %H : %M : %S")

# print(formated_date)





#  Common  Formate  codes:

#  %Y      -------->      Full Year (2025) 
  
#  %m      -------->      Month (1 - 12) 
   
#  %d      -------->      Day (1 - 31) 
   
#  %H      -------->      Hours (00 - 23) 
   
#  %M      -------->      Minutes (00 - 59) 
   
#  %S      -------->      Seconds (00 - 59 )  
  
   








################## ---------  Date Arthimetic Using  timedelta()  ----------------###################


# timedelta()  class allows us to add or subtract time 




# from datetime import datetime
# from datetime import timedelta

# now = datetime.now()

# tomorrow = now  + timedelta(days=1)

# yesterday = now  -  timedelta(days=1)


# print(tomorrow)
# print(yesterday)











################## ---------  Parsing a string into a datetime object  strptime()  ----------------###################

# We can parse a string into datetime object using strptime() class.


# from datetime import datetime
# string_date = "2025-3-28 17:20:58"

# parsed_date = datetime.strptime(string_date, "%Y-%m-%d  %H:%M:%S")


# print(parsed_date)






################## ---------  Difference between two dates  ----------------###################



# from datetime import datetime


# date1 = datetime(2025, 5, 4)

# date2 = datetime(2020, 3, 2)


# diff = date1 - date2

# print(diff)

# print(diff.days)











################## ---------  Handle time zone  pytz   ----------------###################

#  We can use  pytz  module to handle timezone.


# from datetime import datetime

# import pytz


# utc = pytz.utc

# utc_time = datetime.now(utc)

# print(utc_time)                           # This will return utc time








################## ---------  Changing timezone  ----------------###################


# from datetime import datetime 
# import pytz


# utc = pytz.utc
# utc_time = datetime.now(utc)


# new_tz = pytz.timezone("Asia/Karachi")

# loacal_time = utc_time.astimezone(new_tz)
# print(loacal_time)