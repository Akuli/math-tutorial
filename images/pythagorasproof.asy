import boilerplate;
size(9cm);

real a = 0.7;
real b = 1-a;       // total width is 1

// corners:
// green square     everything
pair A = (0,a),     A2 = (0,1);
pair B = (a,1),     B2 = (1,1);
pair C = (1,b),     C2 = (1,0);
pair D = (b,0),     D2 = (0,0);

fill(A2--B2--C2--D2--cycle, yellow);
fill(A--B--C--D--cycle, heavygreen);

draw(A--B, L="c");
draw(B--C, L="c");
draw(C--D, L="c");
draw(D--A, L="c");

draw(A2--A, L="b");
draw(B2--B, L="b");
draw(C2--C, L="b");
draw(D2--D, L="b");
draw(A--D2, L="a");
draw(D--C2, L="a");
draw(C--B2, L="a");
draw(B--A2, L="a");
