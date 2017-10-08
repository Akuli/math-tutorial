Geometry and Trigonometry
=========================

This chapter contains useful stuff that aren't too difficult to get started
with. You'll find it especially useful if you like writing games, and this
chapter contains a working example game.

.. note::

   Usually the y axis is so that more y means up, but in this chapter, it's
   "upside down" and more y means down. Almost all programming things use the
   "more y means down" version and are compatible with this chapter.

   If you're a mathematician everything looks really weird to you, but if
   you're a programmer who wants to get stuff done you'll enjoy not having to
   add minus signs everywhere before using formulas from this tutorial.


Basic Angle Stuff
~~~~~~~~~~~~~~~~~

.. admonition:: Problem

   The ball of a ball-and-paddle game is moving at the angle of 30° and
   it hits a wall at right. How should the angle change?

   .. asymptote::

      import patterns; add("wall",hatch(2mm));

      size(9cm);

      // points of the dotted ball path line
      pair A = (-cos(radians(30))*1.5, sin(radians(30))*1.5);
      pair B = (0,0);
      pair C = (-cos(radians(30))*2, -sin(radians(30))*2);

      draw(A--B--C, p=smalldashes+deepblue);
      dot(C, p=deepblue, L=" the ball", align=S);

      draw((-1.3,C.y/2)--(-0.3,C.y/2), smalldashes);
      draw(arc((C.x/2,C.y/2), 0.2, -150, 0), deepred, L="???");

      // asymptote doesn't like °
      draw((-1.1,A.y*2/3)--(-0.1,A.y*2/3), smalldashes);
      draw(arc((A.x*2/3,A.y*2/3), 0.3, 0, -30), deepgreen, L="$30^\circ$", align=E);

      real wallthickness = 0.15;
      filldraw((0,-1)--(0,1)--(wallthickness,1)--(wallthickness,-1)--cycle, pattern("wall"));

Here ° is the degree sign, and 30° means 30 degrees. Degrees work so
that 360° is a full turn, 180° is a half turn, 90° is a quarter and so
on. It's also possible to measure angles in radians, but we'll look into
that later.

Note that both angles are measured down from a horizontal line clockwise
because that's a standard in programming. In math, angles are usually measured
up from a horizontal line and counter-clockwise.

We can solve our problem by taking the 30° angle sign and moving it like
this:

.. asymptote::

   import patterns; add("wall",hatch(2mm));

   size(7cm);

   // points of the dotted ball path line
   pair B = (0,0);
   pair C = (-cos(radians(30))*2, -sin(radians(30))*2);

   draw(B--C, p=smalldashes+deepblue);
   dot(C, p=deepblue);

   draw((-1.6,C.y/2)--(-0.3,C.y/2), smalldashes);
   draw(arc((C.x/2,C.y/2), 0.2, -150, 0), deepred, L="???");
   draw(arc((C.x/2,C.y/2), 0.3, -150, -180), deepgreen, L="$30^\circ$", align=W);

Now you can see that the angles add up to half turn (or 180°), so we get
this :ref:`equation <equations>`:

.. math::
   30° + \text{???} &= 180° \\
   \text{???} &= 180° - 30° \\
   \text{???} &= 150°

In math it's common to use a letter instead of "???" to represent an
unknown value. For example:

.. math::
   30° + b &= 180° \\
   b &= 180° - 30° = 150°

It's easy to calculate similar things for other directions. Here are the
results, where `a` is the original angle and `b` is the changed angle:

* If the ball hits left or right wall, `b = 180°-a`.
* If the ball hits top or bottom, `b = 360°-a`.

.. _unitcircletrig:

