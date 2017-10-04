import boilerplate;
size(12cm);

real f(real x) { return 0.1*x**3 - 0.1x + 1; }
axises(-0.1,2.2,-0.5,f(2));

guide parabolaaa;
for (real x = -0.1; x <= 2; x += 0.05) {
    parabolaaa = parabolaaa..(x,f(x));
}
//pathlabel(L=Label("MidPoint"), parabolaaa, position=0.5, align=Relative(W), sloped=true);
draw(parabolaaa, L="$y=f(x)$", align=NW, p=heavyred);

real x = 1.5;
real dx = 0.1;

draw((x,0)--(x,f(x)), lightblue);
draw((x+dx,0)--(x+dx,f(x+dx)), lightblue);
draw(brace((x,0), (0,0)), L="$x$", align=S);
draw(brace((x+dx,-0.05), (x,-0.05), amplitude=0.1), L="$dx$", align=S);
draw(brace((x,0), (x,f(x))), L="$f(x)$", align=W);
draw(brace((x+dx,f(x+dx)), (x+dx,0)), L="$f(x+dx)$", align=E);
draw(brace((x,f(x)),(x,f(x+dx)), amplitude=0.1), L="$dy$", align=W);
draw(brace((x,f(x+dx)+0.05),(x+dx,f(x+dx)+0.05), amplitude=0.1), L="$dx$", align=N);
