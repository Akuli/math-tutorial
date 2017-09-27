import boilerplate;
size(8cm);
grid(0,8,0,5);

pair A = (0,0);
pair B = (3,0);
pair C = (3,4);
pair D = (8,4);

draw(A--B, arrow=Arrow(size=vectorarrowsize), L="$3 \overline{i}$");
draw(B--C, arrow=Arrow(size=vectorarrowsize), L="$4 \overline{j}$", align=NW);
draw(C--D, arrow=Arrow(size=vectorarrowsize), L="$5 \overline{i}$", align=N);
draw(A--D, arrow=Arrow(size=vectorarrowsize), L="$8 \overline{i} + 4 \overline{j}$", blue, align=SE);
