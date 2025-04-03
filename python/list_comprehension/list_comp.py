
ages = [23, 34, 35, 60]
stored_age = [f"My friend's age is {age}." for age in ages]
print(stored_age)

names = ["Tao", "Mayowa", "Dayo"]

def replaced_a(name):
    replaced = [n.replace("a", "_") for n in name]
    return replaced

print(replaced_a(names))

def yield_bad_names(customer_names_list):
    """ Function to filter out bad entries in a list """
    yields = [
        name 
        for name in customer_names_list 
        if type(name) != str
        ]
    return yields

cust_names = [10, "mayowa", "zainab", 4, 5]
yielded = yield_bad_names(cust_names)
#for i in yielded:
print(yielded)