Trig (aka trigonometry) with the Unit Circle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Problem

   This time the ball moves at the angle of 60°, and it should move 5 pixels
   every time the screen is updated. How many pixels should its x and y change
   every second?

   .. asymptote::

      size(10cm);

      // start and end of dotted player path line
      pair pathstart = (0.7,0);
      pair pathend = (1.5,-1.5);

      axises(0, 3, 0, -2);

      draw(pathstart--pathend, p=smalldashes+deepblue);
      dot(pathend, deepblue, L=" the ball", align=NE);

      // where does the player's path hit the x axis?
      real deltay = pathend.y-pathstart.y;
      real deltax = pathend.x-pathstart.x;
      real s = deltay/deltax;

      // y-y_0 = s*(x-x_0)      || x axis is the line y=0
      // 0-y_0 = s*(x-x_0)
      // x-x_0 = (0-y_0)/s = -y_0/s
      // x = x_0 - y_0/s
      real x = pathstart.x - pathstart.y/s;
      real t = atan2(deltay, deltax);

      draw(arc((x,0), 0.4, 0, degrees(t)), L="$60^\circ$", align=E);

Our problem has something to do with sine and cosine. The unit circle is a
circle with radius 1 placed in the middle of the xy plane. Here's a picture that
shows what sine and cosine are:

.. asymptote::

   size(9cm);

   axises(-1.2,1.6,1.2,-1.8);
   real t = radians(55);

   draw(unitcircle);
   draw((0,0)--(cos(t),-sin(t)), L="1", align=S);
   dot((cos(t),-sin(t)), p=dotpen);
   draw(arc((0,0), 0.3, -degrees(t), 0), L="$t$");

   draw(brace((cos(t),-1), (0,-1)), deepblue, L="$\cos t$", align=S);
   draw(brace((cos(t)+0.15,0), (cos(t)+0.15,-sin(t))), darkorange, L="$\sin t$", align=E);

This is really simple: the x coordinate is `\cos t` and the y coordinate is
`\sin t`. But the radius of the unit circle is 1 instead of our 5, so we need
to multiply everything by 5 to scale it up. We get this:

.. code-block:: python

   player.x += 5*cos(60)
   player.y += 5*sin(60)

The angle `t` in the above image looks like it's about 60°, so `\sin 60°`
should be somewhere between 0 and 1 since the height of the x axis is 0 and the
circle's bottom is at `y=1`. But if we try this out in Python, something is
wrong:

.. code-block:: python

   >>> import math
   >>> math.sin(60)
   -0.3048106211022167

The problem is that Python, Haskell, C and most other programming languages use
radians by default instead of degrees. Let's convert 60° to radians so
``math.sin`` is happy:

.. code-block:: python

   >>> math.sin(math.radians(60))
   0.8660254037844386
   >>> math.cos(math.radians(60))
   0.5000000000000001

That's more like it. ``0.5000000000000001`` is obviously not an accurate
result, but it's good enough for a programmer while a mathematician would say
that `\sin 60° = \frac{\sqrt 3}2` and `\cos 60° = \frac 1 2`. I might write
more about radians, how the heck I came up with those mathy-accurate values and
how Python's conversion functions work some day.

In most programming languages, functions like ``sin`` and ``cos`` take radians
as arguments, but also note that some functions (like ``atan2``, see
`Trig with a Triangle`_ below) return radians.


.. _triangletrig:

Trig with a Triangle
~~~~~~~~~~~~~~~~~~~~

.. admonition:: Problem

   The ball moves 10 pixels down and 20 pixels right. What angle is that?

Here's another way to define `\sin` and `\cos`, and another function called
`\tan` that we haven't used before.

.. asymptote::
   :align: right

   size(9cm);
   abctriangle(3,2);
   real t = atan2(2,3);
   draw(arc((0,0), 1, 0, degrees(t)), L="$t$");

.. math::
   \sin t &= \frac b c \\
   \cos t &= \frac a c \\
   \tan t &= \frac b a

These things work only if the triangle has a 90° corner, and the little box at
bottom right means that the corner is 90°. These definitions are compatible
with the unit circle stuff above; see
:ref:`this thing <unitcircle-triangle-compat>`.

.. asymptote::
   :align: right

   size(9cm);
   abctriangle(3,-2, lightgreen);
   real t = atan2(-2,3);
   draw(arc((0,0), 1, 0, degrees(t)), L="$t$", align=E);

The green triangle is just like the blue one, but I flipped it so that we can
calculate the stuff by plugging in `a=20` and `b=10` without worrying about
which way things go. Let's figure out how to calculate the `t`:

.. math:: \tan t = \frac b a
.. math:: t = \arctan{\frac b a} = \text{atan2}(b, a)

