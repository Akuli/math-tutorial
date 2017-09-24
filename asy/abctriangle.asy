size(8cm);
defaultpen(.8mm+fontsize(30pt));

write(atan2(1,1));

real corner90 = 0.3;	// side length of 90° corner boxes

pair A = (0,0);		//     /| C
pair B = (3,0);		//    / |
pair C = (3,2);		//  A/__| B

fill(A--B--C--cycle, gray);
draw((B.x-corner90,B.y)--(B.x-corner90,B.y+corner90)--(B.x,B.y+corner90));
draw(A--B, L="a");
draw(B--C, L="b");
draw(C--A, L="c");
