---
author: Daniel Fitz
title: STAT2203 Assignment 1
alt-name: 43961229
logo: /home/sanchez/Documents/logo.jpg
school: University Of Queensland
subject: ~()**STAT2203**~ -- Probability Models and Data Analysis for Engineering
---

# Question 1
Let *S* be the event the system succeeds
Let *A{i}* be the event that a joint is successful
Let *L{i}* be the event that an O-ring is successful
$$$
\mathbb{P}(L_i) &= 1-\mathbb{P}(L_i^c)\\
&= 1-0.1\tag{From question}\\
&= 0.9\\
\mathbb{P}(A_i^c) &= \mathbb{P}(L_i\cap L_i)\\
&=\mathbb{P}(L_i^c)\mathbb{P}(L_i^c)\\
&= 2\times 0.1\\
&= 0.01\\
\mathbb{P}(A_i) &= 0.99\\
\mathbb{P}(S) &= \mathbb{P}(A_i\cap A_i\cap A_i\cap A_i\cap A_i\cap A_i)\\
&= \mathbb{P}(A_i)^6\\
&= 0.99^6\\
&= 0.9415\\
\mathbb{P}(S^c) &= 1-\mathbb{P}(S)\\
&\approx 0.0585
$$$
Therefore the probability that the system will fail is 5.85%

# Question 2
Let *R{i}* be the event that *i* is received
Let *S{i}* be the event that *i* is sent
From the question:
$$$
\mathbb{P}(S_0) &= 0.5\\
\mathbb{P}(S_1) &= 0.5\\
\mathbb{P}(R_1\mid S_1) &= 0.9\\
\mathbb{P}(R_0\mid S_0) &= 0.95
$$$
Using Baynes rule:
$$$
\mathbb{P}(S_0\mid R_1) &= \frac{\mathbb{P}(R_1\mid S_0)\mathbb{P}(S_0)}{\mathbb{P}(R_1\mid S_0)\mathbb{P}(S_0)+\mathbb{P}(R_1\mid S_1)\mathbb{P}(S_1)}\\
&= \frac{(1-0.95)\times0.5}{(1-0.95)\times0.5+0.9\times0.5}\\
&= \frac{1}{19} \approx 0.0526
$$$
Therefore, given we receive a 1 it is 5.26% likely that a 0 was sent

# Question 3
Let *A* be the event that the sum of numbers is 1
$$$
\Omega = \{-1, 0, 1\}
$$$
> Assume that the each number is draw at equal probability

## Without Replacement
$$$
(1, 0), &&(1, -1), &&(0, 1), &&(0, -1), &&(-1, 0), &&(1, 1)\\
1 &&0 &&1 &&-1 &&-1 &&0
$$$
Therefore:
$$$
\mathbb{P}(A) &= \frac{\mid A\mid}{\mid\Omega\mid}\\
&= \frac{2}{6} = \frac{1}{3}
$$$

## With Replacement
$$$
(1, 1), &&(1, 0), &&(1, -1), &&(0, 1), &&(0, 0), &&(0, -1), &&(-1, 1), &&(-1, 0), &&(-1, -1)\\
2 &&1 &&0 &&1 &&0 &&-1 &&0 &&-1 &&-2
$$$
Therefore:
$$$
\mathbb{P}(A) &= \frac{\mid A\mid}{\mid\Omega\mid}\\
&= \frac{2}{9}
$$$
