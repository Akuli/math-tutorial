Geometry and Trig Explanations
==============================

.. _geometry-explained:

If you haven't read :ref:`this geometry section <more-geometry>` yet go ahead
and read it now. This chapter explains how the things I showed in the geometry
section work.


The Diagonal
~~~~~~~~~~~~

In the geometry chapter, the longest side of a triangle with a 90° corner was
magicallly `\sqrt{a^2 + b^2}` where `a` and `b` were the other sides. If we
have a square with triangles in it like this...

.. image:: https://www.mathsisfun.com/geometry/images/pythagorean-theorem-proof.png

...then we can calculate its area in a couple different ways:

   - The square's sides are each `a+b`, so the area must be
     `(a+b)(a+b) = a(a+b) + b(a+b) = a^2+ab+ba+b^2 = a^2+2ab+b^2`.
   - The square consists of the yellow square whose area is `c^2` and 4 blue
     triangles with area `\frac{ab}{2}` each.

We must get the same area with both ways, so we get this:

.. math:: (a+b)(a+b) = c^2 + 4\frac{ab}{2}
.. math:: a^2 + 2ab + b^2 = c^2 + 2ab
.. math:: a^2 + b^2 = c^2
.. math:: \sqrt{a^2+b^2} = |c| = c

The last step assumes `c \ge 0`, but that's not a problem because a triangle
with a negative side length doesn't make much sense. "Hypotenuse" is a fancy
word that means the longest side of a triangle with a 90° angle, and that's why
the `\sqrt{a^2+b^2}` function is named hypot.


The atan2
~~~~~~~~~

In :ref:`the trig section <simpletrig>` we learned how `\sin` and `\cos` are
defined with the unit circle. There's also another, perhaps more common way to
define them using a triangle with one 90° corner.

.. image:: images/abctriangle.png

This triangle is compatible with the `a^2 + b^2 = c^2` thing, but we can also
define sine, cosine and tangent in it like this:

.. math:: \sin t = \frac a c
.. math:: \cos t = \frac b c
.. math:: \tan t = \frac a b

It's also possible to define `\tan t` with the unit circle, but it's not as
simple as `sin` and `cos` so we skipped that.

.. the following image link points to github because image links don't work
   correctly with just sphinx

These triangle definitions are perfectly compatible with the unit circle
equivalents. If you draw
`a triangle like this <https://raw.githubusercontent.com/Akuli/math-tutorial/master/images/unitcircle-triangle.png>`_
into the unit circle and then apply the triangle stuff, you get things like
`\sin t = \frac{\sin t}{1}`.

Let's solve `t` from the `\tan t` formula:

.. math:: \tan t = \frac b a
.. math:: t = \arctan \frac b a

Here `\arctan` is the inverse of `\tan`, so `\arctan (\tan t) = t`. Most
programming languages have an ``atan(x)`` function that returns `\arctan x`,
and ``atan2(b,a)`` simply calculates `\arctan \frac b a`.

Note that if `a=0` then `\frac b a` is dividing by 0 and thus not defined, but
if `a` is really really close to 0 then `t` is about 90°.

.. image:: images/narrow-triangle.png

That's why ``atan2(1, 0)`` returns 90° and ``atan2(-1, 0)`` returns -90°. The
negativeness shouldn't be a problem because negative angles behave correctly
with functions like `\sin`, `\cos` and `\tan`.

Another reason why ``atan2`` is good is that if we're going to top right then
x and y grow at the same speed and
`\arctan \frac b a = \arctan \frac 1 1 = \arctan 1 = 45°`, but if we go to
bottom left then `\arctan \frac b a = \arctan \frac{-1}{-1} = \arctan 1 = 45°`
and there's no way to tell which direction we're moving to. The ``atan2``
function considers the signs of its arguments and does the right thing with
them.
