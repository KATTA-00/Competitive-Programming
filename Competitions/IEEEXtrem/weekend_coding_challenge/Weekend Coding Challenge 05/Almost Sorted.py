n = int(input())

array = list(map(int, input().split()))

def sort_array(array):
    sorted_arr = sorted(array)
    if array == sorted_arr:
        print('yes')
        return
    
    left_index = -1
    right_index = -1
    
    for i in range(len(array)):
        if sorted_arr[i] != array[i]:
            left_index = i
            break

    right_index = sorted_arr.index(array[left_index])
    
    swapped_arr = array.copy()
    temp = swapped_arr[left_index]
    swapped_arr[left_index] = swapped_arr[right_index]
    swapped_arr[right_index] = temp

    if sorted_arr == swapped_arr:
        print('yes')
        print('swap', left_index + 1, right_index + 1)
        return
        
    reversed_ar = array[:left_index] + array[left_index:right_index+1][::-1] + array[right_index+1:]
    
    if reversed_ar == sorted_arr:
        print('yes')
        print('reverse', left_index + 1, right_index + 1)
        return
    
    print('no')

sort_array(array)