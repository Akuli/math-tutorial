The Basics
==========

This tutorial assumes that you know most of these things. If you don't, that's
not a problem at all and you can just keep the basics page open while you read
other chapters.

Functions
~~~~~~~~~

Here's a typical math function:

.. math:: f(x)=2x
.. math:: f(6)=12

There is no special syntax for defining a function. All we have is the
equal sign, and when defining a function we just say that its value at x is
equal to something.

If you're familiar with a functional programming language like Haskell, then
you'll probably realize that the above math looks a lot like this Haskell
session:

.. code-block:: haskell

   Prelude> let f x = 2*x
   Prelude> f 6
   12
   Prelude>

If you're feeling like WTF is this, here's a Python session that should make
everything clear.

.. code-block:: python

   >>> def f(x):
   ...     return 2*x
   ...
   >>> f(6)
   12

Quick note about ``f(x)`` versus ``f x``: if you define your own function
called `f` or `g` you should use `f(x)`, but you can do e.g. `\sin x` or
`\cos x` with some "special" functions for historical reasons.

Also note that mathematicians prefer single-letter variable names because math
was originally written on paper, and writing long things by hand sucks. Again,
this doesn't apply to the "special" functions.


+, -, \*, /
~~~~~~~~~~~

I'm sure you already know how + and - work. Just be careful when you have a
minus in front of parentheses, e.g. `-(1+2)=-1-2` and `-(1-2)=-1-(-2)=-1+2=2-1`.

In this tutorial, ``a/b`` is written as `a/b` or `\frac a b`, and ``a*b`` is
written as `a \cdot b` or simply `ab`.

Handy things:

.. math:: 0a = 0
.. math:: 1a = \frac{a}{1} = a
.. math:: ab = ba
.. math:: (a+b)c = ac+bc

You can use these left-to-right or right-to-left. For example, if you want to
calculate `(1 + 2) \cdot 3` you know you could also do `1 \cdot 3 + 2 \cdot 3`,
but you can also calculate `1 \cdot 3 + 2 \cdot 3` like `(1 + 2) \cdot 3`.

.. _zerodivision:

You can add, substract and multiply any numbers together however you want, but
remember that you cannot divide anything by zero. See
`Numberphile's awesome zero video <https://youtu.be/BRRolKTlF6Q>`_ if you're
wondering why.

The easiest way to work with multiplication and division is to just look at
which numbers are below a division line and which aren't. For example, if we
have `\frac{1}{2} \cdot 3 \cdot \frac{4}{5}` we know that's
`\frac{1 \cdot 3 \cdot 4}{2 \cdot 5}` because 2 and 5 were below the lines but
the other numbers weren't.

If both the top and bottom are being multiplied by something you can get rid of
that multiplier if it isn't zero. For example:

.. math:: \frac{x}{ax+bx} = \frac{1x}{(a+b)x} = \frac{1}{a+b}, x \ne 0

.. _negative-mul-div:

Negative numbers behave like this when multiplied and divided. Note how the two
-'s cancel out.

.. math:: 2 \cdot (-2) = -(2 \cdot 2) = -4
.. math:: (-2) \cdot (-2) = -(-(2 \cdot 2)) = 2 \cdot 2 = 4
.. math:: \frac{-3}{-4} = \frac{(-1) \cdot 3}{(-1) \cdot 4} = \frac 3 4

.. TODO: ask theelous3 whether this is needed? or better yet figure out how to
   put stuff side by side so the code example can be next to the math

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


.. _abs:

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

If you're wondering why anything to the power of 0 is 1, you can do e.g.
`x^2 = x^{0+2} = x^0 x^2`. The equation should be true with any `x`, so
`x^0` must be 1 because `x^2 = 1 x^2`.


.. _equations:

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
with `\sqrt{\ \ }`:

.. math:: x^2 = 4
.. math:: \sqrt{x^2} = \sqrt 4
.. math:: |x| = 2
.. math:: x = 2 \text{ or } x = -2

See Also
~~~~~~~~

This chapter shows only the things you need in the rest of this tutorial, but
`this cheat sheet <http://tutorial.math.lamar.edu/pdf/Algebra_Cheat_Sheet.pdf>`_
is more complete.
