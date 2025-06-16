from pylab import *

figname='vector1.png'

##set ranges to plot
xmin=0; xmax=10; dx=1
ymin=0; ymax=10; dy=10

x1=2
x2=8
y1=3
y2=7

dx=x2-x1
dy=y2-y1
#dr=sqrt(dx^2+dy^2)
#ang=arctan(1.*dy/dx)*180/pi
#print ang

text(x1-0.1,y1-0.4,r'$z_1=f(x_1,y_1)$')
text(x2+0.1,y2+0.1,r'$z_2=z_1+\Delta f$')

text(x1+dx/2, y1-0.3, r'$\Delta x$')
text(x2, y1+dy/2, r'$\Delta y$')
text(x1+1.5, y1+dy*0.8, r'$\Delta r = \sqrt{(\Delta y)^2 + (\Delta x)^2}$', rotation=28)


plot([x1,x2],[y1,y2],'k-', linewidth=3)
plot([x2,x2],[y1,y2],'k--.')
plot([x1,x2],[y1,y1],'k--.')

xlabel(r'$x$',size=20)
ylabel(r'$y$',size=20, rotation=0)
grid()
axis([xmin, xmax, ymin, ymax])



savefig(figname)
