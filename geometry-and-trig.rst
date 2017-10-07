Geometry and Trigonometry
=========================

This chapter contains useful stuff that aren't too difficult to get started
with. You'll find it especially useful if you like writing games.


Basic Angle Stuff
~~~~~~~~~~~~~~~~~

.. admonition:: Problem

   The ball of a ball-and-paddle game is moving at the angle of 30° and
   it hits a wall at right. How should the angle change?

   .. asymptote::

      import patterns; add("wall",hatch(2mm));

      size(9cm);

      real tdeg = 30, t = pi/6;

      // points of the dotted ball path line
      pair A = (-cos(t)*1.5, -sin(t)*1.5);
      pair B = (0,0);
      pair C = (-cos(t)*2, sin(t)*2);

      draw(A--B--C, p=smalldashes+deepblue);
      dot(C, p=deepblue, L=" the ball", align=NE);

      draw((-1.3,C.y/2)--(-0.3,C.y/2), smalldashes);
      draw(arc((C.x/2,C.y/2), 0.2, 0, 180-tdeg), deepred, L="???");

      // asymptote doesn't like °
      draw((-1.1,A.y*2/3)--(-0.1,A.y*2/3), smalldashes);
      draw(arc((A.x*2/3,A.y*2/3), 0.3, 0, tdeg), deepgreen, L="$30^\circ$");

      real wallthickness = 0.15;
      filldraw((0,-1)--(0,1)--(wallthickness,1)--(wallthickness,-1)--cycle, pattern("wall"));

Here ° is the degree sign, and 30° means 30 degrees. Degrees work so
that 360° is a full turn, 180° is a half turn, 90° is a quarter and so
on. It's also possible to measure angles in radians, but we'll look into
that later.

Note that both angles are measured up from a horizontal line. Measuring
them like that is a standard that this tutorial uses and people are
familiar with. You can also measure angles that go down like that; for
example, 270° would be straight down (that's 90° less than a full turn).

We can solve our problem by taking the 30° angle sign and moving it like
this:

.. asymptote::

   import patterns; add("wall",hatch(2mm));

   size(7cm);

   real tdeg = 30, t = pi/6;

   // points of the dotted ball path line
   pair B = (0,0);
   pair C = (-cos(t)*2, sin(t)*2);

   draw(B--C, p=smalldashes+deepblue);
   dot(C, p=deepblue);

   draw((-1.6,C.y/2)--(-0.3,C.y/2), smalldashes);
   draw(arc((C.x/2,C.y/2), 0.2, 0, 180-tdeg), deepred, L="???");
   draw(arc((C.x/2,C.y/2), 0.25, 180-tdeg, 180), deepgreen, L="$30^\circ$");

Now you can see that the angles add up to half turn (or 180°), so we get
this :ref:`equation <equations>`:

.. math:: 30° + \text{???} = 180°
.. math:: \text{???} = 180° - 30° = 150°

In math it's common to use a letter instead of "???" to represent an
unknown value. For example:

.. math:: 30° + t = 180°
.. math:: t = 180° - 30° = 150°


.. admonition:: Exercise

   Calculate similar things when the ball hits a wall at left, top or
   bottom. Don't be arfaid to deal with angles between 180° and 360°.


.. _unitcircletrig:

Trig (aka trigonometry) with the Unit Circle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Problem

   A player moves to top-right at the angle of 60° measured from the
   x axis at 10 pixels per second. How many pixels should the player's x and y
   change every second?

   .. asymptote::

      size(10cm);

      // start and end of dotted player path line
      pair pathstart = (0.1,-0.5);
      pair pathend = (1.5,2);

      axises(-1.5, 3, -0.5, 2);

      draw(pathstart--pathend, p=smalldashes);
      dot(pathend, L=" the player", align=NE);

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

      draw(arc((x,0), 0.4, 0, degrees(t)), L="$60^\circ$");

Note that the y axis goes up in math so higher means bigger, but in programming
it's usually upside down.

Our problem has something to do with sine and cosine. The unit circle is a
circle with radius 1 placed in the middle of the xy plane. Here's a picture that
shows what sine and cosine are:

.. asymptote::

   size(10cm);

   axises(-1.2,1.4,-1.2,1.4);
   real t = pi/3;   // 60°

   draw(unitcircle);
   draw((0,0)--(cos(t),sin(t)), L="1", align=NW);
   dot((cos(t),sin(t)), p=dotpen, L="$(\cos t, \sin t)$", align=NE);
   draw(arc((0,0), 0.3, 0, degrees(t)), L="$t$");

This is really quite simple: the x coordinate is `\cos t` and the y
coordinate is `\sin t`. But the radius of the unit circle is 1 instead
of our 10, so we need to multiply everything by 10 to scale it up. We get this:

.. code-block:: python

   player.x += 10*cos(60)
   player.y += 10*sin(60)

Based on the unit circle, `\sin 60°` should be somewhere between 0 and 1 since
the height of the x axis is 0 and the circle's top is at 1 (the radius is 1).
But if we try this out in Python, something is wrong:

.. code-block:: python

   >>> import math
   >>> math.sin(60)
   -0.3048106211022167

Now you're feeling really WTF. The angles with negative sines should be below
the x axis, e.g. something between 180° and 360°.

The problem is that Python, Haskell, C and most other programming languages use
radians by default instead of degrees. Let's convert 60° to radians so the sine
function is happy:

.. code-block:: python

   >>> math.sin(math.radians(60))
   0.8660254037844386
   >>> math.cos(math.radians(60))
   0.5000000000000001

That's more like it. ``0.5000000000000001`` is obviously not an accurate
result, but it's good enough for a programmer while a mathematician would say
that `\sin 60° = \frac{\sqrt 3}2` and `\cos 60° = \frac 1 2`. I might write
more about radians, how the heck I came up with those mathy-accurate values and
how my conversion functions work some day.

In most programming languages, functions like ``sin`` and ``cos`` take radians
as arguments, but also note that some functions (like ``atan2``, see below)
return radians.


.. _triangletrig:

Trig with a Triangle
~~~~~~~~~~~~~~~~~~~~

.. admonition:: Problem

   A player moves 10 pixels up and 20 pixels right. What angle is that?

Here's another way to define `\sin` and `\cos`, and another function called
`\tan` that we haven't used before.

.. asymptote::
   :align: right

   import abctriangle;

   real t = atan2(C.y, C.x);
   draw(arc((0,0), 1, 0, degrees(t)), L="$t$");

.. math:: \sin t = \frac b c
.. math:: \cos t = \frac a c
.. math:: \tan t = \frac b a

These things only work if the triangle has a 90° corner, and the little box at
bottom right means that the corner is 90°. These definitions are compatible
with the unit circle stuff above; see :ref:`this <unitcircle-triangle-compat>`.

So now we know that `a=20` and `b=10`. Let's figure out how to calculate `t`
from those:

.. math:: \tan t = \frac b a
.. math:: t = \arctan{\frac b a} = \text{atan2}(b, a)

Here `\arctan` is the inverse of `\tan`, so `\arctan (\tan t) = t`. Most
programming languages have an ``atan(x)`` function that returns `\arctan x`,
but I don't recommend using it in this case; the ``atan2(b,a)`` function
returns `\arctan{\frac b a}` and I recommend it instead. ``atan2`` looks at the
signs of `a` and `b` and does the right thing if they're negative (the player
is moving to e.g. bottom left). It also works if ``a`` is 0 and ``b/a`` would
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

   import abctriangle;

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
   draw(A--D, arrow=Arrow(size=vectorarrowsize), L="$8 \overline{i} + 4 \overline{j}$", blue, align=SE);

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

