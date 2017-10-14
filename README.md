# Math for Programmers

You can read this tutorial on
[akuli.github.io/math-tutorial](https://akuli.github.io/math-tutorial).

## Updating the github.io site

These instructions assume a Debian-based Linux system (e.g. Ubuntu or
Mint). You can do everything on other platforms as well but you need to
figure out stuff yourself because I am not interested in writing
instructions for every possible platform.

1. Install dependencies.

        $ sudo apt install git texlive texlive-latex-extra dvipng python3-pip asymptote
        $ python3 -m pip install --user --upgrade pip
        $ python3 -m pip install --user sphinx

2. *OPTIONAL:* Run sphinx and view the output in a web browser and make
   sure that everything's OK.

        $ python3 -m sphinx . _build
        $ ( yourfavoritebrowser _build/index.html &>/dev/null )&

    If you get errors even though you have all the dependencies installed try
    removing the last `.. asymptote::` block from `integrals.rst`. I don't know
    why but 3D asymptote drawings work just fine on one of my computers but not
    the other.

3. Run the crazy script if you dare!

        $ python3 publish.py

## Adding images

Images are drawn with [Asymptote](http://asymptote.sourceforge.net/). The rst
files contain images created with a custom `.. asymptote::` directive
implemented in [asymptote-setup/](asymptote-setup/). All asymptote files that
can be imported from asymptote directives are also there.
