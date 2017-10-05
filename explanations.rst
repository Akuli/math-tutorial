Proofs and Explanations
=======================

I used a bunch of spooky formulas in this tutorial. Some of them are
definitions of e.g. `\sin` or `\cos`, but in this chapter we'll focus on those
that aren't and prove that they actually work.


.. _unitcircle-triangle-compat:

Two ways to define sine and cosine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. asymptote::
   :align: right

   size(11cm);

   real t = pi/3;          // 60°
   real tradius = 0.2;     // radius of t's arc thingy
   real axisloc = 1.1;     // x axis goes from -axisloc to +axisloc, y axis similarly

   draw(unitcircle);
   fill((0,0)--(cos(t),0)--(cos(t),sin(t))--cycle, yellow);
   draw((0,0)--(cos(t),0), L="cos t");
   draw((cos(t),0)--(cos(t),sin(t)), L="sin t");
   draw((cos(t),sin(t))--(0,0), L="1");

   draw(arc((0,0), 0.2, 0, degrees(t)), L="t");

   draw((-axisloc,0)--(axisloc,0));
   draw((0,-axisloc)--(0,axisloc));

In :ref:`the unit circle trig section <unitcircletrig>` we defined `\sin` and
`\cos` with a unit circle, but then in
:ref:`the triangle trig section <triangletrig>` we defined them with a
triangle. These definitions are compatible with each other. If we draw a
picture like the one at right and apply the triangle stuff to the angle `t`, we
get this:

.. this is one chunk of math for alignment reasons

.. math::
   \sin t = \frac{\sin t}{1}

   \cos t = \frac{\cos t}{1}

   \tan t = \frac{\sin t}{\cos t}

.. asymptote::
   :align: right

   import abctriangle;

   real t = atan2(C.y, C.x);
   draw(arc((0,0), 1, 0, degrees(t)), L="t");

The first two formulas are obviously true with any `t`, but the last one is a
bit more interesting. We found another way to define `\tan`, and it
also works with a triangle:

.. math::
   \frac{\sin t}{\cos t} = \frac{b/c}{a/c}
   = \frac{b \cdot \frac 1 c}{a \cdot \frac 1 c} = \frac b a = \tan t


.. _pythagoras-proof:

Pythagorean Theorem
~~~~~~~~~~~~~~~~~~~

This is a well-known proof and I like it because it's simple.

.. asymptote::

   size(9cm);

   real a = 0.7;
   real b = 1-a;       // total width is 1

   // corners:
   // green square     everything
   pair A = (0,a),     A2 = (0,1);
   pair B = (a,1),     B2 = (1,1);
   pair C = (1,b),     C2 = (1,0);
   pair D = (b,0),     D2 = (0,0);

   fill(A2--B2--C2--D2--cycle, yellow);
   fill(A--B--C--D--cycle, heavygreen);

   draw(A--B, L="c");
   draw(B--C, L="c");
   draw(C--D, L="c");
   draw(D--A, L="c");

   draw(A2--A, L="b");
   draw(B2--B, L="b");
   draw(C2--C, L="b");
   draw(D2--D, L="b");
   draw(A--D2, L="a");
   draw(D--C2, L="a");
   draw(C--B2, L="a");
   draw(B--A2, L="a");

We can calculate the total area of the above square in a couple different ways:

- The square's sides are each `a+b`, so the area must be
  `(a+b)(a+b) = a(a+b) + b(a+b) = aa+ab+ba+bb = a^2 + 2ab + b^2`.
- The square consists of the green square whose area is `c^2` and 4 yellow
  triangles with area `\frac{ab}{2}` each. Total area is
  `c^2 + 4 \frac{ab}{2} = c^2 + \frac{4}{2}ab = c^2 + 2ab`.

We must get the same area with both ways, so we get this
:ref:`equation <equations>`:

.. math:: (a+b)(a+b) = c^2 + 4\frac{ab}{2}
.. math:: a^2 + 2ab + b^2 = c^2 + 2ab
.. math:: a^2 + b^2 = c^2


Derivative Rules
~~~~~~~~~~~~~~~~

In the derivative chapter I showed :ref:`a bunch of rules <derivative-rules>`
without explaining or proving why they work. We also used this definition of
derivative:

.. math:: f'(x) = \frac{f(x+dx)-f(x)}{dx}

The warning in the beginning of the derivative chapter is all about this. Some
mathematicians (most?) don't like this at all because `dx` is a "small number"
and it isn't really clear how it behaves in different situations. Here's a
better definition:

.. math:: f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}

