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
        $ python3 -m pip install --user git+https://github.com/akuli/htmlthingy

2. *OPTIONAL:* Run the build script and view the output in a web browser
   to make sure that everything's OK.

        $ ./build.py
        $ ( yourfavoritebrowser html/index.html &>/dev/null )&

    If you get weird libGL errors the problem is probably something with 3D
    drawings. You can either google for a "correct" solution or use this
    horribly dangerous brute-force thing I used:

        $ sudo chmod 777 /dev/dri /dev/dri/*

    The build still errors out randomly. Run it multiple times until it
    succeeds. When it has succeeded once the 3D images are in `imagecache/` and
    it'll succeed every time (unless you change the 3D images).

3. Run the crazy script if you dare!

        $ ./publish.py
