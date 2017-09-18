# Math for Programmers

You can read this tutorial on
[akuli.github.io/math-tutorial](https://akuli.github.io/math-tutorial).

## Updating the github.io site

These instructions assume a Debian-based Linux system (e.g. Ubuntu or
Mint). You can do everything on other platforms as well but you need to
figure out stuff yourself because I am not interested in writing
instructions for every possible platform.

1. Install dependencies.

        $ cd math-tutorial
        $ sudo apt install texlive texlive-latex-extra dvipng
        $ python3 -m venv env
        $ . env/bin/activate
        (env) $ pip install sphinx

2. Run sphinx.

        (env) $ sphinx-build . _build
        (env) $ deactivate

3. View the output in a web browser and make sure that everything's OK.

        $ ( yourfavoritebrowser _build/index.html &>/dev/null )&

4. Run the crazy publishing script if you dare!

        $ python3 publish.py
