from pylab import *

figname='vector_gravity_blank.png'

##set ranges to plot
xmin=0; xmax=10; dx=2
ymin=0; ymax=80; dy=10

##create a mesh
x=[0]#arange(xmin,xmax+dx,dx)
y=[0]#arange(ymin,ymax+dy,dy)
X,Y = meshgrid(x,y)


##text to display
eqntex='${\mathrm{d} v}/{\mathrm{d} t} = 9.8 - {v}/{5}$'

##define differential equation
t = X
v = Y
dt=ones(shape(X))
dv=(9.8-v/5.)*dt


##plotting stuff
dX=dt#/(xmax-xmin)
dY=dv#/(ymax-ymin)

Q = quiver(X,Y,dX, dY,angles='xy', scale_units='xy',scale=1)

qk = quiverkey(Q, 0.5, 1.025, 2, r''+eqntex,
               fontproperties={'weight': 'bold'})
xlabel(r'$t$',size=20)
ylabel(r'$v$',size=20)


axis([xmin,xmax,ymin,ymax])

savefig(figname)