Here `\arctan` is the inverse of `\tan`, so `\arctan (\tan t) = t`. Most
programming languages have an ``atan(x)`` function that returns `\arctan x`,
but I don't recommend using it in this case; the ``atan2(b,a)`` function
returns `\arctan{\frac b a}` and I recommend it instead. ``atan2`` looks at the
signs of `a` and `b` and does the right thing if they're negative (the player
is moving to e.g. top left). It also works if ``a`` is 0 and ``b/a`` would
fail as division by zero is undefined.

.. note::
   Usually people like to put `x` before `y` in different kinds of places, but
   ``atan2`` is used like ``atan2(y_change, x_change)``, **not** like
   ``atan2(x_change, y_change)``.

Finally, it's time to calculate our stuff:

.. code-block:: python

   >>> from math import atan2, degrees
   >>> degrees(atan2(10, 20))
   26.56505117707799


.. _pythagoras:

Pythagorean Theorem
~~~~~~~~~~~~~~~~~~~

.. admonition:: Problem

   A player moves 10 pixels up and 20 pixels right, just like in the previous
   problem. How many pixels is that in total, measured diagonally?

.. asymptote::
   :align: right

   size(6cm);
   abctriangle(3,2);

Here's a handy equation, also known as the Pythagorean theorem:

.. math:: a^2 + b^2 = c^2

Again, the triangle's corner between a and b must be 90° like it is in the
image. If you're wondering how the heck it works see
:ref:`this proof <pythagoras-proof>`.

Let's solve `c` from the equation by applying `\sqrt{\ \ }` on both sides:

.. math:: \sqrt{a^2 + b^2} = \sqrt{c^2} = |c| = c

Here `|c|` is :ref:`the absolute value <abs>`. The last step assumes `c \ge 0`,
but that's not a problem because a triangle with a negative side length doesn't
make much sense.

"Hypotenuse" is a fancy word that means the longest side of a triangle with a
90° angle, and that's why some programming languages have a ``hypot(a, b)``
function that returns `\sqrt{a^2 + b^2}`.

Let's calculate the distance:

.. code-block:: python

   >>> from math import hypot, sqrt
   >>> hypot(10, 20)
   22.360679774997898
   >>> sqrt(10**2 + 20**2)
   22.360679774997898

.. admonition:: Exercise

   Now you should know enough things to create a simple 2D
   ball-and-paddle game where the player moves the paddle (with e.g.
   arrow keys), and the ball bounces between the paddle and the corners
   of the window. Use a library that lets you do the math yourself but
   provides some basic things, like e.g.
   ``draw_circle(centerx, centery, radius)``. Remember that the y axis
   is "upside down" so you may need to add minus signs to the formulas.

   My Python and PyGame implementation is
   `here <https://github.com/Akuli/math-tutorial/blob/master/samplecode/ball-and-paddle.py>`_.
   There are quite a few things that must be taken care of, so remember
   that I created the above game in several small steps and I didn't do
   it in a matter of minutes.


Vectors
~~~~~~~

.. asymptote::
   :align: right

   size(8cm);
   grid(0,8,0,7);
   axises(-0.5,7.5,-0.5,6.5);

   pair A = (1,2);
   pair B = (3,5);

   dot(A, L="$A$", p=dotpen);
   dot(B, L="$B$", p=dotpen);
   draw(A--B, arrow=Arrow(size=vectorarrowsize),
        L=Label(rotate(degrees(atan2(3,2)))*"$\overrightarrow{AB}$"), align=NW);
   draw((6,2)--(7,2), arrow=Arrow(size=vectorarrowsize), L="$\overline{i}$");
   draw((5,3)--(5,4), arrow=Arrow(size=vectorarrowsize), L="$\overline{j}$");

A point is simply a pair of x and y coordinates, and a vector represents the
difference between two points. For example, if we have the points `A=(1,2)` and
`B=(3,5)`, the vector from A to B is
`\overrightarrow{AB} = (3-1) \bar i + (5-2) \bar j = 2 \bar i + 3 \bar j`. Here
`\bar i` and `\bar j` are vectors that go right and up by 1 unit, respectively.

