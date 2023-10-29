from collections import defaultdict
 
 
def getPalindrome(string):
 
    # Store counts of characters
    StringMap = defaultdict(int)
    for i in range(len(string)):
        StringMap[string[i]] += 1
 
    # Find the number of odd elements.
    oddCount = 0
    oddChar=""
 
    for x in StringMap:
        if (StringMap[x] % 2 != 0):
            oddCount += 1
            oddChar = x
 
    # odd_cnt = 1 only if the length of
    # str is odd
    if (oddCount > 1 or (oddCount == 1 and
            len(string) % 2 == 0)):
        return "NO SOLUTION"
 
    # Generate first half of palindrome
    firstHalf = ""
    secondHalf = ""
 
    for x in sorted(StringMap.keys()):
 
        # Build a string of floor(count/2)
        # occurrences of current character
        s = (StringMap[x] // 2) * x
 
        # Attach the built string to end of
        # and begin of second half
        firstHalf = firstHalf + s
        secondHalf = s + secondHalf
 
    # Insert odd character if there
    # is any
    if (oddCount == 1):
        return (firstHalf + oddChar + secondHalf)
    else:
        return (firstHalf + secondHalf)
    


s=input()
print(getPalindrome(s))