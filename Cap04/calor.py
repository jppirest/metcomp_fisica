import numpy as np
import matplotlib.pyplot as plt

def f_inicial(x):
    return 3.15*np.sin(x)

def condicao_inicial(xi,xf,ti,tf,N):
    global dx
    dx = (xf-xi)/N
    f0 = np.zeros(N+1) #N+1 para podermos indexar o ultimo valor.
    i = xi
    count = 0
    while i<=xf:
        f0[count] = f_inicial(i)
        i = i+dx
        count += 1
    f0[0] = ti
    f0[N] = tf
    file = open('CondInicial.txt', "w") #apenas para salvar o arquivo da cond. inicial.
    file.write(str(f0) + '\n')
    file.close()
    np.savetxt('Evolucao.dat', f0)
    return f0

def passo(file_before,dt):
    f0 = np.loadtxt(file_before)
    f1 = np.zeros(len(f0))
    k = 1
    for i in range(len(f0)):
        if i == 0:
            f1[i] = f0[i] #manter as extremidades fixadas
        elif i== (len(f0) - 1):
            f1[i] = f0[i]
        else:
            f1[i]=f0[i]+k*dt/dx**2*(f0[i-1]-2*f0[i]+f0[i+1])

    np.savetxt(file_before, f1)
    #data.write(str(f1) + '\n')
    return f1

xf = 20.5
xi = 0
N = 100
ti = 0
tf = 2.25
dt = 0.001

condicao_inicial(xi,xf,ti,tf,N)

#data = open('Data.txt', "w+")

x = np.linspace(xi,xf,N+1)

i=0
while (i<=150000):
    passo('Evolucao.dat', dt)
    if i==0:
        plt.clf()
        plt.plot(x,passo('Evolucao.dat', dt))
        plt.xlabel('x(m)')
        plt.ylabel('Temperatura (Celsius)')
        plt.title('Instate t = ' + str(i*dt) + 's')
        plt.savefig('t_0.png', format = 'png')
    elif i==2000:
        plt.clf()
        plt.plot(x,passo('Evolucao.dat', dt))
        plt.xlabel('x(m)')
        plt.ylabel('Temperatura (Celsius)')
        plt.title('Instate t = ' + str(i*dt) + 's')
        plt.savefig('t_2.png', format = 'png')
    elif i==3000:
        plt.clf()
        plt.plot(x,passo('Evolucao.dat', dt))
        plt.xlabel('x(m)')
        plt.ylabel('Temperatura (Celsius)')
        plt.title('Instate t = ' + str(i*dt) + 's')
        plt.savefig('t_3.png', format = 'png')
    elif i==5000:
        plt.clf()
        plt.plot(x,passo('Evolucao.dat', dt))
        plt.xlabel('x(m)')
        plt.ylabel('Temperatura (Celsius)')
        plt.title('Instate t = ' + str(i*dt) + 's')
        plt.savefig('t_5.png', format = 'png')
    elif i==10000:
        plt.clf()
        plt.plot(x,passo('Evolucao.dat', dt))
        plt.xlabel('x(m)')
        plt.ylabel('Temperatura (Celsius)')
        plt.title('Instate t = ' + str(i*dt) + 's')
        plt.savefig('t_10.png', format = 'png')
    elif i==50000:
        plt.clf()
        plt.plot(x,passo('Evolucao.dat', dt))
        plt.xlabel('x(m)')
        plt.ylabel('Temperatura (Celsius)')
        plt.title('Instate t = ' + str(i*dt) + 's')
        plt.savefig('t_50.png', format = 'png')
    elif i==100000:
        plt.clf()
        plt.plot(x,passo('Evolucao.dat', dt))
        plt.xlabel('x(m)')
        plt.ylabel('Temperatura (Celsius)')
        plt.title('Instate t = ' + str(i*dt) + 's')
        plt.savefig('t_100.png', format = 'png')
    elif i==150000:
        plt.clf()
        plt.plot(x,passo('Evolucao.dat', dt))
        plt.xlabel('x(m)')
        plt.ylabel('Temperatura (Celsius)')
        plt.title('Instate t = ' + str(i*dt) + 's')
        plt.savefig('t_150.png', format = 'png')

    i+=1

#data.close()
