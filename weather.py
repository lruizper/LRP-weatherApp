import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_time_object=datetime.fromisoformat(iso_string)
    human_date_time=date_time_object.strftime('%A %d %B %Y')
    return(human_date_time)


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_farenheit=float(temp_in_farenheit)
    temp_in_celsius= round ((((temp_in_farenheit-32)*5)/9) , 1)
    return (temp_in_celsius)
   

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    if len(weather_data)>0:
        my_float_list=[]  
        for i in weather_data:
            i=float(i)
            my_float_list.append(i)
        my_lenght=len(my_float_list)
        my_sum=sum(my_float_list)
        my_mean=(my_sum/my_lenght)
        # print (my_mean)
        return(my_mean)
    else:
        print ('data is empty or not numbers')


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    my_list=[]
    with open(csv_file, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        data = list(reader)
        for row in data:
            if len(row)>0:
                row[1]=int(row[1])
                row[2]=int(row[2])
                my_list.append(row)
        return my_list


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if len(weather_data)>0:
        my_float_list=[]  
        for i in weather_data:
            i=float(i)
            my_float_list.append(i)
        my_lowest_temp=min(my_float_list) 
        my_indices_list=[]
        for hit, low_temp in enumerate (my_float_list):
            if low_temp==my_lowest_temp:
                my_indices_list.append(hit)
        my_index=my_indices_list[-1]
        return (my_lowest_temp, my_index)
    else:
        # print ('data is empty or not numbers') 
        return ()       


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if len(weather_data)>0:
        my_float_list=[]  
        for i in weather_data:
            i=float(i)
            my_float_list.append(i)
        my_highest_temp=max(my_float_list) 
        my_indices_list=[]
        for hit, low_temp in enumerate (my_float_list):
            if low_temp==my_highest_temp:
                my_indices_list.append(hit)
        my_index=my_indices_list[-1]
        return (my_highest_temp, my_index)
    else:
        # print ('data is empty or not numbers') 
        return ()       

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    #create empty result message
    result_message=''
    #how many days forecast
    days_forecast=len(weather_data)
    #write to first line of result message
    result_message += f'{days_forecast} Day Overview\n'
    #create empty lists for min and max temperatures
    low_temp_list=[]
    high_temp_list=[]
    human_date_list=[]
    
    for day in weather_data:
        human_date=convert_date(day[0])
        human_date_list.append(human_date)
        min_temperature= convert_f_to_c(day[1])
        low_temp_list.append(min_temperature)
        max_temperature=  convert_f_to_c(day[2])
        high_temp_list.append(max_temperature)
    # evaluate highest and lowest temperatures from lists
    lowest_temp=format_temperature( find_min(low_temp_list)[0])
    lowest_temp_index=find_min(low_temp_list)[1]
    day_of_lowest_temp=human_date_list[lowest_temp_index]
    highest_temp=format_temperature( find_max(high_temp_list)[0])
    highest_temp_index=find_max(high_temp_list)[1]
    day_of_highest_temp=human_date_list[highest_temp_index]
    # evaluate averages min and max
    average_low= format_temperature( round ( calculate_mean(low_temp_list) , 1))
    average_high= format_temperature( round ( calculate_mean(high_temp_list) , 1))
    result_message += f'  The lowest temperature will be {lowest_temp}, and will occur on {day_of_lowest_temp}.\n'
    result_message += f'  The highest temperature will be {highest_temp}, and will occur on {day_of_highest_temp}.\n'
    result_message += f'  The average low this week is {average_low}.\n'
    result_message += f'  The average high this week is {average_high}.\n'
    return result_message


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    result_message=''
    for day in weather_data:
        # print (day)
        human_date=convert_date(day[0])
        # print (human_date)
        min_temperature= format_temperature( convert_f_to_c(day[1]))
        max_temperature= format_temperature( convert_f_to_c(day[2]))
        # result_message= print(f'----  {human_date} ----')
        result_message += f'---- {human_date} ----\n  Minimum Temperature: {min_temperature}\n  Maximum Temperature: {max_temperature}\n\n'            
        # print(result_message)
    return result_message
