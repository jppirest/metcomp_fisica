import numpy as np
import matplotlib.pyplot as plt
import random as rd

dt = 0.001
t = 10000

n_particulas = 2

eps = 10.0
sigma = 1.0



x = np.zeros(n_particulas)
y = np.zeros(n_particulas)
z = np.zeros(n_particulas)

vx = np.zeros(n_particulas)
vy = np.zeros(n_particulas)
vz = np.zeros(n_particulas)


def init_conditions():
    x[0] = sigma*rd.random()
    y[0] = sigma*rd.random()
    z[0] = sigma*rd.random()

    vx[0] = sigma*rd.random()
    vy[0] = sigma*rd.random()
    vz[0] = sigma*rd.random()

    x[1] = x[0] + 2*sigma*rd.random()
    y[1] = y[0] + 2*sigma*rd.random()
    z[1] = z[0] + 2*sigma*rd.random()

    vx[1] = sigma*rd.random()
    vy[1] = sigma*rd.random()
    vz[1] = sigma*rd.random()


init_conditions()

#def forces():
    #for i in range(0,n_particulas):

F = (0,0,0)
F = 2*F
print(F)
