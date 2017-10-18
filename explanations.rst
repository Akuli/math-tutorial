Proofs and Explanations
=======================

If you just want to get things done without worrying about why the calculations
are exactly like they are then you're in the wrong place, but if you got
interested in the math itself you may enjoy reading some of this stuff.

I used a bunch of spooky formulas in this tutorial. Some of them are
definitions of e.g. `\sin` or `\cos`, but in this chapter we'll focus on those
that aren't and prove that they actually work.


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

   draw(A--B, L="$c$");
   draw(B--C, L="$c$");
   draw(C--D, L="$c$");
   draw(D--A, L="$c$");

   draw(A2--A, L="$b$");
   draw(B2--B, L="$b$");
   draw(C2--C, L="$b$");
   draw(D2--D, L="$b$");
   draw(A--D2, L="$a$");
   draw(D--C2, L="$a$");
   draw(C--B2, L="$a$");
   draw(B--A2, L="$a$");

We can calculate the total area of the above square in a couple different ways:

- The square's sides are each `a+b`, so the area must be `(a+b)(a+b)`.
- The square consists of the green square whose area is `c^2` and 4 yellow
  triangles with area `\frac{ab}{2}` each. Total area is `c^2 + 4 \frac{ab}{2}`.

We must get the same area with both ways, so we get this
:ref:`equation <equations>`:

.. math::
   (a+b)(a+b) &= c^2 + 4\frac{ab}{2} \\
   (a+b)a+(a+b)b &= c^2 + \frac{4}{2} ab \\
   aa+ba+ab+bb &= c^2 + 2ab \\
   a^2 + 2ab + b^2 &= c^2 + 2ab \\
   a^2 + b^2 &= c^2


.. asymptote::
   :align: right

   size(12cm);

   axises(-1.1,1.3,-1.1,1.3);
   real t = pi/3;          // 60°
   real tradius = 0.2;     // radius of t's arc thingy

   draw(unitcircle);
   fill((0,0)--(cos(t),0)--(cos(t),sin(t))--cycle, yellow);
   draw((0,0)--(cos(t),0), L="$\cos t$");
   draw((cos(t),0)--(cos(t),sin(t)), L="$\sin t$");
   draw((cos(t),sin(t))--(0,0), L="1");

   draw(arc((0,0), 0.2, 0, degrees(t)), L="$t$");

.. _unitcircle-triangle-compat:

Two ways to define sine and cosine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The y axis of the picture at right goes up because this explanation isn't
really useful for programming; it's just an explanation for people who are
wondering how `\sin` and `\cos` appear both in a unit circle and in triangles.

In :ref:`the unit circle trig section <unitcircletrig>` we defined `\sin` and
`\cos` with a unit circle, but then in
:ref:`the triangle trig section <triangletrig>` we defined them with a
triangle. If we apply the triangle stuff to the angle `t` of the picture at
right, we get this:

.. asymptote::
   :align: right

   size(5cm);
   abctriangle(3,2,lightblue);
   real t = atan2(2,3);
   draw(arc((0,0), 1, 0, degrees(t)), L="$t$");

.. math::
   \sin t &= \frac{\sin t}{1} \\
   \cos t &= \frac{\cos t}{1} \\
   \tan t &= \frac{\sin t}{\cos t}

The first two formulas are obviously true with any `t`, but the last one is a
bit more interesting. We found another way to define `\tan`, and it
also works with a triangle:

.. math::
   \frac{\sin t}{\cos t} = \frac{b/c}{a/c}
   = \frac{b \cdot \frac 1 c}{a \cdot \frac 1 c} = \frac b a = \tan t


.. _accurate-sincos-explained:

Accurate Sine and Cosine Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. asymptote::
   :align: right

   size(10cm);

   axises(-0.2,1.3,-0.2,1.3);
   real t = tau/6;
   real sint = sqrt(3)/2;
   real cost = 1/2;
   real tradius = 0.2;     // radius of t's arc thingy

   draw(arc((0,0), 1, -5, 95));
   fill((0,0)--(cost,0)--(cost,sint)--cycle, yellow);
   draw((cost,0)--(cost,sint));
   draw((cost,sint)--(0,0), L="1");
   draw((cost,sint)--(1,0), smalldashes);
   draw((cost,sint)--(1,sint), smalldashes);

   draw(arc((0,0), tradius, 0, degrees(t)), L="$\frac \tau 6$");
   draw(arc((1,0), tradius, 180-degrees(t), 180), L="$\frac \tau 6$");
   draw(arc((cost,sint), tradius, 180+degrees(t), 270), L="$\frac{\tau}{12}$");
   draw(arc((cost,sint), tradius, -90, -degrees(t)), L="$\frac{\tau}{12}$");

   draw(brace((1,0), (cost,0)), L="$\cos \frac \tau 6$", align=S);
   draw(brace((cost,0), (0,0)), L="$\cos \frac \tau 6$", align=S);
   draw(brace((1.05,sint), (1.05,0)), L="$\sin \frac \tau 6$", align=E);

