#binary search to find lowest values index in lst higher than or equal to val 
def binsearchup(lst,val):
    l = len(lst)
    a,b = 0,l
    while a+1!=b:
        i = (a+b)//2
        if lst[i]<=val:
            a = i
        else:
            b = i
    return b