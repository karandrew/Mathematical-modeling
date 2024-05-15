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


            #S1 += math.sinh(n*math.pi*x)/(n*math.pi) * (1-math.cos(math.degrees(n*math.pi))) * math.sin(math.degrees(n*math.pi*y/b))/math.sinh(n*math.pi*a/b)
            #S2 += math.sinh(n*math.pi*y)/(n*math.pi) * (1-math.cos(math.degrees(n*math.pi))) * math.sin(math.degrees(n*math.pi*x/a))/math.sinh(n*math.pi*b/a)


'''
fig = plt.figure()
mat = plt.matshow(n, fignum=0, vmin=0, vmax=1)
def update(event):
    if event.key == "enter":
        for i in range(1,10):
            for j in range(1,10):
                n[i][j] = 0.25*(n[i-1][j] + n[i+1][j] + n[i][j-1] + n[i][j+1])
        mat.set_data(n)
        fig.canvas.draw_idle()
fig.canvas.mpl_connect("key_press_event", update)
plt.show()

'''

'''
[[ 0.5         1.          1.          1.          1.          1.          1.          1.          1.          1.          1.        ]
 [ 0.          0.5         0.69809696  0.79238783  0.84594052  0.88170673  0.9092855   0.93319763  0.95570004  0.97785002  1.        ]
 [ 0.          0.30190304  0.5         0.62551383  0.70966751  0.77160089  0.82223765  0.86780497  0.91175251  0.95570004  1.        ]
 [ 0.          0.20761217  0.37448617  0.5         0.5956148   0.67279168  0.74025924  0.80403211  0.86780497  0.93319763  1.        ]
 [ 0.          0.15405948  0.29033249  0.4043852   0.5         0.5836918   0.66197552  0.74025924  0.82223765  0.9092855   1.        ]
 [ 0.          0.11829327  0.22839911  0.32720832  0.4163082   0.5         0.5836918   0.67279168  0.77160089  0.88170673  1.        ]
 [ 0.          0.0907145   0.17776235  0.25974076  0.33802448  0.4163082   0.5         0.5956148   0.70966751  0.84594052  1.        ]
 [ 0.          0.06680237  0.13219503  0.19596789  0.25974076  0.32720832  0.4043852   0.5         0.62551383  0.79238783  1.        ]
 [ 0.          0.04429996  0.08824749  0.13219503  0.17776235  0.22839911  0.29033249  0.37448617  0.5         0.69809696  1.        ]
 [ 0.          0.02214998  0.04429996  0.06680237  0.0907145   0.11829327  0.15405948  0.20761217  0.30190304  0.5         1.        ]
 [ 0.          0.          0.          0.          0.          0.          0.          0.          0.          0.          0.5       ]]
'''