:ref:`Here <accurate-sincos>` I said that `\sin \frac \tau 6 = \frac{\sqrt 3}{2}`
and `\cos \frac \tau 6 = \frac 1 2`. I'm sorry to disappoint you, but there's
no general and easy way to find accurate `\sin` and `\cos` values by hand.
However, in many cases there's something special about the angles that allows
us to do some other tricks.

The angle in question is `\frac \tau 6`, a sixth of a turn. If a triangle has
three sides with equal lengths, the angles will be `\frac \tau 6` each. That's
why we can complete the triangle drawn in unit circle like in the image. The
angles at top are `\frac{\tau}{12}` because two `\frac{\tau}{12}` angles added
together is `\tau/6`.

The radius of the unit circle is 1, so we get this on the `x` axis:

.. math:: \cos \frac \tau 6 + \cos \frac \tau 6 &= 1
.. math:: \cos \frac \tau 6 &= \frac 1 2

Now we can apply the Pythagorean theorem (proved
:ref:`above <pythagoras-proof>`) to the yellow triangle and figure out
`\sin \frac \tau 6`:

.. math::
   \left( \cos \frac \tau 6 \right)^2 + \left( \sin \frac \tau 6 \right)^2 &= 1^2 = 1 \\
   \left( \sin \frac \tau 6 \right)^2 &= 1 - \left( \cos \frac \tau 6 \right)^2 \\
   \sqrt{\left( \sin \frac \tau 6 \right)^2} &= \sqrt{1 - \left( \cos \frac \tau 6 \right)^2} \\
   \left| \sin \frac \tau 6 \right| &= \sqrt{1 - \left( \cos \frac \tau 6 \right)^2} \\
      &= \sqrt{1 - \left( \frac 1 2 \right)^2} = \sqrt{1 - \frac{1^2}{2^2}} \\
      &= \sqrt{\frac 4 4 - \frac 1 4} = \sqrt{\frac 3 4}
         = \frac{\sqrt 3}{\sqrt 4} = \frac{\sqrt 3}{2}

We know that `\sin \frac \tau 6` is positive, so
`\sin \frac \tau 6 = |\sin \frac \tau 6|`.


.. _has-derivative:

Which functions have derivatives?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :ref:`the derivative chapter <derivatives>` I said that most functions
you'll come across have a derivative. Let's be a bit more specific. The
derivative doesn't exist in these cases:

.. asymptote::
   :align: right

   size(8cm);
   axises(-3,3,-1,3);
   draw((-3,0)--(0,0), blue);
   filldraw(circle((0,0),0.1), white, blue);

   draw((0,1)--(3,1), blue, L="$y=f(x)$", align=N);
   filldraw(circle((0,1),0.1), blue, blue);

