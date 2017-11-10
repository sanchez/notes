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
Moreover, *l(p;X) -> &infin;* as *p -> 0*  or *p -> 1* (boundary of &Theta;). Thus &hat;p is in fact a global maximiser. Therefore, we have the Maximum Likelihood Estimator:
$$$
\hat{p} = \frac{1}{Nm}\sum^N_{i=1}X_i
$$$

## Summary
- Statistics; definition, example
- Likelihood and log-likelihood; definition, binomial example
- Maximum Likelihood Estimation; definition, examples, bias, consistency

# Confidence Intervals and Hypothesis Testing
## Statistics, Likelihood, and Estimation
- Statistics; definition, example
- Likelihood and log-likelihood; definition, binomial example
- Maximum Likelihood Estimation; definition, examples, bias, consistency

## Confidence Intervals
Last time, we were introduced to ~()maximum likelihood estimation~, which provided a systematic way of obtaining ~()estimates~ and ~()estimators~ &hat;&theta; of unknown parameters contained in &theta; &isin; &Theta;
How can we gauge the ~()accuracy~ of &hat;&theta;?
~()Confidence intervals~ (sometimes called ~()interval estimates~) provide a precise way of describing the uncertainty of &hat;&theta;

Formally, given random variables *X{1}, ..., X{n}* whose joint distribution depends on some unknown &theta; &isin; &Theta;, a **(1 - &alpha;) stochastic confidence interval** is a ~()pair of statistics~
$$$
T_1(X_1, \ldots, X_n) \text{and} T_2(X_1, \ldots, X_n)
$$$
with the property that
$$$
\mathbb{P}(T_1 < \theta < T_2) \geq 1 - \alpha, \text{ for all } \theta\in\Theta
$$$
for some &alpha; &isin; [0, 1]
That is, (T{1}, T{2}) is a ~()random~ interval, based only on the (as yet to be observed) outcomes *X{1}, ..., X{n}*, that contains the unknown &theta; with probability at least *1 - &alpha;*.

A realisation of the random interval, say *(t{1}, t{2})*, is called a **(1 - &alpha;) numeric confidence interval** for &theta;.

**Remark:** Whilst ~()stochastic~ confidence intervals contain the unknown &theta; with probability at least *1 - &alpha;*, their numerical counterparts either contain &theta; or they do not. It may be helpful to think of a Bernoulli analogy, where "success" occurs with probability (at least) *1 - &alpha;* -- then outcomes are either "successes" or "failures"

### Confidence Interval Example
**Example:** Model: *X{1}, X{2}, ..., X{n} ~iid N(&mu;, &sigma;{{2}})*; &sigma;^2 known, &mu; unknown, in &Theta; = R.
We have seen that
$$$
\bar{X} = \frac{1}{N}\sum^N_{i=1}X_i\qquad \sim N(\mu, \frac{\sigma^2}{N})
$$$
Therefore,
$$$
\frac{\bar{X}-\mu}{\frac{\sigma}{\sqrt{N}}} \sim N(0, 1)
$$$
Hence,
$$$
\mathbb{P}\left(z_{\alpha/2}\leq\frac{\bar{X}-\mu}{\frac{\sigma}{\sqrt{N}}} \leq z_{1-\alpha/2}\right) = 1-\alpha
$$$
where *z{&gamma;}* is the &gamma;-quantile of the standard normal distribution.

Rearranging, we have
$$$
\mathbb{P}\left(\bar{X} - z_{1-\alpha/2}\frac{\sigma}{\sqrt{N}}\leq\mu\leq\bar{X} - z_{\alpha/2}\frac{\sigma}{\sqrt{N}}\right) = 1 - \alpha
$$$
Note that, by symmetry, the quantiles satisfy *-z{&alpha;/2} = z{1-&alpha;/2}*. Hence a stochastic *1 - &alpha;* confidence interval for &mu; in this case is
$$$
\left(\bar{X} - z_{1-\alpha/2}\frac{\sigma}{\sqrt{N}}, \bar{X} + z_{1-\alpha/2}\frac{\sigma}{\sqrt{N}}\right)
$$$
which is often abbreviated to
$$$
\bar{X} \pm z_{1-\alpha/2}\frac{\sigma}{\sqrt{N}}
$$$

### Approximate Confidence Intervals
When
$$$
\mathbb{P}(T_1 < \theta < T_2) \geq 1 - \alpha,\ \text{or all}\ \theta\in\Theta
$$$
only holds ~()approximately~, we call (T{1}, T{2}) an **approximate (1 - &alpha;) confidence interval** for &theta;.

**Remark:** We can often employ the central limit theorem to construct such approximate confidence intervals, as we shall see next.

### Approximate Confidence Interval Example
**Example:** Model *X{1}, X{2}, ..., X{N} ~iid Bin(m, p)*; *m* known, *p* unknown, in &Theta; = (0, 1), with MLE for *p*:
$$$
\hat{p} = \frac{1}{Nm}\sum^N_{i=1}X_i
$$$
Notice that *Y = &sum;{{N}}{i=1} X{i}* can be thought of as *Y ~ Bin(Nm, p)*, and so by the central limit theorem,
$$$
Y ~_{approx} \textbf{N}(Nmp, Nmp(1-p))
$$$
or equivalently
$$$
\hat{p} ~_{approx} \textbf{N}\left(p, \frac{p(1-p)}{Nm}\right)
$$$
Therefore, we have
$$$
\mathbb{P}\left(z_{\alpha/2}\leq\frac{\hat{p}-p}{\frac{\sqrt{p(1-p)}}{\sqrt{Nm}}}\leq z_{1-\alpha/2}\right)\approx 1-\alpha
$$$
By the law of large numbers, &hat;p&approx;p, so we may replace *p* in the denominator to obtain
$$$
\mathbb{P}\left(z_{\alpha/2}\leq\frac{\hat{p} - p}{\sqrt{\hat{p}(1-\hat{p})}/\sqrt{Nm}}\leq z_{1-\alpha/2}\right)\approx 1-\alpha
$$$
Rearranging, and using the symmetry of standard normal quantiles, we have
$$$
\mathbb{P}\left( \hat{p} - z_{1-\alpha/2}\frac{\sqrt{\hat{p}(1-\hat{p})}}{\sqrt{Nm}} \leq p \leq \hat{p} + z_{1 - \alpha/2}\frac{\sqrt{\hat{p}(1-\hat{p})}}{\sqrt{Nm}} \right) \approx 1 - \alpha
$$$
which is an approximate *1 - &alpha;* confidence interval for *p*:
$$$
\hat{p}\pm z_{1-\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{Nm}}
$$$

