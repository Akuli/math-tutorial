Integrals
=========

.. attention::
   This chapter assumes that you know what derivatives are and how they work.
   If you don't, I recommend reading :ref:`my derivative chapter <derivatives>`
   first.

There are many practical ways to use derivatives like the game at the end of
the derivative chapter demonstrates. You won't find as many practical uses for
this chapter unless you need a bunch of random area calculations for something,
but as with the derivatives, the math itself is plenty of fun.


The Problem
~~~~~~~~~~~

Here's a picture of a few areas:

.. asymptote::

   size(25cm);

   transform shift1 = shift(-6,0);
   transform shift2 = shift(-3,0);

   real a = 2, b = 1.5;

   filldraw(shift1*((0,0)--(a,0)--(a,b)--(0,b)--cycle), lightblue);
   label("$6$", shift1*(a/2,0), align=S);
   label("$4$", shift1*(a,b/2), align=E);
   label("$6\cdot4=24$", shift1*(a/2,b/2));

   filldraw(shift2*((0,0)--(a,0)--(a,b)--cycle), lightblue);
   label(shift2*(a/2,0), L="$6$", align=S);
   label(shift2*(a,b/2), L="$4$", align=E);
   label("$\frac{6\cdot4}{2}=12$", shift2*(a*2/3,b/4));

   real f(real x) {
      return 1/(2*sqrt(x));
   }

   guide curvie, littlecurvie;
   for (real x=0.05; x<=3; x+=0.1) {
      curvie = curvie..(x,f(x));
      if (1 <= x && x <= 2)
         littlecurvie = littlecurvie..(x,f(x));
   }

   // this stuff goes below curvie
   fill((1,0)--(1,f(1))--littlecurvie--(2,f(2))--(2,0)--cycle, lightblue);
   draw((1,0)--(1,f(1)));
   draw((2,0)--(2,f(2)));
   label("???", (1.5,f(1.5)/2));

   draw(curvie, deepgreen, L="$y=\frac{1}{2 \sqrt x}$", align=NE);
   axises(-0.3,3,-0.3,2.5);
   label("1", (1,0), align=S);
   label("2", (2,0), align=S);

The first two areas are easy to calculate and everything is quite
self-explanatory, but how the heck are we going to do the third one?

If this was a question on a codeacademy-like noob programming site you would
probably write some code that approximates the area by calculating areas of
little rectangles. This Python program prints ``0.42167045099417744``:

.. asymptote::
   :align: right

   size(10cm);
   axises(0.5,2.5,0,0);

   real f(real x) {
      return 1/(2*sqrt(x));
   }

   guide curvie, littlecurvie;
   for (real x=0.5; x<=2.5; x+=0.1) {
      curvie = curvie..(x,f(x));
   }
   draw(curvie, deepgreen, L="$y=\frac{1}{2 \sqrt x}$", align=N);

   for (real x = 1; x < 2-0.001; x += 0.1) {
      filldraw((x,0)--(x+0.1,0)--(x+0.1,f(x))--(x,f(x))--cycle, lightblue);
   }


   label("$1$", (1,0), align=S);
   label("$2$", (2,0), align=S);

.. code-block:: python

   import math

   def f(x):
       return 1/(2 * math.sqrt(x))

   slice_width = 0.1

   result = 0
   x = 1
   while x < 2:
       result += slice_width * f(x)
       x += slice_width
   print(result)

The answer is not too bad and we could make it much better by adjusting
``slice_width``, but I calculated the same area on paper by hand in about
**10 seconds** and I got a precise answer instead of a decimal approximation.
This chapter is all about how I did that and why it works.


The Area
~~~~~~~~

.. asymptote::
   :align: right

   size(12cm);

   real f(real x) { return 0.1*x**3 - 0.1x + 1; }
   axises(-0.1,2.2,-0.5,f(2));

   guide slicebetween(guide p, real a, real b) {
      return firstcut(firstcut(p, (a,-10)--(a,10)).after, (b,-10)--(b,10)).before;
   }

   guide parabolaaa;
   guide littleparab;
   for (real x = -0.1; x <= 2; x += 0.05) {
       parabolaaa = parabolaaa..(x,f(x));
   }

   real x = 1.5;
   real dx = 0.3;

   fill(slicebetween(parabolaaa, 0, x)--(x,0)--(0,0)--cycle, paleyellow);
   label("$A$", (x/2,f(x/2)/2));
   axises(-0.1,2.2,-0.5,f(2));
   draw(parabolaaa, L="$y=f(x)$", align=NW, p=blue);

   draw((x,0)--(x,f(x)), lightblue);
   draw((x+dx,0)--(x+dx,f(x+dx)), lightblue);
   draw(brace((x,0), (0,0)), L="$x$", align=S);
   draw(brace((x+dx,-0.05), (x,-0.05), amplitude=0.1), L="$\Delta x$", align=S);
   draw(brace((x+dx+0.05,f(x)), (x+dx+0.05,0)), L="$f(x)$", align=E);
   label("$\Delta A$", (x+dx/2,f(x+dx/2)/2));

   fill((x,f(x))--(x+dx,f(x))--(x+dx,f(x+dx))--cycle, red);

