

# 1. Find the Number of Days Until Your Next Birthday
# Write a Python program that:

# Takes the user's birth date as input (format: YYYY-MM-DD).
# Calculates how many days are left until their next birthday.
 


# Solution:



# from datetime import datetime


# birth_date = datetime.strptime(input(f"Enter your date of birth (formate: YYYY-MM-DD): "), "%Y-%m-%d")

# today = datetime.today()

# next_birth_year = today.year if today.month < birth_date.month or (today.month == birth_date.month and today.days < birth_date.day) else today.year +1

# next_birth_date = datetime(next_birth_year, birth_date.month, birth_date.day)

# remaining_days = next_birth_date - today

# print(f"{remaining_days.days} days are remaining for your next birthday.")
















# 2. Convert a Given Date to Different Time Zones
# Write a function that takes a date-time string (YYYY-MM-DD HH:MM:SS) and a target timezone (e.g., "Asia/Karachi", "America/New_York").
# Convert the date-time to the specified timezone.
 


# Solution:

# from datetime import datetime
# import pytz


# def get_tz_datetime(timezone):

#     utc_time = datetime.now(pytz.utc)

#     local_time = utc_time.astimezone(timezone)
#     print(local_time)
    
# get_tz_datetime(pytz.timezone(input("Enter your timezone: ")))    
    
















# 3. Generate a List of All Sundays in a Given Year
# Write a function that takes a year (e.g., 2025) and returns a list of all Sundays in that year.
 


# from datetime import date, timedelta


# def get_all_sunday(year):

#     # start day of the year
#     start_date = date(year, 1, 1)


#     # search for the first sunday of year

#     while start_date.weekday() != 6:
#         start_date += timedelta(days=1) 


#     # Generate all sundays of year  

#     sundays = []
#     while start_date.year == year:
#         sundays.append(start_date)  
#         start_date += timedelta(days=7)

#     return sundays

# sunday_list = get_all_sunday(2025)

# for sunday in sunday_list:
#     print(sunday)




















# 4. Find the First Monday of Each Month in a Given Year
# Write a function that:
# Takes a year as input.
# Returns a list of the first Monday of each month in that year.
 



# from datetime import date, timedelta

# def get_first_modays(year):

#     first_mondays = []

#     for month in range(1, 13):
#         first_day = date(year, month, 1)


#         while first_day.weekday() != 0:
#             first_day += timedelta(days=1)  
        
             
#         first_mondays.append(first_day) 

#     return first_mondays

# first_mondays_list = get_first_modays(2025)

# for mondays in first_mondays_list:
#     print(mondays)







 