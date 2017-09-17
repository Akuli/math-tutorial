# Math for Programmers

This tutorial will soon be hosted on
[akuli.github.io/math-tutorial](https://akuli.github.io/math-tutorial).

## Building

I'll create a publishing script soon, but while you're waiting for it
you can clone the repository and build the docs locally. You need Python
3, Sphinx and some LaTeX stuff that I'm not sure what exactly it was
that made things work.

    $ git clone https://github.com/Akuli/math-tutorial
    $ cd math-tutorial
    $ python3 -m sphinx . _build
    $ ( yourwebbrowser _build/index.html &>/dev/null )&
