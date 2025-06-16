from pylab import *

figname='euler_heat10m.png'

##set ranges to plot
xmin=0; xmax=12.0*60*60; dx=60*60*2.0 #every 2 hours
ymin=0; ymax=30.0

t=arange(1.0*xmin,1.0*xmax+dx,dx/100)

##text to display
#eqntex=r'$\mathrm{d} \theta/\mathrm{d} t = - k(\theta-5)$, $k=4.7\times 10^{-5}$'
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

##plot exact solution
u=25.*exp(-k*t)+5
plot(t,u,'g-',linewidth=3.0,label='Exact solution')
title(eqntex)

##change axes to hours
ticks = np.arange(xmin, xmax+1, 60*60)
labels = range(ticks.size)
xticks(ticks, labels)
axis([xmin, xmax, ymin, ymax])


for dt,col in [(60*60*4,'k*-'),(60*60,'bx-'),(60*10,'r.-')]:
  ##use euler on differential equation
  ti=0
  vi=30.
  tvals=[ti]
  vvals=[vi]
  for ti in arange(dt,12*60*60+dt,dt):
    dv=-k*(vi-5.)*dt
    vi=vi+dv
    tvals.append(ti)
    vvals.append(vi)
  plot(tvals,vvals,col,label=r'$\delta t = %ds$'%dt,markersize=10)
legend()

xlabel(xvarname,size=20)
ylabel(yvarname,size=20)

savefig(figname)


























