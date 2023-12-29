def list_to_set(lst):
        return set(lst)

def set_to_list(st):
        return list(st)

    # Test the functions
my_list = [1, 2, 3, 4, 4, 5]
my_set = list_to_set(my_list)
print("Converted Set:", my_set)  # Output: {1, 2, 3, 4, 5}

my_new_list = set_to_list(my_set)
print("Converted List:", my_new_list)