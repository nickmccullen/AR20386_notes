set term postscript eps color enhanced 20
set size square
set xrange[-1:6]
set yrange[-1:5]

set xlabel '{/Itallic Re(z)}'
set ylabel '{/Itallic Im(z)}'

set xtics 1
set ytics 1

set grid

set arrow from 0,-1 to 0,5 lw 2 nohead
set arrow from -1,0 to 6,0 lw 2 nohead



set out 'grid.eps'
p 11 title ''
set out

!epstopdf grid.eps



set arrow from 0,0 to 2,3 lw 3 lc rgb'blue'
set arrow from 0,0 to 3,1 lw 3 lc rgb'red'

set arrow from 2,3 to 5,4 lt 0 lw 2 lc rgb'red'
set arrow from 3,1 to 5,4 lt 0 lw 2 lc rgb'blue'

set arrow from 0,0 to 5,4 lw 3 lc rgb'purple'

set arrow from 0,-0.1 to 2,-0.1 lw 2 heads
set arrow from 2,-0.1 to 5,-0.1 lw 2 heads

set arrow from -0.1,0 to -0.1,3 lw 2 heads
set arrow from -0.1,3 to -0.1,4 lw 2 heads

set label '{/Itallic z_1 = x_1 + i y_1}' at 0.6,1.3 rotate by 60
set label '{/Itallic z_2 = x_2 + i y_2}' at 1.5,0.3 rotate by 20
set label '{/Itallic z_3 = z_1 + z_2}' at 2.1,2.0 rotate by 43

set label '{/Itallic x_1 = 2}' at 0.6,-0.3
set label '{/Itallic x_2 = 3}' at 3.1,-0.3

set label '{/Itallic y_1 = 3}' at -0.4,1 rotate by 90
set label '{/Itallic y_2 = 1}' at -0.4,3.05 rotate by 90

set out 'addcomplex.eps'
p 11 title ''
set out

!epstopdf addcomplex.eps
