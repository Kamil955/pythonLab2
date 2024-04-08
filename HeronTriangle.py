def TriangleArea(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def main():
    while True:
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))

        if(a <= 0 or b <= 0 or c <= 0):
            print("Sides must be positive")
            continue
        
        if(a + b <= c or a + c <= b or b + c <= a):
            print("This triangle does not exist")
            continue
    
        print(f"Area of triangle is equal: {TriangleArea(a, b, c)}")
        break

if __name__ == "__main__":
    main()