We just replaced `dx` with `h` and threw in a `\lim`. The `\lim_{h \to 0}`
means that we take the limit as `h` approaches `0`, so it's just like our `dx`
thing but more explicit and also better-defined in some corner cases.

These proofs are ordered so that they don't use any derivative rules that
haven't been proved before them.

.. asymptote::
   :align: right

   size(7cm);
   real xmin = -2;
   real xmax = 3;
   real c = 3;
   axises(xmin,xmax,-1,6);

   draw((xmin,c)--(0,c), blue);
   draw((0,c)--(xmax,c), blue, L="y=c");
   draw(brace((-1,0),(-1,c)), L="c", align=W);

`\frac{d}{dx} c = 0`

   The graph `y=c` is a horizontal line, so the slope is 0.

   We can also plug `f(x)=c` into the definition of derivative:

   .. math:: \lim_{h\to0} \frac{c - c}{h} = \lim_{h\to0} \frac{0}{h} = 0

`\frac{d}{dx} cx = c`

   The slope of the line `y=cx` is `c` because every time `x` is incremented by
   something, `y` is incremented by `c` times as much. We did an example with
   `y=2x` in the derivative chapter.

   Again, we can confirm this with the definition of derivative:

   .. math::
      & \lim_{h\to0} \frac{c\cdot(x+h)-cx}{h} = \lim_{h\to0} \frac{cx+ch-cx}{h} \\
      &= \lim_{h\to0} \frac{cx-cx+ch}{h} = \lim_{h\to0} \frac{ch}{h} = c

.. asymptote::
   :align: right

   size(9cm);
   real xmax = 10;
   real ymax = 6;
   axises(-1,xmax,-1,ymax);
   grid(-1,xmax,-1,ymax);
   draw((-1,-1)--(ymax,ymax), blue, L=rotate(45)*Label("y=x"), align=NW);
   draw((2,2)--(5,2), smalldashes, L="$\Delta x$");
   draw((5,2)--(5,5), smalldashes, L="$\Delta y = \Delta x$");

`\frac{d}{dx} x = 1`

   The graph `y=x` is a straight line. If we increment `x` by something the `y`
   gets incremented by the same amount, so `\frac{\Delta y}{\Delta x}=1`. You
   can also plug in `c=1` to the previous rule.

   .. TODO: draw image

`\frac{d}{dx} (f(x)+g(x)) = f'(x)+g'(x)`

   This rule is particularly handy for differenciating long functions with many
   things added together. Let's see what we get with the definition of
   derivative.

   .. math::
      & \lim_{h\to0} \frac{(f(x+h)+g(x+h))-(f(x)+g(x))}{h} \\
      &= \lim_{h\to0} \frac{f(x+h)+g(x+h)-f(x)-g(x)}{h} \\
      &= \lim_{h\to0} \frac{f(x+h)-f(x)+g(x+h)-g(x)}{h} \\
      &= \lim_{h\to0} \left(\frac{f(x+h)-f(x)}{h} + \frac{g(x+h)-g(x)}{h}\right) \\
      &= \lim_{h\to0} \frac{f(x+h)-f(x)}{h} + \lim_{h\to0} \frac{g(x+h)-g(x)}{h} \\
      &= f'(x) + g'(x)

   The `\frac{d}{dx} (f(x)-g(x)) = f'(x)-g'(x)` rule can be proved in a very
   similar way.

`\frac{d}{dx} (f(x)g(x)) = f'(x)g(x) + f(x)g'(x)`

   It's not pretty, but we can use the definition.

   .. math::
      & \lim_{h\to0} \frac{f(x+h)g(x+h)-f(x)g(x)}{h} \\
      &= \lim_{h\to0} \frac{\overbrace{f(x)g(x+h)-f(x)g(x+h)}^\text{this is 0}
                            +f(x+h)g(x+h)-f(x)g(x)}{h} \\
      &= \lim_{h\to0} \frac{f(x+h)g(x+h)-f(x)g(x+h)+f(x)g(x+h)-f(x)g(x)}{h} \\
      &= \lim_{h\to0} \frac{(f(x+h)-f(x))g(x+h)+f(x)(g(x+h)-g(x))}{h} \\
      &= \lim_{h\to0} \left(
            \frac{(f(x+h)-f(x))\ g(x+h)}{h} + \frac{f(x)\ (g(x+h)-g(x))}{h}
         \right) \\
      &= \lim_{h\to0} \left(
         \frac{f(x+h)-f(x)}{h}g(x+h) + f(x)\frac{g(x+h)-g(x)}{h}
      \right) \\
      &= \lim_{h\to0} \left(\frac{f(x+h)-f(x)}{h}g(x+h)\right)
            + \lim_{h\to0}\left(f(x)\frac{g(x+h)-g(x)}{h}\right) \\
      &= \left(\lim_{h\to0}\frac{f(x+h)-f(x)}{h}\right)
        \left(\lim_{h\to0}g(x+h)\right)
        + f(x) \left(\lim_{h\to0}\frac{g(x+h)-g(x)}{h}\right) \\
      &= f'(x)g(x) + f(x)g'(x)

