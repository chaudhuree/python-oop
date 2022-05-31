class OperatingSystem:
    multitask=True
    name='Lenovo'

class Lenovo:
    website="www.lenovo.com"
    name='e15'

# inheritate from two parents and name is lenovo not e15 because of order
class Laptop(OperatingSystem,Lenovo):
    def __init__(self):
        if self.multitask is True:
            print(f"your favourite laptop is {self.name}")
            print(f"buy it from here: {self.website}")

mylaptop= Laptop()
