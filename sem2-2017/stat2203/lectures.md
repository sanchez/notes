---
author: Daniel Fitz
title: STAT2203 Lecture Notes
alt-name: 43961229
logo: /home/sanchez/Documents/logo.jpg
school: University of Queensland
subject: ~()**STAT2203**~ -- Probability and Statistics for Engineering
---
\toc
\\
\
# Sums and Extremes of Independent Random Variables
## Multivariate Normal Distribution
- Jointly Gaussian Random Variables; as affine transform of vector of independent standard normals, examples
- Expectation of Vector- and Matrix-valued RVs; application to multivariate normal
- Affine combinations of independent normals; result, examples

### Affine Combinations of Normals Example
**Exercise:** Let *X{1}, ..., X{n} ~ N(u,o{{2}})* represent repeated measurements. Find is the distribution of the average measurement
$$$
Y=\frac{X_1 + \cdots + X_n}{n}
$$$

## Sums of Independent Random Variables
**Law of Large Numbers** and the **Central Limit Theorem**. Both theorems deal with **Sums of Independent Random Variables**. They arise for example in the following situations:
1. We flip a (biased) coin infinitely many times. Let *X{i} = 1* if the ith flip is "heads" and *X{i} = 0* otherwise. In general we do not know *p = P(X{i} = 1)*. However, using the outcomes *x{1}, ..., x{n}*, we could estimate *p* by *(x{1} + ... + x{n})/n*
1. A certain machine needs to work continuously. The machine has one component that is very unreliable. This component is replaced immediately upon failure. Suppose there are *n* such (spare) components. If we denote the component lifetimes by *X{1}, ..., X{n}*, then the lifetime of the machine is given by *X{1} + ... + X{n}*.
1. We weigh 20 randomly selected people. The average weight of the group is *(X{1} + ... + X{20})/20*
Let *X{1}, ..., X{n}*  be independent and identically distributed random variables. For each *n* let
$$$
S{n} = X{1} + \cdots + X{n}
$$$
Let *EX{i} = u* and *Var(X{i}) = o^2* (assuming that these are finite).

Some easy results are:
$$$
\mathbb{E}S_n = n\mathbb{E}X_1 = n\mu
$$$
and, by the independence of the summands,
$$$
Var(S_n) = n\ Var(X_1) = n\sigma^2
$$$

If we know the pdf or pmf of *X{i}*, then we can (in principle) determine the pdf or pmf of *S{n}*. The easiest way is to use **transform** techniques (Laplace transform, Characteristic function, etc).
An important property of these transforms is that ~()the transform of the **sum** of independent random variables is equal to the **product** of the individual transforms~.

### Example
**Example:** Suppose each *X{i} ~ Exp(lambda)*. The Laplace transform of *X{i}*, say *L* is given by
$$$
L(s) = \mathbb{E}e^{-sX_i} = \frac{\lambda}{\lambda+s}
$$$
The Laplace transform of *S{n}*, is given by
$$$
\mathbb{E}e^{-sS_n} &= \mathbb{E}e^{-s(X_1+\cdots+X_n)}\\
&= \mathbb{E}e^{-sX_1}\cdots\mathbb{E}e^{-sX_n}=(L(s))^n\\
&= \left(\frac{\lambda}{\lambda+s}\right)^n
$$$
Using the uniqueness of Laplace transforms, this shows that *S{n}* has a Gamma(*n*, lambda) distribution (Erlang distribution)

## Law of Large Numbers
Consider the coin flip example. We expect that *S{n}/n* is close to the unknown *p* for large *n*.
We know this happens "empirically".

In general, we expect *S{n}/n* to be close to *u*. Does this happen in our mathematical model?
By *Chebyshev's inequality* we have for all *e > 0*,
$$$
\mathbb{P}\left(\mid\frac{S_n}{n} - \mu\mid > \epsilon\right) \leq \frac{Var(S_n/n)}{\epsilon^2} = \frac{\sigma^2}{n\epsilon^2} \rightarrow 0
$$$
as *n -> infinite*.

