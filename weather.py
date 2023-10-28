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
    # human_date_time=date_time_object.strftime('%A %d %B %Y at %I:%M %p')
    human_date_time=date_time_object.strftime('%A %d %B %Y')
    # print(human_date_time)
    return(human_date_time)

#debigging
# convert_date('2020-06-22T07:00:00+08:00')


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
        # print ('in first leg')
        # print (type(weather_data[0]))
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

#debugging
# test_list= [ '45', 34, 45, 35, 21, 15 ]
# my_average_temp=calculate_mean(test_list)
# print(my_average_temp)


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
                # #check the format of the numbers and date
                # for i in row:
                #     print(type (i))
                #convert to temperatures to integer
                row[1]=int(row[1])
                row[2]=int(row[2])
                my_list.append(row)
                # print(row)
            # else:
            #     # print("Data is empty, not appending.")
        # print (my_list)
        return my_list

#debugging
# load_data_from_csv('tests/data/example_two.csv')

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

# #debugging
# temperatures = [10.4, 14.5, 12.9, 8.9, 10.5, 11.7]
#         # expected_result = (8.9, 3)
# my_min=find_min(temperatures)
# print(my_min)

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
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
