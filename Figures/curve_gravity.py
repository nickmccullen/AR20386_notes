from pylab import *

figname='curve_gravity.png'

##set ranges to plot
xmin=0; xmax=25; dx=1
ymin=0; ymax=60; dy=10

##create a mesh
t=arange(1.0*xmin,1.0*xmax+dx,dx)
y=arange(1.0*ymin,1.0*ymax+dy,dy)

##text to display
eqntex="$v' = 9.8 - {v}/{5}$"

##plot exact solution
u=49.*(1-exp(-t/5.))
plot(t,u,'r-',label='Solution Curve')

v=0
##define differential equation
dt=1.
dv=(9.8-v/5.)*dt

#plot initial slope
plot([0,ymax/dv],[0,ymax],label=r"Initial gradient $v_0=0$, $v'_0=9.8$")

#plot equilibium
plot([0,25],[49,49],label=r"Equilibrium $v'=0$, $v^*=49$")

title(eqntex)
legend(loc=4)
#axis([xmin, xmax, ymin, ymax])





##plotting stuff
xlabel(r'$t$ ($s$)',size=20)
ylabel(r'$v$ ($m/s$)',size=20)



savefig(figname)