In other words ~()the probability that *S{n}/n* is more than *e* away from *u* can be made arbitrarily small by choosing *n* large enough.~
This is the **Weak Law of Large Numbers**.

There is also a **Strong Law of Large Numbers:**
$$$
\mathbb{P}\left(\lim_{n\rightarrow\infty} \frac{S_n}{n} = \mu\right) = 1
$$$
as *n -> infinite*

## Central Limit Theorem
The Central Limit Theorem states, roughly, this: ~()The **sum** of a large number of **iid** random variables has **approximately** a **Gaussian** distribution.~
More precisely, it states that for all *x*
$$$
\lim_{n\rightarrow\infty}\mathbb{P}\left(\frac{S_n - n\mu}{\sigma\sqrt{n}}\leq x\right) = \Phi(x)
$$$
where *Phi* is the cdf of the standard normal distribution.

### Approximating Binomial by Normal
Using the CLT we thus find the following important approximation:
Let *X ~ Bin(n, p)*. For large *n*, we have
$$$
\mathbb{P}(X\leq k)\approx\mathbb{P}(Y\leq k)
$$$
where *Y ~ N(np, np(1 - p))*.

As a rule of thumb, the approximation is accurate if both *np* and *n(1 - p)* are larger than 5.

We can improve on this somewhat by using a ~()continuity correction~, as illustrated by the following graph for the pmf of the *Bin(10, 1/2)* distribution.
![Approximating Binomial by Normal](sem2-2017/stat2203/ABN.png)[50]
For example,
$$$
\mathbb{P}(X = k)\approx\mathbb{P}(k - \frac{1}{2}\leq Y\leq k+\frac{1}{2})
$$$

### Example
**Example:** Let *X ~ Bin(200, 0.51)*, and suppose we wish to to calculate *P(X <= 99)*.
Let *Y ~ N(200 x 0.51, 200 x 0.51 x 0.49)*, and let *Z* be standard normal. Using the CLT we have
$$$
\mathbb{P}(X\leq99)&\approx\mathbb{P}(Y\leq99)\\
&=\mathbb{P}\left(\frac{Y - 102}{\sqrt{49.98}}\leq\frac{99-102}{\sqrt{49.98}}\right)\\
&=\mathbb{P}(Z\leq-0.4243) = 1 - \mathbb{P}(Z\leq0.4243)\\
&= 0.3357
$$$
Using the continuity correction we find
$$$
\mathbb{P}(X\leq99)\approx\mathbb{P}(Y\leq99+\frac{1}{2})=0.3618
$$$

### Approximating via the CLT
**Exercise:** The number of calls *X* arriving at a call centre during an hour has a *Poi(100)* distribution.
Show, using probability generating functions, that *X* has the same distribution as *X{1} + ... + X{100}*, where *X{1}, ..., X{100}* are independent *Poi(1)*-distributed random variables.
Use this fact to approximate (with the CLT) the probability that there are more than 130 arrivals during an hour

## Extremes of Independent Random Variables
In addition to the ~()average~ behaviour of iid variates *X{1}, ..., x{n}*, we are often interested in the ~()extremes~ -- that is, how the largest (or smallest) variate behaves.

If *M = max\{X{1}, ..., X{n}\}*, we have seen (by example) that
$$$
F_M(m) &= \mathbb{P}(M\leq m) = \mathbb{P}(X_1\leq m, \ldots, X_n\leq m)\\
&= \mathbb{P}(X_1\leq m)^n = (F_X(m))^n
$$$
What distribution does *M* have, as *n -> infinite*

