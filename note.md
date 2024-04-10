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

<summary>ABC158</summary>

## A, B, C

omit.

## D

文字列の結合はコストが高く、今回の場合はqueryごとに結合しているとTLEとなるので、両側からデータを出し入れできるdequeを使用する。
リストではpopやinsertでO(N)のコストが必要となるが、dequeではそれら（append, leftappend, pop, popleft）がすべてO(1)で実行できる。
（両端以外のデータアクセスはリストが有利）

</details>
