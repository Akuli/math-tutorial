import boilerplate;
import abctriangle;

real t = atan2(C.y, C.x);
draw(arc((0,0), 1, 0, degrees(t)), L="t");
