The Basics
==========

This tutorial assumes that you know these things. If you don't, that's not a
problem at all and you can just keep this page open while you read rest of the
tutorial.

+, -, \*, /
~~~~~~~~~~~

I'm sure you know already how + and - work.

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

.. _negative-mul:

Negative numbers behave like this when multiplied and divided. Note how the two
-'s cancel out.

.. math:: 2\cdot(-2)=-4
.. math:: (-2)\cdot(-2)=4
.. math:: \frac{-1}{-2} = \frac{(-1) \cdot 1}{(-1) \cdot 2} = \frac 1 2

Absolute Value
~~~~~~~~~~~~~~

.. math::

   |x| = \left\{\begin{matrix}
      x  \text{ if } x \ge 0 \\
      -x \text{ if } x < 0
   \end{matrix}\right.

For example, `|2|=2` and `|-3|=3`. `|x|` is ``abs(x)`` in most programming
languages, but you may need e.g. ``Math.abs(x)`` depending on the language.

Powers and Square Root
~~~~~~~~~~~~~~~~~~~~~~

In most programming languages, `x^y` is ``x**y`` or ``pow(x, y)`` and `\sqrt x`
is ``sqrt(x)``.

.. math:: x^5=x\cdot x\cdot x\cdot x\cdot x
.. math:: x^{a+b}=\underbrace{x\cdot x\cdot x\cdot...\cdot x}_\text{a+b pcs}=\underbrace{x\cdot...\cdot x}_\text{a pcs}\cdot\underbrace{x\cdot...\cdot x}_\text{b pcs}=x^ax^b
.. math:: (x^a)^b=\underbrace{\overbrace{x^a}^{x\cdot...\cdot x,\ \text{a pcs}} \cdot\ \ x^a\ \cdot ... \cdot x^a}_\text{b pcs}=\underbrace{x\cdot x\cdot...\cdot x}_{a\cdot b\ \text{pcs}}=x^{ab}
.. math:: \sqrt x = x^\frac 1 2
.. math:: (\sqrt x)^2=x^\frac 1 2 \cdot x^\frac 1 2 = x^{\frac 1 2 + \frac 1 2} = x^1 = x

Note that `\sqrt x` only works if `x \ge 0`, and also
`\sqrt x \ge 0` (unless you use complex numbers, but so far we haven't
needed them in this tutorial).

Confusingly `\sqrt{x^2}=|x|`, e.g. `\sqrt{(-2)^2}=\sqrt4=2`
where `(-2)^2 = 4` (see :ref:`above <negative-mul>`).

Equations
~~~~~~~~~

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