## Hypothesis Testing
\ _f
Closely related to the notion of confidence intervals is that of ~()hypothesis tests~. In ~()hypothesis testing~, given data, we wish to determine which of two competing hypotheses *H{0} : &theta; &isin; &Theta;{0}* and *H{1} : &theta; &isin; &Theta;{1}* holds true. *H{0}* is called the **null hypothesis** and contains the "status quo" statement, whereas *H{1}* is called the **alternative hypothesis** which is unlikely to have occurred if *H{0}* were true.
**Remark:** Usually, *&Theta;{0} &cap; &Theta{1} = (/)*

Outcomes of hypothesis tests are ~()decisions~ as to whether to accept the "status quo" *H{0}*, or reject the "status quo" in favour of the alternative *H{1}*. As such, we seek a ~()decision rule~ based on the outcome of a statistic *T*.
- ~()Decision Rule 1:~ Reject *H{0}* if *T* falls in some ~()critical region~ *C*
- ~()Decision Rule 2:~ Reject *H{0}* if *P(T &isin; C)* is less than some ~()critical p-value~ *p{c}*.
**Remark:** Common critical regions are one-sided (C = (-&infin;, c], C = [c, &infin;)), or two-sided (C = (-&infin;, c{1}] &cup; [c{2}, &infin;), c{1} <= c{2})

Regardless of which type of decision rule is employed, we can make two types of error.

| Decision | H{0} True | H{1} True
| --- | --- | --- | --- |
| Retain H{0} | Correct | Type II Error
| Reject H{0} | Type I Error | Correct

**Remark:** We can think of Type I error as a "false positive" and Type II error as a "false negative".
In classical statistics, Type I error is considered more serious, and so decision rules are designed to control this type of error.

We will denote the probability of a Type I error by &alpha;, and the probability of a Type II error by &beta;.
**Remark:** The **power** of a statistical test is the probability of correctly rejecting the null, 1 - &beta;
We will design our decision rules around a predetermined **significance level** &alpha;, which describes the acceptable level of Type I error for our test. In this framework, the two types of decision rule are ~()equivalent~:
- Decision Rule 2: Reject *H{0}* if *P(T &isin; C{&alpha;}) <= &alpha;*
- Decision Rule 1: Reject *H{0}* if *T* falls in *C{&alpha;}*

### Hypothesis Testing Example
**Example:** Model *X{1}, X{2}, ..., X{N} ~iid N(&mu;, &sigma;{{2}})*; &sigma;{{2}} known, &mu; unknown, in &Theta; = R. We can readily adapt our previous work to form a hypothesis test together with a decision rule about the unknown &mu;.
Let *H{0}: &mu; = &mu;{0}* and *H{1}: &mu; /= &mu{0};*
Under the null hypothesis *H{0}*,
$$$
T = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{N}} ~ N(0, 1)
$$$
and so
$$$
C_\infty = (-\infty, z_{\alpha/2}]\cup[z_{1-\alpha/2}, \infty)
$$$
is a critical region satisfying
$$$
\mathbb{P}_{H_0}(T\in C_\alpha) \leq \alpha
$$$
\ _f
Therefore, we reject *H{0}* if our observed statistic *t* falls in *C{&alpha;}*

## Summary
- Confidence intervals; definition, stochastic, numerical, approximate, examples
- Hypothesis testing; decision rules, null and alternative hypotheses, Type I and II error, significance level, power, critical region, critical *p*-value, one- and two-sided regions (hence tests).

# Confidence Intervals and Hypothesis Testing II
## Sample Variance
For a single normal random sample with known variance &sigma;{{2}}, we have seen that the ~()sample mean~ (X bar) is normally distributed, and can therefore construct confidence intervals and hypothesis tests for the unknown mean &mu;

How can we proceed when &sigma;{{2}} is unknown?
First, we will determine an appropriate ~()estimator~ for &sigma;{{2}}, and state its distribution for a normal random sample.

Recall that we defined the ~()sample variance~ of data as
$$$
\hat{\sigma^2} = \frac{1}{N} \sum^N_{i=1} (x_i - \bar{x})^2 = \frac{1}{N} \sum^N_{i=1} x_i^2 - \bar{x}^2
$$$
For a ~()random sample~, is the associated random variable an ~()unbiased~ estimator for &sigma;{{2}}?
We have
$$$
\mathbb{E}\hat{\sigma^2} &= \frac{1}{N}\sum^N_{i=1} \mathbb{E}[X_i^2] - \mathbb{E}[\bar{X}^2]\\
&= \mathbb{E}[X_1^2] - \mathbb{E}\left[\left( \frac{1}{N}\sum^N_{i=1}X_i \right)^2\right]\\
&= \mathbb{E}[X_1^2] - \mathbb{E}\left[ \frac{1}{N^2}\sum^N_{i=1}\sum^N_{j=1} X_i X_j \right]\\
&= \mathbb{E}[X_1^2] - \frac{1}{N^2} \mathbb{E}\left[ \sum^N_{i=1}X_i^2+\sum^N_{i=1}\sum^N_{j=1,j\ne i} X_iX_j \right]\\
&= \mathbb{E}[X_1^2] - \frac{1}{N} \mathbb{E}[X_1^2] - \frac{N(N-1)}{N^2} \mathbb{E}[X_1]^2\\
&= \frac{N-1}{N}(\mathbb{E}[X_1^2] - \mathbb{E}[X_1]^2) = \frac{N-1}{N}\sigma^2
$$$
Therefore, &hat;&sigma;{{2}} is a biased (but ~()consistent~) estimator for &sigma;{{2}}.
**Remark:** &hat;&sigma;{{2}} is the MLE of &sigma;{{2}} for a normal random sample.

