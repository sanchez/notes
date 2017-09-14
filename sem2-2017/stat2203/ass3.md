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
&= \frac{8}{3}\left(\left(\frac{3}{8}\right) - \left(\frac{1}{3} - \frac{1}{18}\right)\right)\\
&= \frac{8}{3}\left(\frac{3}{8}-\frac{5}{18}\right)\\
&= \frac{8}{3}\frac{7}{72}\\
&= \frac{7}{27}
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

# Question 5
```
function result = ass3q5
  N=1e3;
  numOfInsideRange = 0;
  sumOfInsideRange = 0;
  for i = 1:N
    tempVal = outcome(rand);
    if (tempVal > 1/3 && tempVal < 1/2)
      numOfInsideRange++;
      sumOfInsideRange += tempVal;
    endif
  endfor
  avg = sumOfInsideRange/numOfInsideRange
endfunction

function result = outcome(y)
  lambda = 8/3;
  a = -lambda/2;
  b = lambda;
  c = -y;
  result = (sqrt(b^2 - 4*a*c) - b)/(2*a);
endfunction
```

The above code, when run, gives an approximate answer of 0.40

# Question 6
```
function result = ass3q6
  N=1e3;
  results1 = 1:N;
  results10 = 1:N;
  for i = 1:N
    results1(i) = simVariable(1);
    results10(i) = simVariable(10);
    results100(i) = simVariable(100);
  endfor
  subplot(3, 1, 1);
  hist(results1, -4:.5:4);
  title("Z = 1");
  ylabel("Num of hits");
  xlabel("x of Xn");
  subplot(3, 1, 2);
  hist(results10, -4:.5:4);
  title("Z = 10");
  ylabel("Num of hits");
  xlabel("x of Xn");
  subplot(3, 1, 3);
  hist(results100, -4:.5:4);
  title("Z = 100");
  ylabel("Num of hits");
  xlabel("x of Xn");
endfunction

function result = simVariable(n)
  X = -log(rand(1, n));
  Z = (sum(X) - n)/sqrt(n);
  result = Z;
endfunction
```

The above code outputs the following image:
![Question 6 answer](sem2-2017/stat2203/ass3.q6.png)[100]