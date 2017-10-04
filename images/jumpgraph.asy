import boilerplate;

size(9cm);
axises(-0.3, 3.5, -0.4, 2, "t", "h");

real f(real x) { return -x**2 + 3*x - 0.5; }

guide parabolaaa;
for (real x = 0; x <= 3; x += 0.1) {
    parabolaaa = parabolaaa..(x,f(x));
}
draw(parabolaaa);
