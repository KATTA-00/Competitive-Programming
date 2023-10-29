from collections import Counter


my_list = [1, 2, 2, 3, 3, 3,3,3,3,3, 4, 4, 4, 4]
# my_list = ['a', 'b', 'c', 'b', 'a', 'a', 'c', 'd', 'd']

# finding most common element in a list
most_common_element = max(Counter(my_list), key=Counter(my_list).get)

# find count of the most common element
most_common_element_count = Counter(my_list).most_common(1)[0][1]

print(most_common_element_count)