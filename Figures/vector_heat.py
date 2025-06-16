from pylab import *
from matplotlib import rc

figname='vector_heat.png'

##set ranges to plot
xmin=0; xmax=24.0*60*60; dx=60*60*2.0 #every 2 hours
ymin=-5.0; ymax=30.0; dy=5.0


##create a mesh
x=arange(1.0*xmin,1.0*xmax,dx)
y=arange(1.0*ymin,1.0*ymax+dy,dy)
X,Y = meshgrid(x,y)

##text to display
eqntex=r'$\mathrm{d} \theta/\mathrm{d} t = - k(\theta-5)$, $k=4.7\times 10^{-5}$'
xvarname=r'$t\ (hours)$'
yvarname=r'$\theta\ (^\circ C)$'

U=1.0 #average W/m^2/dK
Cp=1000.0 #J/(kg*K) #assume all same at 1. J/g/K
rho_air=1.#25 #kg/m^3
rho_walls=1000.0 #kg/m^3

A=(5*5)*4.0 #m^2 area of walls and roof
V=5*5*5.0-1 #m^3 volume of internal space

m_air=rho_air*V #mass of air (kg)
tma=Cp*m_air #thermall mass of air (J/K)

V_struct=A*0.02 #assume light walls
m_struct=1000.0*V_struct#+4000.
tms=Cp*m_struct #thermal mass of structure (kJ/K)

C=U*A #J/(s*dK) total conductivity 
k=C/(tma+tms) #1/s

print m_air,m_struct,tma,tms,C,k

t = X
v = Y

##define differential equation
dt=ones(shape(X))
dv=-k*(v-5.)*dt

##plotting stuff
dX=dt#/float(xmax-xmin)
dY=dv#/float(ymax-ymin)
Q = quiver(X, Y, dX, dY,angles='xy', scale_units='xy',scale=0.75/3600.)
qk = quiverkey(Q, 0.5, 1.025, 2, eqntex,fontproperties={'weight': 'bold'})
xlabel(xvarname,size=20)
ylabel(yvarname,size=20)
#, rotation=0


l,r,b,t = axis()
hx, hy = r-l, t-b
#axis([l-0.05*hx, r+0.05*hx, b-0.05*hy, t+0.05*hy])

v=arange(1.0*xmin,1.0*xmax+dx,dx/5)
u=25.*exp(-k*v)+5
plot(v,u,'r-')

#axis([l, r+1, b, t])
axis([0, 24, -5, 30])

ticks = np.arange(xmin, xmax+1, 60*60)
labels = range(ticks.size)
xticks(ticks, labels)


savefig(figname)
