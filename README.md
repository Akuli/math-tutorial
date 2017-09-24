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

3. Run the crazy script if you dare!

        $ python3 publish.py

## Adding images

I recommend using asymptote. See [the asy directory](asy/).

Unfortunately there are also quite a few things I drew with LibreOffice Draw
before I learned about Asymptote. These images are in [images/](images/). I
use this awful process to export them to png:

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
6. Check "View" -> "Grid" -> "Display Grid" if you want to see the grid.
