my_dict = {}

# Checking if a Key Exists:
if 'd' in my_dict:
    print('Key "d" exists in the dictionary')

# Getting a Default Value:
value = my_dict.get('x', 0)  # Get the value for key 'x'; if not found, return 0


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}  # Merge two dictionaries


sorted_dict = dict(sorted(my_dict.items()))  # Sort by keys
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))  # Sort by values


from collections import Counter
my_list = [1, 2, 2, 3, 3, 3]
count_dict = Counter(my_list)  # Count elements and store in a dictionary
