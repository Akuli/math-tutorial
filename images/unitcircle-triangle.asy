import boilerplate;
size(11cm);

real t = pi/3;          // 60°
real tradius = 0.2;     // radius of t's arc thingy
real axisloc = 1.1;     // x axis goes from -axisloc to +axisloc, y axis similarly

draw(unitcircle);
fill((0,0)--(cos(t),0)--(cos(t),sin(t))--cycle, yellow);
draw((0,0)--(cos(t),0), L="cos t");
draw((cos(t),0)--(cos(t),sin(t)), L="sin t");
draw((cos(t),sin(t))--(0,0), L="1");

draw(arc((0,0), 0.2, 0, degrees(t)), L="t");

draw((-axisloc,0)--(axisloc,0));
draw((0,-axisloc)--(0,axisloc));
