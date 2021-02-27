import operator


class eq:

    def __init__(self, value):
        self.value = value
        self.ops = {
            '<' : operator.lt,
            '<=' : operator.le,
            '=' : operator.eq,
            '>' : operator.gt,
            '>=' : operator.ge,
        }

    def is_logically_in_range(self, min_, max_, logical_operator, than):
        for i in range(min_, max_):
            if not self.ops[logical_operator](self.value(i), than):
                return False
        return True


eq1 = eq(lambda x : (3*x-1)/(x+1))

#print(eq1.is_logically_in_range(3,'>',10))
print(eq1.is_logically_in_range(3,10000,'<=',3))
print(not eq1.is_logically_in_range(-10000,2,'<=',3))

eq2 = eq(lambda x : abs(x-1)-abs(x))
print(eq2.is_logically_in_range(1,100,'>',0))
