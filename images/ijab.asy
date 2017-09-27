import boilerplate;
size(8cm);
grid(0,8,0,7);
axises(-0.5,7.5,-0.5,6.5);

pair A = (1,2);
pair B = (3,5);

dot(A, L="A", p=dotpen);
dot(B, L="B", p=dotpen);
draw(A--B, arrow=Arrow(size=vectorarrowsize), L="$\overline{AB}$", align=NW);
draw((5,3)--(5,4), arrow=Arrow(size=vectorarrowsize), L="$\overline{i}$");
draw((6,2)--(7,2), arrow=Arrow(size=vectorarrowsize), L="$\overline{j}$");
