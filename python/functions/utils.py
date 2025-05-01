
print("module imported!")

def greet(person:str, first_time = False):
    """
    A function to return a greeting along with a user's name

    params:
    person: a string

    returns:
    greeting with "person's" value
    """
    if first_time:
        return f"First time? Welcome {person}!"
    else:
        return f"Hello {person}!"


def greet_all(people:list):
    """
    Function to return a greeting message for each names/items in the list.

    params:
    people: a list of names

    returns:
    greeting message for all
    """
    message = []
    for person in people:
        message.append(greet(person, True))
    refined_message = "\n".join(message) #Add a new line to each item
    return refined_message

def hello_fun():
   ''' Function to return a basic greeting. It takes no argument.'''

   return("Hello function!")


def student_info(*args, **kwargs):
    """
    Function to take in an arbitrary number of positional arguments and keyword arguments.

    params:
    *args: positional argument of any length
    **kwargs: keyword arguments of any length

    returns:
    a tuple for args and a dictionary for kwargs if set
    """
    print(args)
    print(kwargs)


def leap_year_check(year : int):
    """
    Function to check if a year is leap or not.

    param: 
    year: an int. Example year = 2000, 2009

    returns:
    a bool
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def month_days(year : int, month : int):
    """
    Function to return the number of days in a month.
    """
    days_count = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check the validity of the month parameter passed
    if month in range(1,13):
        if leap_year_check(year) and month == 2:
            return 29
        return days_count[month]
    return "Invalid month!"


def string_rev(word : str):
    ''' Function to return the reverse of letters in a word '''

    return(word[::-1])

def max_num(value):
    ''' Function to return the maximum number in a list of integers '''

    return max(value)

def unique_list(value : list):
    ''' Function to return the unique items in a list as a new list'''

    new_list = []
    for i in value:
        if i not in new_list:
            new_list.append(i)
    return new_list


def sum_numbers(value):
    ''' Function to calculte the sum of numbers in a list '''

    item_sum = 0
    for i in value:
        item_sum = item_sum + i
    return item_sum
    