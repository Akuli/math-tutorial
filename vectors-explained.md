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

![math:\sqrt{a^2+b^2}=c][]

If you look carefully you notice that the last step assumes ![math:c \ge 0][].
This is no problem because a triangle with a negative side length doesn't make
much sense anyway.

Note that this is not limited to vectors in any way, you can easily calculate
any diagonal like this.

## How the heck does atan2 work?

Now you should know how ![math:\sin][] and ![math:\cos][] can be defined in the
unit circle. There's also another, perhaps more common way to define them using
a triangle with one 90° corner.

![triangle with sides abc, c opposite of 90° corner](images/abctriangle.png)

This triangle is compatible with the ![math:a^2+b^2=c^2][] thing, but we can
also define sine, cosine and tangent in it like this:

![math:\sin t = \frac a c][]

![math:\cos t = \frac b c][]

![math:\tan t = \frac a b][]

It's also possible to define ![math:\tan t][] with the unit circle, but it's not
as simple as sine and cosine so we skipped that.

These triangle definitions are perfectly compatible with the unit circle
equivalents. If you draw [a triangle like this](images/unitcircle-triangle.png)
into the unit circle and then apply the triangle stuff, you get things like
![math:\sin t = \frac{\sin t}{1}][].

Let's look at the vector image again:

![the vector image u saw before](images/vector-calc.png)

Now with the tangent stuff we get this:

![math:\tan t = \frac b a][]

![math:t = \arctan \frac b a][]

Here ![math:\arctan][] is the inverse of ![math:\tan][], so
![math:\arctan (\tan t) = t][]. Most programming languages have an `atan(x)`
function that returns ![math:\arctan x][], and `atan2(b,a)` simply calculates
![math:\arctan \frac b a][].

Note that if ![math:a=0][] then ![math:\frac b a][] is dividing by 0 and thus
not defined, but if ![math:a][] is really really close to 0 then ![math:t][]
is about 90°.

![narrow triangle](images/narrow-triangle.png)

That's why `atan2(1, 0)` returns 90° and `atan2(-1, 0)` returns -90°. The
negativeness shouldn't be a problem because negative angles behave correctly
with functions like ![math:\sin][], ![math:\cos][] and ![math:\tan][].

[math:<a,b>]: images/math/aa1f3ce566ba1f6a19e4c6036e3bb61f.gif
[math:\sqrt{a^2 + b^2}]: images/math/49a12ba4c3e7dcb2a56081b67324dc91.gif
[math:a+b]: images/math/65c884f742c8591808a121a828bc09f8.gif
[math:(a+b)(a+b)=a(a+b)+b(a+b)=a^2+ab+ba+b^2=a^2+2ab+b^2]: images/math/f2da0d16615d4b60aef9414379059b0e.gif
[math:c^2]: images/math/2796af5074a7f27ecccd3cd17e165d53.gif
[math:\frac{ab}{2}]: images/math/4fcb01c272e647ff8050bf6babc44d56.gif
[math:(a+b)(a+b)=c^2+4\frac{ab}{2}]: images/math/f2a82b58e6a587c127bb48fb16d113cc.gif
[math:a^2+2ab+b^2=c^2+2ab]: images/math/5ebfc07c1dec4c7e1477e2a8eea93ead.gif
[math:a^2+b^2=c^2]: images/math/4e4cad74f2dc2eb92cc5b8fbf76de692.gif
[math:\sqrt{a^2+b^2}=c]: images/math/4e8bc0594ee08af065403ed3bf20b084.gif
[math:c \ge 0]: images/math/3f42f9a2cf87ec23780682aa5d81f95d.gif
[math:\sin]: images/math/5912fc1251cd0c1e212f6dd8d19f17ef.gif
[math:\cos]: images/math/8effff999de692c242b9f7a539c63e58.gif
[math:a^2+b^2=c^2]: images/math/4e4cad74f2dc2eb92cc5b8fbf76de692.gif
[math:\sin t = \frac a c]: images/math/834ad652ac63555b51075213a3506b26.gif
[math:\cos t = \frac b c]: images/math/55c6f6b4136c0f0fa1dcd3bb61ce15c6.gif
[math:\tan t = \frac a b]: images/math/95def45724b2544946420f6a5bc85c1a.gif
[math:\tan t]: images/math/8839bec86ca6a7a27ea4f73f70d54117.gif
[math:\sin t = \frac{\sin t}{1}]: images/math/c8c6a06df33fe7cf18f897708696d763.gif
[math:\tan t = \frac b a]: images/math/ea47439497e6f3d42683dec4b0d2afbf.gif
[math:t = \arctan \frac b a]: images/math/cce1d75de022fd4c19d364d8c3d53478.gif
[math:\arctan]: images/math/88ff4a6f25e9a1675fc702f8ee41a28a.gif
[math:\tan]: images/math/b00c5bd0cdc3e9432babf4fb3512b848.gif
[math:\arctan (\tan t) = t]: images/math/4ed921efd32595a9cbd97f70f42ff237.gif
[math:\arctan x]: images/math/be0e21a53d044912466e8b6663cdb405.gif
[math:\arctan \frac b a]: images/math/67b98867ca4f55b0cdbea34dfca9aecd.gif
[math:a=0]: images/math/ded681eaa02d11064c9a469dd1b3e04c.gif
[math:\frac b a]: images/math/bce982e75467fa5308996ef62525fbb0.gif
[math:a]: images/math/0cc175b9c0f1b6a831c399e269772661.gif
[math:t]: images/math/e358efa489f58062f10dd7316b65649e.gif
[math:\sin]: images/math/5912fc1251cd0c1e212f6dd8d19f17ef.gif
[math:\cos]: images/math/8effff999de692c242b9f7a539c63e58.gif
[math:\tan]: images/math/b00c5bd0cdc3e9432babf4fb3512b848.gif
