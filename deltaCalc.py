import math as math
def Main():
    a = int(input("Enter the first parametr: "))
    b = int(input("Enter the second parametr: "))
    c = int(input("Enter the third parametr: "))

    delta_val = delta(a,b,c)
    if delta_val is not None:
         points = zeroPoints(delta_val, a,b)
         print("Zero point(s):", points)


def delta(a, b,c):
    delta_val = b**2-(4*a*c)
    if(delta_val)<0:
        print("No zero points in this function")
        return None
    return math.sqrt(delta_val)

def zeroPoints(delta_val, a, b):
    if delta_val >= 0:
        x1 = (-b - delta_val) / (2 * a)
        x2 = (-b + delta_val) / (2 * a)
        if x1 == x2:
            return x1
        return x1, x2
    else:
        return None

if __name__ == "__main__":
    Main()