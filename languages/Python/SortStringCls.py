strlst = []

class StringSortCls(object):
    def __init__(self, num, *args):
        self.num = num
    def __lt__(self, other):
        if len(self.num) != len(other.num):
            return len(self.num) < len(other.num)
        else:
            return self.num < other.num
    def __gt__(self, other):
        return other < self
    def __eq__(self, other):
        return self.num == other.num
    def __le__(self, other):
        return not (self > other)
    def __ge__(self, other):
        return (other <= self)
    def __ne__(self, other):
        return self.num != other.num

strlst.sort(key = StringSortCls)