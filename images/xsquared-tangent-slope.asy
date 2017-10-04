import boilerplate;
size(10cm);

axises(-3,6,-1,20);

// this is drawn first so it goes below the x^2 line
real tangent(real x) {
    return 4*x-4;
}
draw((0.8,tangent(0.8))--(6,tangent(6)), p=darkorange,
     L=rotate(degrees(atan(4)))*Label("this thing's slope is 4", position=Relative(0.6)));

guide xsquared;
for (real x = -3; x <= 4.5; x+= 1/16) {
    xsquared = xsquared..(x,x**2);
}
draw(xsquared, p=blue, L=Label(rotate(75)*"$y = x^2$"), align=NW);

draw((2,0)--(2,2**2), smalldashes);
label("2", (2,0), align=S);