**Remark:** It turns out that, when *M* is suitably shifted and scaled, there are essentially ~()three~ possibilities (listed here for completeness). The ~()Gumbel~ distribution (*u element R, o > 0*):
$$$
f(x) = \frac{1}{\sigma}exp\left[ -\frac{x-\mu}{\sigma} - exp\left[ -\frac{x-\mu}{\sigma}\right]\right], x\in\mathbb{R}
$$$
The ~()Frechet~ distribution (*u element R, o > 0, alpha > 0*):
$$$
f(x) = \frac{\alpha}{\sigma}\left(\frac{x-\mu}{\sigma}\right)^{-\alpha-1} exp\left[-\left(\frac{x-\mu}{\alpha}\right)^{-\alpha}\right], x > 0
$$$
The ~()reversed Weibull~ distribution (*u element R, o > 0, alpha > 0*):
$$$
f(x) = \frac{\alpha}{\sigma}\left(\frac{\mu-x}{\sigma}\right)^{\alpha-1} exp\left[-\left(\frac{\mu-x}{\sigma}\right)^\sigma\right], x < \mu
$$$

Similarly, if *M = min\{X{1}, ..., X{n}\}*, we have that
$$$
F_M(m) &= \mathbb{P}(M\leq m) = 1 - \mathbb{P}(M > m)\\
&= 1 - \mathbb{P}(X_1 > m, \ldots, X_n > m)\\
&= 1 - \mathbb{P}(X_1 > m)^n = 1 - (1 - F_X(m))^n
$$$
**Remark:** It turns out that, when *M* is suitably shifted and scaled, there are again essentially ~()three~ possibilities as *n -> infinite*, being the distribution of *Y = -X*, where *X* is one of the three listed for the largest extreme value.

## Summary
- Law of Large Numbers: statement, weak, strong
- Central Limit Theorem: statement, approximation of sums via CLT, examples
- Extreme Value Distributions: calculation (finite *n*), limiting behaviour (statement)

# Statistics, Likelihood, and Estimation
## Sums and Extremes of Independent Random Variables
- Law of Large Numbers; statement, weak, strong
- Central Limit Theorem; statement, approximation of sums via CLT, examples
- Extreme Value Distributions; calculation (finite *n*), limiting behaviour (statement)

## Statistics
Data *x* is viewed as the outcome of a random variable *X* described by a probabilistic model. Usually, model is specified up to a (multidimensional) parameter: *X ~ F(.;&theta;)* for some element in &Theta;. In ~()classical (frequentist)~ statistics, purely concerned with the model and in particular with the parameter (/).
For example, given data, we may wish to
- estimate the parameter,
- perform ~()statistical tests~ on that parameter, or
- validate the model
In ~()Bayesian statistics~, concerned with ~()distribution~ of parameter *&theta; ~ F(&theta;)*.

Any real- or vector-valued function of data *x* or *X* is called a **statistic** of the data.
For example, the sample mean is a statistic:
$$$
T = T(x) = \frac{1}{N}\sum^N_{i=1}x_i
$$$
given an outcome of *X*, or as a random variable
$$$
T = T(X) = \frac{1}{N}\sum^N_{i=1}X_i
$$$

Often, we will view data as a series of independent outcomes from the same random experiment: *X = (X{1}, ..., X{N})*, where *X{1}, ..., X{N}* are iid from *F(.;&theta;)*. *\{X{1}, ..., X{N}\}* is called a **random sample** (from *F(.;&theta;)* or from *X*).
Therefore, the joint cdf of a random sample is given by
$$$
F(x;\theta) = \prod^N_{k=1}F(x_k;\theta)
$$$
and so the joint pdf/pmf is of the same form:
$$$
f(x;\theta) = \prod^N_{k=1}f(x_k;\theta)
$$$

## Likelihood
When viewed as a function of &theta;, then point pdf/pmf of a random sample is called the **Likelihood**:
$$$
L(\theta;x) = f(x;\theta)
$$$
The (natural) logarithm of the likelihood
$$$
l(\theta;s) = ln L(\theta;x)
$$$
is called the **log-likelihood**

