
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def substract(self):
        return self.x - self.y


    
    

object1 = Calculator(8, 1);
print(object1.add())