`\frac{d}{dx} x^c = c\ x^{c-1}`

   It's easy to prove that this works for an individual `c` value. For example,
   our very first derivative example shows that `\frac{d}{dx} x^2 = 2x`. Here
   I'll prove that this works with all positive integers using a powerful
   technique known as **induction**.

   Let's start by showing that this works with e.g. `c=1`:

      `\frac{d}{dx} x^1 = \frac{d}{dx} x = 1 = 1x^0 = 1x^{1-1}`

   Next we'll prove that **if** it works at `c=k` **then** it also works at
   `c=k+1`. Let's write things down just to be clear:

   :We assume: `\frac{d}{dx} x^k = k x^{k-1}`
   :We'll prove: `\frac{d}{dx} x^{k+1} = (k+1)x^{(k+1)-1}`

   .. math:: \frac{d}{dx} x^{k+1} = \frac{d}{dx} (x^k x^1) = \frac{d}{dx} (x \cdot x^k)

   Let's apply the `\frac{d}{dx}(f(x)g(x))` and `\frac{d}{dx} x` rules we
   proved above:

   .. math::
      \frac{d}{dx} (x \cdot x^k)
      = \left(\frac{d}{dx} x\right) \cdot x^k + x \cdot \frac{d}{dx} x^k
      = 1 \cdot x^k + x \cdot \frac{d}{dx} x^k
      = x^k + x \cdot \frac{d}{dx} x^k

   Now we can use our assumption.

   .. math::
      & x^k + x \cdot \frac{d}{dx} x^k = x^k + x \cdot k x^{k-1} = x^k + k\ x\ x^{k-1} \\
      &= x^k + kx^k = (1+k)x^k = (k+1)x^{(k+1)-1}

   So all in all, `\frac{d}{dx} x^{k+1} = (k+1)x^{(k+1)-1}` which is what we
   were supposed to prove. Now we know that this works when `c=0`, and thus it
   also must work when `c=1`, and that means it works when `c=2` and so on.

   Note that we only proved that it works when `c` is a positive integers, but
   it also works when `c` is e.g. `\frac{1}{2}`. It's possible to prove that
   the rule isn't limited to positive integers, but that's beyond the scope of
   this tutorial.

`\frac{d}{dx} \sqrt x = \frac{1}{2\ \sqrt x}`

   We could prove this with the `\frac{d}{dx} x^c` rule because
   `\sqrt x = x^\frac{1}{2}`, but we proved the `x^c` rule only for positive
   integers. Let's survive without it. Again, it's a mess, but it works.

   .. math::

      & \lim_{h\to0} \frac{\sqrt{x+h}-\sqrt x}{h} \\
      &= \lim_{h\to0} \frac{(\sqrt{x+h}-\sqrt x)(\sqrt{x+h}+\sqrt x)}{
                            h \cdot (\sqrt{x+h} + \sqrt x)} \\
      &= \lim_{h\to0} \frac{(\sqrt{x+h}-\sqrt x)\sqrt{x+h}
            +(\sqrt{x+h}-\sqrt x)\sqrt x}{h \cdot (\sqrt{x+h} + \sqrt x)} \\
      &= \lim_{h\to0} \frac{\sqrt{x+h}\sqrt{x+h}
         \overbrace{-\sqrt x\sqrt{x+h}+\sqrt{x+h}\sqrt x}^\text{this is 0}
         - \sqrt x\sqrt x}{h \cdot (\sqrt{x+h} + \sqrt x)} \\
      &= \lim_{h\to0} \frac{\left(\sqrt{x+h}\right)^2 - \left(\sqrt x\right)^2}{
                            h \cdot (\sqrt{x+h} + \sqrt x)} \\
      &= \lim_{h\to0} \frac{(x+h)-x}{h\cdot(\sqrt{x+h} + \sqrt x)} \\
      &= \lim_{h\to0} \frac{h}{h\cdot(\sqrt{x+h} + \sqrt x)} \\
      &= \lim_{h\to0} \frac{1}{\sqrt{x+h} + \sqrt x} \\
      &= \frac{1}{\sqrt x + \sqrt x} \\
      &= \frac{1}{2\ \sqrt x}
