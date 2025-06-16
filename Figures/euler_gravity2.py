from pylab import *

figname='euler_gravity2.png'

##set ranges to plot
xmin=0; xmax=8; dx=1
ymin=0; ymax=40; dy=10

##create a mesh
t=arange(1.0*xmin,1.0*xmax+dx,dx/100.)
y=arange(1.0*ymin,1.0*ymax+dy,dy)

##text to display
eqntex=''#r"                           $v' = 9.8-v_1/5$"

##plot exact solution
u=49.*(1-exp(-t/5.))
plot(t,u,'r-',label=r"Solution Curve")

v0=0
##define differential equation
dt=1.
t0=0
dv=(9.8-v0/5.)*dt

plot([0,dx],[0,dv],'k-')

#plot initial slope
v1=v0+dv
t1=t0+dt
dv=(9.8-v1/5.)*dt


plot([t1,t1+dt],[v1,v1+dv],'k-',label='Approximation')
plot([t1+dt,t1+dt],[v1,v1+dv],'k--.')
plot([t1,t1+dt],[v1,v1],'k--.')
text(1.4, 8.8, r'$\delta t$')
text(2, 13, r"$\delta v = v'\delta t$")
text(0.8,17,r"$v' = 9.8-v_1/5$",rotation=50)


title(eqntex)
legend(loc=4)
axis([xmin, xmax, ymin, ymax])

##plotting stuff
xlabel(r'$t$ ($s$)',size=20)
ylabel(r'$v$ ($m/s$)',size=20)



savefig(figname)