*  The function is not *continuous*; that is, the graph consists of multiple
   lines. For example, this function is not continuous at `x=0` and thus
   `f'(0)` is not defined:

   .. math::
      f(x) = \left\{\begin{matrix}
         1 \text{ if } x \ge 0\\ 
         0 \text{ if } x < 0
      \end{matrix}\right.

.. asymptote::
   :align: right

   size(6cm);
   axises(-3,3,-1,3);
   draw((-3,3)--(0,0), blue);
   draw((0,0)--(3,3), blue, L=rotate(45)*Label("$y=|x|$"), align=N);

*  The graph of the function has a spike in it. Derivatives describe
   "growing speed" and it isn't clear how fast the values grow on top of a
   spike. For example, the :ref:`absolute value <abs>` `|x|` has a derivative
   everywhere except at `x=0`.

Of course, there are more precise definitions about continuity and "spikes",
but this should be enough to give you some kind of idea about the limitations.


.. _derivative-proofs:

Derivative Rules
~~~~~~~~~~~~~~~~

The derivative chapter contains :ref:`a bunch of rules <derivative-rules>`
with no explainations or proofs about how they work. These proofs are ordered
so that they don't use any derivative rules that haven't been proved before
them.

.. asymptote::
   :align: right

   size(7cm);
   real xmin = -2;
   real xmax = 3;
   real c = 3;
   axises(xmin,xmax,-1,6);

   draw((xmin,c)--(0,c), blue);
   draw((0,c)--(xmax,c), blue, L="$y=c$");
   draw(brace((-1,0),(-1,c)), L="$c$", align=W);

`\frac{d}{dx} c = 0`
^^^^^^^^^^^^^^^^^^^^

   The graph `y=c` is a horizontal line, so the slope is zero.

   We can also plug `f(x)=c` into the definition of derivative:

   .. math::
      f'(x) = \lim_{h\to0} \frac{f(x+h)-f(x)}{h} = \lim_{h\to0} \frac{c-c}{h}
      = \lim_{h\to0} \frac{0}{h} = 0

.. asymptote::
   :align: right

   size(9cm);
   real xmax = 5;
   real c = 2;
   //grid(-1,xmax,-1*c,xmax*c);
   axises(-1,xmax,-1*c,xmax*c);

   draw((-1,-1*c)--(xmax,xmax*c), blue,
        L=rotate(degrees(atan(c)))*Label("$y=cx$"), align=NW);
   draw((1,c)--(3,c), smalldashes, L="$\Delta x$");
   draw((3,c)--(3,3c), smalldashes, L="$\Delta y$");

`\frac{d}{dx} cx = c`
^^^^^^^^^^^^^^^^^^^^^

   The slope of the line `y=cx` is `c` because every time `x` is incremented by
   something, `y` increments `c` times as much. In other words,
   `\Delta y = c \cdot \Delta x` and `\frac{\Delta y}{\Delta x} = c`.

   Again, we can confirm this with the definition of derivative:

   .. math::
      \frac{d}{dx} cx &= \lim_{h\to0} \frac{c\cdot(x+h)-cx}{h} \\
      &= \lim_{h\to0} \frac{cx+ch-cx}{h} \\
      &= \lim_{h\to0} \frac{cx-cx+ch}{h} \\
      &= \lim_{h\to0} \frac{ch}{h} \\
      &= c

`\frac{d}{dx}(c\ f(x)) = c\ f'(x)`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   The previous rule actually works with all functions that have a derivative,
   not just `x`.

   .. math::
      \frac{d}{dx}(c\ f(x)) &= \lim_{h\to0} \frac{c\ f(x+h) - c\ f(x)}{h} \\
      &= \lim_{h\to0} \frac{c \cdot (f(x+h)-f(x))}{h} \\
      &= \lim_{h\to0} \left(c\ \frac{f(x+h)-f(x)}{h} \right) \\
      &= c \cdot \lim_{h\to0} \frac{f(x+h)-f(x)}{h} \\
      &= c\ f'(x)

.. asymptote::
   :align: right

   size(6cm);
   real xmax = 7;
   real ymax = 6;
   grid(-1,xmax,-1,ymax);
   axises(-1,xmax,-1,ymax);
   draw((-1,-1)--(ymax,ymax), blue, L=rotate(45)*Label("$y=x$"), align=NW);
   draw((2,2)--(5,2), smalldashes, L="$\Delta x$");
   draw((5,2)--(5,5), smalldashes, L="$\Delta y$");

`\frac{d}{dx} x = 1`
^^^^^^^^^^^^^^^^^^^^

   This is just like the `\frac{d}{dx} cx = c` rule, but `c=1` and
   `\Delta y = \Delta x`.

`\frac{d}{dx} (f(x)+g(x)) = f'(x)+g'(x)`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   This rule is particularly handy for differenciating long functions with many
   things added together. Let's see what we get with the definition of
   derivative.

   .. math::
      \frac{d}{dx} (f(x)+g(x))
      &= \lim_{h\to0} \frac{(f(x+h)+g(x+h))-(f(x)+g(x))}{h} \\
      &= \lim_{h\to0} \frac{f(x+h)+g(x+h)-f(x)-g(x)}{h} \\
      &= \lim_{h\to0} \frac{f(x+h)-f(x)+g(x+h)-g(x)}{h} \\
      &= \lim_{h\to0} \left(\frac{f(x+h)-f(x)}{h} + \frac{g(x+h)-g(x)}{h}\right) \\
      &= \lim_{h\to0} \frac{f(x+h)-f(x)}{h} + \lim_{h\to0} \frac{g(x+h)-g(x)}{h} \\
      &= f'(x) + g'(x)

   The `\frac{d}{dx} (f(x)-g(x)) = f'(x)-g'(x)` rule can be proved in a very
   similar way.

`\frac{d}{dx} (f(x)g(x)) = f'(x)g(x) + f(x)g'(x)`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   It's not pretty, but we can use the definition.

   .. math::
      &  \frac{d}{dx} (f(x)g(x)) \\
      =& \lim_{h\to0} \frac{f(x+h)g(x+h)-f(x)g(x)}{h} \\
      =& \lim_{h\to0} \frac{\overbrace{f(x)g(x+h)-f(x)g(x+h)}^\text{this is 0}
                            +f(x+h)g(x+h)-f(x)g(x)}{h} \\
      =& \lim_{h\to0} \frac{f(x+h)g(x+h)-f(x)g(x+h)+f(x)g(x+h)-f(x)g(x)}{h} \\
      =& \lim_{h\to0} \frac{(f(x+h)-f(x))g(x+h)+f(x)(g(x+h)-g(x))}{h} \\
      =& \lim_{h\to0} \left(
            \frac{(f(x+h)-f(x))\ g(x+h)}{h} + \frac{f(x)\ (g(x+h)-g(x))}{h}
         \right) \\
      =& \lim_{h\to0} \left(
         \frac{f(x+h)-f(x)}{h}g(x+h) + f(x)\frac{g(x+h)-g(x)}{h}
      \right) \\
      =& \lim_{h\to0} \left(\frac{f(x+h)-f(x)}{h}g(x+h)\right)
            + \lim_{h\to0}\left(f(x)\frac{g(x+h)-g(x)}{h}\right) \\
      =& \left(\lim_{h\to0}\frac{f(x+h)-f(x)}{h}\right)
        \left(\lim_{h\to0}g(x+h)\right)
        + f(x) \left(\lim_{h\to0}\frac{g(x+h)-g(x)}{h}\right) \\
      =& f'(x)g(x) + f(x)g'(x)

`\frac{d}{dx} x^c = c\ x^{c-1}`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   It's easy to prove that this works for an individual `c` value. For example,
   our very first derivative example shows that `\frac{d}{dx} x^2 = 2x`. Here
   I'll prove that this works with all positive integers using a powerful
   technique known as **induction**.

   Let's start by showing that this works with e.g. `c=1`:

      `\frac{d}{dx} x^1 = \frac{d}{dx} x = 1 = 1x^0 = 1x^{1-1}`

   Next we'll prove that **if** the rule works at `c=k` **then** it also works
   at `c=k+1` where `k` is a positive integer. Let's write things down just to
   be clear:

   :We assume: `\frac{d}{dx} x^k = k x^{k-1}`
   :We'll prove: `\frac{d}{dx} x^{k+1} = (k+1)x^{(k+1)-1}`

   Let's use the `\frac{d}{dx}(f(x)g(x))` and `\frac{d}{dx} x` rules we
   proved above and the assumption.

   .. math::
      \frac{d}{dx} x^{k+1}
      &= \frac{d}{dx} (x^k x^1) \\
      &= \frac{d}{dx} (x \cdot x^k) \\
      &= \left(\frac{d}{dx} x\right) \cdot x^k + x \cdot \left(\frac{d}{dx} x^k\right) \\
      &= 1x^k + x \cdot k x^{k-1} \\
      &= 1x^k + kx^1x^{k-1} \\
      &= 1x^k + kx^k \\
      &= (1+k)x^k \\
      &= (k+1)x^{(k+1)-1}

   We proved that if `\frac{d}{dx} x^k = k x^{k-1}` then
   `\frac{d}{dx} x^{k+1} = (k+1)x^{(k+1)-1}`. Now we know that the rule works
   when `c=1`, and then if we plug in `k=1` we know it works when `c=2`, and so
   on.

   .. asymptote::

      size(15cm);

      for (real c = 1; ; c+=1) {
         if (c == 4) {
            label("...", (c,-0.2));
            break;
         }
         label("$c="+(string)c+"$", (c,-0.2));
         draw((c+0.1,0)..(c+0.5,0.2)..(c+0.9,0), arrow=Arrow(size=5mm),
              L="$k="+(string)c+"$", align=N);
      }

   Note that we only proved that the rule works when `c` is a positive integer,
   but it also works when `c` is e.g. `\frac{1}{2}`. It's possible to prove
   that the rule isn't limited to positive integers, but that's beyond the
   scope of this tutorial.

`\frac{d}{dx} \sqrt x = \displaystyle \frac{1}{2\ \sqrt x}`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   We could prove this with the `\frac{d}{dx} x^c` rule because
   `\sqrt x = x^\frac{1}{2}`, but we proved the `x^c` rule only for positive
   integers. Let's survive without it. Again, it's a mess, but it works.

   .. math::

      \frac{d}{dx} \sqrt x
      &= \lim_{h\to0} \frac{\sqrt{x+h}-\sqrt x}{h} \\
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

`\frac{d}{dx}(1/x) = \displaystyle \frac{-1}{x^2}`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   We could use the `\frac{d}{dx} x^c` rule again because `1/x` is actually
   `x^{-1}`, but as before, we haven't proved that it works at `c=-1` so we'll
   do this without it.

   .. math::
      \frac{d}{dx} (1/x) &= \lim_{h\to0} \frac{\frac{1}{x+h} - \frac 1 x}{h} \\
      &= \lim_{h\to0} \frac{\frac{x}{(x+h)x} - \frac{x+h}{(x+h)x}}{h} \\
      &= \lim_{h\to0} \frac{\left(\frac{x-(x+h)}{(x+h)x}\right)}{h} \\
      &= \lim_{h\to0} \frac{x-(x+h)}{(x+h)xh} \\
      &= \lim_{h\to0} \frac{x-x-h}{(x+h)xh} \\
      &= \lim_{h\to0} \frac{-h}{(x+h)xh} \\
      &= \lim_{h\to0} \frac{-1}{(x+h)x} \\
      &= \frac{-1}{x^2}

`\frac{d}{dx} f(g(x)) = f'(g(x))g'(x)`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   This rule looks simple, but it's surprisingly difficult to prove correctly
   while keeping it easy to read. Here's the best proof I managed to make.

   Let's start by plugging stuff into the definition of derivative:

   .. math:: g'(x) = \lim_{h\to0} \frac{g(x+h)-g(x)}{h}
   .. math:: f'(g(x)) = \lim_{k\to0} \frac{f(g(x)+k)-f(g(x))}{k}
   .. asymptote::
      :align: right

      size(9cm);
      real xymin = -0.2;
      real xymax = 1.5;
      real the_x = 0.5;      // there's also a loop variable called x (lol)
      real h = 0.1;

      axises(xymin,xymax,xymin,xymax);

      real g(real x) { return sin(x+0.5); }

      path ggraph;
      for (real x = xymin; x < xymax; x += 1/16) {
         ggraph = ggraph..(x,g(x));
      }
      draw(ggraph, blue, L=rotate(20)*Label("$y=g(x)$"), align=N);

      draw((the_x,0)--(the_x,g(the_x)), lightblue);
      draw((the_x+h,0)--(the_x+h,g(the_x+h)), lightblue);
      label((the_x,0), L="$x$", align=SW);
      draw(brace((the_x+h,0),(the_x,0), amplitude=0.1), L="$h$", align=S);
      draw(brace((the_x,0),(the_x,g(the_x))), L="$g(x)$", align=W);
      draw(brace((the_x+h,g(the_x+h)),(the_x+h,0)), L="$g(x+h)$", align=E);

   Note that I used `h` with one limit and `k` with the other; the limits are
   completely independent of each other and I wanted to make it stand out. In
   other words, it doesn't matter how `h` and `k` relate to each other as long
   as both of them approach 0.

   The rule can be used only if `g'(x)` exists, and thus `g` must be
   continuous; see `the derivative existence stuff above <#which-functions-have-derivatives>`_.
   So, if `h \to 0` (read: h approaches 0) then `g(x+h) \to g(x)` and
   `(g(x+h)-g(x)) \to 0`.

   If we put all this together we can set `k=g(x+h)-g(x)`. Now it's time to
   calculate `f'(g(x))g'(x)`.

   .. math::

      &  f'(g(x))g'(x) \\
      =& \lim_{k\to0} \frac{f(g(x)+k)-f(g(x))}{k} \cdot \lim_{h\to0} \frac{g(x+h)-g(x)}{h} \\
      =& \lim_{k\to0} \lim_{h\to0} \left(
            \frac{f(g(x)+k)-f(g(x))}{k} \cdot \frac{g(x+h)-g(x)}{h}
      \right) \\
      =& \lim_{h\to0} \left(
            \frac{f(g(x)+g(x+h)-g(x))-f(g(x))}{g(x+h)-g(x)}
            \cdot \frac{g(x+h)-g(x)}{h}
      \right) \\
      =& \lim_{h\to0} \frac{f(g(x)+g(x+h)-g(x))-f(g(x))}{h} \\
      =& \lim_{h\to0} \frac{f(g(x)-g(x)+g(x+h))-f(g(x))}{h} \\
      =& \lim_{h\to0} \frac{f(g(x+h))-f(g(x))}{h} \\
      =& \frac{d}{dx} (f(g(x))

   .. asymptote::
      :align: right

      size(9cm);
      real xymin = -0.2;
      real xymax = 1.5;
      real the_x = 0.6;      // there's also a loop variable called x (lol)
      real h = 0.1;

      axises(xymin,xymax,xymin,xymax);
      real flatleft = the_x-2h, flatright=the_x+3h;

      real g(real x) {
         // flat spot around the_x
         if (flatleft < x && x < flatright)
            return 1;

         // elsewhere: cosine graph moved appropriately
         if (x < the_x)
            return cos(x-flatleft);
         return cos(x-flatright);
      }

      path ggraph;
      for (real x = xymin; x < xymax; x += 1/16) {
         ggraph = ggraph..(x,g(x));
      }
      draw(ggraph, blue, L="$y=g(x)$", align=N);

      draw((the_x,0)--(the_x,g(the_x)), lightblue);
      draw((the_x+h,0)--(the_x+h,g(the_x+h)), lightblue);
      label((the_x,0), L="$x$", align=SW);
      draw(brace((the_x+h,0),(the_x,0), amplitude=0.1), L="$h$", align=S);
      draw(brace((the_x,0),(the_x,g(the_x))), L="$g(x)$", align=W);
      draw(brace((the_x+h,g(the_x+h)),(the_x+h,0)), L="$g(x+h)$", align=E);

      draw((flatleft,g(the_x))--(flatright,g(the_x)), red);

   This looks nice, but we are not done yet! We divided by `k`. What if
   `k=g(x+h)-g(x)=0` when `h \to 0` but `h \ne 0`? Practically it means that
   the graph `y=g(x)` is a horizontal and straight line around `x` because
   `g(x+h)=g(x)` with a small `h`. So, we can say that `g(x)=c` on this
   interval (`c` is a constant) and prove this case separately:

   .. math:: f(g(x))g'(x) = f(c) \left(\frac{d}{dx} c\right) = f(c) \cdot 0 = 0
   .. math:: \frac{d}{dx} f(g(x)) = \frac{d}{dx} f(c) = 0

   Look carefully: `\frac{d}{dx} f(c) = 0` because we differenciated `f(c)`
   with respect to `x`, so `f(c)` was actually yet another constant because it
   doesn't depend on the value of `x`.

`\frac{d}{dx} \displaystyle \left(\frac{f(x)}{g(x)}\right) = \frac{f'(x)g(x) - f(x)g'(x)}{(g'(x))^2}`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   We need these rules that are proved above:

      * `\frac{d}{dx} (f(x)g(x)) = f'(x)g(x) + f(x)g'(x)`
      * `\frac{d}{dx} (1/x) = \displaystyle \frac{-1}{x^2}`
      * `\frac{d}{dx} f(g(x)) = f'(g(x))g'(x)`

   Now this is quite straight-forward.

   .. math::
      \frac{d}{dx} \left( \frac{f(x)}{g(x)} \right)
      =& \frac{d}{dx} \left( f(x) \frac{1}{g(x)} \right) \\
      =& f'(x)\frac{1}{g(x)} + f(x)\left(\frac{d}{dx}\left(\frac{1}{g(x)}\right)\right) \\
      =& \frac{f'(x)}{g(x)} + f(x) \frac{-1}{(g(x))^2} g'(x) \\
      =& \frac{f'(x)g(x)}{g(x)g(x)} - \frac{f(x)g'(x)}{(g(x))^2} \\
      =& \frac{f'(x)g(x) - f(x)g'(x)}{(g(x))^2}
