# Vector Explanations

If you haven't read [this thing](README.md#vectors) yet go ahead and read it
now. This chapter focuses on explaining how the things in it work. **This thing
is not for you if you just want to get things done**

## The Length

In the vector section I said that the length of a vector ![math:<a,b>][] is
![math:\sqrt{a^2 + b^2}][]. If we have a square with triangles in it like this...

![classic proof](https://www.mathsisfun.com/geometry/images/pythagorean-theorem-proof.png)

...then we can calculate its area in a couple different ways:

- The square's sides are each ![math:a+b][], so the area must be
  ![math:(a+b)(a+b)=a(a+b)+b(a+b)=a^2+ab+ba+b^2=a^2+2ab+b^2][].
- The square consists of the yellow square whose area is ![math:c^2][] and 4
  blue triangles with area ![math:\frac{ab}{2}][] each.

We must get the same area with both ways, so we get this:

![math:(a+b)(a+b)=c^2+4\frac{ab}{2}][]

![math:a^2+2ab+b^2=c^2+2ab][]

![math:a^2+b^2=c^2][]

![math:sqrt{a^2+b^2}=c][]

If you look carefully you notice that the last step assumes ![math:c \ge 0][].
This is no problem because a triangle with a negative side length doesn't make
much sense anyway.

Note that this is not limited to vectors in any way, you can easily calculate
any diagonal like this.

## How the heck does atan2 work?

Now you should know how ![math:sin][] and ![math:cos][] can be defined in the
unit circle. There's also another, perhaps more common way to define them using
a triangle with one 90° corner.

![triangle with sides abc, c opposite of 90° corner](images/abctriangle.png)

Not only is this triangle compatible with the ![math:a^2+b^2=c^2][] thing, but
we can also define sine, cosine and tangent in it like this:

![math:\sin t = \frac a c][]

![math:\cos t = \frac b c][]

![math:\tan t = \frac a b][]

It's also possible to define tangent with the unit circle, but it's not as
simple as sine and cosine so we skipped that.

These triangle definitions are perfectly compatible with the unit circle
equivalents. If you draw [a triangle like this](images/unitcircle-triangle.png)
into the unit circle and then apply the triangle stuff, you get things like
![math:sin t = \frac{sin t}{1}][].

Let's look at the vector image again:

![the vector image u saw before](images/vector-calc.png)

Now with the new tangent stuff we just learn get this:

![math:\tan t = \frac b a][]

![math:t = \arctan \frac b a][]

Here ![math:\arctan][] is the inverse of ![math:\tan][], so
![math:\arctan \tan t = t][]. Most programming languages have an `atan(x)`
function that returns ![math:\arctan x][], and `atan2(b,a)` simply calculates
![math:\arctan \frac b a][].

Note that if ![math:a=0][] then ![math:\frac b a][] is dividing by 0 and thus
not defined, but if ![math:a][] is really really close to 0 then ![math:t][]
is about 90°.

![narrow triangle](images/narrow-triangle.png)

That's why `atan2(1, 0)` returns 90° and `atan2(-1, 0)` returns -90°. The
negativeness shouldn't be a problem because negative angles behave correctly
with functions like ![math:\sin][], ![math:\cos][] and ![math:\tan][].
