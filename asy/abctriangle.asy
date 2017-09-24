import boilerplate;

pair A = (0,0);     //     /| C
pair B = (3,0);     //    / |
pair C = (3,2);     //  A/__| B

fill(A--B--C--cycle, gray);
draw((B.x-corner90, B.y)--(B.x-corner90, B.y+corner90)--(B.x, B.y+corner90));
draw(A--B, L="a");
draw(B--C, L="b");
draw(C--A, L="c");
