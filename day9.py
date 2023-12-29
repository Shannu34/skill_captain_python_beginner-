def add_item(dictionary, key, value):
        dictionary[key] = value

def remove_item(dictionary, key):
        if key in dictionary:
            del dictionary[key]

def update_value(dictionary, key, new_value):
        if key in dictionary:
            dictionary[key] = new_value

def check_key(dictionary, key):
        return key in dictionary

def print_keys(dictionary):
        for key in dictionary.keys():
            print(key)

    # Test the functions
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

add_item(my_dict, 'occupation', 'Engineer')
print(my_dict)  # Output: {'name': 'John', 'age': 25, 'city': 'New York', 'occupation': 'Engineer'}

remove_item(my_dict, 'age')
print(my_dict)  # Output: {'name': 'John', 'city': 'New York', 'occupation': 'Engineer'}

update_value(my_dict, 'city', 'San Francisco')
print(my_dict)  # Output: {'name': 'John', 'city': 'San Francisco', 'occupation': 'Engineer'}

print(check_key(my_dict, 'age'))  # Output: False
print(check_key(my_dict, 'name'))  # Output: True

print_keys(my_dict)  # Output: name city occupation
