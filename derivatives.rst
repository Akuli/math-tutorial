Derivatives
===========

This chapter contains more not-so-practical math than the trig and geometry
chapter, but you may find it surprisingly fun. However, the math is not useless
gibberish isolated from real life and there's a practical and fun example at
the end.

.. warning::

   **If you're an experienced mathematician** you might feel like some of the
   notation used in this chapter is wrong. Stay calm and keep in mind that the
   whole purpose of notation is to express the math in a way that is easy to
   understand for others, and in this tutorial that's much more important than
   perfect correctness.


What is a derivative?
~~~~~~~~~~~~~~~~~~~~~

A *difference* means how much a value changes. For example, if the value of `x`
is first `5` and then we change it to `6`, `x` changes by `\Delta x = 1`. Here
`\Delta` is the Greek delta letter, so if someone's code has a variable named
``deltax`` it means this.

Let's draw a graph of something like `y = 2x+1`:

.. asymptote::

   size(14cm);
   grid(-1,5,-2,9);

   axises(-1,5,-2,9);
   // TODO: move this shit to axises()?
   for (real x = 1; x <= 4; x += 1) {
       draw((x,0)--(x,0), L=(string) x, align=S);
   }
   for (real y = 1; y <= 7; y += 1) {
       draw((0,y)--(0,y), L=(string) y, align=W);
   }

   real f(real x) { return 2*x + 1; }

   draw((-1,f(-1))--(3,f(3)));
   draw((3,f(3))--(4,f(4)), L=Label("$y=2x+1$", Rotate((1,2))), align=W);
   draw((0,f(0))--(3,f(0)), smalldashes, L="$\Delta x = 3$", align=N);
   draw((3,f(0))--(3,f(3)), smalldashes, L="$\Delta y = 6$", align=E);

For example, at `x=3` we know that `y = 2x+1 = 2 \cdot 3 + 1 = 7`.

Let's calculate the **slope** of this line:

.. math:: \frac{\Delta y}{\Delta x} = \frac{6}{3} = 2

The bigger the slope, the faster the line goes up, so the slope describes the
"**growing speed**" or "**changing speed**". I used the points `(1,0)` and
`(3,7)` when calculating the slope, but you should get the same slope with any
pair of points chosen from the line because the height grows at the same speed
everywhere.

.. TODO: turn "dividing by zero" into a link

The **derivative** `\frac{dy}{dx}` **is also a "changing speed"**, but `d`
instead of `\Delta` means that the changes we use for calculating derivatives
are *infinitely* tiny. You might be worried about calculating the
`\frac{dy}{dx}` because if `dx=0` then we're dividing by zero, but `dx` is not
zero; it's just really, really small.

If the graph is not a straight line, we get different `\frac{\Delta y}{\Delta x}`
ratios depending on which points we choose for calculating `\Delta y` and
`\Delta x`. The derivative `\frac{dy}{dx}` is not the same number everywhere,
but let's try to figure out how to calculate it anyway.

.. asymptote::
   :align: right

   size(12cm);

   real f(real x) { return 0.1*x**3 - 0.1x + 1; }
   axises(-0.1,2.2,-0.5,f(2));

   guide parabolaaa;
   for (real x = -0.1; x <= 2; x += 0.05) {
       parabolaaa = parabolaaa..(x,f(x));
   }
   //pathlabel(L=Label("MidPoint"), parabolaaa, position=0.5, align=Relative(W), sloped=true);
   draw(parabolaaa, L="$y=f(x)$", align=NW, p=heavyred);

   real x = 1.5;
   real dx = 0.1;

   draw((x,0)--(x,f(x)), lightblue);
   draw((x+dx,0)--(x+dx,f(x+dx)), lightblue);
   draw(brace((x,0), (0,0)), L="$x$", align=S);
   draw(brace((x+dx,-0.05), (x,-0.05), amplitude=0.1), L="$dx$", align=S);
   draw(brace((x,0), (x,f(x))), L="$f(x)$", align=W);
   draw(brace((x+dx,f(x+dx)), (x+dx,0)), L="$f(x+dx)$", align=E);
   draw(brace((x,f(x)),(x,f(x+dx)), amplitude=0.1), L="$dy$", align=W);
   draw(brace((x,f(x+dx)+0.05),(x+dx,f(x+dx)+0.05), amplitude=0.1), L="$dx$", align=N);

Let's look at `dy` and `dx`. The image at right seems to say that
`f(x) + dy = f(x+dx)`, so we should be able to solve `\frac{dy}{dx}`:

.. these are all in one ..math because i want them to be aligned with each
   other, and having sphinx align them at right is not a problem because
   they're about same length each

