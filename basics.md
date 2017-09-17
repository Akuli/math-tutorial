# The Basics

This tutorial assumes that you know these things. If you don't, that's not a
problem at all and you can just keep this page open while you read rest of the
tutorial.

## +, -, \*, /

I'm *sure* you know + and -.

In this tutorial, `a/b` is written as ![math:\frac a b][], and `a*b` is
sometimes written as ![math:a \cdot b][] but more often ![math:ab][].

You can also use these handy things:

![math:0x=0][]

![math:ab=ba][] (but ![math:\frac a b=\frac b a][] only when ![math:a=b\ne0][])

![math:(a+b)c=ac+bc][]

![math:\frac{ac}{bc}=\frac a b][] if ![math:b\ne0][] and ![math:c\ne0][]

See [Numberphile's awesome zero video](https://youtu.be/BRRolKTlF6Q) if you're
wondering why dividing by zero is not allowed.

Negative numbers behave like this when multiplied and divided. Note how two -'s
cancel out.

![math:2\cdot(-2)=-4][]

![math:(-2)\cdot(-2)=4][]

![math:\frac{-1}{-2}=\frac{(-1)\cdot 1}{(-1)\cdot 2}=\frac 1 2][]

## Absolute Value

![math:|x|=\left\{\begin{matrix}x\text{ if }x\ge0\\-x\text{ if }x<0\end{matrix}\right][]

For example, ![math:|2|=2][] and ![math:|-3|=3][]. ![math:|x|][] is `abs(x)` in
most programming languages, but you may need e.g. `Math.abs(x)` depending on the
language.

## Powers and Square Root

In most programming languages, ![math:x^y][] is `x**y` or `pow(x, y)` and
![math:\sqrt x][] is `sqrt(x)`.

![math:x^5=x\cdot x\cdot x\cdot x\cdot x][]

![math:x^{a+b}=\underbrace{x\cdot x\cdot x\cdot...\cdot x}_\text{a+b pcs}=\underbrace{x\cdot...\cdot x}_\text{a pcs}\cdot\underbrace{x\cdot...\cdot x}_\text{b pcs}=x^ax^b][]

![math:(x^a)^b=\underbrace{\overbrace{x^a}^{x\cdot...\cdot x,\ \text{a pcs}} \cdot\ \ x^a\ \cdot ... \cdot x^a}_\text{b pcs}=\underbrace{x\cdot x\cdot...\cdot x}_{a\cdot b\ \text{pcs}}=x^{ab}][]

![math:\sqrt x = x^\frac 1 2][]

![math:(\sqrt x)^2=x^\frac 1 2 \cdot x^\frac 1 2 = x^{\frac 1 2 + \frac 1 2} = x^1 = x][]

Note that ![math:\sqrt x][] only works if ![math:x \ge 0][], and also
![math:\sqrt x \ge 0][] (unless you use complex numbers, but so far we haven't
needed them in this tutorial).

Confusingly ![math:\sqrt{x^2}=|x|][], e.g. ![math:\sqrt{(-2)^2}=\sqrt4=2][]
where ![math:(-2)^2=4][] (see [above](#----)).

## Equations

For example:

![math:2x+1=9][]

![math:2x=8][]

![math:x=4][]

You can add or substract any numbers from both sides, like substracting 1 in the
first step, or you can multiply or divide both sides by any nonzero number.

## See Also

This chapter shows only the things you need in the rest of this tutorial, but
[this cheat sheet](http://tutorial.math.lamar.edu/pdf/Algebra_Cheat_Sheet.pdf)
is more complete.

[math:\frac a b]: images/math/bf97403b855d7684b583323d15579b8b.gif
[math:a \cdot b]: images/math/11e60ba50ad18c52fd95e243667a62cd.gif
[math:ab]: images/math/187ef4436122d1cc2f40dc2b92f0eba0.gif
[math:0x=0]: images/math/8177684c0f20605d5cb599a2e572a016.gif
[math:ab=ba]: images/math/e535c14059b453f327db1fc15f33f108.gif
[math:\frac a b=\frac b a]: images/math/24259f28ef4d734d302276f1d7486499.gif
[math:a=b\ne0]: images/math/22abfbe4e0f52006656d398a51aa28a8.gif
[math:(a+b)c=ac+bc]: images/math/fda516801265bdcecd104f840b535c04.gif
[math:\frac{ac}{bc}=\frac a b]: images/math/240a3f880e24b5b0ee3851678d011545.gif
[math:b\ne0]: images/math/902294c62589bf0ded2e67a20fb13807.gif
[math:c\ne0]: images/math/0f3c387a0d09fb844f5faca72ae22375.gif
[math:2\cdot(-2)=-4]: images/math/4776ce379db4fa3932ad3517c05463b6.gif
[math:(-2)\cdot(-2)=4]: images/math/0b6eaa1d7f84d189c5e44e87d665a1d0.gif
[math:\frac{-1}{-2}=\frac{(-1)\cdot 1}{(-1)\cdot 2}=\frac 1 2]: images/math/edb893bab76cad27869b4ff1bf1a085d.gif
[math:|x|=\left\{\begin{matrix}x\text{ if }x\ge0\\-x\text{ if }x<0\end{matrix}\right]: images/math/48a80243158416d73cd18a6a18f774f7.gif
[math:|2|=2]: images/math/1d5b280040c7b5897d313e812280316f.gif
[math:|-3|=3]: images/math/1f7f1085e75aad46877e7eb8629199b9.gif
[math:|x|]: images/math/cf513decf6e4ace0e25cb1c932aaa049.gif
[math:x^y]: images/math/67d8bd969cb2cf1b378f5e534a19d936.gif
[math:\sqrt x]: images/math/f108a3d88b22ff91ddbd459b0f359bc9.gif
[math:x^5=x\cdot x\cdot x\cdot x\cdot x]: images/math/2cbab7c8fba9a07388d76ae664eb6b26.gif
[math:x^{a+b}=\underbrace{x\cdot x\cdot x\cdot...\cdot x}_\text{a+b pcs}=\underbrace{x\cdot...\cdot x}_\text{a pcs}\cdot\underbrace{x\cdot...\cdot x}_\text{b pcs}=x^ax^b]: images/math/89d150a6e7cdd864be80b9edbff6c1b1.gif
[math:(x^a)^b=\underbrace{\overbrace{x^a}^{x\cdot...\cdot x,\ \text{a pcs}} \cdot\ \ x^a\ \cdot ... \cdot x^a}_\text{b pcs}=\underbrace{x\cdot x\cdot...\cdot x}_{a\cdot b\ \text{pcs}}=x^{ab}]: images/math/553cf0adbc819d51ac33024b8f1fc8b7.gif
[math:\sqrt x = x^\frac 1 2]: images/math/a0249919292fdb950e1b1b923a837488.gif
[math:(\sqrt x)^2=x^\frac 1 2 \cdot x^\frac 1 2 = x^{\frac 1 2 + \frac 1 2} = x^1 = x]: images/math/1363bafcef384a920d12184ff336b93a.gif
[math:\sqrt x]: images/math/f108a3d88b22ff91ddbd459b0f359bc9.gif
[math:x \ge 0]: images/math/074097ea89225398ceb1128b5405b9fb.gif
[math:\sqrt x \ge 0]: images/math/696f86ff9bbd38678a7c05a016b15d63.gif
[math:\sqrt{x^2}=|x|]: images/math/959babe8407cdf233d2ae124dc0f8329.gif
[math:\sqrt{(-2)^2}=\sqrt4=2]: images/math/432c66cae765f66e18d8854e76ccbd3d.gif
[math:(-2)^2=4]: images/math/b0361d47a79858018a3b6318baeabff5.gif
[math:2x+1=9]: images/math/a5a26bfedee6b498ecfc7794197137d9.gif
[math:2x=8]: images/math/e1d072e3de30611949b31a21229cef6a.gif
[math:x=4]: images/math/440bcb2225cd249b09bb29454f83249d.gif