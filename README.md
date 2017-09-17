# Math for Programmers

You can read this tutorial on
[akuli.github.io/math-tutorial](https://akuli.github.io/math-tutorial).

## Updating the github.io site

You need to have Python 3, Sphinx and some LaTeX stuff installed. I
installed a bunch of LaTeX stuff when I tried to get this to work and
I'm not sure what exactly you need.

1. Run sphinx.

        $ cd math-tutorial
        $ python3 -m sphinx . _build

2. View the output in a web browser and make sure that everything's OK.

        $ ( yourfavoritebrowser _build/index.html &>/dev/null )&

3. Publish it.

        $ python3 publish.py
