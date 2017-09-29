import boilerplate;
size(10cm);

axises(-1.2,1.4,-1.2,1.4);
real t = pi/3;   // 60°

draw(unitcircle);
draw((0,0)--(cos(t),sin(t)), L="1", align=NW);
dot((cos(t),sin(t)), p=dotpen, L="$(\cos t, \sin t)$", align=NE);
draw(arc((0,0), 0.3, 0, degrees(t)), L="$t$");
