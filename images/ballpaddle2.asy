import boilerplate;
import patterns; add("wall",hatch(2mm));

size(7cm);

real tdeg = 30, t = pi/6;

// points of the dotted ball path line
pair B = (0,0);
pair C = (-cos(t)*2, sin(t)*2);

draw(B--C, p=smalldashes+deepblue);
dot(C, p=deepblue);

draw((-1.6,C.y/2)--(-0.3,C.y/2), smalldashes);
draw(arc((C.x/2,C.y/2), 0.2, 0, 180-tdeg), deepred, L="???");
draw(arc((C.x/2,C.y/2), 0.25, 180-tdeg, 180), deepgreen, L="$30^\circ$");
