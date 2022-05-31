class Apple:
    manufacturer = "Apple Inc."
    contactWebsite = "www.apple.com/contact"

    def contactDetails(self):
        print("To contact us,log on to", self.contactWebsite)


class MacBook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2017

    def manufactureDetails(self):
        print(f"This MacBook was manufactured in the year {self.yearOfManufacture} by {self.manufacturer}")


apple=Apple()
apple.contactDetails()
macbook=MacBook()
print(macbook.yearOfManufacture)
macbook.manufactureDetails()
