# アルゴリズムとデータ構造の第 3 章を Python で解いてみた

Python の勉強のため、[問題解決力を鍛える!アルゴリズムとデータ構造](https://www.amazon.co.jp/%E5%95%8F%E9%A1%8C%E8%A7%A3%E6%B1%BA%E5%8A%9B%E3%82%92%E9%8D%9B%E3%81%88%E3%82%8B-%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0%E3%81%A8%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0-KS%E6%83%85%E5%A0%B1%E7%A7%91%E5%AD%A6%E5%B0%82%E9%96%80%E6%9B%B8-%E5%A4%A7%E6%A7%BB-%E5%85%BC%E8%B3%87/dp/4065128447/ref=pd_lpo_14_img_0/355-1660948-1917632?_encoding=UTF8&pd_rd_i=4065128447&pd_rd_r=85fc5fc0-6650-41b2-beaa-2a75e0e94bf5&pd_rd_w=6muXq&pd_rd_wg=hVxMm&pf_rd_p=cb2cef9d-b0a3-4b58-a575-45abfc5e07e8&pf_rd_r=5WKFBZPK0014FGC29YPR&psc=1&refRID=5WKFBZPK0014FGC29YPR)を Python で解いてみました(原本は C++で書かれています)。
本記事における引用はすべて、上記の本から引用しております。

もしより良い書き方があれば教えていただけると嬉しいです。

[第 4 章「設計技法(2) : 再帰と分割統治法」はこちら](https://qiita.com/eyuta/items/22ec7447e309e6a35512)

## 環境

Python 3.8.5

## Code 全文

<https://github.com/eyuta/book_algorithm_solution/blob/main/src/03__full_search_algorithm.py>

## 本文

### 第 3 章 設計技法(1) : 全探索

#### 問題 1: 基本的な探索問題

> N 個の整数 $a_0, a_1, ..., a_{N-1}$ と整数値$v$が与えられます。 $a_i=v$ となるデータが存在するかどうかを判定してください.

C++の[cin](https://www.programiz.com/cpp-programming/library-function/iostream/cin)の代わりに、組み込み関数の[input](https://docs.python.org/ja/3/library/functions.html#input)を使用しました。

```py
def input_num(description: str) -> int:
    while True:
        try:
            return int(input(description))
        except ValueError:
            print('Invalid input.')
```

##### code 3.1 線形探索法

本文通り、フラグ`exist`を使用したコードです。

```py
N = input_num('Number: ')
v = input_num('Value: ')
a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

exist = False
for x in a:
    if x == v:
        exist = True

print('Yes' if exist else 'No')
```

フラグを用いずに記述する場合は、[next 関数](https://www.programiz.com/python-programming/methods/built-in/next)を使うときれいに書けそうです。
next 関数は、引数のイテレータから、次の値を取得します。

```py
N = input_num('Number: ')
v = input_num('Value: ')
a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

# x == vであれば True を返す iterator
iterator = (True for x in a if x == v)
# next で次の値を取得して返す。取り出せる値が存在しない場合、第二引数の値を返す
exist = next(iterator, False)

print('Yes' if exist else 'No')
```

##### code 3.2 特定の要素の存在する「添字」も取得する

本文では for loop を使用していますが、今回は list の[index method](https://www.programiz.com/python-programming/methods/list/index)を使用してみます。
index method は、要素が見つからない場合に`ValueError`を投げるため、try-except で捕まえる必要があります。

```py
def find(l: list, v: int) -> int:
    try:
        return l.index(v)
    except ValueError:
        return -1


N = input_num('Number: ')
v = input_num('Value: ')
a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

found_id = find(a, v)
print(found_id)
```

#### 問題 2: 最小値を求める

```py
INF = 20_000_000

N = input_num('Number: ')
a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

min_value = INF
for x in a:
    if x < min_value:
        min_value = x

print(min_value)
```

#### 問題 3: ペア和の K 以上の中での最小値

> $N$個の整数$a_0, a_1, ..., a_{N-1}$と, $N$個の整数$b_0, b_1, ..., b_{N-1}$が与えられます. 2 組の整数列からそれぞれ 1 個ずつ整数を選んで和をとります. その和として考えられる値のうち, 整数$K$以上の範囲内での最小値を求めてください.

```py
INF = 20_000_000

N = input_num('Number N: ')
K = input_num('Number K: ')
a = [input_num('Array a[{}]: '.format(i)) for i in range(N)]
b = [input_num('Array b[{}]: '.format(i)) for i in range(N)]

min_value = INF
for x in a:
    for y in b:
        if x + y < K:
            continue
        if x + y < min_value:
            min_value = x + y

print('Result: {}'.format(min_value))
```

また、[itertools.product](https://docs.python.org/ja/3/library/itertools.html#itertools.product)を使うことで、計算量は変わらないものの、ネストを浅くすることができました。

```py
from itertools import product

INF = 20_000_000

N = input_num('Number N: ')
K = input_num('Number K: ')
a = [input_num('Array a[{}]: '.format(i)) for i in range(N)]
b = [input_num('Array b[{}]: '.format(i)) for i in range(N)]

min_value = INF
for x, y in product(a, b):
    if x + y < K:
        continue
    if x + y < min_value:
        min_value = x + y

print('Result: {}'.format(min_value))
```

#### 問題 4: 部分和問題

> $N$個の正の整数$a_0, a_1, ..., a_{N-1}$と, 正の整数$W$が与えられます. $a_0, a_1, ..., a_{N-1}$の中から何個かの整数を選んで総和を$W$とすることができるかどうかを判定してください.

Python でも、C++と同様`<<`で数値を左シフトすることができます。
また、合計値は組み込み関数 sum を使用しています。

```py
N = input_num('Number: ')
W = input_num('Wa: ')
a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

exist = False
for bit in range(1 << N):
    subset = [a[i] for i in range(N) if bit & 1 << i]
    if sum(subset) == W:
        exist = True

print('result: {}'.format('Yes' if exist else 'No'))
```

next 関数を用いると、以下のようになります。
部分和を計算する処理を`get_subset_sum`に切り離しています。

```py
N = input_num('Number: ')
W = input_num('Wa: ')
a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

def get_subset_sum(bit: int) -> int:
    subset = [a[i] for i in range(N) if bit & 1 << i]
    return sum(subset)

it = (True for bit in range(1 << N) if get_subset_sum(bit) == W)
exist = next(it, False)

print('result: {}'.format('Yes' if exist else 'No'))
```

### 章末問題

章末問題は、解答をそのまま Python に落とし込むのではなく、自身で解いたものを載せています。
そのため、ところどころ解答との差異がありますがご了承ください。

#### 章末問題 3.2

> $N$個の整数$a_0, a_1, ..., a_{N-1}$のうち, 整数値$v$が何個含まれるかを求める$O(N)$のアルゴリズムを設計してください.

そのまま。

```py
N = input_num('Number: ')
v = input_num('Value: ')
a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

filtered = [x for x in a if x == v]
print('result: {}'.format(len(filtered)))
```

#### 章末問題 3.3

> $N(≧0)$個の相異なる整数$a_0, a_1, ..., a_{N-1}$が与えられます. このうち 2 番目に小さい値を求める$O(N)$のアルゴリズムを設計してください.

これもそのまま。

```py
INF = 20_000_000
N = input_num('Number: ')
a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

min_value = INF
second_min_value = INF
for x in a:
    if x < min_value:
        second_min_value = min_value
        min_value = x
    elif x < second_min_value:
        second_min_value = x

print('result: {}'.format(second_min_value))
```

#### 章末問題 3.4

> $N$個の整数$a_0, a_1, ..., a_{N-1}$が与えられます. この中から 2 つ選んで差をとります. その差の最大値を求める$O(N)$のアルゴリズムを設計してください.

自分で解けませんでした......。どうしても組み合わせ($O(N^2)$)になってしまいました。
答えを見て、自分の頭の固さに驚きました。

```py
INF = 20_000_000
N = input_num('Number: ')
a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

min_value = INF
max_value = -INF

if N == 1:
    raise ValueError('Invalid input.')

for x in a:
    if x < min_value:
        min_value = x
    if x > max_value:
        max_value = x

print('result max_value: {}'.format(max_value))
print('result min_value: {}'.format(min_value))
print('result diff     : {}'.format(max_value - min_value))
```

#### 章末問題 3.5

> $N$個の整数$a_0, a_1, ..., a_{N-1}$が与えられます. これらに対して「$N$個の整数がすべて偶数ならば 2 で割った値に置き換える」という操作を, 操作が行えなくなるまで繰り返します. 何回の操作を行うことになるかを求めるアルゴリズムを設計してください.

解答と比べると、while するタイミングを for loop を回すタイミングが異なるが、計算量的には同じと思われます。

```py
N = input_num('Number: ')
a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

count = 0

while True:
    even = [ x / 2 for x in a if x % 2 == 0]
    if len(even) != N:
        break
    a = even
    count += 1
print('result: {}'.format(count))
```

#### 章末問題 3.6

> 2 つの正の整数$K, N$が与えられます. $0≦X,Y,X≦K$を満たす整数$(X,Y,Z)$の組であって$X+Y+X=N$を満たすものが何通りあるかを求める$O(N^2)$のアルゴリズムを設計してください.

単純に解くと$O(N^3)$になるので、$O(N^2)$を満たすためにどうやるか悩みました。
これで難易度 ★★ なんですね......。

```py
from itertools import product

N = input_num('Number N: ')
K = input_num('Number K: ')

count = 0

for X, Y in product(range(K + 1), range(K + 1)):
    if X + Y >= N - K and X + Y <= N:
        count += 1

print('result: {}'.format(count))

```

解答とは異なりますが、以下より$N-K≦X+Y≦N$を満たす$X, Y$を探す形で解きました。

$$
X+Y+Z=N\\
Z=N-X-Y\\
0≦Z≦Kより\\
0≦N-X-Y≦K\\
-N≦-X-Y≦K-N\\
N-K≦X+Y≦N\\
$$

#### 章末問題 3.7

> 各桁の値が 1 以上 9 以下の数値のみである整数とみなせるような, 長さ$N$の文字列$S$が与えられます. この文字列の中で, 文字と文字の間のいくつかの場所に「+」を入れることができます. 1 つも入れなくてもかまいませんが, 「+」が連続してはいけません. このようにしてできるすべての文字列を数値とみなして, 総和を計算する$O(2^N)$のアルゴリズムを設計してください. たとえば$S="125"$のときは, $125, 1+25(=26), 12+5(=17), 1+2+5(=8)$の総和をとって 176 となります.

10 倍するタイミングが異なるものの、概ね解答通りの結果となりました。

```py
S = str(input_num('Number: '))
N = len(S)
between = N - 1

total = 0
for bit in range(1 << between):
    temp = 0
    for i in range(between):
        temp += int(S[i])
        if bit & 1 << i:
            total += temp
            temp = 0
        else:
            temp *= 10
    total += temp + int(S[-1])
print('result: {}'.format(total))
```

## 参考

- [問題解決力を鍛える!アルゴリズムとデータ構造](https://www.amazon.co.jp/%E5%95%8F%E9%A1%8C%E8%A7%A3%E6%B1%BA%E5%8A%9B%E3%82%92%E9%8D%9B%E3%81%88%E3%82%8B-%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0%E3%81%A8%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0-KS%E6%83%85%E5%A0%B1%E7%A7%91%E5%AD%A6%E5%B0%82%E9%96%80%E6%9B%B8-%E5%A4%A7%E6%A7%BB-%E5%85%BC%E8%B3%87/dp/4065128447/ref=pd_lpo_14_img_0/355-1660948-1917632?_encoding=UTF8&pd_rd_i=4065128447&pd_rd_r=85fc5fc0-6650-41b2-beaa-2a75e0e94bf5&pd_rd_w=6muXq&pd_rd_wg=hVxMm&pf_rd_p=cb2cef9d-b0a3-4b58-a575-45abfc5e07e8&pf_rd_r=5WKFBZPK0014FGC29YPR&psc=1&refRID=5WKFBZPK0014FGC29YPR)
- [Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax)
- [Asking the user for input until they give a valid response](https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response)
- [typing --- 型ヒントのサポート](https://docs.python.org/ja/3/library/typing.html#module-typing)
- [組み込み関数 input([prompt])](https://docs.python.org/ja/3/library/functions.html#input)
- [Using None](https://www.python.org/dev/peps/pep-0484/#using-none)
- [Python List Comprehension](https://www.programiz.com/python-programming/list-comprehension)
- [itertools.product](https://docs.python.org/ja/3/library/itertools.html#itertools.product)
