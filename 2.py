class Car:
    def printSize(self):
        print("small")

class HatchBack(Car):
    def printSize(self):
        super().printSize() #This statement prints the parent class value in the result.
        print("medium")

hatch=HatchBack()
hatch.printSize()