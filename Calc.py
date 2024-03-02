
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def substract(self):
        return self.x - self.y
    def multiply(self):
        return self.x * self.y
    def division(self):
        if self.x == 0 or self.y == 0:
            return None
        else:
            return self.x / self.y


    
    

object1 = Calculator(8, 0);
print(object1.division())