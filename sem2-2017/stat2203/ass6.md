---
author: Daniel Fitzmaurice
title: STAT2203 Assignment 6
alt-name: 43961229
logo: /home/sanchez/Documents/logo.jpg
school: University of Queensland
subject: ~()**STAT2203**~ -- Probability Models and Data Analysis for Engineering
---

# Question 1

# Question 2
Let
$$$
\beta = \begin{pmatrix} \mu \\ \alpha_1 \\ \alpha_2 \\ \alpha_3 \end{pmatrix}
$$$
If *&alpha;{4} == &alpha;{1} + &alpha;{2} + &alpha;{3}*, then
$$$
A = \begin{pmatrix} 1 & 1 & 0 & 0 \\
                    1 & 1 & 0 & 0 \\
                    1 & 0 & 1 & 0 \\
                    1 & 0 & 1 & 0 \\
                    1 & 0 & 0 & 1 \\
                    1 & 0 & 0 & 1 \\
                    1 & 1 & 1 & 1 \\
                    1 & 1 & 1 & 1 \end{pmatrix}
$$$
Therefore *&epsilon; ~ N(**0**, &sigma;{{2}}I)*

# Question 3

$$$
\mathbb{E}\left[\frac{1}{\hat{\lambda}}\right] &= \frac{1}{\lambda}\\
\text{Var}\left(\frac{1}{\hat{\lambda}^2}\right) &= \frac{\left(\frac{1}{\lambda^2}\right)}{n}\\
&= \frac{n}{\lambda^2}
$$$
Therefore the stochastic interval is:
$$$
\frac{1}{\lambda} \pm z_{1-\frac{\alpha}{2}} \frac{\sqrt{\frac{n}{\lambda^2}}}{\sqrt{n}}\\
\frac{1}{\lambda} \pm z_{1-\frac{\alpha}{2}} \frac{n}{\lambda}
$$$

# Question 4
![Question 4 Answer](sem2-2017/stat2203/ass6.q4.png)[75]

```
load('PearsonFather.csv');
load('PearsonSon.csv');
x = PearsonFather;
y = PearonSon;
N = 1e3;
xx = linspace(58, 76, N);
A = [ones(length(x), 1), x];
beta = (A' * A) \ A' * y;
sigma2 = mean((y - A * beta).^2);
AAInv = inv(A' * A);
for i = 1:N
    ax = [1 xx(i)];
    mux = ax * beta;
    sx = sqrt(sigma2 * ax * AAInv * ax');
    yy(i) = mux;
    yy1(i) = mux - 1.95*sx;
    yy2(i) = mux + 1.95*sx;
end;
figure(1);
plot(x, y, 'k.', xx, yy, 'r-', xx, yy1, 'r:', xx, yy2, 'r:');
xlabel("Father Height");
ylabel("Son Height");
sigma2
```

*&sigma;{{2}}* is estimated to be 5.9335

# Question 5
```
tbl = [13.8, 11.7, 14.0, 12.6;
12.9, 16.7, 15.5, 13.8;
25.9, 29.8, 27.8, 25.0;
15.2, 20.2, 19.9, 13.7];
anova(tbl)
```

This results in output equivalent to 0.2652
