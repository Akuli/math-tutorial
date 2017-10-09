// TODO: get rid of corner90 and bracedistance because picture-specific
//       values turned out to be a better idea
// TODO: stop using a weird mixture of mm and raw numbers?
defaultpen(0.8mm + fontsize(25pt));
pen dotpen = defaultpen() + 0.3cm;
pen smalldashes = linetype(new real[] {4, 4});
pen darkorange = rgb(0.9,0.4,0);
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

void axises(real xmin, real xmax, real ymin, real ymax,
            string xlabel="$x$", string ylabel="$y$") {
    // TODO: come up with a nice way to add numbers along the axises
    draw((xmin,0)--(xmax,0), arrow=Arrow(size=0.7cm));
    draw((xmax,0)--(xmax,0.01), L=xlabel);
    if (ymin != 0 || ymax != 0) {
        draw((0,ymin)--(0,ymax), arrow=Arrow(size=0.7cm));
        draw((0,ymax)--(0,ymax+0.01), L=ylabel);
    }
}

void abctriangle(real x, real y, pen fillcolor=mediumblue) {
    fill((0,0)--(x,0)--(x,y)--cycle, fillcolor);
    draw((x-corner90, 0)--(x-corner90, sgn(y)*corner90)--(x, sgn(y)*corner90));
    draw((0,0)--(x,0), L="$a$", align=(y > 0 ? S : N));
    draw((x,0)--(x,y), L="$b$", align=E);
    draw((x,y)--(0,0), L="$c$", align=(y > 0 ? N : S));
}


// copy/pasted from asymptote source because not-very-newest asymptotes
// don't have this
real braceinnerangle=radians(60);
real braceouterangle=radians(70);
real bracemidangle=radians(0);
real bracedefaultratio=0.14;
path brace(pair a, pair b, real amplitude=bracedefaultratio*length(b-a))
{
  real length=length(b-a);
  real sign=sgn(amplitude);
  real hamplitude=0.5*amplitude;
  real hlength=0.5*length;
  path brace;
  if(abs(amplitude) < bracedefaultratio*length) {
    real slope=2*bracedefaultratio;
    real controldist=(abs(hamplitude))/slope;
    brace=(0,0){expi(sign*braceouterangle)}::
    {expi(sign*bracemidangle)}(controldist,hamplitude)::
    {expi(sign*bracemidangle)}(hlength-controldist,hamplitude)::
    {expi(sign*braceinnerangle)}(hlength,amplitude) {expi(-sign*braceinnerangle)}::
    {expi(-sign*bracemidangle)}(hlength+controldist,hamplitude)::
    {expi(-sign*bracemidangle)}(length-controldist,hamplitude)::
    {expi(-sign*braceouterangle)}(length,0);
  } else {
    brace=(0,0){expi(sign*braceouterangle)}::
    {expi(sign*bracemidangle)}(0.25*length,hamplitude)::
    {expi(sign*braceinnerangle)}(hlength,amplitude){expi(-sign*braceinnerangle)}::
    {expi(-sign*bracemidangle)}(0.75*length,hamplitude)::
    {expi(-sign*braceouterangle)}(length,0);
  }
  return shift(a)*rotate(degrees(b-a,warn=false))*brace;
}
