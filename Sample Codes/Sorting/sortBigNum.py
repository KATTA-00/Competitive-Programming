def bigSorting(unsorted):
    # Write your code here
    return sorted(unsorted,key=lambda s: (len(s),s))