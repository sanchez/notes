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

# Question 4
```
~(blue)function~ result = ass1
  N = ~(green)1e3~;
  x = linspace(~(green)0~, ~(green)1~, N);
  y = [~(green)1~:N];
  for i = ~(green)1~:N
    y(i) = systemFailure(x(i));
  end
  plot(x, y, ~(gold)"linewidth"~, ~(green)2~, x, x, ~(gold)"linewidth"~, 2);
  xlabel(~(gold)"Probability of ring failure"~);
  ylabel(~(gold)"Probability of system failure"~);
~(blue)endfunction~

~(blue)function~ result = linkSuccess(p)
  result = ~(green)1~ - p;
~(blue)endfunction~

~(blue)function~ result = sealSuccess(p)
  result = ~(green)1~ - (~(green)1~ - linkSuccess(p))^~(green)2~;
~(blue)endfunction~

~(blue)function~ result = systemSuccess(p)
  result = sealSuccess(p)^~(green)6~;
~(blue)endfunction~

~(blue)function~ result = systemFailure(p)
  result = ~(green)1~ - systemSuccess(p);
~(blue)endfunction~
```
By running the above code, we get the output provided below. The point at which `systemFailure(p) = p` occurs at points `[0, 0.18, 1]` as visible from the diagram below.
![Question 4 Answer](sem2-2017/stat2203/ass1.q4.png)[100]
\\
# Question 5
```
~(blue)function~ result = ass1q5
  N = ~(green)1e4~;
  received = ~(green)0~;
  sent0 = ~(green)0~;
  for i = ~(green)1~:N
    [s, r] = get\_receive\_bit();
    ~(blue)if~ r == ~(green)1~
      received += ~(green)1~;
      ~(blue)if~ s == ~(green)0~
        sent0 += ~(green)1~;
      ~(blue)endif~
    ~(blue)endif~
  end
  printf(~(gold)"%d:%d\n"~, received, sent0);
~(blue)endfunction~

~(blue)function~ [sent, received] = get\_receive\_bit
  bit = get\_sent\_bit();
  ~(blue)if~ bit == ~(green)1~
    ~(blue)if~ rand >= ~(green)0.9~
      received = bit;
    ~(blue)else~
      received = ~(green)0~;
    ~(blue)endif~
  ~(blue)else~
    ~(blue)if~ rand >= ~(green)0.95~
      received = bit;
    ~(blue)else~
      received = ~(green)1~;
    ~(blue)endif~
  ~(blue)endif~
  sent = bit;
~(blue)endfunction~

~(blue)function~ result = get\_sent\_bit
  ~(blue)if~ rand >= ~(green)0.5~
    result = ~(green)1~;
  ~(blue)else~
    result = ~(green)0~;
  ~(blue)endif~
~(blue)endfunction~
```
Based on the code above, the output by running `ass1q5`, we can expect an answer close to `5241:4728`

# Question 6
```
~(blue)function~ ass1q6
  N=1e4;
  result = [~(green)-3~:~(green)3~];
  ~(blue)for~ i = ~(green)1~:N
    result(i) = sumWithReplace();
  ~(blue)endfor~
  result;
  hist(result, ~(green)-3~:~(green)3~);
  xlabel(~(gold)"Sum of draw with replace"~);
  ylabel(~(gold)"Number of sums"~);
~(blue)endfunction~

~(blue)function~ result = sumWithReplace
  result = sum(int8(rand(~(green)3~, ~(green)1~) * ~(green)2~) - ~(green)1~);
~(blue)endfunction~
```
The above code generates the following histogram:
![Question 6 Answer](sem2-2017/stat2203/ass1.q6.png)[100]