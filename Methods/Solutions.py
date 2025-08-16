from typing import Callable

class Solutions(object):
    def __init__(self):
        pass
    def bisection(self, f: Callable[[float], float], a: float, b: float, error: float, max_iter: int):
        i = 0
        F_a = f(a)
        while i <= max_iter:
            if (F_x := f(x := (a + b) / 2)) == 0 or (b - a) / 2 < error:
                return x, i
            
            if F_a * F_x > 0:
                a, F_a = x, F_x
            else:
                b=x
            i+=1

        if i==max_iter:
            print("Maximum iterations reached!")
        return x,i # type: ignore