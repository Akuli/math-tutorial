# Math for Programmers

You can read this tutorial on
[akuli.github.io/math-tutorial](https://akuli.github.io/math-tutorial).

## Updating the github.io site

These instructions assume a Debian-based Linux system (e.g. Ubuntu or
Mint). You can do everything on other platforms as well but you need to
figure out stuff yourself because I am not interested in writing
instructions for every possible platform.

1. Install dependencies.

        $ sudo apt install git dvipng python3-pip asymptote graphviz texlive-binaries
        $ python3 -m pip install --user --upgrade pip
        $ python3 -m pip install --user git+https://github.com/akuli/htmlthingy

    `texlive-binaries` is just for `dvisvgm`. If you know some other package
    that contains a `dvisvgm` program you might be able to use it instead.

2. Check your asymptote version.

        $ asy --version

    If your asymptote version is less than 2.31 things might not work.
    Click [here](https://sourceforge.net/projects/asymptote/files/) to
    download a newer asymptote. Then compile it like this (replace 2.31
    with the correct version number if you downloaded a different version):

        $ sudo apt-get build-dep asymptote
        $ cd path/to/where/you/downloaded/asymptote
        $ tar xf asymptote-2.31.src.tgz
        $ cd asymptote-2.31
        $ ./configure --prefix=$HOME/.local && make && make install

    Be sure to use `--prefix` instead of `sudo make install`. This way
    nothing is too terribly screwed if something goes wrong.

    Try `asy --version`. If it doesn't work, add this to `~/.bashrc`:

        PATH="$HOME/.local/bin:$PATH"

    You can also uninstall the old asymptote that came from apt:

        $ sudo apt remove asymptote

2. *OPTIONAL:* Run the build script and view the output in a web browser
   to make sure that everything's OK.

        $ ./build.py
        $ ( yourfavoritebrowser html/index.html &>/dev/null )&

    If you get weird libGL errors like this one...

        libGL error: failed to open drm device: Lupa evätty
        libGL error: failed to load driver: i965

    ...the problem is probably something with 3D drawings. You can either
    google for a "correct" solution or use this horribly dangerous
    brute-force hack thing I used:

        $ sudo chmod 777 /dev/dri/card0

    Compiling 3D images still fails randomly. Run the build script multiple
    times until it succeeds. When it has succeeded once the 3D images are in
    `imagecache/` and it'll succeed every time (unless you change the 3D images
    or delete them from `imagecache/`).

3. Run the crazy script if you dare!

        $ ./publish.py
