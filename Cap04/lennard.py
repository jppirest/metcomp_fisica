
import numpy as np
import random as random
import numpy as np
import matplotlib.pyplot as plt
import string

def date(txt):
	y=open(txt,"r")
	header = y.readlines()[0:5]
	count=0
	for item in header:
		print(item)
		header[count]=float(item)
		count+=1
	
	return header
class point(object):
	"""docstring for point"""
	def __init__(self, x=0,y=0,z=0,vx=0,vy=0,vz=0):
		self.X = x
		self.Y = y
		self.Z = z
		self.VX = vx
		self.VY = vy
		self.VZ = vz
	def move(self,Fx,Fy,Fz,dt):
		self.VX = self.VX + dt*Fx
		self.VY = self.VZ + dt*Fy
		self.VZ = self.VZ + dt*Fz
		self.X = self.X + self.VX*dt 
		self.Y = self.Y +self.VY*dt
		self.Z = self.Z +self.VZ*dt
	def getX(self):
		x = self.X
		return x 
	def getY(self):
		return self.Y 
	def getZ(self):
		return self.Z
	def K(self):
		return ((self.VX**2+self.VY**2+self.VZ**2)/2) 
	def __str__(self):
		return "Point(%s,%s,%s)"%(self.X,self.Y,self.Z)

def inicial(sigma):
	rx = random.uniform(0,3)
	ry = random.uniform(0,3)
	rz = random.uniform(0,3)
	vx = random.uniform(0,1)
	vy = random.uniform(0,1)
	vz = random.uniform(0,1)
	alfabeto=list(string.ascii_uppercase)
	A= point(rx,ry,rz,vx,vy,vz)
	B= point(rx+2*sigma,ry+2*sigma,rz+2*sigma,vx,vy,vz)
	C= point(rx+7*sigma*random.uniform(0,1),ry+7*sigma*random.uniform(0,1),rz+7*sigma*random.uniform(0,1),vx*random.uniform(0,1),vy,vz)
	D= point(rx+4*sigma*random.uniform(0,1),ry+4*sigma*random.uniform(0,1),rz+4*sigma*random.uniform(0,1),vx*random.uniform(0,1),vy,vz)
	E= point(rx+2*sigma*random.uniform(0,1),ry+2*sigma*random.uniform(0,1),rz+2*sigma*random.uniform(0,1),0,0,vz)
	F= point(rx+3*sigma*random.uniform(0,2),ry+3*sigma*random.uniform(0,1),rz+3*sigma*random.uniform(0,2),vx,random.uniform(0,1),vz)
	G= point(rx+5*sigma*random.uniform(0,2),ry+5*sigma*random.uniform(0,2),rz+5*sigma*random.uniform(0,1),random.uniform(0,1),vy,vz)
	return A,B,C,D,E,F,G

def forca(lista,sigma,eps):
	forcas=[]
	F=(0,0,0)
	for i in lista:
		Fx1=0
		Fy1=0
		Fz1=0
		for j in lista:
			if j==i:
				continue
			else:
				r=((+j.getX()-i.getX())**2+(j.getY()-i.getY())**2+(j.getZ()-i.getZ())**2)**0.5
				V=24*eps*((sigma/r)**12-(sigma/r)**6)/r**2
				Fx1 += (j.getX()-i.getX())*V
				Fy1 += (j.getY()-i.getY())*V
				Fz1 += (j.getZ()-i.getZ())*V
				#print((j.getX()-i.getX())*V)
		F=(-Fx1,-Fy1,-Fz1)
		#print(F)
		forcas.append(F)
	#r=((+x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**0.5
	#V=24*eps*((sigma/r)**12-(sigma/r)**6)/r**2
	#print(-x2+x1,+x2-x1)
	return forcas

dados=date("dados.dat")
Nt=dados[0]
dt=dados[1]
Np=dados[2]
eps=dados[3]
sigma=dados[4]
A,B,C,D,E,F,G=inicial(sigma)
part=[A,B,C,D,E,F,G]
N=10000
#print(part)
#print(F1,F2)
#print(listF)
#print((listF[0])[0])
temp=np.linspace(0,N*dt,N)
Ax= []
Ay= []
Az= []
Ak= []
Bx = []
By = []
Bz= []

Cy = []
Cx = []
Cz= []
Dy = []
Dx = []
Dz = []
Ey = []
Ex = []
Ez = []
Fy = []
Fx = []
Fz = []
Gx = []
Gy = []
Gz =[]
for i in range(0,N):
	listaF= forca(part,sigma,eps)
	#print(listaF)
	A.move((listaF[0])[0],(listaF[0])[1],(listaF[0])[2],dt)
	B.move((listaF[1])[0],(listaF[1])[1],(listaF[1])[2],dt)
	C.move((listaF[2])[0],(listaF[2])[1],(listaF[2])[2],dt)
	D.move((listaF[3])[0],(listaF[3])[1],(listaF[3])[2],dt)
	E.move((listaF[4])[0],(listaF[4])[1],(listaF[4])[2],dt)
	F.move((listaF[5])[0],(listaF[5])[1],(listaF[5])[2],dt)
	G.move((listaF[6])[0],(listaF[6])[1],(listaF[6])[2],dt)
	Ax.append(A.getX())
	Ay.append(A.getY())
	Az.append(A.getZ())
	Ak.append(A.K())
	Bx.append(B.getX())
	By.append(B.getY())
	Bz.append(B.getZ())
	Cx.append(C.getX())
	Cy.append(C.getY())
	Cz.append(C.getZ())
	Dx.append(D.getX())
	Dy.append(D.getY())
	Dz.append(D.getZ())
	Ex.append(E.getX())
	Ey.append(E.getY())
	Ez.append(E.getZ())
	Fx.append(F.getX())
	Fy.append(F.getY())
	Fz.append(F.getZ())
	Gx.append(G.getX())
	Gy.append(G.getY())
	Gz.append(G.getY())
	if i==50:
		plt.plot(Ax,Ay,'k',Bx,By,'r',Cx,Cy,'b',Dx,Dy,'g',Ex,Ey,'c',Fx,Fy,'m',Gx,Gy,'y')
		plt.show()
	if i==N-20:
		plt.plot(Ax,Ay,'k',Bx,By,'r',Cx,Cy,'b',Dx,Dy,'g',Ex,Ey,'c',Fx,Fy,'m',Gx,Gy,'y')
		plt.show()
#print(listaF)
print(Ak)
ax = plt.axes(projection='3d')
ax.plot3D(Ax,Ay,Az)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()


plt.plot(temp,Ak)
plt.show()
#x1,y1,z1,x2,y2,z2