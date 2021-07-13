import numpy as np
import matplotlib.pyplot as plt
import random as rd
import pandas as pd
import matplotlib.animation as animation
import matplotlib.patches as mpatches

dt = 0.001
t = 10000

n_particulas = 3

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


    x[2] = x[0] + 2*sigma*rd.random()
    y[2] = y[0] + 2*sigma*rd.random()
    z[2] = z[0] + 2*sigma*rd.random()

    vx[2] = sigma*rd.random()
    vy[2] = sigma*rd.random()
    vz[2] = sigma*rd.random()



init_conditions()

print(x,y,z)

file = open('din_jones.dat', "w")
file.write('x,y,z\n')

for i in range(0,n_particulas):
    file.write(str(x) + ',' + str(y) + ',' + str(z) + '\n' )

for i in range(0,n_particulas):
    nome = 'particula' + str(i) + '.dat'
    arquivo = open(nome, "w")
    arquivo.write('x,y,z\n')
    arquivo.write(str(x[i]) + ',' + str(y[i]) + ',' + str(z[i]) + '\n' )
    arquivo.close()

def forces(x,y,z):
    F = np.zeros((n_particulas,3))
    for i in range(0,n_particulas):
        for j in range(0,n_particulas):
            if i!=j:
                r=np.sqrt((x[i]-x[j])**2 +(y[i]-y[j])**2 +(z[i]-z[j])**2)
                V=24*eps*((sigma/r)**12-(sigma/r)**6)/r
                F[i][0] += (x[i]-x[j])*V/r
                F[i][1] += (y[i]-y[j])*V/r
                F[i][2] += (z[i]-z[j])*V/r
    return F

def move(x,y,z,vx,vy,vz):
    F = forces(x,y,z)
    for i in range(0,n_particulas):
        vx[i] = vx[i]+dt*F[i][0]
        vy[i] = vy[i]+dt*F[i][1]
        vz[i] = vz[i]+dt*F[i][2]

        x[i]=x[i] + vx[i]*dt
        y[i]=y[i] + vy[i]*dt
        z[i]=z[i] + vz[i]*dt
        nome = 'particula' + str(i) + '.dat'
        arquivo = open(nome, "a")
        arquivo.write(str(x[i]) + ',' + str(y[i]) + ',' + str(z[i]) + '\n' )
        arquivo.close()
    file.write(str(x) + ',' + str(y) + ',' + str(z) + '\n' )



def run():
    for i in range(0,1000):
        move(x,y,z,vx,vy,vz)
run()

file.close()

particula0 = pd.read_csv('particula0.dat', header = 0)
particula1 = pd.read_csv('particula1.dat', header = 0)
particula2 = pd.read_csv('particula2.dat', header = 0)

particulas = [particula0,particula1,particula2]

#fig=plt.figure()
#ax=fig.gca(projection ='3d')


#aux = 0
#for dados in particulas:
    #ax.plot(dados['x'],dados['y'],dados['z'], label = 'Particula ' + str(aux) )
    #ax.scatter(dados['x'][0],dados['y'][0],dados['z'][0], color = 'black', label = 'Posicao Inicial' + str(aux) )
    #aux += 1

#plt.legend()
#plt.show()

xp0 = particula0['x'].tolist()
yp0 = particula0['y'].tolist()
zp0 = particula0['z'].tolist()

xp1 = particula1['x'].tolist()
yp1 = particula1['y'].tolist()
zp1 = particula1['z'].tolist()

xp2 = particula2['x'].tolist()
yp2 = particula2['y'].tolist()
zp2 = particula2['z'].tolist()


def animacao():
    fig=plt.figure()
    ax=fig.gca(projection ='3d')
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.set_zlim(-10,10)
    lines = []
    i = 1
    for i in range(1000):
        #for dados in particulas:
        head = i - 1
        line1, = ax.plot(xp0[:i],yp0[:i],zp0[:i] , zorder = 1, color = 'black')
        line2, = ax.plot([xp0[head]],[yp0[head]], [zp0[head]], color = 'red', marker = 'o', markeredgecolor = 'r', zorder = 20)

        line3, = ax.plot(xp1[:i],yp1[:i],zp1[:i] , zorder = 1, color = 'black')
        line4, = ax.plot([xp1[head]],[yp1[head]], [zp1[head]], color = 'blue', marker = 'o', markeredgecolor = 'blue', zorder = 20)

        line5, = ax.plot(xp2[:i],yp2[:i],zp2[:i] , zorder = 1, color = 'black')
        line6, = ax.plot([xp2[head]],[yp2[head]], [zp2[head]], color = 'green', marker = 'o', markeredgecolor = 'green', zorder = 20)

        lines.append([line1, line2, line3, line4, line5, line6])
    #FFwriter = animation.FFMpegWriter(fps=30)
    anim = animation.ArtistAnimation(fig,lines,interval=1, blit = True)
    plt.rcParams['animation.html'] = 'html5'
    #anim.save('animacao.mp4', writer = FFwriter, dpi = 80)
    plt.show()



animacao()
