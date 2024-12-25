# 常用的latex公式
## 基本的
指数
$\exp_a b = a^b,10^m$

根号
$\surd, \sqrt{2}, \sqrt[2]{n}, \sqrt[3]{\frac{x^3+y^3}{2}}$

对数
$\ln c, \lg d = \log e, \log_{10} f$

三角函数
$\sin a,\cos a, \tan c$

绝对值
$\left\vert s \right\vert$

最大值、最小值
$\min(x,y), \max(x,y)$

运算符
$+, -, \pm, \mp, \dotplus, \times, \div, \divideontimes$

## 极限，界限
min max
$\min x, \max x$

极限
$\lim u, \liminf v, \limsup v$

极限
$\lim_{x \to \infin} \frac{1}{n(n+1)}$

微分及导数
$dt, \mathrm{d}t, \partial t, \nabla\psi$

dy/dx...
$dy/dx, \mathrm{d}y/\mathrm{d}x, \frac{dy}{dx}$/

导数
$\prime, \backprime, f^\prime, f', f'', f^{(3)}, \dot y, \ddot y$

类字母
$\infin, \eth, \mho$

模运算
$s_k \equiv 0 \pmod{m}, a \bmod b,$+

## 集合
集合符号
$\{ \}, \empty, \varnothing$

集合关系
$\in, \notin, \not\in, \ni, \not\ni,\subset, \supset, \subseteq, \supseteq, \nsubseteq, \nsupseteq, \subseteqq, \supseteqq$

集合运算符号
$\cap, \cup$

## 矩阵
$\begin{matrix}
    x & y \\
    z & v
\end{matrix}$
$\begin{pmatrix}
    x & y \\
    z & v
\end{pmatrix}$
$\begin{Vmatrix}
    x & y \\
    z & v
\end{Vmatrix}$
$\begin{vmatrix}
    x & y \\
    z & v
\end{vmatrix}$
$\begin{bmatrix}
0      & \cdots & 0      \\
\vdots & \ddots & \vdots \\
0      & \cdots & 0
\end{bmatrix}$

## 关系符号
等的关系
$=, \ne, \neq, \equiv, \not\equiv$

约等于
$\approx, \thickapprox, \approxeq, \propto, \varpropto$

大小于
$<, \nless, \ll, \lll, >, \ngtr, \gg, \ggg$

大小等于
$\ge, \le, \lneq, \gneq, \leqslant, \geqslant$

## 几何符号
集合关系
$\perp, \parallel, \angle, \measuredangle, 45^\circ$

反正是三角
$\triangle, \bigtriangleup, \triangledown, \bigtriangledown, \blacktriangle, \blacktriangledown$

## 逻辑符号
存在、任何
$\forall, \exists, \nexists$

因为所以
$\therefore, \because, \And$

或
$\lor, \vee$

不知道啥
$\land$

头上戴的东西
$\bar{q}, \bar{abc}, \overline{a}, \overline{abc}, \lnot, \neg, \not\operatorname{R}$

## 条件表达式
$f(n) =
\begin{cases}
n/2,  & \text{if }n\text{ is even} \\
3n+1, & \text{if }n\text{ is odd}
\end{cases}$

## 箭头
$\rightarrow, \leftarrow, \Rightarrow, \Leftarrow, \Rrightarrow, \Lleftarrow, \Leftrightarrow, \Longleftrightarrow, \uparrow, \downarrow, \leftrightarrow$

## 组合示例
极限
$\lim_{n \to \infin}x_n$

积分
$\int_{-N}^{N} e^x\,{\rm d}x$

$\begin{matrix}
    \int_{-N}^{N} e^x\,{\rm d}
\end{matrix}$

求和
$\sum_{k=1}^N k^2$

累乘
$\prod_{i=1}^N x_i$

双重积分
$\iint_{D}^{W} \, \mathrm{d}x\,\mathrm{d}y$

分数
$\frac ab, \frac{a}{b}$, $a \over b$, $\cfrac{2}{c + \cfrac{2}{d + \cfrac{2}{4}}} = a$

二项式系数
$\dbinom{n}{r}=\binom{n}{n-r}=\mathrm{C}_n^r=\mathrm{C}_n^{n-r}$

多行等式
整齐且居中，使用`\begin{aligned}`
$\begin{aligned}
f(x) & = (m+n)^2 \\
     & = m^2+2mn+n^2 \\
\end{aligned}$

>^{}表示的是上标，_{}表示下标
