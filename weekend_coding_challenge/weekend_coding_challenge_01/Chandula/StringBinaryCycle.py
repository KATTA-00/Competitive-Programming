string = input()

def cyclicShift(string):
    return string[-1] + string[:-1]

powArr = []

for i in range(len(string)):
    if string[-1] == "1":
        string = cyclicShift(string)
        continue

    reversedString = string[::-1]
    pw = reversedString.find("1")
    powArr.append(pw)
    string = cyclicShift(string)

print(max(powArr))