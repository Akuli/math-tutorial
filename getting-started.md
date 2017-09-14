# Math for Programmers

This tutorial goes **really fast**. I'll explain things more peacefully
if someone has trouble following it.

## Functions

As a programmer you know or guess what this Python code does:

```python
def f(x):
    return 2*x

print(f(6))
```

It prints the number `12`.

The syntax in math is more like that of functional programming
languages. For example, here's Haskell:

```haskell
Prelude> let f x = 2*x
Prelude> f 6
12
Prelude>
```

And finally, here's the same thing in math:

![math:f(x)=2x][]

![math:f(6)=12][]

That wasn't so hard at all!

Note that there is no special syntax for defining a function. All we have is the
equal sign, and when defining a function we just say that f of x is equal to 2x
and thus f of 6 is equal to 12.

A small note about `f(x)` versus `f x`: if you define your own function called
`f` or `g` or whatever people expect you to use parentheses, but you may omit
them with some "special" functions like `sin` and `cos` for historical reasons.
Also note that mathematicians prefer single-letter variable names because math
was originally written on paper, and writing long things by hand sucks.

## Very basic trig

**Problem:** A player moves to top-right at the angle of 60° measured from the
x axis at 10 pixels per second. How many pixels should the player's x and y
change every second?


```
            y
            |      O     <-- the player
            |     /
            |    /
            |   / ) 60°
------------|--/-----------> x
            | /
            |
```

Note that the y axis goes up in math so higher means bigger, but in programming
it's usually upside down.

This will have something to do with sine and cosine.

The unit circle is a circle with radius 1 placed in the middle of the xy plane.
Here's a picture that shows:

![unit circle](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Unit_circle.svg/352px-Unit_circle.svg.png)

This is really quite simple: the y coordinate is ![math:\sin t][] and the x
coordinate is ![math:\cos t][]. But the radius of the unit circle is 1 instead of
our 10, so we need to multiply everything by 10 to scale it up. We get this:

```python
player.x += 10*cos(60)
player.y += 10*sin(60)
```

Based on the unit circle, ![math:\sin 60\degree][] should be somewhere between
0.5 and 1 since the height of the x axis is 0 and the circle's top is at 1 (the
radius is 1). But something is wrong:

```python
>>> import math
>>> math.sin(60)
-0.3048106211022167
>>>
```

Now you're really like WTF. The angles with negative sines should be below the
x axis, e.g. something between 180° and 360°.

The problem is that Python, Haskell, C and most other programming languages use
radians by default instead of degrees. Let's convert them to radians so the sine
function is happy:

```python
>>> math.sin(math.radians(60))
0.8660254037844386
>>> math.cos(math.radians(60))
0.5000000000000001
>>> 
```

That's more like it. `0.5000000000000001` is obviously not an accurate result,
but it's good enough for a programmer.

Note that a real mathematician would say that ![math:\sin 60\degree][] is
![math:\frac{\sqrt{3}}{2}][] and ![math:\cos 60\degree][] is ![math:\frac{1}{2}][].

I might write more about radians, how the heck I came up with those
mathy-accurate values and how Python's conversion functions work some day.

[math:f(x)=2x]: images/math/080320743c76f725cd1f62a2c774c4e6.gif
[math:f(6)=12]: images/math/152e1ca519e8fcf69c2dbda118348af2.gif
[math:\sin t]: images/math/5732d78efedc927ac0d505b0b839d142.gif
[math:\cos t]: images/math/4d3eb39ad6e06c939af4dee7de899759.gif
[math:\sin 60\degree]: images/math/10eb7bf694bb1144845276b2337dd629.gif
[math:\sin 60\degree]: images/math/10eb7bf694bb1144845276b2337dd629.gif
[math:\frac{\sqrt{3}}{2}]: images/math/aed430fdf4c64058b58e05bf9ccbbbde.gif
[math:\cos 60\degree]: images/math/9964a77a0f345afa9b62df0d64c7993b.gif
[math:\frac{1}{2}]: images/math/93b05c90d14a117ba52da1d743a43ab1.gif