We can easily correct for the bias in the **(bias corrected) sample variance:**
$$$
S^2 &= \frac{N}{N-1}\hat{\sigma^2}\\
&= \frac{1}{N-1}\sum^N_{i=1}(X_i - \bar{X})^2\\
&= \frac{1}{N-1}\sum^N_{i=1}X_i^2 - \frac{N}{N-1}\bar{X}^2
$$$
For a normal random sample, it turns out that
$$$
(N-1)\frac{S^2}{\sigma^2} \sim X^2_{N-1} \equiv \text{Gamma}(\frac{N-1}{2}, \frac{1}{2})
$$$
\ _f
**Remark:** The fact that the ~()degrees of freedom~ is *N - 1* comes from the fact that there are only *N - 1* linearly independent elements of
$$$
\begin{pmatrix}
X_1 - \bar{X}\\
\cdot\\\cdot\\\cdot\\
X_N - \bar{X}
\end{pmatrix}
$$$

### Sample Variance Example
**Example:** For a normal random sample *X{1}, ..., X{N} ~iid N(&mu;, &sigma;{{2}})* with unknown mean &mu; and variance &sigma;{{2}}, find a *1 - &alpha;* (stochastic) confidence interval for &sigma;{{2}}.
Since *(N - 1)S{{2}}/&sigma;{{2}} ~ X{N-1}{{2}}*, we have by definition
$$$
\mathbb{P}\left( X^2_{N-1;\alpha/2} \leq (N-1)\frac{S^2}{\sigma^2} \leq X^2_{N-1;1-\alpha/2} \right) = 1-\alpha
$$$
where *X{N-1;&gamma;}{{2}}* denotes the &gamma;-quantile of this chi-squared distribution
Since *&sigma;{{2}} > 0* and *S{{2}} > 0*, we rearrange as follows:
$$$
\mathbb{P}\left( \frac{1}{X^2_{N-1;\alpha/2}} \geq \frac{\sigma^2}{(N-1)S^2} \geq \frac{1}{X^2_{N-1;1-\alpha/2}} \right) = 1-\alpha
$$$
giving
$$$
\mathbb{P}\left( \frac{(N-1)S^2}{X^2_{N-1;1-\alpha/2}} \leq \sigma^2 \leq \frac{(N-1)S^2}{X^2_{N-1;\alpha/2}} \right) = 1-\alpha
$$$
Hence, a stochastic *1 - &alpha;* confidence interval for &sigma;{{2}} for a normal random sample is
$$$
\left(\frac{(N-1)S^2}{X^2_{N-1;1-\alpha/2}}, \frac{(N-1)S^2}{X^2_{N-1;\alpha/2}}\right)
$$$
We can easily construct hypothesis tests at ~()significance level &alpha;~.

If *H{0} : &sigma;{{2}} = &sigma;{0}{{2}}* and *H{1} : &sigma;{{2}} /= &sigma;{0}{{2}}*, then our ~()test statistic~ is
$$$
T = (N-1)\frac{S^2}{\sigma_0^2}
$$$
which (under *H{0}*) has a *X{{2}}{N-1}* distribution

Therefore, we reject *H{0}* in favour of *H{1}* if *T* falls in the (two-sided) critical region
$$$
(-\infty, X^2_{N-1;\alpha/2}]\cup[X^2_{N-1;1-\alpha/2}, \infty)
$$$
Similarly, if *H{0} : &sigma;{{2}} = &sigma;{0}{{2}}* and *H{1} : &sigma;{{2}} > &sigma;{0}{{2}}*, we reject *H{0}* in favour of *H{1}* if *T* falls in the (right one-sided) critical region
$$$
[X^2_{N-1;1-\alpha}, \infty)
$$$
\ _f
and if *H{0} : &sigma;{{2}} = &sigma;{0}{{2}}* and *H{1} : &sigma;{{2}} < &sigma;{0}{{2}}*, we reject *H{0}* in favour of *H{1}* if *T* falls in the (left one-sided) critical region
$$$
(-\infty, X^2_{N-1;\alpha}]
$$$
\ _f

