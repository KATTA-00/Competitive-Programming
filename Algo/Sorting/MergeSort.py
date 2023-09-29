#slowerrrrr or wrong

# def pair(grid):
#     length = len(grid)
#     newgrid = []
#     for i in range(0,length,2):
#         newel = []
#         el1 = grid[i]
#         try:
#             el2 = grid[i+1]
#             while el1!=[] and el2!=[]:
#                 if el1[0]>=el2[0]:
#                     newel.append(el2[0])
#                     el2=el2[1:]
#                 else:
#                     newel.append(el1[0])
#                     el1=el1[1:]
#             newel+=el1
#             newel+=el2
#             newgrid.append(newel)
        
#         except:
#             newgrid.append(el1)

#     if len(newgrid)==1:
#         return newgrid[0]
#     else:
#         return pair(newgrid)

# def mergesort(numlst):
#     pairlst = []
#     length = len(numlst)
#     for i in range(0,length,2):
#         try:
#             num1 = numlst[i]
#             num2 = numlst[i+1]
#             if num1>=num2:
#                 pairlst.append([num2,num1])
#             else:
#                 pairlst.append([num1,num2])
#         except:
#             pairlst.append([numlst[i]])

#     return pair(pairlst)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1


    # Add remaining elements (if any) from both lists
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

# Example usage
if __name__ == "__main__":
    n = int(input().strip())

    arr = []
    for i in range (n):
        arr.append(map(int, input().rstrip().split()))
    sorted_list = merge_sort(arr)
    print("[", end="")
    print(','.join(map(str, sorted_list)),end="")
    print("]", end="")
    



# print(mergesort([5,6,8,10,1,13,0,4,7,2,65,5,5,5,6,6,5,6,6,8,69,6,7,659,6,74,9,96,4,8,6,4,96,5]))