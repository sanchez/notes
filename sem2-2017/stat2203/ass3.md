---
author: Daniel Fitzmaurice
title: STAT2203 Assignment 3
alt-name: 43961229
logo: /home/sanchez/Documents/logo.jpg
school: University Of Queensland
subject: ~()**STAT2203**~ -- Probability Models and Data Analysis for Engineering
---

# Question 1
$$$
&\quad\ \mathbb{E}\left((X-\mathbb{E}(X))^2\right)\\
&= \mathbb{E}(X^2 - 2X\mathbb{E}(X) + \mathbb{E}(X)^2)\\
&= \mathbb{E}(X^2) - 2\mathbb{E}(X\mathbb{E}(X)) + \mathbb{E}(X)^2 \tag{\text{Using }$\mathbb{E}(aX + bY) = a\mathbb{E}(X) + b\mathbb{E}(Y)$}\\
&= \mathbb{E}(X^2) - 2\mathbb{E}(X)^2 + \mathbb{E}(X)^2\\
&= \mathbb{E}(X^2) - \mathbb{E}(X)^2
$$$

# Question 2
Let *S* be the system success
Let *X* be component 1's lifetime
Let *Y* be component 2's lifetime
Let *Z* be component 3's lifetime

Since:
$$$
\lambda = \frac{1}{\bar{x}}
$$$
Therefore,
$$$
X&\sim Exp\left(\frac{1}{5}\right)\\
Y&\sim Exp\left(\frac{1}{3}\right)\\
Z&\sim Exp\left(\frac{1}{3}\right)\\
S&=X\cap(Y\cup Z)\\
\mathbb{P}(S\geq s) &= \mathbb{P}(X\geq s)\cap (\mathbb{P}(Y\geq s)\cup\mathbb{P}(Z\geq s))\\
&= \mathbb{P}(X\geq s)\cap(\mathbb{P}(Y\geq s)+\mathbb{P}(Z\geq s) - \mathbb{P}(Y\geq s)\mathbb{P}(Z\geq s))\\
&= \mathbb{P}(X\geq s)\mathbb{P}(Y\geq s)+\mathbb{P}(X\geq s)\mathbb{P}(Z\geq s)-\mathbb{P}(X\geq s)\mathbb{P}(Y\geq s)\mathbb{P}(Z\geq s)\\
&= \left(-e^{-\frac{s}{5}}\right)\left(-e^{-\frac{s}{3}}\right)+\left(-e^{-\frac{s}{5}}\right)\left(-e^{-\frac{s}{3}}\right)-\left(-e^{-\frac{s}{5}}\right)\left(-e^{-\frac{s}{3}}\right)\left(-e^{-\frac{s}{3}}\right)\\
&= e^{\frac{8}{15}s}+e^{\frac{8}{15}s} - e^{\frac{13}{15}s}\\
&= 2e^{\frac{8}{15}s} - e^{\frac{13}{15}s}
$$$

# Question 3
## Part A
Set F(x) to be one and measure the area under the curve
$$$
F(x) &= \int_0^{\frac{1}{2}}\alpha(1-x) dx\\
&=\int_0^{\frac{1}{2}}\alpha\quad dx-\int_0^{\frac{1}{2}}\alpha x\quad dx\\
&=\left[\alpha x - \alpha\frac{x^2}{2}\right]_0^{\frac{1}{2}}\\
1 &= \frac{\alpha}{2} - \frac{\alpha}{8}\\
&= \alpha\frac{3}{8}\\
\alpha &= \frac{8}{3}
$$$

## Part B
$$$
\mathbb{P}\left(\frac{1}{3} < X < \frac{1}{2}\right) &= \int_\frac{1}{3}^\frac{1}{2} \frac{8}{3}(1-x)\quad dx\\
&= \frac{8}{3}\int_\frac{1}{3}^\frac{1}{2} (1-x)\quad dx\\
&= \frac{8}{3}\left[x-\frac{x^2}{2}\right]_\frac{1}{3}^\frac{1}{2}\\
&= \frac{8}{3}\left(\left(\frac{3}{8}\right) - \left(\frac{1}{3} - \frac{1}{12}\right)\right)\\
&= \frac{8}{3}\left(\frac{3}{8}-\frac{1}{4}\right)\\
&= \frac{8}{3}\frac{1}{8}\\
&= \frac{1}{3}
$$$

# Question 4
## Part A
The variance of an Exp is
$$$
\frac{1}{\lambda^2}
$$$
Therefore since lambda is 1, the variance is 1

## Part B
$$$
Var(Z_n) &= Var\left( \frac{X_1+\ldots+X_n - \mathbb{E}(X_1+\ldots+X_n)}{\sqrt{Var(X_1+\ldots+X_n)}} \right)\\
&= Var\left( \frac{1}{\sqrt{n}}(X_1+\ldots+X_n) - \frac{n}{\sqrt{n}} \right)\\
&= \frac{Var(X_1+\ldots+X_n)}{n} \tag{$a^2 Var(X) = Var(aX + b)$}\\
&= \frac{n}{n}\\
&= 1
$$$
