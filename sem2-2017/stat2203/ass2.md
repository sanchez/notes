---
author: Daniel Fitz
title: STAT2203 Assignment 2
alt-name: 43961229
logo: /home/sanchez/Documents/logo.jpg
school: University Of Queensland
subject: ~()**STAT2203**~ -- Probability Models and Data Analysis for Engineering
---

# Question 1
Let *X* be the event that the ball falls in box *x*. Where *X ~ Bin(4, 0.5)*

## SubQuestion A
$$$
\mathbb{P}(X=x) &= {{4}\choose{x}} \left(\frac{1}{2}\right)^x\times \left(1-\frac{1}{2}\right)^{4-x}\\
&= {4\choose{x}}\left(\frac{1}{2}\right)^4\\
&= \frac{1}{16}{4\choose{x}}\\
\mathbb{P}(X=3) &= \frac{1}{16}{4\choose{3}}\\
&= \frac{4}{16} = \frac{1}{4}
$$$

## SubQuestion B
$$$
\mathbb{P}(X=x) &= {4\choose{x}}\left(\frac{1}{2}\right)^x\times\left(1-\frac{1}{2}\right)^{4-x}\\
&={4\choose{x}}\frac{1}{2^x}\times\frac{1}{2^{4-x}}\\
&={4\choose{x}}\frac{2^x}{2^4 2^x}\\
&=\frac{1}{16}{4\choose{x}}
$$$

# Question 2
## Part 1
We are given:
$$$
\mathbb{P}(X=1) &= r\\
\mathbb{P}(X=0) &= 1-r\\
\mathbb{P}(Y=1) &= s\\
\mathbb{P}(Y=0) &= 1-s
$$$
Therefore the following table can be generated:
| Y\X | 0 | 1
| 0 | *(1-r)(1-s)* | *r(1-s)*
| 1 | *s(1-r)* | *rs*
: Combinations of *P(X=x)P(Y=y)*
Using the above table, we can see that U and V will both take on values {*0, 1*}
| U,V | X,Y | Solution
| --- | --- | --- |
| 0,0 | 0,0 | *(1-r)(1-s)*
| 0,1 | 1,0 + 0,1 | *r(1-s) + s(1-r)*
| 1,0 | *Not possible* | *0*
| 1,1 | 1,1 | *rs*
Therefore the following joint pmf table can be calculated
| U\V | 0 | 1
| 0 | *(1-r)(1-s)* | *r(1-s) + s(1-r)*
| 1 | *0* | *rs*

## Part 2
$$$
\mathbb{P}(V=1, U=1) &= \mathbb{P}(V=1)\mathbb{P}(U=1)\\
rs &= (rs)(r+s-rs)\\
1 &= r+s-rs\\
1-s &= r-rs\\
&= r(1-s)\\
1 &= r\\
\mathbb{P}(V=0, U=0) &= \mathbb{P}(V=0)\mathbb{P}(U=0)\\
(1-r)(1-s) &= (1-rs)(1-s-r+rs)\\
1-r-s+rs &= 1-s-r+rs-rs+rs^2+sr^2+(rs)^2\\
1+rs &= 1+rs^2 + sr^2 - (rs)^2\\
1+s &= 1+s^2+s-s^2\tag{\text{When $r$ is 1}}\\
1+s &= 1+s\\
\mathbb{P}(V=1, U=0) &= \mathbb{P}(U=0)\mathbb{P}(V=1)\\
r+s-2rs &= (1-rs)(r+s-rs)\\
r+s-2rs &= r+s-rs-r^2s-rs^2+r^2s^2\\
rs &= -r^2s-rs^2+r^2s^2\\
s &= -s-s^2+s^2\tag{\text{When $r$ is 1}}\\
s &= -s\\
s &= 0\\
\mathbb{P}(U=1, V=0) &= \mathbb{P}(U=1)\mathbb{P}(V=0)\\
0 &= rs(1-s-r+rs)\tag{\text{When $r$ is 1, When $s$ is 0}}\\
0 &= 0
$$$

# Question 3
$$$
L(\theta;p) &= \prod^5_{i=1}(1-p)^{x_i}p\\
l(\theta;p) &= \sum^5_{i=1}\log\left((1-p)^{x_i-1}\right) + \log(p)\\
&= n\log(p) + \sum^5_{i=1}(x_i-1)\log(1-p)\\
&= n\log(p) + \log(1-p)\sum^5_{i=1}(x_i-1)\\
\frac{d}{dp}\quad &\frac{n}{p}-\frac{\sum^5_{i=1}(x_i-1)}{1-p}\\
0 &= \frac{n}{p}-\frac{\sum^5_{i=1}(x_i-1)}{1-p}\\
\frac{n}{p} &= \frac{\sum^5_{i=1}(x_i-1)}{1-p}\\
\frac{n}{p} - n &= -n\sum^5_{i=1}(x_i)\\
\frac{n}{p} &= \sum^5_{i=1}(x_i)\\
p &= \frac{n}{\sum^5_{i=1}(x_i)} = \frac{1}{\bar{x}}
$$$
