from pylab import *

def f1(x):
    return -(2*x-2)**2+4

x=linspace(0.5,1.5,100)
y=f1(x)

x1=0.6
x2=0.8

plot(x,y,'-')
for x1 in [0.6,0.8,1.0,1.2]:
    x2=x1+0.2
    plot([x1,x2],[f1(x1),f1(x2)],'k.-',markersize=10,linewidth=2)
    plot([x1,x1],[0,f1(x1)],'k--')
plot([1.4,1.4],[0,f1(1.4)],'k--')
axis([0.5,1.5,2.5,4.5])
xlabel(r'$x$',size=18)
ylabel(r'$u$',size=18,rotation=0)

xt=2.55
text(0.6,xt,r'$x_{i-2}$',size=18)
text(0.8,xt,r'$x_{i-1}$',size=18)
text(1.0,xt,r'$x_{i}$',size=18)
text(1.2,xt,r'$x_{i+2}$',size=18)
text(1.4,xt,r'$x_{i+4}$',size=18)

text(0.5,f1(0.6)+0.05,r'$u(x_{i-2})$',size=16)
text(0.7,f1(0.8)+0.05,r'$u(x_{i-1})$',size=16)
text(1.0,f1(1.0)+0.05,r'$u(x_{i})$',size=16)
text(1.2,f1(1.2)+0.05,r'$u(x_{i+2})$',size=16)
text(1.38,f1(1.4)+0.05,r'$u(x_{i+4})$',size=16)

text(0.85,f1(0.9)-0.2, r'$(u_x)_{i-1}$',size=18)
text(1.05,f1(0.9)-0.2, r'$(u_x)_{i+1}$',size=18)

savefig('differences.png')


