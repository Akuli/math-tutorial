import three;
import boilerplate;

void axises3d(real xmin, real xmax, real ymin, real ymax, real zmin, real zmax,
              string xlabel="$x$", string ylabel="$y$", string zlabel="$z$",
              real labeldistance=0.2) {
    draw((xmin,0,0)--(xmax,0,0), arrow=Arrow3(size=0.7cm));
    label(xlabel, (xmax+labeldistance,0,0));

    if (ymin != 0 || ymax != 0) {
        draw((0,ymin,0)--(0,ymax,0), arrow=Arrow3(size=0.7cm));
        label(ylabel, (0,ymax+labeldistance,0));
    }

    if (zmin != 0 || zmax != 0) {
        draw((0,0,zmin)--(0,0,zmax), arrow=Arrow3(size=0.7cm));
        label(zlabel, (0,0,zmax+labeldistance));
    }
}
