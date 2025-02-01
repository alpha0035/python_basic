# public members
class Alpha:
    current = 'alpha'
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
alp = Alpha('ymm', 0.55)
print(alp.current, alp.name, alp.rate, sep= '\n')

# protected members
# identified with a single underscore (_)
class Beta:
    def __init__(self, name, rate):
        self._name = name
        self._rate = rate
    def getName(self):
        return self._name
    def getRate(self):
        return self._rate
bta = Beta('sese', 0.33)
print(bta._name)

# identified with a double underscore (__)
# Python’s private and protected members can be accessed outside the class through python name mangling