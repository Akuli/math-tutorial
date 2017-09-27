// TODO: stop using a weird mixture of mm and raw numbers
defaultpen(0.8mm + fontsize(25pt));
pen dotpen = defaultpen() + 0.3cm;
pen smalldashes = linetype(new real[] {4, 4});
real corner90 = 0.3;    // side length of 90° corner boxes
real vectorarrowsize = 0.7cm;
real bracedistance = 0.2;

void grid(real xmin, real xmax, real ymin, real ymax) {
    pen thingray = defaultpen() + 1pt + gray;
    for (real x = xmin; x <= xmax; x+=1)
        draw((x,ymin-0.5)--(x,ymax+0.5), thingray);
    for (real y = ymin; y <= ymax; y+=1)
        draw((xmin-0.5,y)--(xmax+0.5,y), thingray);
}

void axises(real xmin, real xmax, real ymin, real ymax) {
    // TODO: come up with a better way to label the axises
    draw((xmin,0)--(xmax,0), arrow=Arrow(size=0.7cm));
    draw((0,ymin)--(0,ymax), arrow=Arrow(size=0.7cm));
    draw((xmax,0)--(xmax,0.01), L="x");
    draw((0,ymax)--(0,ymax+0.01), L="y");
}
