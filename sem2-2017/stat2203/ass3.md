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
