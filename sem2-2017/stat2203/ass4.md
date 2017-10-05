---
author: Daniel Fitzmaurice
title: STAT2203 Assignment 4
alt-name: 43961229
logo: /home/sanchez/Documents/logo.jpg
school: University of Queensland
subject: ~()**STAT2203**~ -- Probability Models and Data Analysis for Engineering
---

# Question 1
## Part A
Let *C{1}* be circle with radius 2
Let *C{2}* be circle with radius 1.5
The area of *C{1}* and *C{2}* are 4pi and 2.25pi respectively
Therefore:
$$$
\mathbb{P}(R>1.5) &= \frac{\mathbb{P}(C_1) - \mathbb{P}(C_2)}{\mathbb{P}(C_1)}\\
&= \frac{4\pi - 2.25\pi}{4\pi}\\
&= 0.4375
$$$

## Part B
Using the information above, replacing 1.5 with *r*
$$$
\mathbb{P}(R>r) &= \frac{4\pi - \pi r^2}{4\pi}\\
&= \frac{4 - r^2}{4}\\
&= 1 - \frac{r^2}{4}\\
F_R(r) = \mathbb{P}(R\leq r) &= 1-\mathbb{P}(R>r)\\
&= 1 - \left(1 - \frac{r^2}{4}\right)\\
&= \frac{r^2}{4}\\
f_R(r) &= \frac{d}{dr} \frac{r^2}{4}\\
&= \begin{cases}\frac{r}{2} & 0 \leq r \leq 2\\0 & \text{otherwise}\end{cases}
$$$

# Question 2
## Part A
Because *f{X,Y}(x,y) = f{X}(x)f{Y}(y)* where *f{X} = 2x* when *0 &le; x &le; 1* and *f{Y}(y) = 2y* when *0 &le; y &le; 1*

## Part B
$$$
\mathbb{P}(2X > Y) &= \mathbb{P}\left(X > \frac{Y}{2}\right)\\
\mathbb{P}\left(X > \frac{Y}{2}\right) &= 1 - \mathbb{P}\left(X \leq \frac{Y}{2}\right)\\
&= 1-\int_0^1\int^{\frac{y}{2}}_0 4xy\quad dxdy\\
&= 1-\int_0^1\left[4y\frac{x^2}{2}\right]^{\frac{y}{2}}_0 \quad dy\\
&= 1-\int_0^1\left[2yx^2\right]^{\frac{y}{2}}_0 \quad dy\\
&= 1-\int_0^1\frac{2y^3}{4} \quad dy\\
&= 1-\int_0^1\frac{y^3}{2} \quad dy\\
&= 1-\left[\frac{y^4}{8}\right]^1_0\\
&= 1-\frac{1}{8}\\
&= \frac{7}{8}
$$$

# Question 3
$$$
\mathbb{P}(U\leq u) &= \mathbb{P}(\frac{X}{X+Y}\leq u)\\
&= \mathbb{P}(X \leq u(X+Y))\\
&= \mathbb{P}(X \leq uX + uY)\\
&= \mathbb{P}(X - uX \leq uY)\\
&= \mathbb{P}(X(1-u)\leq uY)\\
&= \mathbb{P}\left(X\frac{1-u}{u}\leq Y\right)\\
&= \mathbb{P}\left(Y\geq X\frac{1-u}{u}\right)
$$$
Since *f{X,Y}(x,y) = f{X}(x)f{Y}(y)*:
$$$
\mathbb{P}\left(Y\geq X\frac{1-u}{u}\right) &= \int_0^\infty\int^\infty_{x\frac{(1-u)}{u}} f_{X,Y}(x,y)\quad dydx\\
&= \int_0^\infty\int^\infty_{x\frac{1-u}{u}} f_X(x)f_Y(y)\quad dydx\\
&= \int_0^\infty\int^\infty_{x\frac{1-u}{u}} e^{-x}e^{-y}\quad dydx\\
&= \int_0^\infty e^{-x}\int^\infty_{x\frac{1-u}{u}} e^{-y}\quad dydx\\
&= \int_0^\infty e^{-x}\left[-e^{-y}\right]^\infty_{x\frac{1-u}{u}}\quad dx\\
&= \int_0^\infty e^{-x}\left(0+e^{-x\frac{1-u}{u}}\right)\quad dx\\
&= \int_0^\infty e^{-x}e^{\frac{-x}{u}}e^{x}\quad dx\\
&= \int_0^\infty e^{\frac{-x}{u}}\quad dx\\
&= \left[-ue^{\frac{-x}{u}}\right]^\infty_0\quad dx\\
&= ue^0\\
&= u
$$$

# Question 4
```
function result = ass4q4
    N = 1e7;
    R = 2.*sqrt(rand(N,1));
    I = (R > 1);
    mean(I);
endfunction
```
This yields a response of approximately 0.74992

# Question 5
```
function result = ass4q5
    N = 1e7;
    X = sqrt(rand(N,1));
    Y = sqrt(rand(N,1));
    I = (2.*X>Y);
    mean(I);
endfunction
```
This yields a response of approximately 0.8751

# Question 6
```
function result = ass4q6
    N = 1e7;
    X = -log(rand(N,1));
    Y = -log(rand(N,1));
    U = X./(X+Y);
    hist(U, (0:0.05:0.0975));
    ylabel("U Frequencies");
    xlabel("u");
endfunction
```

![Question 6 answer](sem2-2017/stat2203/ass4q6.png)[100]
