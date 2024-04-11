<script>
MathJax = { chtml: { displayAlign: "left", }
};
</script>
<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
<script type="text/x-mathjax-config">
 MathJax.Hub.Config({
 tex2jax: {
 inlineMath: [['$', '$'] ],
 displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
 }
 });
</script>

<details>

<summary>ABC154</summary>

## A, B, C

omit.

## D

累積和を用いる。
数列 $a_i$ の $l<=i<=r$ 区間における和は

$$
\begin{align}
& s_j = \Sigma_{i=0}^j a_i
\end{align}
$$

を満たす部分和 $s$ を用いて $s_r - s_l$ で簡単に表現できる

</details>

<details>

<summary>ABC087</summary>

## B

動的計画法ではなく、シンプルにfor文を回す。
文字列を使ったり、ループ数が多くなるなら検討しなければならないが、今回は時間的にかなり余裕があるのでごり押しで全く問題ない。

</details>

<details>

<summary>ABC158</summary>

## A, B, C

omit.

## D

文字列の結合はコストが高く、今回の場合はqueryごとに結合しているとTLEとなるので、両側からデータを出し入れできるdequeを使用する。
リストではpopやinsertでO(N)のコストが必要となるが、dequeではそれら（append, leftappend, pop, popleft）がすべてO(1)で実行できる。
（両端以外のデータアクセスはリストが有利）

</details>

<details>

<summary>ABC299</summary>

## A, B

omit.

## C

'o'のみで構成される文字列の前後いずれかに'-'があればそれらはダンゴ文字列となる。
このような場合は横着せずに、'o'のみで構成される文字列の前に'-'がある場合と後にある場合を**別で考えれば**、同じ動作の繰り返して簡単に記述できる。

- 文字列Sの反転

```py
 S = S[::-1]
```

## D

omit.

</details>

<details>

<summary>tessoku_book</summary>

## A18

動的計画法を利用する。

A = [2, 3] の場合

||0|1|2|3|4|5|6|7|8|9|...|
|-----|-|-|-|-|-|-|-|-|-|-|-|
|dp[0][j]|1|0|0|0|0|0|0|0|0|0|...|
|dp[1][j]|1|0|1|0|1|0|1|0|1|0|...|
|dp[2][j]|1|0|0|1|0|1|1|0|0|1|...|

$$
\left\{
  \begin{align}
    &\begin{split}
      dp[i][j] &= 1 \quad (if \quad dp[i-1][j] = 1 \quad or \quad dp[i-1][j-A[i]])\\
      &=0
    \end{split}\\
  \end{align}
\right.
$$

以上のようにdp表を用意して、dp[N][S]（目的の値）が1が否かを判定すればよい。


</details>
