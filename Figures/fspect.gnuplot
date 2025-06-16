set term png 18
set out 'spect.png'

a=2/pi
b=2/(3.*pi)
c=2/(5.*pi)
d=2/(7.*pi)

print a,b,c,d

set yrange[0:0.7]
set xtics (0.5, 1.5, 2.5, 3.5)
set xlabel "Frequency (Hz)"
set ylabel "Amplitude (V)"

set style fill pattern 3 border -1
p '-' u 1:2 notitle w boxes
0.5 0.637
1.5 0.212
2.5 0.127
3.5 0.091
end

set out
