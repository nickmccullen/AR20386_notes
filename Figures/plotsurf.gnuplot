set term png
set out 'surf2.png'


unset colorbox
set zrange[-1000:0]
set xrange[-30:30]
set yrange[-30:30]

set style fill pattern 1
set style line 3  linetype -1 linewidth 0.5
set pm3d depthorder hidden3d 3
set style fill  transparent solid 0.65 border
set palette
set hidden3d
set view 60,30,1,0.5
set isosample 40

#sp x**2-y**2 notitle with pm3d
#sp x**2+y**2 notitle with pm3d
sp -x**2-y**2 notitle with pm3d

set out
