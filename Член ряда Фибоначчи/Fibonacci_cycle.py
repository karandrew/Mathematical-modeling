n = int(input("Номер элемента = "))
a = 0
b = 1
if n == 1:
    c = a
elif n == 2:
    c = b
else:
    for i in range(n-2):
        c = a + b
        a = b
        b = c
print("Значение:",c)
    
