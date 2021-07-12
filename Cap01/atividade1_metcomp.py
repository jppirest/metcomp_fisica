import numpy as np
import time

def trapezioa(xi, xf, N):
    global starta
    starta = time.time()
    dx = (xf-xi)/(N)
    integral = 0
    for i in range(0,N+1):
        integral += dx*(f(xi+i*dx))
    global enda
    enda = time.time()
    return integral

def trapezio1d(xi, xf, N): #Algoritmo igual ao algoritmo trapeziob
    global startb
    startb = time.time()
    dx = (xf-xi)/(N)
    x = xi
    integral = 0
    while (x+dx<xf):
        f1 = f(x)
        f2 = f(x+dx)
        integral += 0.5*(f1+f2)
        x = x+dx
    global endb
    endb = time.time()
    return dx*integral

def trapeziob(xi, xf, N): #Faz a media no ponto. x[i] = (x[i-1] + x[i+1])*0.5
    global startb
    startb = time.time()
    dx = (xf-xi)/(N)
    integral = (f(xi)+f(xf))*0.5 #Precisamos incluir xi e xf, ja que eles nao sao calculados na iteracao.
    for i in range(1,N):
        integral += f(xi+i*dx)
    global endb
    endb = time.time()
    return dx*integral

def trapezoid(A,B,N): #Landau's Book Algorithm, equals to trapeziob
    global startL
    startL = time.time()
    h = (B-A)/(N)
    sum = (f(A)+f(B))*0.5
    for i in range(1,N):
        sum += f(A+i*h)
    global endL
    endL = time.time()
    return h*sum

def simpson(xi, xf, N):
    global starts
    starts = time.time()
    dx = (xf-xi)/(N)
    integral = (dx/3)*(f(xi) + f(xf))
    h = 4.
    for i in range(1,N):
        integral += (h/3)*(dx*f(xi+i*dx))
        if i%2==0:
            h=4
        elif i%2==1:
            h=2
    global ends
    ends = time.time()
    return integral


xi = 0
xf = 1
N = int(1e3)
dx = (xf-xi)/(N)


def f(x):
    return (1-(x**2))**(1/2)

pi_4 = np.pi/4


a = trapezioa(xi,xf,N)
b = trapeziob(xi,xf,N)
c = simpson(xi,xf,N)


print('Estudante: João Pedro Pires Thomaz \nMatrícula: 2019035086 \n')
print('Integrando a função f(x) = (1-(x**2))**(1/2)')
print('\nTomando o intervalo de [0,1], com N =', N, ' \n')
print('\nPi/4 = ', pi_4, '\n')
print ('Trapézio: Algoritmo Simples =', a, '. Tempo =', enda-starta)

print ('Trapézio: Algoritmo Composto =', b, '. Tempo =', endb-startb)

print ('Parábola: Regra de Simpson =', c, '. Tempo =', ends-starts, '\n')
print ('Vemos que o Método da Parábola é mais efetivo.\n ')

erroa = abs(pi_4 - a)
errob = abs(pi_4 - b)
erroc = abs(pi_4 - c)


print('Erro relativo Trapézio Simples =', erroa**2, '\n')
print('Erro relativo Trapezio Composto =', errob**2, '\n')
print('Erro relativo Parábola Simpson =', erroc**2, '\n')
print('Valor de dx^2 = ', dx**2)
