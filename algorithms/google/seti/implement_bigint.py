class BigInt(object):
    # stored in reversed order
    def __init__(self, s):
        self.sign, self.digits = self.parse_str(s)

    def parse_str(self, s):
        sign = 1
        digits = []

        if not s:
            digits.append(0)
        elif s[0] == '-':
            sign = -1

        for i in range(len(s) - 1, -1, -1):
            if s[i].isdigit():
                digits.append(int(s[i]))

        return sign, digits

    def increment(self):
        if self.sign < 0:
            return self.decrement()

        carry = 1
        for i in range(len(self)):
            carry, digit = divmod(self[i] + carry, 2)
            self[i] = digit
        if carry:
            self.digits.append(1)
        return self

    def decrement(self):
        if self.sign < 0:
            return self.increment()

        carry = -1
        for i in range(len(self)):
            carry, digit = divmod(self[i] + carry, 2)
            self[i] = digit
        if self[-1] == 0:
            self.digits.pop()
        return self

    def __cmp__(self, other):
        if self.sign > 0 and other.sign < 0:
            return 1
        if self.sign < 0 and other.sign > 0:
            return -1
        if len(self) > len(other):
            return 1
        if len(self) < len(other):
            return -1
        for i in range(len(self)):
            if self[i] == 1 and other[i] == 0:
                return 1
            if self[i] == 0 and other[i] == 1:
                return -1
        return 0

    def __len__(self):
        return len(self.digits)

    def __getitem__(self, i):
        return self.digits[i]

    # operators overloading
    # do it in binary form just like the way we do in tenth form
    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass

    # and bit operations...
