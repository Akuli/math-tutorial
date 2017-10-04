import boilerplate;

size(20cm);

draw((0,0)--(0,1)--(1,1)--(1,0.5), smalldashes);
dot((1,0.5));

draw((1.5,0)--(1.5 + 2/3, 1)--(2.5,0.5), smalldashes);
dot((2.5,0.5));

real f(real x) {
    /* top of parabola should be between x=3.7 and x=4, calculations with x=4:
        f(x) = ax^2 + bx + c
        f'(x) = 2ax + b
        f'(3.7) = 0
        2*a*3.7 + b = 0
        -a approx 7.5 b

       i found the constant with trial and error */
    return -2x**2 + 15*x - 27.2;
}

guide parabolaaa;
for (real x = 3; x <= 4.2; x += 0.05) {
    parabolaaa = parabolaaa..(x,f(x));
}
draw(parabolaaa, smalldashes);
dot((4.2, f(4.2)));
