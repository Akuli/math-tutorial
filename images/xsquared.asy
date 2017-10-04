import boilerplate;
size(10cm);

axises(-3,3,-1,10);
grid(-3,3,-1,10);

guide xsquared_left, xsquared_right;
for (real x = -3; x <= 0; x+= 1/8) { xsquared_left  = xsquared_left ..(x,x**2); }
for (real x = 0 ; x <= 3; x+= 1/8) { xsquared_right = xsquared_right..(x,x**2); }
draw(xsquared_left, p=blue);
draw(xsquared_right, p=blue, L=Label(rotate(70)*"$y = x^2$"), align=W);
