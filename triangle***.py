# a)
n = int(input("Enter the number of rows: "))
for i in range(n):
    i+=1
    print(i*"*")
#b)
print()
def triangle(n):
    if n == 0:
        return "*"
        
    triangle(n-1)
    print(n*"*")

triangle(5)