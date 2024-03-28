import datetime
import pytz
def result_time(call_time , last_time):
    date_1 = datetime.datetime.strptime(last_time, "%Y-%m-%d %H:%M:%S")
    date_2 = datetime.datetime.strptime(call_time, "%Y-%m-%d %H:%M:%S")
    unix_timestamp1 = int(date_1.timestamp())
    unix_timestamp2 = int(date_2.timestamp())
    result = unix_timestamp2 - unix_timestamp1
    return result





def return_tosh():
    country = 'Asia/Tashkent'  # Replace with the desired country/timezone

    # Get the current time in the specified country
    country_timezone = pytz.timezone(country)
    current_time = datetime.datetime.now(country_timezone)

    # Format the current time as a string
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time




