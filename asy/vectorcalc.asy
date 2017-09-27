import boilerplate;
size(8cm);

real a = 4;
real b = 6;
grid(-1,6,-1,7);

// this is before <a,b> because that way <a,b> is drawn on top of this
draw(arc((0,0), 1, 0, degrees(atan2(b,a))), L="t", align=NE, brown);

// l looks like 1 without $$ and < and > turn into ¿ and ! without $$ (lol)
draw((0,0)--(a,b), arrow=Arrow(size=vectorarrowsize), align=NW,
     L=Label("$<$a,b$>$", Rotate((a,b))));
pair llabeloffset = (-1,a/b);
draw(brace((0,0)+llabeloffset, (a,b)+llabeloffset),
     L="$l$", align=NW, deepblue);

draw((a,0)--(0,0), smalldashes);
draw((a,0)--(a,b), smalldashes);
draw(brace((a,-bracedistance), (0,-bracedistance)), L="a", align=S);
draw(brace((a+bracedistance,b), (a+bracedistance,0)), L="b", align=E);
