import numpy as np
import matplotlib.pyplot as plt
import time
import math
matrix = [[0.5, 1,1,1,1,1,1,1,1,1, 1],
             [0, 0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5, 1],
             [0, 0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5, 1],
             [0, 0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5, 1],
             [0, 0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5, 1],
             [0, 0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5, 1],
             [0, 0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5, 1],
             [0, 0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5, 1],
             [0, 0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5, 1],
             [0, 0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5, 1],
             [0, 0,0,0,0,0,0,0,0,0, 0.5]]
a=1
b=1
h=1/10
for i in range(1,10):
    for j in range(1,10):
        S1 = 0
        S2 = 0
        k=1
        x = j * h
        y = 1 - i * h
        for n in range(1,4000):
            S1 += math.sinh(math.radians(n*math.pi*x))/(n*math.pi) * (1-math.cos(math.radians(n*math.pi))) * math.sin(math.radians(n*math.pi*y/b)) / math.sinh(math.radians(n*math.pi*a/b))
            S2 += math.sinh(math.radians(n*math.pi*y))/(n*math.pi) * (1-math.cos(math.radians(n*math.pi))) * math.sin(math.radians(n*math.pi*x/a)) / math.sinh(math.radians(n*math.pi*b/a))
        matrix[i][j] = 2/b*S1+2/a*S2
for i in range(0,11):
    print(matrix[i])
fig = plt.figure()
plt.imshow(matrix)
plt.colorbar()
plt.show()


f = open('data2.txt', 'w')
for j in range(0,11):
    r=""
    for i in range(0,11):
        x = 1-i/10
        y = j/10
        r += str(x) + " " + str(y) + " " + str(matrix[i][j]) + "\n"
    r+="\n"
    f.write(r)
f.close()
