set term png size 600,300
set out "foursquare.png"

set samples 1000

set xlabel "t"
set ylabel "g(t) (to n=7)"

omega=0.5*2*pi
plot [-2:2] 1/2. + 2./pi * sin(omega*x) + 2./(3.*pi) * sin(3*omega*x) + 2./(5.*pi)*sin(5*omega*x) + 2./(7*pi)*sin(7*omega*x) notitle w l lw 2

set out