A vector like `x \bar i + y \bar j` can be also written as `<x,y>`. Use
whatever style you want.

We could also use vectors to do similar things as in
:ref:`the unit circle trig section <unitcircletrig>`. The advantage with
vectors is that moving the player is really easy:

.. code-block:: python

   player.x += speed_vector.x
   player.y += speed_vector.y

A disadvantage is that if we want to change the angle that the player moves at
by 1° we can't just do ``moving_angle += 1``. We'll look into how this is done
below.

.. asymptote::
   :align: right

   size(8cm);
   grid(0,8,0,5);

   pair A = (0,0);
   pair B = (3,0);
   pair C = (3,4);
   pair D = (8,4);

   draw(A--B, arrow=Arrow(size=vectorarrowsize), L="$3 \overline{i}$");
   draw(B--C, arrow=Arrow(size=vectorarrowsize), L="$4 \overline{j}$", align=NW);
   draw(C--D, arrow=Arrow(size=vectorarrowsize), L="$5 \overline{i}$", align=N);
   draw(A--D, arrow=Arrow(size=vectorarrowsize), blue,
      L=Label(rotate(degrees(atan(4/8)))*"$8 \overline{i} + 4 \overline{j}$"), align=SE);

Another nice thing about vectors is that they can be +'ed together easily. For
example, if we first move 3 units to right, then 4 units up and finally 5 more
units to right, we move a total of 8 units to right and 4 units up. That's how
`3 \bar i + 4 \bar j + 5 \bar i = 8 \bar i + 4 \bar j`.

.. asymptote::
   :align: left

   size(8cm);

   real a = 4;
   real b = 6;
   grid(-1,6,-1,7);

   // this is before <a,b> because that way <a,b> is drawn on top of this
   draw(arc((0,0), 1, 0, degrees(atan2(b,a))), L="$t$", align=NE, brown);

   draw((0,0)--(a,b), arrow=Arrow(size=vectorarrowsize), align=NW,
        L=Label("$<a,b>$", Rotate((a,b))));
   pair llabeloffset = (-1,a/b);
   draw(brace((0,0)+llabeloffset, (a,b)+llabeloffset),
        L="$l$", align=NW, deepblue);

   draw((a,0)--(0,0), smalldashes);
   draw((a,0)--(a,b), smalldashes);
   draw(brace((a,-bracedistance), (0,-bracedistance)), L="$a$", align=S);
   draw(brace((a+bracedistance,b), (a+bracedistance,0)), L="$b$", align=E);

These vector calculations are just like the
:ref:`Pythagorean theorem <pythagoras>` and
:ref:`unit circle trig <unitcircletrig>` stuff above:

.. math::
   l &= \sqrt{a^2+b^2} = \text{hypot}(a, b) \\
   t &= \text{atan2}(b,a) \\
   a &= l \cdot \cos t \\
   b &= l \cdot \sin t

Example: if we move 1 unit to the right and 2 units up, our vector is `<1,2>`,
its length is `\sqrt{1^2+2^2} = \sqrt 5 \approx 2.24` and the angle is
`\text{atan2}(2,1) \approx 63.4°`. On the other hand,
`2.24 \cdot \cos 63.4° \approx 1` and `2.24 \cdot \sin 63.4° \approx 2`.

One way to change the angle of a vector is to first convert it to a length and
an angle, change that angle and create a new vector. It looks like this in
pseudo-ish code:

.. code-block:: python

   length = hypot(speed_vector.x, speed_vector.y)
   angle = atan2(speed_vector.y, speed_vector.x) + angle_change
   speed_vector.x = cos(angle) * length
   speed_vector.y = sin(angle) * length

Example: Vector class in Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here's a ``Vector`` class I implemented in Python running with
`repl.it <https://repl.it/>`_. A ``Vector(x, y)`` represents
`x \bar i + y \bar j`. I didn't add operator overloading because I wanted to
keep everything nice and simple. Click the "play"-shaped button at top to run
the code and then use the Python shell at right.

.. raw:: html

   <iframe frameborder="0" width="100%" height="800px" src="https://repl.it/MRCz/1"></iframe>
