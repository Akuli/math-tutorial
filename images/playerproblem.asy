import boilerplate;

size(10cm);

// start and end of dotted player path line
pair pathstart = (0.1,-0.5);
pair pathend = (1.5,2);

axises(-1.5, 3, -0.5, 2);

draw(pathstart--pathend, p=smalldashes);
dot(pathend, L=" the player", align=NE);

// where does the player's path hit the x axis?
real deltay = pathend.y-pathstart.y;
real deltax = pathend.x-pathstart.x;
real s = deltay/deltax;

// y-y_0 = s*(x-x_0)      || x axis is the line y=0
// 0-y_0 = s*(x-x_0)
// x-x_0 = (0-y_0)/s = -y_0/s
// x = x_0 - y_0/s
real x = pathstart.x - pathstart.y/s;
real t = atan2(deltay, deltax);

// this isn't 60° because ° doesn't appear :/
draw(arc((x,0), 0.4, 0, degrees(t)), L="60 degrees");
