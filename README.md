# Math for Programmers

You can read this tutorial on
[akuli.github.io/math-tutorial](https://akuli.github.io/math-tutorial).

## Updating the github.io site

These instructions assume a Debian-based Linux system (e.g. Ubuntu or
Mint). You can do everything on other platforms as well but you need to
figure out stuff yourself because I am not interested in writing
instructions for every possible platform.

1. Install dependencies.

        $ sudo apt install git texlive texlive-latex-extra dvipng python3-pip
        $ python3 -m pip install --user --upgrade pip
        $ python3 -m pip install --user sphinx

2. *OPTIONAL:* Run sphinx and view the output in a web browser and make
   sure that everything's OK.

        $ python3 -m sphinx . _build
        $ ( yourfavoritebrowser _build/index.html &>/dev/null )&

3. Run the crazy script if you dare!

        $ python3 publish.py

## Adding images

This is the process I use for creating images with LibreOffice Draw. It's by no
means the best possible program for this purpose and if you end up maintaining
this tutorial you are free to use whatever other tools you want.

I create the png images like this:

1. Install LibreOffice Draw.

        $ sudo apt install libreoffice-draw

2. Edit the images.

        $ libreoffice --draw images/drawings.odg

    I recommend going to "Options" -> "Tools" -> "LibreOffice Draw" and setting
    up similar settings as mine are for compatibility with existing drawings.
    Here are my settings:

    - "General" at left: the measurement unit is centimeter
    - "Grid" at left:
        - "Snap to grid" and "Visible grid" are checked
        - Both "Subdivision" numbers are 2

3. Uncheck "View" -> "Grid" -> "Display Grid".
4. Zoom in 75%. See the thingy at bottom right and use ctrl+mousewheel.
5. Take a *screenshot* (lol) with your favorite screenshot tool. I recommend a
    screenshot tool that lets you select an area with the mouse.
