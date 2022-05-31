class StaticMethod:
    def name(self):
        self.name="chaudhuree"
    @staticmethod
    def add(a,b):
        return a+b
    # in static method no need to add self


stat = StaticMethod()
print(stat.add(1,2))
print(StaticMethod.add(3,4))