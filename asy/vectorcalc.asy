import boilerplate;
size(8cm);
grid(0,8,0,5);

real a = 4;
real b = 6;

draw((0,0)--(a,b), arrow=Arrow(size=vectorarrowsize), L="$<a,b>$");
draw((0,0)--(a,0), arrow=Arrow(size=vectorarrowsize), dotpen);
