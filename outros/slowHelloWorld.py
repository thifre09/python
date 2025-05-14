import random
import time

class H:

    def __init__(self, num1: int, num2: int, num3: int):
        self.num1: int = num1
        self.num2: int = num2
        self.num3: int = num3

    def verificarIgualdade(self):
        if self.num1 == self.num2 == self.num3:
            time.sleep(5)
        elif self.num1 == self.num2:
            time.sleep(4)
        elif self.num2 == self.num3:
            time.sleep(3)
        elif self.num3 == self.num1:
            time.sleep(2)
        else:
            time.sleep(10)
        
        return True

class E:

    def verificarA(self):
        a = ""
        for i in range(600000):
            a += "a"
        
        a = a
        if a == a:
            a = a
            return True


class L:
    
    def verificarAleatorio(self):
        aleatorio1 = random.randint(1, 1000000)
        aleatorio2 = random.randint(1, 1000000)

        while aleatorio1 != aleatorio2:
            aleatorio2 = random.randint(1, 1000000)
        return True

class O:
    def __init__(self):
        pass

class W:
    def __init__(self):
        pass

class R:
    def __init__(self):
        pass

class D:
    def __init__(self):
        pass

class HelloWorld(H, E, L, O, W, R, D):
    def __init__(self):
        pass


a = ""
for i in range(700000):
    a += "a"

print("AAA")