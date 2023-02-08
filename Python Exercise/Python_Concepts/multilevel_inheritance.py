class Cars:

    def audi(self):
        print("Audi")

    def bmw(self):
        print("BMW")

    def ford(self):
        print("Ford")


class Colour(Cars):

    def red(self):
        print("red")

    def black(self):
        print("black")

    def blue(self):
        print("blue")


class Buyers(Colour):

    def buyer1(self):
        self.audi()
        self.red()

    def buyer2(self):
        self.bmw()
        self.black()

    def buyer3(self):
        self.ford()
        self.blue()


data = Buyers()
data.buyer1()
data.buyer2()
data.buyer3()
