from numpy import *
from scipy import integrate
import matplotlib.pyplot as plt

alpha = float(input("Коэффициент рождаемости жертв: "))
beta = float(input("Коэффициент смертности жертв: "))
gamma = float(input("Коэффициент убыли хищников: "))
delta = float(input("Коэффициент рождаемости хищников: "))

def dX_dt(X, t=0):
    return array([ alpha*X[0] -   beta*X[0]*X[1] ,  
                  -gamma*X[1] + delta*X[0]*X[1] ])

t = linspace(0, 15, 1000)              
X0 = array([10, 5])                    

X = integrate.odeint(dX_dt, X0, t)

rabbit, fox = X.T

f1 = plt.figure()
plt.plot(t, rabbit, 'g-', label='Жертвы')
plt.plot(t, fox  , 'r-', label='Хищники')
plt.grid()
plt.legend(loc='best')
plt.xlabel('Время')
plt.ylabel('Популяция')
plt.title('Модель Лотки-Вольтерры')
f1.savefig('modelX.png')
