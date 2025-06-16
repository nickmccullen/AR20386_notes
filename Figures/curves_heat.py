from pylab import *
from matplotlib import rc

figname='curves_heat.png'

##set ranges to plot
xmin=0; xmax=24.0*60*60; dx=60*60*2.0 #every 2 hours
ymin=-5; ymax=30.0

t=arange(1.0*xmin,1.0*xmax+dx,dx/10)

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

t00=0
for u0 in [30.,15.,5.,-5.]:
  ##plot exact solutions
  A=(u0-5)/exp(-k*t00)
  u=A*exp(-k*t)+5
  plot(t,u,label=r'$t_0=%d$, $\theta_0=%d$'%(t00,u0))
  
u0=30.
for t00 in [5.,10.]:
  ##plot exact solutions
  t0=t00*60*60
  A=(u0-5)/exp(-k*t0)
  u=A*exp(-k*t)+5
  plot(t,u,label=r'$t_0=%d$, $\theta_0=%d$'%(t00,u0))
  
u0=-5.
for t00 in [5.,10.]:
  ##plot exact solutions
  t0=t00*60*60
  A=(u0-5)/exp(-k*t0)
  u=A*exp(-k*t)+5
  plot(t,u,label=r'$t_0=%d$, $\theta_0=%d$'%(t00,u0))

legend(bbox_to_anchor=(1.1, 1.1))
title(eqntex)





##change axes to hours
ticks = np.arange(xmin, xmax+1, 60*60)
labels = range(ticks.size)
xticks(ticks, labels)
axis([xmin, xmax, ymin, ymax])

##use euler on differential equation
dt=60*60*1
ti=0
vi=30.

#for ti in arange(0,12*60*60+dt,dt):
#  dv=-k*(vi-5.)*dt
#  print ti/3600, '&', ti ,'&', vi , '&', dv, r'\\'
#  plot([ti,ti+dt],[vi,vi+dv],'b-')
#  plot([ti+dt,ti+dt],[0,vi+dv],'k.--')
#  vi=vi+dv
  
##plotting stuff
xlabel(xvarname,size=20)
ylabel(yvarname,size=20)

savefig(figname)



























quit()