.. math::
   f(x) + dy = f(x+dx)

   dy = f(x+dx) - f(x)

   \frac{dy}{dx} = \frac{f(x+dx)-f(x)}{dx}

.. asymptote::
   :align: right

   size(10cm);

   axises(-3,3,-1,10);
   grid(-3,3,-1,10);

   guide xsquared_left, xsquared_right;
   for (real x = -3; x <= 0; x+= 1/8) { xsquared_left  = xsquared_left ..(x,x**2); }
   for (real x = 0 ; x <= 3; x+= 1/8) { xsquared_right = xsquared_right..(x,x**2); }
   draw(xsquared_left, p=blue);
   draw(xsquared_right, p=blue, L=Label(rotate(70)*"$y = x^2$"), align=W);

For example, the graph `y=x^2` is curvy. Let's find its derivative by plugging
in `y=f(x)=x^2` to the above formula. It'll be a mess, but don't worry, we can
do it.

.. math::

   \frac{dy}{dx}  &= \frac{f(x+dx)-f(x)}{dx} \\
                  &= \frac{(x+dx)^2 - x^2}{dx} \\
                  &= \frac{(x+dx)(x+dx) - x^2}{dx} \\
                  &= \frac{x(x+dx) + dx(x+dx) - x^2}{dx} \\
                  &= \frac{x^2 + x \cdot dx + dx \cdot x + (dx)^2 - x^2}{dx} \\
                  &= \frac{\overbrace{x^2 - x^2}^0 + x \cdot dx + dx \cdot x + (dx)^2}{dx} \\
                  &= \frac{x \cdot dx + x \cdot dx + dx \cdot dx}{dx} \\
                  &= \frac{(x + x + dx)dx}{dx} \\
                  &= x + x + dx \\
                  &= 2x+dx

.. asymptote::
   :align: right

   size(10cm);

   axises(-3,6,-1,20);

   // this is drawn first so it goes below the x^2 line
   real tangent(real x) {
       return 4*x-4;
   }
   draw((0.8,tangent(0.8))--(6,tangent(6)), p=darkorange,
        L=rotate(degrees(atan(4)))*Label("this thing's slope is 4", position=Relative(0.6)));

   guide xsquared;
   for (real x = -3; x <= 4.5; x+= 1/16) {
       xsquared = xsquared..(x,x**2);
   }
   draw(xsquared, p=blue, L=Label(rotate(75)*"$y = x^2$"), align=NW);

   draw((2,0)--(2,2**2), smalldashes);
   label("2", (2,0), align=S);

As `dx` gets smaller and smaller, `2x+dx` gets closer to `2x` and we can say
`\frac{dy}{dx} = 2x`.

I think this is cool. We started with a really horribly complicated-looking
thing but we arrived at just `2x`. What's more, the `2x` is not just a random
value we got out of a spooky calculation; for example, at `x=2` the derivative
is `2 \cdot 2 = 4`, so if we draw a straight line that barely touches `y=x^2`
at that point its slope will also be 4 like in the image at right.

You can also find the derivative of the `y=2x` example we looked at earlier,
and turns out that `\frac{dy}{dx}=2=\frac{\Delta y}{\Delta x}`. It makes sense
because derivatives are just like slopes but they also work with curvy things,
and there's no difference between a slope and a derivative of a straight line.

.. note::

   The derivative `\frac{dy}{dx}` can be also written as `\frac{d}{dx} y`, even
   though it doesn't make much sense because `dx` doesn't mean `d` times `x`.

   Another common style is to put a single quote after a function name, like
   `f'(x) = \frac{d}{dx} f(x)`.


Faster!
~~~~~~~

Finding the derivative was kind of complicated and really slow. With these
handy-dandy rules, you can get `2x` from `x^2` in a matter of seconds. Most of
these rules are easy to prove so there is no magic involved.

I have listed many rules here, but **don't panic**; there's no need to memorize
them. Here `f` and `g` can be any functions (e.g. `f(x)=\sqrt x - x` and
`g(x)=1`), and `c` can be any constant like `4` or `-\pi` but not e.g. `2x`
because that depends on the value of `x`. 

.. math::

   \begin{matrix}
      \frac{d}{dx}\ c = 0     & \frac{d}{dx}(c\ f(x)) = c\ f'(x) & \\
      &&\\
      \frac{d}{dx}\ x = 1     & \frac{d}{dx} (f(x)+g(x)) = f'(x)+g'(x) & \\ 
      &&\\
      \frac{d}{dx}\ cx = c    & \frac{d}{dx} (f(x)-g(x)) = f'(x)-g'(x) & \\
      &&\\
      \frac{d}{dx}\ x^c = c\ x^{c-1} & \frac{d}{dx} (f(x)g(x)) = f'(x)g(x) + g'(x)f(x) & \\
      &&\\
      \frac{d}{dx} \sqrt x = \frac{1}{2\ \sqrt x} & \frac{d}{dx} f(g(x)) = f'(g(x))g'(x)
   \end{matrix}

