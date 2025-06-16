set term postscript eps color enhanced 20
set size square 

set xrange[-5:5]
set yrange[-5:5]

set xlabel '{/Itallic Re(z)}'
set ylabel '{/Itallic Im(z)}'
set xtics 1
set ytics 1
set grid

######################################################
unset arrow
set arrow from 0,-5 to 0,5 lw 2 nohead
set arrow from -5,0 to 5,0 lw 2 nohead

a=3.0;b=-4.0

set arrow from 0,0 to a,b lw 3 lc rgb'blue'

set arrow from 0,-0.1 to a,-0.1 lw 2 heads
set arrow from -0.1,0 to -0.1,b lw 2 heads

set label '{/Itallic x}' at a/2,-0.5
set label '{/Itallic y}' at -0.5,b/2 rotate by 90


phi=-atan(b/a)

set label '{/Symbol f}' at -1.3,0.3

deg2rad(x)=x/180.*pi 

print phi

set parametric 
set trange [0:1] 

set out 'angle4.eps'

ang=2*pi-phi
plot cos(t*(ang)),sin(t*(ang)) title '' lw 2

set out
!epstopdf angle4.eps


######################################################
unset arrow; unset label
set arrow from 0,-5 to 0,5 lw 2 nohead
set arrow from -5,0 to 5,0 lw 2 nohead

a=3.0;b=4.0

set arrow from 0,0 to a,b lw 3 lc rgb'blue'

set arrow from 0,-0.1 to a,-0.1 lw 2 heads
set arrow from -0.1,0 to -0.1,b lw 2 heads

set label '{/Itallic x}' at a/2,-0.5
set label '{/Itallic y}' at -0.5,b/2 rotate by 90


phi=atan(b/a)

set label '{/Symbol f}' at 1,0.5

deg2rad(x)=x/180.*pi 

set parametric 
set trange [0:1] 

set out 'angle1.eps'

plot cos(t*phi),sin(t*phi) title '' lw 2

set out
!epstopdf angle1.eps

######################################################
unset arrow; unset label
set arrow from 0,-5 to 0,5 lw 2 nohead
set arrow from -5,0 to 5,0 lw 2 nohead

a=-3.0;b=4.0

set arrow from 0,0 to a,b lw 3 lc rgb'blue'

set arrow from 0,-0.1 to a,-0.1 lw 2 heads
set arrow from -0.1,0 to -0.1,b lw 2 heads

set label '{/Itallic x}' at a/2,-0.5
set label '{/Itallic y}' at -0.5,b/2 rotate by 90


phi=atan(b/a)

set label '{/Symbol f}' at 0.7,0.9

deg2rad(x)=x/180.*pi 

print phi

set parametric 
set trange [0:1] 

set out 'angle2.eps'

ang=pi+phi
plot cos(t*(ang)),sin(t*(ang)) title '' lw 2

set out
!epstopdf angle2.eps

######################################################
unset arrow; unset label
set arrow from 0,-5 to 0,5 lw 2 nohead
set arrow from -5,0 to 5,0 lw 2 nohead

a=-3.0;b=-4.0

set arrow from 0,0 to a,b lw 3 lc rgb'blue'

set arrow from 0,-0.1 to a,-0.1 lw 2 heads
set arrow from -0.1,0 to -0.1,b lw 2 heads

set label '{/Itallic x}' at a/2,-0.5
set label '{/Itallic y}' at -0.5,b/2 rotate by 90


phi=atan(b/a)

set label '{/Symbol f}' at -0.7,1.1

deg2rad(x)=x/180.*pi 

print phi

set parametric 
set trange [0:1] 

set out 'angle3.eps'

ang=pi+phi
plot cos(t*(ang)),sin(t*(ang)) title '' lw 2

set out
!epstopdf angle3.eps

