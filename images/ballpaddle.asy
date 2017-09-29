import boilerplate;
import patterns; add("wall",hatch(2mm));

size(9cm);

real tdeg = 30, t = pi/6;

// points of the dotted ball path line
pair A = (-cos(t)*1.5, -sin(t)*1.5);
pair B = (0,0);
pair C = (-cos(t)*2, sin(t)*2);

draw(A--B--C, p=smalldashes+deepblue);
dot(C, p=deepblue, L=" the ball", align=NE);

draw((-1.3,C.y/2)--(-0.3,C.y/2), smalldashes);
draw(arc((C.x/2,C.y/2), 0.2, 0, 180-tdeg), deepred, L="???");

// asymptote doesn't like °
draw((-1.1,A.y*2/3)--(-0.1,A.y*2/3), smalldashes);
draw(arc((A.x*2/3,A.y*2/3), 0.3, 0, tdeg), deepgreen, L="$30^\circ$");

real wallthickness = 0.15;
filldraw((0,-1)--(0,1)--(wallthickness,1)--(wallthickness,-1)--cycle, pattern("wall"));