With these formulas you can find derivatives of long and scary functions
really easily. For example:

.. math::

   & \frac{d}{dx} (5x^3-6x^2+7x-123) \\
   &= \frac{d}{dx}(5x^3) - \frac{d}{dx}(6x^2) + \frac{d}{dx}(7x) - \frac{d}{dx}123 \\
   &= 5 \frac{d}{dx}(x^3) - 6 \frac{d}{dx}(x^2) + 7 - 0 \\
   &= 5 \cdot 3x^{3-1} - 6 \cdot 2x + 7 \\
   &= 15x^2 - 12x + 7

Of course, there's no need to write down all of these steps.

You can also use a nice symbolic calculation library, like Python's
`sympy <http://www.sympy.org>`_ (can be installed with pip):

.. code-block:: python

   >>> from sympy import *
   >>> init_printing(use_unicode=True)
   >>> x = Symbol('x')
   >>> diff(5 * x**3 - 6 * x**2 + 7*x - 123)
       2           
   15⋅x  - 12⋅x + 7

Here "diff" is short for "differenciate", and it means finding a derivative.

Libraries like sympy are also useful for doing long and messy calculations like
the one we did above:

.. code-block:: python

   >>> def f(x):
   ...     return x**2
   ...
   >>> dx = Symbol('dx')
   >>> expand((f(x+dx)-f(x))/dx)
   dx + 2⋅x


Example: Smooth Jumps
~~~~~~~~~~~~~~~~~~~~~

Let's say you're making a game where a player can jump over something. If the
player moves right at a steady speed, which of these jumps looks best?

.. asymptote::

   size(20cm);

   draw((0,0)--(0,1)--(1,1)--(1,0.5), smalldashes);
   dot((1,0.5));

   draw((1.5,0)--(1.5 + 2/3, 1)--(2.5,0.5), smalldashes);
   dot((2.5,0.5));

   real f(real x) {
       /* top of parabola should be between x=3.7 and x=4, calculations with x=4:
           f(x) = ax^2 + bx + c
           f'(x) = 2ax + b
           f'(3.7) = 0
           2*a*3.7 + b = 0
           -a approx 7.5 b

          i found the constant with trial and error */
       return -2x**2 + 15*x - 27.2;
   }

   guide parabolaaa;
   for (real x = 3; x <= 4.2; x += 0.05) {
       parabolaaa = parabolaaa..(x,f(x));
   }
   draw(parabolaaa, smalldashes);
   dot((4.2, f(4.2)));

The answer is obvious -- the rightmost jump looks best. It's time to figure out
how to make games with jumps like that.

Let's say that `t` is time and `h` is the height of our player, so we get this
graph:

.. asymptote::

   size(9cm);
   axises(-0.3, 3.5, -0.4, 2, "t", "h");

   real f(real x) { return -x**2 + 3*x - 0.5; }

   guide parabolaaa;
   for (real x = 0; x <= 3; x += 0.1) {
       parabolaaa = parabolaaa..(x,f(x));
   }
   draw(parabolaaa);

This looks like a parabola, and the equation of a parabola is `h = at^2+bt+c`
where `a`, `b` and `c` are constants. The changing speed of height is velocity
`v`:

.. math:: v = \frac{dh}{dt} = \frac{d}{dt} (at^2+bt+c) = 2at+b

On the other hand, the changing speed of velocity is the acceleration caused by
gravity. Let's call that `g`.

.. math:: g = \frac{dv}{dt} = \frac{d}{dt} (2at+b) = 2a

Note how the `t` disappeared and we're left with just the constant `2a`. This
makes sense because the gravity is always the same, no matter what time it is.

This Python program...

.. code-block:: python

   height = 0
   velocity = 10
   gravity = 2

   while height >= 0:
       print(' '*height + 'O')
       height += velocity
       velocity -= gravity

...prints this awesome parabola:

.. code-block:: none

   O
             O
                     O
                           O
                               O
                                 O
                                 O
                               O
                           O
                     O
             O
   O

You can use similar code for doing jumps in games.

.. admonition:: Exercise

   Create a minimal game where a player can be moved side to side with arrow
   keys and the player jumps when arrow up is pressed. I'll create an example
   implementation soon.
