The Basics
==========

This page contains all kinds of boring details that I don't want to clutter the
rest of the tutorial with.

+, -, \*, /
~~~~~~~~~~~

I'm sure you already know how + and - work.

In this tutorial, ``a/b`` is written as `\frac a b`, and ``a*b`` is
sometimes written as `a \cdot b` but more often `ab`.

You can also use these handy things:

.. math:: 0a = 0
.. math:: ab = ba
.. math:: (a+b)c = ac+bc
.. math:: \frac{ab}{cd} = \frac a c \cdot \frac b d
.. math:: \frac{ac}{bc} = \frac a b, c \ne 0

See `Numberphile's awesome zero video <https://youtu.be/BRRolKTlF6Q>`_ if
you're wondering why dividing by zero is not allowed.

.. _negative-mul-div:

Negative numbers behave like this when multiplied and divided. Note how the two
-'s cancel out.

.. math:: 2 \cdot (-2) = -(2 \cdot 2) = 4
.. math:: (-2) \cdot (-2) = -(-(2 \cdot 2)) = 2 \cdot 2 = 4
.. math:: \frac{-3}{-4} = \frac{(-1) \cdot 3}{(-1) \cdot 4} = \frac 3 4

Python examples:

.. code-block:: python

   >>> 2 * (-2)
   -4
   >>> (-2) * (-2)
   4
   >>> (-3)/(-4)
   0.75
   >>> 3/4
   0.75
   >>> 


Absolute Value
~~~~~~~~~~~~~~

The absolute value of `x` is `|x|` in math and something like ``abs(x)`` or
``Math.abs(x)`` in most programming languages. It's easiest to think of the
absolute value as stripping off the minus sign. For example, `|2| = 2` and
`|-3| = 3`.

Powers and Square Root
~~~~~~~~~~~~~~~~~~~~~~

`x^y` is ``x**y`` or ``pow(x, y)`` and `\sqrt x` is ``sqrt(x)`` in most
programming languages.

.. math:: x^5=x\cdot x\cdot x\cdot x\cdot x
.. math::
   x^{a+b}  = \underbrace{x \cdot x \cdot x \cdot... \cdot x}_\text{a+b pcs}
            = \underbrace{x \cdot...\cdot x}_\text{a pcs} \cdot
              \underbrace{x \cdot...\cdot x}_\text{b pcs}
            = x^a x^b
.. math::
   (x^a)^b = \underbrace{\overbrace{x^a}^{x\cdot...\cdot x,\ \text{a pcs}}
              \cdot\ \ x^a\ \cdot ... \cdot x^a}_\text{b pcs}
           = \underbrace{x \cdot x \cdot...\cdot x}_{a\cdot b\ \text{pcs}}
           = x^{ab}
.. math:: \sqrt x = x^\frac 1 2
.. math::
   (\sqrt x)^2 = x^\frac 1 2 \cdot x^\frac 1 2
               = x^{\frac 1 2 + \frac 1 2} = x^1 = x
.. math:: x^0 = 1

Note that `\sqrt x` only works if `x \ge 0` (unless you use complex numbers,
but so far we haven't needed them in this tutorial). The square root is never
negative.

Confusingly `\sqrt{x^2}=|x|`, e.g. `\sqrt{(-2)^2}=\sqrt4=2`
where `(-2)^2 = 4` (see :ref:`above <negative-mul-div>`).

If you're wondering why anything to the power of 0 is 1, you can do e.g. this:

.. math:: x^2 = x^{0+2}
.. math:: x^2 = x^0x^2

Because `x^2 = x^2` with any `x`, `x^0` must be 1.

Solving Equations
~~~~~~~~~~~~~~~~~

For example, if you know that `2x+1 = 9` you can find `x` like this:

.. math:: 2x+1 = 9
.. math:: 2x = 8
.. math:: x = 4

I started by substracting 1 from both sides and then I divided everything by 2.
You can add and substract any numbers you want, but you cannot multiply or
divide by zero; multiplying by zero would give `0 = 0` and make anything true.

You can also apply most functions to both sides. For example, you can do this
with `\sqrt{\text{ }\text{ }}`:

.. math:: x^2 = 4
.. math:: \sqrt{x^2} = \sqrt 4
.. math:: |x| = 2
.. math:: x = 2 \text{ or } x = -2

See Also
~~~~~~~~

This chapter shows only the things you need in the rest of this tutorial, but
`this cheat sheet <http://tutorial.math.lamar.edu/pdf/Algebra_Cheat_Sheet.pdf>`_
is more complete.
