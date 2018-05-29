# Begin SortArray Class--------------------------------------------------
class SortArray(object):
    def __init__(self, arr):
        self.arr = arr

    # Begin Compare Class-------------------------------------
    class Compare(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b

    #--- Rich Comparison Methods---------------------
        # Return If a < 
        def __lt__(self, other):
            if self.a == other.a:
                return self.b < other.b
            return self.a < other.b

        # Return If a <= b
        def __le__(self, other):
            if self.a == other.a:
                return self.b <= other.b
            return self.a <= other.b

        # Return If a > b
        def __gt__(self, other):
            return other.__lt__(self)

        # Return If a >= b
        def __ge__(self, other):
            return other.__le__(self)

        #Return If Equal
        def __eq__(self, other):
            return self.a == other.b \
            and self.b == other.b

        # Return If Not Equal
        def __ne__(self, other):
            return not self.__eq__(other)

    #--- Compare a to b-----------------------------
        def compareTo(self, other):
            return ((self > other) - (self < other))

        def Compare(self, a, b):
            self.a = a
            self.b = b
    # End Compare Class--------------------------------------

    def SortArray(self, arr):
        self.arr = arr
# End SortArray Class---------------------------------------------------