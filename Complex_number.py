# complex number
# for sub: (a + bi) + (c + di) -----> (a + c) + (b + d)i
# for mul: (a + bi) * (c + di) -----> (ac) + (adi) + (bci) + (bdi)
# for sub: (a + bi) - (c + di) -----> (a - c) + (b - d)i

from unittest import result


class complex_number:
    def __init__(self, x=None , y=None):
        self.x = x
        self.y = y

    def add(self , B):
        result=complex_number()
        result.x = self.x + B.x
        result.y = self.y + B.y
        return result

    def mul(self, B):
        result = complex_number()
        result.x = self.x * B.x + self.x + B.y
        result.y = self.y * B.x + self.y + B.y
        return result

    def sub(self, B):
        result = complex_number()
        result.x = self.x - B.x
        result.y = self.y - B.y
        return result

    def show(self):
        return str(self.x ) + '+' + str(self.y) + 'i'

numerator1 = int(input())
denominator1 = int(input())

numerator2 = int(input())
denomirator2 = int(input())

complex1=complex_number(numerator1,denominator1)
complex2=complex_number(numerator2,denomirator2)

print('ADD:')
print((complex1.add(complex2)).show(),'\n')

print('MUL:')
print((complex1.mul(complex2)).show(),'\n')

print('SUB:')
print((complex1.sub(complex2)).show(),'\n')
