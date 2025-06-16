set term postscript eps color enhanced 20
set size square 

set xrange[-5:5]
set yrange[-5:5]

set xlabel '{/Itallic Re(z)}'
set ylabel '{/Itallic Im(z)}'

set xtics 1
set ytics 1

set grid

set arrow from 0,-5 to 0,5 lw 2 nohead
set arrow from -5,0 to 5,0 lw 2 nohead

set out 'blankgrid.eps'

p 10 notitle

set out
!epstopdf blankgrid.eps



set arrow from 0,0 to 0,4 lw 5
set arrow from 0,0 to 0,4 lc rgb'yellow' lw 3
set label '{/Itallic 4i}' at 0,4.3

set arrow from 0,0 to 3,4 lc rgb'brown' lw 3
set label '{/Itallic 3 + 4i}' at 3,4

set arrow from 0,0 to 3,0 lw 5
set arrow from 0,0 to 3,0 lc rgb'orange' lw 3
set label '{/Itallic 3}' at 3,0.3

set arrow from 0,0 to -4,2 lw 5
set arrow from 0,0 to -4,2 lc rgb'green' lw 3
set label '{/Itallic -4 + 2i}' at -4,2.2

set arrow from 0,0 to 2,-3 lc rgb'blue' lw 3
set label '{/Itallic 2 - 3i}' at 2,-3.1


set out 'arganddiagram.eps'

p 10 notitle

set out
!epstopdf arganddiagram.eps


set arrow from 0,0 to 2,3 lw 3 lc rgb'blue'
set arrow from 0,-0.1 to 2,-0.1 lw 2 heads
set arrow from -0.1,0 to -0.1,3 lw 2 heads

deg2rad(x)=x/180.*pi 

set parametric 
set trange [0:1] 

set out 'angle1.eps'

plot 0.5*sin(t*deg2rad(45.)+deg2rad(45.)),0.5*cos(t*deg2rad(45.)+deg2rad(45.)) title ''

set out
!epstopdf angle1.eps




