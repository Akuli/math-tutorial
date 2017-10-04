import boilerplate;
size(14cm);
grid(-1,5,-2,9);

axises(-1,5,-2,9);
// TODO: move this shit to axises()?
for (real x = 1; x <= 4; x += 1) {
    draw((x,0)--(x,0), L=(string) x, align=S);
}
for (real y = 1; y <= 7; y += 1) {
    draw((0,y)--(0,y), L=(string) y, align=W);
}

real f(real x) { return 2*x + 1; }

draw((-1,f(-1))--(3,f(3)));
draw((3,f(3))--(4,f(4)), L=Label("$y=2x+1$", Rotate((1,2))), align=W);
draw((0,f(0))--(3,f(0)), smalldashes, L="$\Delta x = 3$", align=N);
draw((3,f(0))--(3,f(3)), smalldashes, L="$\Delta y = 6$", align=E);

