
class RangeDict:
    """

    A dictionary that have ranged keys.

    The set method can be used in two ways:
    d.set(1, 1, 'a') will set 'a' on key 1;
    d.set(2, 5, 'b') will set 'b' on keys 2 to 5, inclusive.

    All values in the range are inclusive, so it does not function like the
    standard range function.

    To get a value, use the method get:
    d.get(1) will return 'a';
    d.get(5) will return 'b'.

    """
    def __init__(self):
        self._dict = {}

    def set(self, begin_range, end_range, value):
        for key in range(begin_range, end_range+1):
            self._dict[key] = value

    def get(self, index):
        return self._dict[index]
