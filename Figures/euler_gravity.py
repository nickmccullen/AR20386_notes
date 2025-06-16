from pylab import *

figname='euler_gravity.png'

##set ranges to plot
xmin=0; xmax=8; dx=1
ymin=0; ymax=40; dy=10

##create a mesh
t=arange(1.0*xmin,1.0*xmax+dx,dx/100.)
y=arange(1.0*ymin,1.0*ymax+dy,dy)

##text to display
eqntex=r"$v' = 9.8$"

##plot exact solution
u=49.*(1-exp(-t/5.))
plot(t,u,'r-',label=r"Solution Curve")

v=0
##define differential equation
dt=1.
dv=(9.8-v/5.)*dt

#plot initial slope
plot([0,ymax/dv],[0,ymax])
plot([0,dx],[0,dv],'k-',label="Approximation")

text(0.4, 10.1, r'$\delta t$')
text(1.1, 5, r"$\delta v = v'\delta t$")
plot([dt,dt],[0,dv],'k--.')
plot([0,dt],[dv,dv],'k--.')

title(eqntex)
legend(loc=4)
axis([xmin, xmax, ymin, ymax])

##plotting stuff
xlabel(r'$t$ ($s$)',size=20)
ylabel(r'$v$ ($m/s$)',size=20)



savefig(figname)
