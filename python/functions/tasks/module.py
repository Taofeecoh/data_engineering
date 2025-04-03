import utils as ut

# ~~~~~~~~~~~~~~~~~~~~~~~ TASK ONE ~~~~~~~~~~~~~~~~~~~~~~~
def first_name(x: str):
    ''' Function to return first name'''

    x = x.split(sep= " ") # x.split(sep= (" " or "-" or "_" or "+"))
    return x[0]


def last_name(x: str):
    ''' Function to return last name'''

    x = x.split(sep= " ")
    return x[-1]


def task_one(x: str):
    ''' Function to concatenate first and last name'''

    return (f"My full name is {first_name(x)} {last_name(x)}.")



# ~~~~~~~~~~~~~~~~~~~~~~~ TASK TWO ~~~~~~~~~~~~~~~~~~~~~~~
def space_check(x: str):
    """
    Function to replace space characters with underscores

    Args:
    x: str

    Returns:
    x with " " replaced "_"
    
    """

    for i in x:
        if i == " ":
            x = x.replace(i, "_")
    return(x)

def task_two(attr: list):
    """ 
    Function to return a list of items in snake_case format
    """

    new_attr = []
    for i in attr:
        if space_check(i):
            i = space_check(i)
        new_attr.append(i)
    return f"Old attributes: {attr}, New attributes: {new_attr}"



# ~~~~~~~~~~~~~~~~~~~~~~~ TASK THREE ~~~~~~~~~~~~~~~~~~~~~~~

def extract_names(names: list):
    """
    Function to extract the first and last letters of an item

    Args:
    names: list of names

    Returns:
    new list
    """

    new_names = []
    for name in names:
        if name[0].isupper() and name[-1].endswith("a"):
            new_names.append(name)
        elif name[0].isupper() and not name.endswith("a"):
            name = name.replace(name[-1], "a")
            new_names.append(name)
    return new_names


def upper_check(x: str):
    """ Function to check if a string starts with upper case"""

    if x[0].isupper():
        return x
    # else:
      #  x = ""
       # return x
    

def last_letter_check(x: str):
    """ 
    Function to check if the last letter of a string is "a" 
    
    Args:
    x: string

    Returns:
    New string with replaced last letter == "a" if not true
    """

    if x.endswith("a"):
        return x
    else:
        x = x.replace(x[-1], "a")
        return x
    
def task_three(names: list):
    """
    Function to extract the first and last letters of an item

    Args:
    names: list of names

    Returns:
    new list
    """

    new_name = []
    for name in names:
        if upper_check(name):
            name = last_letter_check(name)
            new_name.append(name)
    return new_name



# ~~~~~~~~~~~~~~~~~~~~~~~ TASK FOUR ~~~~~~~~~~~~~~~~~~~~~~~

def alpha_check(x: str):
    """ 
    Function to check if characters in a string is not alphabet 
    
    Args:
    x: str

    Returns:
    x, if it contains non-alphabet character

    """
    for i in x:
        if not i.isalpha():
                return x

def task_four(data: list):
    """ 
    Function to detect bad entries in a list 

    Args:
    data: list

    Retrun:
    bad_data, a unique list with items containing non-alphabet characters
    """

    bad_data = []
    for i in data:
        if alpha_check(i):
            bad_data.append(i)
    return f"Failed to run due bad entries: {ut.unique_list(bad_data)}"


def yield_bad_names(customer_names_list):
    """ Function to filter out bad entries in a list """

    for name in customer_names_list:
        if type(name) != str:
            yield name