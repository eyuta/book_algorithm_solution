# アルゴリズムとデータ構造の第 4 章「設計技法(2) : 再帰と分割統治法」を Python で解いてみた

Python の勉強のため、[問題解決力を鍛える!アルゴリズムとデータ構造](https://www.amazon.co.jp/%E5%95%8F%E9%A1%8C%E8%A7%A3%E6%B1%BA%E5%8A%9B%E3%82%92%E9%8D%9B%E3%81%88%E3%82%8B-%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0%E3%81%A8%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0-KS%E6%83%85%E5%A0%B1%E7%A7%91%E5%AD%A6%E5%B0%82%E9%96%80%E6%9B%B8-%E5%A4%A7%E6%A7%BB-%E5%85%BC%E8%B3%87/dp/4065128447/ref=pd_lpo_14_img_0/355-1660948-1917632?_encoding=UTF8&pd_rd_i=4065128447&pd_rd_r=85fc5fc0-6650-41b2-beaa-2a75e0e94bf5&pd_rd_w=6muXq&pd_rd_wg=hVxMm&pf_rd_p=cb2cef9d-b0a3-4b58-a575-45abfc5e07e8&pf_rd_r=5WKFBZPK0014FGC29YPR&psc=1&refRID=5WKFBZPK0014FGC29YPR)を Python で解いてみました(原本は C++で書かれています)。
本記事における引用はすべて、上記の本から引用しております。

もしより良い書き方があれば教えていただけると嬉しいです。

[第 3 章「設計技法(1) : 全探索」はこちら](https://qiita.com/eyuta/items/3e25ac0fd9a155c313e8)

## 環境

Python 3.8.5

## Code 全文

<https://github.com/eyuta/book_algorithm_solution/blob/main/src/04__recursion_and_divide_and_conquer_algorithm.py>

## 本文

### 第 4 章 設計技法(2) : 再帰と分割統治法

#### code 4.1 $1$ から$N$までの総和を計算する再帰関数

[Python の三項演算子](https://book.pythontips.com/en/latest/ternary_operators.html)は順番が少し特殊なので注意です。

```py
def func(N: int) -> int:
    return 0 if N == 0 else N + func(N - 1)

result = func(input_num('Number: '))
print('result: {}'.format(result))
```

#### code 4.2 $1$ から$N$までの総和を計算する再帰関数 (コメントあり)

```py
def func(N: int) -> int:
    print('func({}) を呼び出しました'.format(N))
    if N == 0:
        return 0

    result = N + func(N - 1)
    print('{} までの和 = {}'.format(N, result))
    return result

result = func(input_num('Number: '))
print('result: {}'.format(result))
```

#### code 4.3

上と対して変わらないので省略。

#### code 4.4 ユークリッドの互除法によって最大公約数を求める

```py
def GCD(m: int, n: int) -> int:
    return m if n == 0 else GCD(n, m % n)

GCD(15, 51)  # 3
GCD(51, 15)  # 3
```

#### code 4.5, 4.6 フィボナッチ数列を求める再帰関数

```py
def fibo(N: int) -> int:
    print('fibo({}) を呼び出しました'.format(N))

    if N == 0:
        return 0
    if N == 1:
        return 1

    result = fibo(N-1) + fibo(N-2)
    print('{} 項目 = {}'.format(N, result))
    return result

print('result: {}'.format(fibo(input_num('Number: '))))
```

<details><summary>出力
</summary><div>

```sh
fibo(6) を呼び出しました
fibo(5) を呼び出しました
fibo(4) を呼び出しました
fibo(3) を呼び出しました
fibo(2) を呼び出しました
fibo(1) を呼び出しました
fibo(0) を呼び出しました
2 項目 = 1
fibo(1) を呼び出しました
3 項目 = 2
fibo(2) を呼び出しました
fibo(1) を呼び出しました
fibo(0) を呼び出しました
2 項目 = 1
4 項目 = 3
fibo(3) を呼び出しました
fibo(2) を呼び出しました
fibo(1) を呼び出しました
fibo(0) を呼び出しました
2 項目 = 1
fibo(1) を呼び出しました
3 項目 = 2
5 項目 = 5
fibo(4) を呼び出しました
fibo(3) を呼び出しました
fibo(2) を呼び出しました
fibo(1) を呼び出しました
fibo(0) を呼び出しました
2 項目 = 1
fibo(1) を呼び出しました
3 項目 = 2
fibo(2) を呼び出しました
fibo(1) を呼び出しました
fibo(0) を呼び出しました
2 項目 = 1
4 項目 = 3
6 項目 = 8
result: 8
```

</div></details>

#### code 4.7 フィボナッチ数列を for 文による反復で求める

```py
K = input_num('Number: ')
F = [0, 1]

for N in range(2, K + 1):
    F.append(F[N -1] + F[N -2])
    print('{} 項目: {}'.format(N, F[N]))

print('result: {}'.format(F))
```

<details><summary>出力
</summary><div>

```sh
Number: 6
2 項目: 1
3 項目: 2
4 項目: 3
5 項目: 5
6 項目: 8
result: [0, 1, 1, 2, 3, 5, 8]
```

</div></details>

#### code 4.8 フィボナッチ数列を求める再帰関数をメモ化

Jupyter Notebook を使用すると、code 4.6 のコードでは N=40 くらいから処理落ちするようになりました。
しかし、メモ化すると N=1000 でも余裕です。すごい！

```py
K = input_num('Number: ')
memo = [-1] * (K + 1)
# ここでN=0,1を初期化すれば、ベースケースが不要になります
memo[0] = 0
memo[1] = 1

def fibo(N: int) -> int:
    if memo[N] != -1:
        return memo[N]

    memo[N] = fibo(N-1) + fibo(N-2)
    return memo[N]

fibo(K)
print('result: {}'.format(memo))
```

今回、メモ化を List を用いて行いましたが、Python の標準ライブラリに[functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)というメモ化(Memorize)用のライブラリがあります。
これを使うことでシンプルにメモ化が可能です。
尚、Python 3.9 以上であれば上記よりさらに軽量な[functools.cache](https://docs.python.org/3/library/functools.html#functools.cache)が使えるようです！

```py
from functools import lru_cache

@lru_cache
def fibo(N: int) -> int:
    print('fibo({}) を呼び出しました'.format(N))

    if N == 0:
        return 0
    if N == 1:
        return 1

    result = fibo(N-1) + fibo(N-2)
    print('{} 項目 = {}'.format(N, result))
    return result

print('result: {}'.format(fibo(input_num('Number: '))))
```

フィボナッチ数列を求めるコードは[code 4.6](#code-45-46-フィボナッチ数列を求める再帰関数)と同様のものを利用していますが、code 4.6 とは異なり N=1000 でも処理可能です。
内部的には、引数の値毎に返り値をキャッシュし、同じ引数であればキャッシュされた値を返しているようです。

<details><summary>出力
</summary><div>

```sh
Number: 10
fibo(10) を呼び出しました
fibo(9) を呼び出しました
fibo(8) を呼び出しました
fibo(7) を呼び出しました
fibo(6) を呼び出しました
fibo(5) を呼び出しました
fibo(4) を呼び出しました
fibo(3) を呼び出しました
fibo(2) を呼び出しました
fibo(1) を呼び出しました
fibo(0) を呼び出しました
2 項目 = 1
3 項目 = 2
4 項目 = 3
5 項目 = 5
6 項目 = 8
7 項目 = 13
8 項目 = 21
9 項目 = 34
10 項目 = 55
result: 55
```

</div></details>

#### code 4.9 部分和問題を再帰関数を用いる全検索で解く

※[for 文で解いたコードはこちら](https://qiita.com/eyuta/items/3e25ac0fd9a155c313e8#%E5%95%8F%E9%A1%8C-4-%E9%83%A8%E5%88%86%E5%92%8C%E5%95%8F%E9%A1%8C)

```py
def func(i: int, w: int, a: list) -> bool:
    # ベースケース
    if i == 0:
        return w == 0

    # a[i - 1]を選ばない場合
    if func(i - 1, w, a):
        return True

    # a[i - 1]を選ぶ場合
    if func(i - 1, w - a[i - 1], a):
        return True

    return False

N = input_num('Number N: ')
W = input_num('Number W: ')
a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

print('result: {}'.format('Yes' if func(N, W, a) else 'No'))
```

#### 章末問題

##### 4.1, 4.2 トリボナッチ数列

> トリボナッチ数列とは,
>
> - $T_0 = 0$
> - $T_1 = 0$
> - $T_2 = 1$
> - $T_N = T_{N-1} + T_{N-2} + T_{N-3} (N = 3,4,...)$
>
> によって定義される数列です.
> $0,0,1,1,2,4,7,13,24,44,...$と続いていきます.
> トリボナッチ数列の第 $N$ 項の値を求める再帰関数を設計してください.

ちなみに、初期値が$4$つ存在する場合は[テトラナッチ数列(Tetranacci numbers)](https://en.wikipedia.org/wiki/Generalizations_of_Fibonacci_numbers#Tetranacci_numbers)というそうです。

4.2 のメモ化も同時にやってしまいました。
メモ化時の計算量は、フィボナッチ数列同様$O(N)$となります。

```py
N = input_num('Number: ')

memo = [-1] * N

def tri(N: int) -> int:
    if N == 0 or N == 1:
        return 0
    if N == 2:
        return 1
    if memo[N] != -1:
        return memo[N]

    result = tri(N-1) + tri(N-2) + tri(N-3)

    memo[N] = result

    return result

for i in range(N):
    print('N: {:2d}, result: {:10d}'.format(i, tri(i)))
```

フォーマットを`{:2d}`のように定義することで、右揃えにすることができます。
(`{:<2d}`のように記述すると左揃えになります)

参考: [Python String Format Cookbook](https://mkaz.blog/code/python-string-format-cookbook/)

<details><summary>出力
</summary><div>

```sh
Number: 40
N:  0, result:          0
N:  1, result:          0
N:  2, result:          1
N:  3, result:          1
N:  4, result:          2
N:  5, result:          4
N:  6, result:          7
N:  7, result:         13
N:  8, result:         24
N:  9, result:         44
N: 10, result:         81
N: 11, result:        149
N: 12, result:        274
N: 13, result:        504
N: 14, result:        927
N: 15, result:       1705
N: 16, result:       3136
N: 17, result:       5768
N: 18, result:      10609
N: 19, result:      19513
N: 20, result:      35890
N: 21, result:      66012
N: 22, result:     121415
N: 23, result:     223317
N: 24, result:     410744
N: 25, result:     755476
N: 26, result:    1389537
N: 27, result:    2555757
N: 28, result:    4700770
N: 29, result:    8646064
N: 30, result:   15902591
N: 31, result:   29249425
N: 32, result:   53798080
N: 33, result:   98950096
N: 34, result:  181997601
N: 35, result:  334745777
N: 36, result:  615693474
N: 37, result: 1132436852
N: 38, result: 2082876103
N: 39, result: 3831006429
```

</div></details>

##### 4.3 フィボナッチ数列の一般項

> フィボナッチ数列の一般項が$F_N = \frac{1}{\sqrt{5}}((\frac{1+\sqrt{5}}{2})^N-(\frac{1-\sqrt{5}}{2})^N)$で表されることを示してください.

~~Markdown で書くのがしんどいため、解答を省略します~~
参考: [フィボナッチ数列の一般項と数学的帰納法 (高校数学の美しい物語)](https://manabitimes.jp/math/643)

以下さえ認識していれば、後は簡単に解けそうです。

- $α=\frac{1+\sqrt{5}}{2}$, $β=\frac{1-\sqrt{5}}{2}$としたときに以下が成り立つ
  - $α^2=α+1$
  - $β^2=β+1$
  - $α+β=1$
  - $αβ=-1$

##### 4.4 [コード 4.5](#code-45-46-フィボナッチ数列を求める再帰関数) で示したアルゴリズムの計算量が$O((\frac{1+\sqrt{5}}{2})^N)$であることを示す

フィボナッチ数列の一般項$F_N = \frac{1}{\sqrt{5}}((\frac{1+\sqrt{5}}{2})^N-(\frac{1-\sqrt{5}}{2})^N)$のうち、後者は$\lim_{N \to \infin}$のとき収束します。
($\lvert \frac{1-\sqrt{5}}{2} \rvert < 1$のため)
また、係数$\frac{1}{\sqrt{5}}$は無視できるため、計算量は残りの$(\frac{1+\sqrt{5}}{2})^N$となります。

##### 4.5 $753$ 数

> 十進法表記で各桁の値が$7,5,3$のいずれかであり, かつ$7,5,3$がいずれも一度以上は登場する整数を「$753$ 数」とよぶこととします. 正の整数$K$が与えられたときに, $K$以下の $753$数が何個あるかを求めるアルゴリズムを設計してください. ただし$K$の桁数を$d$として$O(3^d)$程度の計算量を許容できるものとします.

最初作成時、`use3: bool, use5: bool, use7: bool`のようにそれぞれのフラグを用意していました。
が、解答で使用しているビットフラグに変更しました。

```py
def count753Number(K: int, n: int, use: int, result: list) -> int:
    if n > K:
        return

    if use == 0b111:
        result.append(n)

    count753Number(K, n*10 + 3, use | 0b001, result)
    count753Number(K, n*10 + 5, use | 0b010, result)
    count753Number(K, n*10 + 7, use | 0b100, result)

K = input_num('Number: ')

if K < 357:
    raise ValueError('Invalid input')

result = []
count753Number(K, 0, 0b000, result)
print('result: {}'.format(result))
print('count : {}'.format(len(result)))

```

<details><summary>出力
</summary><div>

```sh
Number: 999
result: [357, 375, 537, 573, 735, 753]
count : 6
```

```sh
Number: 9999
result: [3357, 3375, 3537, 3557, 357, 3573, 3575, 3577, 3735, 375, 3753, 3755, 3757, 3775, 5337, 5357, 537, 5373, 5375, 5377, 5537, 5573, 573, 5733, 5735, 5737, 5753, 5773, 7335, 735, 7353, 7355, 7357, 7375, 753, 7533, 7535, 7537, 7553, 7573, 7735, 7753]
count : 42
```

</div></details>

また、以下のようなコードで count753Number の実行回数を調べると、$a_d ≒ 4.5 * 3 ^ d$となりました。
そのため、計算量は$O(3^d)$と言えそうです。

※関数内でローカルに存在しない変数を使用する場合、`nonlocal`で変数を定義する必要があります。
参考: [Python nonlocal Keyword](https://www.w3schools.com/python/ref_keyword_nonlocal.asp)

```py
    called = 0

    def count753Number(K: int, n: int, use: int, result: list) -> int:
        nonlocal called
        called += 1

        if n > K:
            return

        if use == 0b111:
            result.append(n)

        count753Number(K, n*10 + 3, use | 0b001, result)
        count753Number(K, n*10 + 5, use | 0b010, result)
        count753Number(K, n*10 + 7, use | 0b100, result)

    for d in range(3, 10):
        K = int('9' * d)
        result = []
        called = 0
        count753Number(K, 0, 0b000, result)
        print('d                : {}'.format(d))
        print('K                : {}'.format(K))
        print('Expected(O(3**d)): {}'.format(3**d))
        print('Called           : {}'.format(called))
        print('Actual / Expected: {}'.format(called / 3**d))
        print('count            : {}'.format(len(result)))
        print('======================================')
```

<details><summary>出力
</summary><div>

```sh
d                : 3
K                : 999
Expected(O(3**d)): 27
Called           : 121
Actual / Expected: 4.481481481481482
count            : 6
======================================
d                : 4
K                : 9999
Expected(O(3**d)): 81
Called           : 364
Actual / Expected: 4.493827160493828
count            : 42
======================================
d                : 5
K                : 99999
Expected(O(3**d)): 243
Called           : 1093
Actual / Expected: 4.497942386831276
count            : 192
======================================
d                : 6
K                : 999999
Expected(O(3**d)): 729
Called           : 3280
Actual / Expected: 4.499314128943759
count            : 732
======================================
d                : 7
K                : 9999999
Expected(O(3**d)): 2187
Called           : 9841
Actual / Expected: 4.499771376314587
count            : 2538
======================================
d                : 8
K                : 99999999
Expected(O(3**d)): 6561
Called           : 29524
Actual / Expected: 4.4999237921048625
count            : 8334
======================================
d                : 9
K                : 999999999
Expected(O(3**d)): 19683
Called           : 88573
Actual / Expected: 4.499974597368287
count            : 26484
======================================
```

</div></details>

##### 4.6 [code 4.9](#code-49-部分和問題を再帰関数を用いる全検索で解く)のメモ化

> 部分和問題に対する再帰関数を用いる計算量$O(2^N)$のコード 4.9 に対しメモ化して, $O(NW)$の計算量で動作するようにしてください.

[code 4.9](#code-49-部分和問題を再帰関数を用いる全検索で解く)からの変更点としては、

- 回数カウント用のクロージャ`count`を引数に追加
- メモ化を行うラッパー関数`memorize`を用意し、デコレータとして使用
  - `@memorize`と書くと、`func(N, W, a, count)`したときに自動的に`memorize(func)(N, W, a, count)`が実行される
  - 参考: [Python のデコレータについて](https://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e)
  - デコレータを使うことで、既存の関数に触れずにメモ化処理を加えることができる
- メモ化は、`tuple(N, W)`を Key とした dict で行った
  - Key が存在しなければ、`func`を実行し、その結果をメモ化
  - Key が存在すれば、該当 Key の Value を返す
- 関数の hint は Callable 型を使う
  - `Callable[[int], None]`と書くと、引数 1 が int, 返り値が None というように詳細な型を指定できる
  - 参考: [typing.Callable](https://docs.python.org/3/library/typing.html#callable)

```py
from typing import Callable

def memorize(func: Callable) -> Callable:
    memo = {}

    def wrapper(*args, **kwargs):
        if (args[:2]) not in memo:
            # args[:2] == (i, w)
            memo[args[:2]] = func(*args, **kwargs)
        return memo[args[:2]]
    return wrapper

@memorize
def func(i: int, w: int, a: list, count: Callable) -> bool:
    # これだけ追加
    count()

    # ベースケース
    if i == 0:
        return w == 0

    # a[i - 1]を選ばない場合
    if func(i - 1, w, a, count):
        return True

    # a[i - 1]を選ぶ場合
    if func(i - 1, w - a[i - 1], a, count):
        return True

    return False

def counter() -> Callable:
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count
    return inner

def main(N, W):
    count = counter()
    a = [1, 2, 3, 4, 5]*int(N/5)
    print('N     : {}'.format(N))
    print('W     : {}'.format(W))
    print('result: {}'.format('Yes' if func(N, W, a, count) else 'No'))
    print('count : {}'.format(count() - 1))

N = input_num('Number N: ')
W = input_num('Number W: ')

main(N, W)
```

<details><summary>出力
</summary><div>

メモ化

```sh
# メモ化した場合
N       : 10
W       : 30
result  : Yes
count   : 179

N       : 20
W       : 60
result  : Yes
count   : 674

N       : 20
W       : 100
result  : No
count   : 674

N       : 25
W       : 100
result  : No
count   : 1034

# メモ化しなかった場合 (@memorizeをコメントアウト)
N       : 10
W       : 30
result  : Yes
count   : 2047

N       : 20
W       : 60
result  : Yes
count   : 2097151

N       : 20
W       : 100
result  : No
count   : 2097151

N       : 25
W       : 100
result  : No
count   : 67108863
```

</div></details>

## 参考

- [問題解決力を鍛える!アルゴリズムとデータ構造](https://www.amazon.co.jp/%E5%95%8F%E9%A1%8C%E8%A7%A3%E6%B1%BA%E5%8A%9B%E3%82%92%E9%8D%9B%E3%81%88%E3%82%8B-%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0%E3%81%A8%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0-KS%E6%83%85%E5%A0%B1%E7%A7%91%E5%AD%A6%E5%B0%82%E9%96%80%E6%9B%B8-%E5%A4%A7%E6%A7%BB-%E5%85%BC%E8%B3%87/dp/4065128447/ref=pd_lpo_14_img_0/355-1660948-1917632?_encoding=UTF8&pd_rd_i=4065128447&pd_rd_r=85fc5fc0-6650-41b2-beaa-2a75e0e94bf5&pd_rd_w=6muXq&pd_rd_wg=hVxMm&pf_rd_p=cb2cef9d-b0a3-4b58-a575-45abfc5e07e8&pf_rd_r=5WKFBZPK0014FGC29YPR&psc=1&refRID=5WKFBZPK0014FGC29YPR)
- [Python のデコレータについて](https://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e)
- [typing.Callable](https://docs.python.org/3/library/typing.html#callable)
- [Python nonlocal Keyword](https://www.w3schools.com/python/ref_keyword_nonlocal.asp)
