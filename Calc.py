#Calculator продовжує роботу 
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
        try:
            r = self.x / self.y
        except ZeroDivisionError:
            r = ('На 0 ділити ніні')
        finally:
            return r
 


    
    

object1 = Calculator(8, 0);
