class StaticMethod:
    def __init__(self,name):
        self.name=name
    @staticmethod
    def add(a,b):
        return a+b
    # in static method no need to add self


stat = StaticMethod('chaudhuree')
print(stat.name)
print(stat.add(1,2))
print(StaticMethod.add(3,4))