Let's say that our curve is of the form `y=f(x)` where `f` is a
:ref:`continuous <has-derivative>` function. Maybe we could find out what the
area `A` is under the curve between 0 and `x`?

Let's imagine that we choose some point `x` and *move* it right by `\Delta x`.
Then the area grows by a slice of width `\Delta x` and height `f(x)`. If we
assume that the slice is a rectangle we get a small error (red triangle in
image), but we can calculate the slice's area `\Delta A` with the rectangle
formula:

.. math::
   \Delta A & \approx f(x) \Delta x \\
   \frac{\Delta A}{\Delta x} & \approx f(x)

Now if we make the `\Delta x` *infinitely* tiny, the red triangle is so small
compared to `\Delta A` that we can ignore it:

.. math::
   \frac{dA}{dx} = f(x)

Yes, this is correct! We can use a derivative here. This is precise, so we can
get rid of `\approx` and replace it with `=`.

So, if we want to calculate areas all we really need is an antiderivative
function `F` so that `F'(x)=f(x)`.

.. asymptote::
   :align: right

   size(8cm);

   real f(real x) {
      return 1/(2*sqrt(x));
   }

   guide curvie, littlecurvie;
   for (real x=0.05; x<=3; x+=0.1) {
      curvie = curvie..(x,f(x));
      if (1 <= x && x <= 2)
         littlecurvie = littlecurvie..(x,f(x));
   }

   // this stuff goes below curvie
   fill((1,0)--(1,f(1))--littlecurvie--(2,f(2))--(2,0)--cycle, lightblue);
   draw((1,0)--(1,f(1)));
   draw((2,0)--(2,f(2)));
   label("???", (1.5,f(1.5)/2));

   draw(curvie, deepgreen, L="$y=f(x)=\frac{1}{2 \sqrt x}$", align=NE);
   axises(-0.3,3,-0.3,2.5);
   label("1", (1,0), align=S);
   label("2", (2,0), align=S);


Our First Integral
~~~~~~~~~~~~~~~~~~

Let's go back to our original problem. One of
:ref:`our derivative rules <derivative-rules>` was this:

.. math:: \frac{d}{dx} \sqrt x = \frac{1}{2 \sqrt x}

.. asymptote::
   :align: right

   size(12cm);

   real f(real x) {
      return x**2/3;
   }
   real a = 2;
   real b = 2.8;

   guide curvie, littlecurvie;
   for (real x=0.05; x<=3; x+=0.1) {
      curvie = curvie..(x,f(x));
   }

   guide slicebetween(guide p, real a, real b) {
      return firstcut(firstcut(p, (a,-10)--(a,10)).after, (b,-10)--(b,10)).before;
   }

   // this stuff goes below curvie
   fill((a,0)--(a,f(a))--slicebetween(curvie, a, b)--(b,f(b))--(b,0)--cycle, lightblue);
   fill((0,f(0))--slicebetween(curvie, 0.1, a)--(a,0)--cycle, lightyellow);
   draw((a,0)--(a,f(a)));
   draw((b,0)--(b,f(b)));
   label(rotate(70)*"$F(b)-F(a)$", (a+0.2,0.2), align=N);

   draw(curvie, L=Label(rotate(50)*"$y=f(x)$"), align=NW);
   axises(-0.3,3.5,-0.3,3);
   label("$a$", (a,0), align=S);
   label("$b$", (b,0), align=S);
   label("$F(a)$", (a*3/4,f(a)/5));

So it looks like the antiderivative function `F` that gives us the area between
`0` and `x` is `F(x) = \sqrt x`. But how about `\sqrt x + 1`? Its derivative is
`\frac{1}{2 \sqrt x}` because `\frac{d}{dx} 1 = 0`. Or how about
`\sqrt x + 100` or `\sqrt x - 10`? We don't know what the function is, all we
know is that `F(x) = \sqrt x + C` where `C` is a constant.

Let's try to calculate our area:

.. math::

   F(b)-F(a)   &= (\sqrt b + C) - (\sqrt a + C) \\
               &= \sqrt b + C - \sqrt a - C \\
               &= \sqrt b - \sqrt a \\
               &= \sqrt 2 - \sqrt 1 \\
               &= \sqrt 2 - 1 \\
               &= 0.414213562373...

That's all there's to it! A precise area.

This took quite a while because we went through all the steps needed to
understand everything, but now that you know ho
