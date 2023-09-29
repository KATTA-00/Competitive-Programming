# Enter your code here. Read input from STDIN. Print output to STDOUT
def compute_lps_array(pattern):
    length = 0  
    lps = [0] * len(pattern)

    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def find_pattern_indexes(text, pattern):
    lps = compute_lps_array(pattern)
    i = 0  
    j = 0  
    indexes = []

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            
            start_index = i - j
            end_index = i - 1
            indexes.append((start_index, end_index))
            j = lps[j - 1]

        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indexes

n = int(input())
text = input()
m = int(input())
pattern = input()
index_array = []
index_array2 = []
indexes = find_pattern_indexes(text, pattern)
for start, end in indexes:
    index_array.append((start, end))
i = 0
while i <len(index_array):
      
    start = index_array[i][0]
    if i < len(index_array)-1:
        while index_array[i][1] >= index_array[i+1][0]-1:
            i += 1
            end = index_array[i][1]
            if i == len(index_array)-1:
                break
    end = index_array[i][1]
    i += 1
    index_array2.append((start, end))

j = 0

i = 0
while i < len(text):
    if j < len(index_array2):
        if i < index_array2[j][0]:
            print(text[i],end="")
        if i == index_array2[j][0]:
            print("#",end="") 
            while i <= index_array2[j][1]:
                print(text[i],end="")
                i += 1
            print("#",end="")
            j += 1
            i -= 1
        if i > index_array2[len(index_array2)-1][1]:
            print(text[i],end="")
        i+=1
    else:
        print(text[i],end="")
        i += 1
    
    
    