# The Basics

This tutorial assumes that you know these things. If you don't, that's not a
problem at all and you can just keep this page open while you read rest of the
tutorial.

## +, -, \*, /

I'm *sure* you know + and -.

In this tutorail, `a/b` is written as ![math:\frac a b][], and `a*b` is
sometimes written as ![math:a \cdot b][] but more often ![math:ab][].

Negative numbers behave like this when multiplied and divided. Note how two -'s
cancel out.

![math:2\cdot(-2)=-4][]

![math:(-2)\cdot(-2)=4][]

![math:\frac{-1}{-2}=\frac{1}{2}][]

## Powers and Roots

![math:x^5=x\cdot x\cdot x\cdot x\cdot x][]

![math:x^{a+b}=\underbrace{x\cdot x\cdot x\cdot...\cdot x}_\text{a+b pcs}=\underbrace{x\cdot...\cdot x}_\text{a pcs}\cdot\underbrace{x\cdot...\cdot x}_\text{b pcs}=x^ax^b][]

![math:(x^a)^b=\underbrace{\overbrace{x^a}^{x\cdot...\cdot x,\ \text{a pcs}} \cdot\ \ x^a\ \cdot ... \cdot x^a}_\text{b pcs}=\underbrace{x\cdot x\cdot...\cdot x}_{a\cdot b\ \text{pcs}}=x^{ab}][]

![math:\sqrt x = x^\frac 1 2][]

![math:(\sqrt x)^2=x^\frac 1 2 \cdot x^\frac 1 2 = x^{\frac 1 2 + \frac 1 2} = x^1 = x][]

Note that ![math:\sqrt x][] only works if ![math:x \ge 0][], and also
![math:\sqrt x \ge 0][] (unless you use complex numbers, but so far we haven't
needed them in this tutorial).

In most programming languages, ![math:x^a][] is `x**y` or `pow(x, y)` and
![math:\sqrt x][] is `sqrt(x)`. Depending on the language you might need e.g.
`Math.sqrt` instead of `sqrt`.

[math:\frac a b]: images/math/bf97403b855d7684b583323d15579b8b.gif
[math:a \cdot b]: images/math/11e60ba50ad18c52fd95e243667a62cd.gif
[math:ab]: images/math/187ef4436122d1cc2f40dc2b92f0eba0.gif
[math:2\cdot(-2)=-4]: images/math/4776ce379db4fa3932ad3517c05463b6.gif
[math:(-2)\cdot(-2)=4]: images/math/0b6eaa1d7f84d189c5e44e87d665a1d0.gif
[math:\frac{-1}{-2}=\frac{1}{2}]: images/math/ec288525cac3614fa7764d5e589d8a4d.gif
[math:x^5=x\cdot x\cdot x\cdot x\cdot x]: images/math/2cbab7c8fba9a07388d76ae664eb6b26.gif
[math:x^{a+b}=\underbrace{x\cdot x\cdot x\cdot...\cdot x}_\text{a+b pcs}=\underbrace{x\cdot...\cdot x}_\text{a pcs}\cdot\underbrace{x\cdot...\cdot x}_\text{b pcs}=x^ax^b]: images/math/89d150a6e7cdd864be80b9edbff6c1b1.gif
[math:(x^a)^b=\underbrace{\overbrace{x^a}^{x\cdot...\cdot x,\ \text{a pcs}} \cdot\ \ x^a\ \cdot ... \cdot x^a}_\text{b pcs}=\underbrace{x\cdot x\cdot...\cdot x}_{a\cdot b\ \text{pcs}}=x^{ab}]: images/math/553cf0adbc819d51ac33024b8f1fc8b7.gif
[math:\sqrt x = x^\frac 1 2]: images/math/a0249919292fdb950e1b1b923a837488.gif
[math:(\sqrt x)^2=x^\frac 1 2 \cdot x^\frac 1 2 = x^{\frac 1 2 + \frac 1 2} = x^1 = x]: images/math/1363bafcef384a920d12184ff336b93a.gif
[math:\sqrt x]: images/math/f108a3d88b22ff91ddbd459b0f359bc9.gif
[math:x \ge 0]: images/math/074097ea89225398ceb1128b5405b9fb.gif
[math:\sqrt x \ge 0]: images/math/696f86ff9bbd38678a7c05a016b15d63.gif
[math:x^a]: images/math/347b99be8c291ade0c6b4d680e18916a.gif
[math:\sqrt x]: images/math/f108a3d88b22ff91ddbd459b0f359bc9.gif
