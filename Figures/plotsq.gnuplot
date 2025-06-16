set term png size 600,300
set out "sqwav.png"


set yrange[0:1.3]

set ytics (0,1)
set xtics (-2,-1,0,1,2)
set xlabel "t [seconds]"
set ylabel "g(t)"

p '-' u 1:2 notitle w l lt 3 lw 3
-2 0
-2 1
-1 1
-1 0
0 0
0 1
1 1
1 0
2 0
2 1
end

set out