### Likelihood Example
**Example:** Model *X{1}, {2}, ..., X{N} ~ iid Bin(m, p)*; *m* known, *p* unknown, in &Theta; = (0, 1)
pmf:
$$$
f(x;p) = \begin{pmatrix} m \\ x \end{pmatrix} p^x (1-p)^{m-x}, x\in\{0, 1, \ldots, m\}
$$$
Therefore, the likelihood can be written as
$$$
L(p;X) &= \prod^N_{i=1} \begin{pmatrix} m\\x_i \end{pmatrix} p^{x_i} (1-p)^{m-x_i}\\
&= p^{\sum^N_{i=1}x_i} (1-p)^{Nm-\sum^N_{i=1} x_i} \prod^N_{i=1} \begin{pmatrix} m\\x_i \end{pmatrix}
$$$

## Maximum Likelihood Estimation
How do we find "good" estimators for model parameters? Given data and a parametric model, how to find a member of that family (point estimate) from which the data is "most likely" to have come?
Given data *x*, one approach is to ~()maximize~ the likelihood in &theta; -- that is, find 
$$$
\hat\theta\in\Theta
$$$
for which
$$$
L(\hat\theta;x) \geq L(\theta;x), \theta\in\Theta
$$$
A maximizer
$$$
\hat\theta\equiv\hat\theta(x)
$$$
of L is called a **maximum likelihood estimate** (MLE). The corresponding random variable &hat;&theta;(X) is called a ~()maximum likelihood estimator~ (also MLE).
**Remark:** A maximiser of *l* equivalent to a maximiser of *L*

### ML Estimation Example: Binomial Probability
**Example:** Continuing our example, recall that we found
$$$
L(p;X) &= \prod^N_{i=1} \begin{pmatrix} m\\x_i \end{pmatrix} p^{x_i} (1-p)^{m-x_i}\\
&= p^{\sum^N_{i=1}x_i} (1-p)^{Nm-\sum^N_{i=1} x_i} \prod^N_{i=1} \begin{pmatrix} m\\x_i \end{pmatrix}
$$$
How do we find an MLE?
Maximisation Strategy: Since *L* is a continuous function of *p*, find *p* such that
$$$
\frac{d}{dp} L(p;x) = 0
$$$
Working directly with *L* appears cumbersome; obtain the log-likelihood and work with that instead.
Taking the natural logarithm of *L*, we obtain the log-likelihood:
$$$
l(p;X) = ln (p) \sum^N_{i=1}x_i + ln(1-p)\left(Nm - \sum^N_{i=1}x_i\right) + \sum^N_{i=1}ln\left(\begin{pmatrix}m\\x_i\end{pmatrix}\right)
$$$
First Derivative with respect to *p*:
$$$
\frac{d}{dp} l(p;X) = \frac{1}{p}\sum^N_{i=1}x_i - \frac{1}{1-p}\left(Nm - \sum^N_{i=1}x_i\right)
$$$
Set to zero and rearrange to find critical point:
$$$
(1-p)\sum^N_{i=1}x_i=p\left(Nm-\sum^N_{i=1}x_i\right)
$$$
Unique solution:
$$$
\hat{p} = \frac{1}{Nm}\sum^N_{i=1}x_i
$$$
What type of critical point is this?
Second Derivative with respect to *p*:
$$$
h(p) = \frac{d^2}{dp^2} l(p;X) = -\frac{1}{p^2}\sum^N_{i=1}x_i - \frac{1}{(1-p)^2}\left(Nm - \sum^N_{i=1}x_i\right) < 0
$$$
Therefore &hat;p is a local maximiser.
Moreover, *l(p;X) -> &infty;* as *p -> 0*  or *p -> 1* (boundary of &Theta;). Thus &hat;p is in fact a global maximiser. Therefore, we have the Maximum Likelihood Estimator:
$$$
\hat{p} = \frac{1}{Nm}\sum^N_{i=1}X_i
$$$

## Summary
- Statistics; definition, example
- Likelihood and log-likelihood; definition, binomial example
- Maximum Likelihood Estimation; definition, examples, bias, consistency