## Sample Mean with Unknown Variance
We have seen how to construct confidence intervals and hypothesis tests for a normal random sample with ~()known~ variance &sigma;{{2}}. How does this change when &sigma;{{2}} is ~()unknown~, and must instead be replaced by an estimate?
Recall that *X{1}, X{2}, ..., X{N} ~iid N(&mu;, &sigma;{{2}})*, and consider the hypothesis test *H{0} : &mu; = &mu;{0}* and *H{1} : &mu; /= &mu;{0}*. Our ~()test statistic~ in this case simply replaces the ~()known~ &sigma; with its unbiased estimator *S = &sqrt;S{{2}}*, giving
$$$
T = \frac{\bar{X} - \mu_0}{S/\sqrt{N}}
$$$
If *H{0}* is true, then it turns out that *T* has a **(Student's) t** distribution, with *N - 1* ~()degrees of freedom~, which we will write as *t{N-1}*. We will not concern ourselves with the particulars of this distribution, other than to note a few salient points:
- A *t*-distribution random variable is continuous, symmetric around zero, and has non-zero pdf over R (just like the standard normal distribution)
- As with any other distribution, we may compute &gamma;-quantiles for a *t{N}*-distributed random variable, which we will denote by *t{N;&gamma;}*.
    - Like the standard normal distribution, we will rely on tables or numerical computation for quantiles and probabilities.
- As *N -> &infin;*, *t{N}* converges in distribution to N(0, 1). (Moreover, *t{1}* is the ~()Cauchy~ distribution)

Accepting that *T ~ t{N-1}*, we construct a two-sided critical region at significance level &alpha;:
$$$
(-\infty,t_{N-1;\alpha/2}]\cup[t_{N-1;1-\alpha/2},\infty)
$$$
and we reject *H{0}* if the outcome of our test statistic falls in this region. Similarly, critical regions for one-sided tests are easily constructed:
- *H{0} : &mu; = &mu;{0}* vs *H{1} : &mu; > &mu;{0}*. Critical region: *[t{N-1;1-&alpha;}, &infin;)*
- *H{0} : &mu; = &mu;{0}* vs *H{1} : &mu; < &mu;{0}*. Critical region: *(-&infin;, t{N-1;&alpha;}]*
Moreover, confidence intervals for the mean are straight-forwardly constructed from *T*:
$$$
\left(\bar{X} - t_{N-1;1-\alpha/2}\frac{S}{\sqrt{N}}, \bar{X} - t_{N-1;\alpha/2}\frac{S}{\sqrt{N}}\right)
$$$
or more compactly, by the symmetry of this distribution around zero:
$$$
\bar{X}\pm t_{N-1;1-\alpha/2}\frac{S}{\sqrt{N}}
$$$
\ _f

## Summary
- Sample variance; bias and correction, confidence intervals and hypothesis tests for normal population.
- Sample mean with unknown variance; Student's *t* distribution (briefly), confidence intervals and hypothesis tests for normal population

# Confidence Intervals and Hypothesis Testing III
- Sample variance; bias and correction, confidence intervals and hypothesis tests for normal population
- Sample mean with uknown variance; Student's *t* distribution (briefly), confidence intervals and hypothesis tests for normal population

## Two Sample Inference
Previously, we have seen how to construct confidence intervals and hypothesis tests for unknown parameters for a ~()single~ random sample. However, in many cases we are interested in inference regarding the unknown parameters of ~()two~ random samples. How does the construction of confidence intervals and hypothesis tests extend to this situation?

### Two Sample Inference Example
**Example:** Model *X{1}, ..., X{M} ~iid N(&mu;{X}, &sigma;{{2}}{X})* independent of *Y{1}, ..., Y{N} ~iid N(&mu;{Y}, &sigma;{{2}}{Y})*, with ~()known~ variances &sigma;{{2}}{X} and &sigma;{{2}}{Y}, but unknown means &mu;{X} and &mu;{Y}.
Construct a *1 - &alpha;* stochastic confidence interval for the ~()difference~ in means, *&mu;{X} - &mu;{Y}*
Firstly, notice that *&bar;X ~ N(&mu;{X}, &sigma;{{2}}{X}/M)* independent of *&bar;Y ~ N(&mu;{Y}, &sigma;{{2}}{Y}/N)*.
Therefore, *&bar;X - &bar;Y ~ N(&mu;{X} - &mu;{Y}, &sigma;{X}{{2}}/M + &sigma;{Y}{{2}}/N)*, and so
$$$
Z = \frac{(\bar{X} - \bar{Y}) - (\mu_X - \mu_Y)}{\sqrt{\frac{\sigma^2_X}{M}+\frac{\sigma^2_Y}{N}}} \sim N(0, 1)
$$$
Hence, by definition,
$$$
\mathbb{P}(z_{\alpha/2} \leq Z \leq z_{1-\alpha/2}) = 1-\alpha
$$$
Rearranging as usual, we obtain an output which can be put more compactly (and using the symmetry of normal quantiles)
$$$
(\bar{X} - \bar{Y}) \pm z_{1-\alpha/2}\sqrt{\sigma_X^2/M+\sigma^2_Y/N}
$$$
as a *1 - &alpha;* stochastic confidence interval for the difference in means.

**Remark:** If each random sample has a common known variance *&sigma;{X}{{2}} = &sigma;{Y}{{2}} = &sigma;{{2}}*, then this confidence interval reduces to
$$$
(\bar{X} - \bar{Y}) \pm z_{1-\alpha/2}\sigma\sqrt{\frac{1}{M}+\frac{1}{N}}
$$$
\ _f

This work can be extended to create hypothesis tests in the usual way, as follows. For the two-sided test, with a pair of normal random samples with known variances *&sigma;{X}{{2}}* and *&sigma;{Y}{{2}}*, we have *H{0} : (&mu;{X} - &mu;{Y}) = &delta;{0}* and *H{1} : (&mu;{X} - &mu;{Y}) /= &delta;{0}*.
Under *H{0}*
$$$
T = \frac{(\bar{X} - \bar{Y}) - \delta_0}{\sqrt{\frac{\sigma^2_X}{M}+\frac{\sigma^2_Y}{N}}} \sim N(0, 1)
$$$
and so the critical region for a test with significance level &alpha; is
$$$
C_\alpha = (-\infty, z_{\alpha/2}] \cup [z_{1-\alpha/2}, \infty)
$$$
\ _f
One-sided tests, and tests with common variance &sigma;{{2}} can be constructed in the same way.

## Two Sample Inference with Unknown Variance
How does this change when the variances of the samples are ~()unknown~?
There are two possibilities:
- The unknown variances are ~()not assumed~ to be the same
- The unknown variances are ~()assumed~ to be the same
In the first case, we may ~()estimate~ &sigma;{X}{{2}} by S{X}{{2}}, and &sigma;{Y}{{2}} by S{Y}{{2}}.
Then we may construct the ~()same~ intervals and tests as before, replacing each variance by its estimator. This will yield ~()approximate~ confidence intervals, and ~()approximate~ hypothesis tests, which become more exact as both of the sample sizes become large.
In the second case, we need to estimate the common variance. The ~()(uncorrected) pooled sample variance~ would just be
$$$
\hat{\sigma^2_p} = \frac{1}{M+N}\left( \sum^M_{i=1}(X_i - \bar{X})^2+\sum^N_{j=1}(Y_j-\bar{Y})^2 \right)
$$$
However, as we have seen before, this is a ~()biased~ estimator. Here, we can easily compute
$$$
\mathbb{E}[\hat{\sigma^2_p}] = \frac{M-1+N-1}{M+N}\sigma^2
$$$
so the ~()(bias corrected) pooled sample variance~ is just
$$$
S^2_p = \frac{1}{M+N-2} \left(  \sum^M_{i=1}(X_i - \bar{X})^2+\sum^N_{j=1}(Y_j - \bar{Y})^2  \right)
$$$
Therefore, we can use our previous work, and note that
$$$
T = \frac{(\bar{X} - \bar{Y}) - (\mu_X - \mu_Y)}{S_p \sqrt{\frac{1}{M}+\frac{1}{N}}} \sim t_{M+N-2}
$$$
\ _f
Hence, a *1 - &alpha;* stochastic confidence interval for *(&mu;{X} - &mu;{Y})* with ~()unknown common variance~ is
$$$
(\bar{X} - \bar{Y}) \pm t_{M+N-2;1-\alpha/2} S_p \sqrt{\frac{1}{M}+\frac{1}{N}}
$$$
For the two-sided test, with a pair of normal random samples with unknown common variance &sigma;{{2}}, we have *H{0} : (&mu;{X} - &mu;{Y}) = &delta;{0}* and *H{1} : (&mu;{X} - &mu;{Y}) /= &delta;{0}*. Under *H{0}*,
$$$
T = \frac{(\bar{X} - \bar{Y}) - \delta_0}{S_p\sqrt{\frac{1}{M}+\frac{1}{N}}} \sim t_{M+N-2}
$$$
\ _f
and so the critical region for a test with significance level &alpha; is
$$$
C_\alpha = (-\infty, t_{M+N-2;\alpha/2}] \cup [t_{M+N-2;1-\alpha/2}, \infty)
$$$
\ _t
One-sided tests are simply constructed as seen previously

### Approximate Intervals and Tests
We can readily adapt the confidence intervals and tests described so far to give ~()approximate~ results by appealing to the central limit theorem.

**Exercise:** If *X ~ Bin(M, p{X})* independently of *Y ~ Bin(N, P{Y})*, show that an approximate *1 - &alpha;* stochastic confidence interval for *p{X} - p{Y}* is
$$$
(\hat{p_X} - \hat{p_Y}) \pm z_{1-\alpha/2}\sqrt{  \frac{\hat{p_X}(1-\hat{p_X})}{M}+\frac{\hat{p_Y}(1-\hat{p_Y})}{N}  }
$$$
where
$$$
\hat{p_X} = \frac{X}{M},\qquad\hat{p_Y}=\frac{Y}{N}
$$$

## Two Sample Inference for Variances
How can we construct confidence intervals and hypothesis tests for the unknown variances of two random samples?
Last time, we stated that for a normal random sample, *X{1}, ..., X{M} ~iid N(&mu;{X}, &sigma;{X}{{2}})*,
$$$
(M-1)\frac{S_X^2}{\sigma^2_X}\sim X^2_{M-1}\equiv\text{Gamma}(\frac{M-1}{2},\frac{1}{2})
$$$
\ _f
This time, we will state that if we have two independent normal random samples *X{1}, ..., X{M} ~iid N(&mu;{X}, &sigma;{X}{{2}})* and *Y{1}, ..., Y{N} ~iid N(&mu;{Y}, &sigma;{Y}{{2}})*,
$$$
\frac{S^2_X/\sigma^2_X}{S^2_Y/\sigma^2_Y} \sim F_{M-1,N-1}
$$$
\ _f
where *F{m,n}* is the *F*-distribution with *m* and *n* ~()degrees of freedom~

**Remark:** As with the *t*-distribution, we will not go into details regarding the *F*-distribution, but simply accept this and rely on numerical computation or tabulation of its quantiles.
Using this fact, we may write by definition
$$$
\mathbb{P}\left(  F_{N-1,M-1;\alpha/2} \leq \frac{S^2_Y/\sigma^2_Y}{S^2_X/\sigma^2_X} \leq F_{N-1,M-1;1-\alpha/2}  \right) = 1-\alpha
$$$
\ _f
Rearranging, we have a stochastic *1 - &alpha;* confidence interval for the ratio of the unknown population variances:
$$$
\mathbb{P}\left( F_{N-1,M-1;\alpha/2}\frac{S^2_X}{S^2_Y} \leq \frac{\sigma^2_X}{\sigma^2_Y} \leq F_{N-1,M-1;1-\alpha/2}\frac{S^2_X}{S^2_Y} \right) = 1-\alpha
$$$
We may use this to construct hypothesis tests: *H{0} : &sigma;{X}{{2}} = &sigma;{Y}{{2}}* vs *H{1} : &sigma;{X}{{2}} /= &sigma;{Y}{{2}}*.
Under *H{0}*,
$$$
\frac{S^2_X}{S^2_Y} \sim F_{M-1,N-1}
$$$
\ _f
and so an appropriate critical region at the &alpha; significance level is
$$$
C_\alpha = (-\infty, F_{M-1,N-1;\alpha/2}]\cup [F_{M-1,N-2;1-\alpha/2}, \infty)
$$$
\ _f
One-sided tests can be constructed as seen before.

## Summary
- Two-sample difference of means; confidence intervals and hypothesis tests for normal population, known and unknown (common and not) variance.
- Two-sample ratio of variances; *F* distribution (briefly), confidence intervals and hypothesis tests for normal population.

# Confidence Intervals and Hypothesis Testing IV
- Two-sample difference of means; confidence intervals and hypothesis tests for normal population, known and unknown (common and not) variance

## Two Sample Inference for Variances
How can we construct confidence intervals and hypothesis tests for the unknown variances of two random samples?
Last time, we stated that for a normal random sample, *X{1}, ..., X{M} ~iid N(&mu;{X}, &sigma;{X}{{2}})*,
$$$
(M-1)\frac{S^2_X}{\sigma^2_X} \sim X^2_{M-1} \equiv \text{Gamma}(\frac{M-1}{2}, \frac{1}{2})
$$$
\ _f
This time, we will state that if we have two independent normal random samples *X{1}, ..., X{M} ~iid N(&mu;{X}, &sigma;{X}{{2}})* and *Y{1}, ..., Y{N} ~iid N(&mu;{Y}, &sigma;{Y}{{2}})*,
$$$
\frac{S^2_X/\sigma^2_X}{S^2_Y/\sigma^2_Y} \sim F_{M-1,N-1}
$$$
\ _f
where *F{m,n}* is the *F*-distribution with *m* and *n* ~()degrees of freedom~

**Remark:** As with the *t*-distribution, we will not go into details regarding the *F*-distribution, but simply accept this and rely on numerical computation or tabulation of its quantiles.
Using this fact, we may write by definition
$$$
\mathbb{P}\left( F_{N-1,M-1;\alpha/2} \leq \frac{S^2_Y/\sigma^2_Y}{S^2_X/\sigma^2_X} \leq F_{N-1,M-1;1-\alpha/2} \right) = 1-\alpha
$$$
\ _f
Rearranging, we have a stochastic *1 - &alpha;* confidence interval for the ratio of the unknown population variances:
$$$
\mathbb{P}\left( F_{N-1,M-1;\alpha/2}\frac{S^2_X}{S^2_Y} \leq \frac{\sigma^2_X}{\sigma^2_Y} \leq F_{N-1,M-1;1-\alpha/2}\frac{S^2_X}{S^2_Y} \right) = 1 - \alpha
$$$
We may use this to construct hypothesis tests: *H{0} : &sigma;{X}{{2}} = &sigma{Y}{{2}}* vs *H{1} : &sigma;{X}{{2}} /= &sigma;{Y}{{2}}*
Under *H{0}*
$$$
\frac{S^2_X}{S^2_Y} \sim F_{M-1,N-1}
$$$
\ _f
and so an appropriate critical region at the &alpha; significance level is
$$$
C_\alpha = (\infty, F_{M-1,N-1;\alpha/2}] \cup [F_{M-1,N-1;1-\alpha/2}, \infty)
$$$
\ _f
One-sided tests can be constructed as seen before

## Goodness of Fit
~()Goodness of Fit~ refers to assessing the quality of a model in light of data. We have seen ~()graphical~ goodness of fit procedures -- namely quantile-quantile plots. We can also approach goodness of fit from a ~()statistical~ viewpoint, by devising ~()statistical tests~ based on the data directly (through the empirical cdf), or through first ~()binning~ the data, and comparing ~()expected~ bin values (based on our probabilistic model) to ~()observed~ bin values from data.

### Kolmogorov-Smirnov Test
Suppose that *X{1}, ..., X{N}* is an random sample (that is, an iid sample) from some distribution with cdf *F*. If indeed *X{1}, ..., X{N} ~iid F*, then, when ordered *X{(1)} < ... < X{(N)}*,
$$$
\mathbb{P}(\frac{k-1}{N} < F(X_{(k)}) \leq \frac{k}{N}) = \frac{1}{N},\qquad k=1,\ldots,N
$$$
\ _f
In other words, if *X{1}, ..., X{N}* were a random sample from *F*, then *F(X{1}), ..., F(X{N})* would be random sample from *U[0, 1]*
This observation is basis of the ~()Kolmogorov-Smirnov test~, which utilizes the distribution of maximum deviation of a uniform random sample from the straight line (0, 0) - (1, 1)
The ~()(scaled) Kolmogorov-Smirnov~ statistic is
![Kolmogorov-Smirnov Statistic](sem2-2017/stat2203/kolmogorov.png)[75]
which, under the null hypothesis that the data is a random sample from *F* has a ~()Kolmogorov-Smirnov~ distribution. Once more, we will not go into the details of this distribution, other than to note that its quantiles may be tabulated or computed numerically. In particular, for a particular outcome *k{N}* of *K{N}*, we can computer the *p*-value under the null hypothesis *p = P(K{N} > k{N})*, and reject the null if *p <= &alpha;*, for some pre-specified significance level &alpha;.

**Remark:** The ~()Kolmogorov-Smirnov~ test is ~()non-parametric~, in the sense that it does not test parameters of a particular distribution, but rather is applicable to any distribution form. Moreover, it can be used when the hypothesised *F* itself is an empirical cdf, and we wish to test whether certain observed data could have come from the same distribution as other known data.

### X2 Goodness of Fit Tests
Suppose that we have an underlying model that *X{1}, ..., X{N}* is a random sample from a distribution with cdf *F*. Then, we may consider ~()binning~ the random sample into *M* mutually exclusive and exhaustive intervals, say *I{1} = (-&infin;, a{1}], I{2} = (a{1}, a{2}], ..., I{M-1} = (a{M-2}, a{M-1}], I{M} = (a{M-1}, &infin;)*. If our model were true, then the ~()counts~ of the number in each bin would follow a ~()multinomial~ distribution: *(Y{1}, ..., Y{M}) ~ Mnom(N, &pi;)*, where
$$$
\pi_k = \mathbb{P}(X_1\in I_k)
$$$

The ~()X{{2}} test statistic~ measures the discrepancy between ~()observed~ counts in each bin, and the ~()expected~ counts, if our model were true:
$$$
T = \sum^K_{i=1}\frac{(X_i-N\pi_i)^2}{N\pi_i}
$$$
It turns out that, if our model were true,
$$$
T\sim X^2_{K-1}
$$$
and so we can use this to test whether it is reasonable that observed data comes from our hypothesised distribution *F*.
**Remark:** A rule of thumb for the validity of this approximation is *N&pi; >= 5*, for *i = 1, ..., K*.
In particular, if our observed test statistic *t* falls in the critical region
$$$
[X^2_{K-1;\alpha}, \infty)
$$$
then we would ~()reject~ the hypothesis that our data is a random sample from *F*, at the &alpha; significance level.
**Remark:** Once again, notice that this form of testing is ~()non-parametric~, as it does not test the parameters of a particular distribution, or rely on a particular parametric distribution form for *F*.

### X2 GoF Example
**Example:** Suppose we ~()expect~ the number of hits to our website to be equally divided between Spring, Summer, Autumn, and Winter. Therefore, with *N* hits, and letting (Y{1}, Y{2}, Y{3}, Y{4}) be the number of hits per quarter, our model is* **Y** ~ Mnom(N, (1/4, 1/4, 1/4, 1/4))*. If we had 100,000 hits last year, our ~()expected~ number of hits per quarter under our model is 25,000. Suppose we ~()observe~ 25,790, 25,618, 25,671, and 22,921 hits, and we wish to test our model at the &alpha; = 0.01 level. Then our test statistic is:
$$$
t = \frac{(25790 - 25000)^2}{25000}+\frac{(25618-25000)^2}{25000}+\frac{(25671-25000)^2}{25000}+\frac{(22921-25000)^2}{25000}\approx 231.1402
$$$
Under the null hypothesis, *T ~{appprox} X{3}{{2}}*, and so the *p*-value for this outcome is
$$$
\mathbb{P}(T > t) \approx 0
$$$
This is less than 0.01, so we reject *H{0}* and conclude that the data is ~()not~ consistent with the model at the &alpha; = 0.01 significance level

## Summary
- Two-sample ratio of variances; *F* distribution (briefly), confidence intervals and hypothesis tests for normal population.
- Goodness of fit; Kolmogorov-Smirnov (basis, statistic, test, illustration), X{{2}} (basis, statistic, test, example)

# Regression
## Regression
**Regression models** are used to describe functional relationships between ~()explanatory~ variables **X** and ~()response~ variables **Y**. In such models, the response variables **Y** are assumed to be a function **f** of the explanatory variables **X**, corrupted by noise from a (zero-mean) ~()error model~. Usually, the function **f** is ~()parametric~, depending on some parameter vector **&beta;**, so that we may write the regression model as
$$$
Y = f(X;\beta) + \epsilon
$$$
where &epsilon; is a zero-mean random variable encoding our error model.
**Remark:** Usually, we assume that *&epsilon; ~ N(0, &sigma;{{2}}I)*, independent of all other random variables.
In this framework, given outcomes of the explanatory variables **X = x**, the response variables **Y** have conditional expectation
$$$
\mathbb{E}[Y\mid X=x] = f(x;\beta)
$$$
In a **linear regression** model, this relationship is linear, so that
$$$
\mathbb{E}[Y\mid X=x] = \beta_0 + \beta_1 x
$$$
In other words, in a linear regression model, given the outcome of the *i*-th explanatory variable *X{i} = x{i}*, the *i*-th response variable *Y{i}* modelled as
$$$
Y_i = \beta_0+\beta_1x_i+\epsilon_i,\qquad i=1,\ldots,N
$$$
where the usual error model is *&epsilon;{1}, ..., &epsilon;{N} ~iid N(0, &sigma;{{2}})*

### Linear Regression
The line
$$$
y = \beta_0+\beta_1x
$$$
is called the **regression line** (or more generally, ~()regression curve~). Notice that the linear regression model depends on the unknown coefficients &beta;{0} and &Beta;{1}, as well as the (typically unknown) error variance &sigma;{{2}}. Given outcomes of the explanatory variables **X = x** and response variables **Y = y**, how can we determine the unknown coefficients in &beta; = (&beta;{0}, &beta;{1}){{T}}?

## Least Squares Method
To do so, we first need a reasonable way of determining how well a given parameter setting &beta; fits the data. The usual approach is to examine the **residuals** given a particular parameter setting:
$$$
r_i = y_i - (\beta_0+\beta_1x_i)
$$$
which is just the ~()residual~ value of observed response *y{i}* once the model involving the explanatory variables has been removed. A typical measure of overall model fit is then the sum of the squared residuals:
$$$
\sum^N_{i=1} r^2_i = \sum^N_{i=1}(y_i - (\beta_0+\beta_1x_i))^2
$$$
The usual approach for finding the best parameters is to ~()minimise~ the sum of the squared residuals. This approach is called the **method of least squares**.
Formally, we seek to minimise
$$$
\sum^N_{i=1}r^2_i = \mid\mid r\mid\mid^2
$$$
with respect to the parameter vector &beta;. Whenever we may write a **linear model**
$$$
Y = A\beta+\epsilon,\qquad\epsilon\sim N(0, \sigma^2I)
$$$
for some parameter vector &beta; and **design matrix** *A* (whose elements may depend on the outcomes of explanatory variables **X = x**), for given outcomes **Y = y** we have
$$$
\mid\mid r\mid\mid^2 = \mid\mid y-A\beta\mid\mid^2
$$$

Therefore, for a linear model, we seek a parameter vector &beta; that solves
$$$
\nabla_\beta \mid\mid y-A\beta\mid\mid^2 = 0
$$$
or in other words
$$$
A^T(y-A\beta)=0
$$$
\ _f
This set of ~()linear~ equations in &beta; are called the **normal equations.** Rearranging, we have
$$$
A^TA\beta=A^Ty
$$$
so that if (A{{T}}A) is ~()invertible~,
$$$
\beta = (A^TA)^{-1}A^Ty
$$$
**Remark:** The design matrix *A* can always be chosen so that (A{{T}}A) is invertible. However, in practice, we never explicitly compute its inverse, but rather solve the set of linear equations numerically (for example via Gaussian elimination).

### Least Squares Example
**Example:** Suppose we have the ~()linear regression~ model.
$$$
Y_i = \beta_0+\beta_1x_i+\epsilon_i,\qquad i=1,\ldots,N
$$$
where *&epsilon;{1}, ..., &epsilon;{N} ~iid N(0, &sigma;{{2}})*. Given an outcome **Y = y**, what is the ~()least squares solution~ for *&beta; = (&beta;{0}, &beta;{1}){{T}}*?
It is convenient to rewrite this model as
$$$
Y=A\beta+\epsilon
$$$
where the ~()design matrix~ A is given by
$$$
\begin{pmatrix}
1&x_1\\
.&.\\
.&.\\
.&.\\
1&x_N
\end{pmatrix}
$$$
Then, given **Y = y**, the least squares solution *&hat;&beta;* solves
$$$
(A^TA)\hat{\beta}=A^Ty
$$$
**Remark:** In this case, we can solve for *&hat;&beta;* exactly, yielding
$$$
\hat{\beta_1} = \frac{\sum^N_{i=1}(x_i-\bar{x})(y_i-\bar{y})}{\sum^N_{i=1}(x_i-\bar{x})^2}
$$$
and
$$$
\hat{\beta_0} = \bar{y} - \beta_1\bar{x}
$$$
where as usual *&bar;x* and *&bar;y* denote the average of outcomes *\{x{i}\}* and *\{y{i}\}* respectively.

**Example:** Suppose we have a ~()quadratic regression~ model
$$$
Y_i = \beta_0+\beta_1x_i+\beta_2x^2_i+\epsilon_i,\qquad i=1,\ldots,N
$$$
where *&epsilon{1}, ..., &epsilon{N} ~iid N(0, &sigma;{{2}})*. Given an outcome **Y = y**, what is the ~()least squares solution~ for *&beta; = (&beta;{0}, &beta;{1}, &beta;{2}){{T}}*? Once again, it is convenient to rewrite this model as
$$$
Y=A\beta+\epsilon
$$$
where the ~()design matrix~ A is given by
$$$
A = 
\begin{pmatrix}
1&x_1&x^2_1\\
.&.&.\\
.&.&.\\
.&.&.\\
1&x_N&x^2_N
\end{pmatrix}
$$$
Then, given **Y = y**, the least squares solution *&hat;&beta;* solves the ~()normal equations~
$$$
(A^TA)\hat{\beta} = A^Ty
$$$
**Remark 1:** As these illustrate, ~()linear models~ depend linearly on the unknown parameters &beta;, and do ~()not~ require that the form of the regression curve be linear. In contrast, whenever the regression model is not linear in &beta;, then it is said to be a ~()nonlinear regression model~.
**Remark 2:** For linear models, it turns out that the least squares solution &hat;&beta; is the maximum likelihood solution.

## Summary
- Regression; model, error term, linear regression, quadratic regression, linear models, residuals
- Least squares; basis, normal equations, examples

# Regression II
## Linear Models
Recall that a ~()linear model~ is a regression model of the form
$$$
Y = A\beta+\epsilon,\qquad\epsilon\sim N(0,\sigma^2I)
$$$
for some parameter vector &beta; and **design matrix** A (whose elements may depend on the outcomes of explanatory variables **X = x**). Given observed responses **Y = y** for a linear model, we had that the ~()least squares solution~ &hat;&beta; for the unknown parameters solved
$$$
A^TA\hat{\beta}=A^Ty
$$$
**Remark:** Geometrically, &hat;&beta; is the projection of **y** onto the subspace spanned by the columns of the design matrix A. We saw two examples of linear models, namely the ~()linear regression~ model and the ~()quadratic regression~ model. What other useful regression models are linear models?

### Linear Models Example
**Example:** ~()Polynomial regression models~ seek to find the best polynomial fit to noisy data. Formally, for a polynomial model of degree *n*, each response variable *Y{i}* is modelled as
$$$
Y_i=\sum^n_{k=0}\beta_kx^k_i+\epsilon_i
$$$
where *&epsilon;{i} ~ N(0, &sigma;{{2}})*.
This can be seen as a linear model with design matrix
$$$
A = 
\begin{pmatrix}
1&x_i&x^2_i&\cdots&x^n_1\\
\vdots&\vdots&\vdots&\vdots&\vdots\\
1&x_N&x^2_N&\cdots&x^n_N
\end{pmatrix}
$$$
Therefore, we can fit the regression model by solving for &hat;&beta;

**Remark 1:** This suggests that a sensible approach to model fitting is to successively increase model complexity ~()until~ the variability seen in data is well explained by the model -- and the remaining variability is consistent with our assumptions on the error model.
**Remark 2:** However, one pitfall is ~()overfitting~, where a more complex model will ~()always~ fit data better than a simpler model nested inside it. Therefore, we always seek the ~()simplest~ model that fits the data well.

## Coefficient of Determination
A measure of model fit is the **coefficient of determination**, which can be constructed by scaling the residuals by the sum of squared deviations from the mean of the observed responses:
$$$
R^2 = 1-\frac{\mid\mid r\mid\mid^2}{\mid\mid y-\bar{y}\mid\mid^2}
$$$
If *R{{2}}* is close to 0, then the model does no better than a constant model set to the sample mean *&bar;y*. On the other hand, if R{{2}} is close to 1, then the model well explains the variability inherent in the observed responses **y**.

### R2 Example
**Example (Response Surface Model):** Suppose we have reponse *\{y{i}\}* with two explanatory variables *x{i,1}* and *x{i,2}*. We wish to model data through a two-dimensional polynomial model
$$$
Y_i = \sum^n_{j=0}\sum^n_{k=0}\beta_{j,k}x^j_{i,1}x^k_{i,2}+\epsilon_i
$$$
We can rewrite this model as a linear model, and solve for &hat;&beta; for successively larger *n*, until the coefficient of determination *R{{2}}* is close to 1.

## Residual Testing
It seems that our final model fits well -- how can we test the quality of the fit? If our model consistent with observed data, then the ~()residuals~ *\{r{i}\}* should be a random sample from N(0, &sigma;{{2}}), where typically &sigma;{{2}} is not known. Note that, when the ~()design matrix A~ is of dimension *N &times; K* with *N > K*, there are only *N - K* linearly independent elements of **r**. Therefore,
$$$
\mathbb{E}[\mid\mid R\mid\mid^2 \mid X=x]=\mathbb{E}\left[ \sum^N_{i=1}(Y_i-A\hat{\beta})^2\mid X=x \right] = (N-K)\sigma^2
$$$
and so an ~()unbiased~ estimator of &sigma;{{2}} from the residuals is
$$$
S^2_R = \frac{1}{N-K}\sum^N_{i=1}R^2_i=\frac{1}{N-K}\sum^N_{i=1}(Y_i-A\hat{\beta})^2
$$$
Therefore, we can perform a hypothesis test on the residuals: *H{0} : &mu; = 0* vs *H{1} : &mu; /= 0*. Under *H{0}*, the statistic
$$$
T=\frac{\bar{R}}{S_R/\sqrt{N}}\sim t_{N-K}
$$$
\ _f
where &bar;R and S{R} denote the sample mean and (unbiased) standard deviation of the residuals, respectively. Thus, ~()provided that the assumption of common variance is reasonable~, the *p*-value associated with this statistic under *H{0}* is a measure of the quality of our error model:
$$$
p = 2\text{max}\{\mathbb{P}(T>t),\mathbb{P}(T<t)\}
$$$
**Remark:** This assumption can be checked visually by examining plots of the residuals
**Remark:** Up to now, we have implicitly assumed that there is only ~()one~ observation of the response for the ~()same~ set of explanatory variables. How multiple observations change our analysis will be subject of our next set of lectures.

## Summary
- Linear models; polynomial regression, response surface models, philosophy and pitfalls.
- Coefficient of determination; definition, interpretation, example.
- Residual testing; *t*-test for residuals
