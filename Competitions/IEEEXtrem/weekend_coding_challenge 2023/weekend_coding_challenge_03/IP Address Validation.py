num = int(input())

import re

byte = '([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])'  # 0 - 255
regex = '^{0}(\.{0}){{3}}$'.format(byte)
pattern4 = re.compile(regex)

hex_group = '[0-9A-Fa-f]{1,4}'  # Four hex digits
regex = '^({0})(:{0}){{7}}$'.format(hex_group)
pattern6 = re.compile(regex)

for _ in range(num):
    s = input().strip()
    
    if pattern4.match(s):
        print("IPv4")
    elif pattern6.match(s):
        print("IPv6")
    else:
        print("Neither")
        
        
        
        
        