.. math:: l = \sqrt{a^2+b^2} = \text{hypot}(a, b)
.. math:: t = \text{atan2}(b,a)
.. math:: a = l \cdot \cos t
.. math:: b = l \cdot \sin t

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

.. admonition:: Exercise

   Create a ``Vector`` class in your favorite programming language that
   represents `x \bar i + y \bar j`. The class should implement a
   ``Vector(x, y)`` constructor and the properties (or setters and getters if
   you use e.g. Java) ``x``, ``y``, ``length`` and ``angle``. Additionally, if
   the programming language supports it, you can add a nice ``"Vector(x, y)"``
   string representation and operator overloading; e.g.
   `(1 \bar i + 2 \bar j) + (3 \bar i + 4 \bar j) = 4 \bar i + 6 \bar j`, so
   ``Vector(1, 2) + Vector(3, 4) == Vector(4, 6)``.

   I found it easiest to implement things by storing only ``x`` and
   ``y`` and calculating everything else as needed.

   For example, here I'm playing with my Python implementation:

   .. code-block:: python

      >>> v = Vector(1, 2)
      >>> v         # the string representation
      Vector(1, 2)
      >>> v.x
      1
      >>> v.y
      2
      >>> v.length
      2.23606797749979
      >>> math.degrees(v.angle)
      63.43494882292201
      >>> v.angle = math.radians(45)
      >>> v
      Vector(1.5811388300841898, 1.5811388300841895)
      >>> v.length      # setting the angle didn't change this
      2.23606797749979
      >>> v.length = 0     # lol
      >>> v
      Vector(0.0, 0.0)

   My code is
   `here <https://github.com/Akuli/math-tutorial/blob/master/samplecode/vector.py>`_.
   I didn't add operator overloading because I wanted to keep the
   implementation simple and easy to read.
