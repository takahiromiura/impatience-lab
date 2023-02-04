# Python チュートリアル: BMI・肥満度を計算しよう

Python をインストールして、初めて起動した時、どのような気持ちになりましたか？
私は混乱でした。
操作方法が分からなければ宝の持ち腐れですね。
他にも通じますが、何か目標があると学習が捗ります。
ここでは、簡単な練習問題を通して、Python の基本的な操作について学んでいきます。

まずは、BMI (Body Mass Index) の計算プログラムを作ってみましょう。
体重 $kg$、身長 $m$ に対し、BMI は次のように定義されます。

$$
\textrm{BMI} = kg / m^2
$$

日本肥満学会の出している[ガイドライン](http://www.jasso.or.jp/data/magazine/pdf/medicareguide2022_2.pdf)によると、肥満度は BMI によって次のように分類されます。

$$
\begin{aligned}
\textrm{Underweight}&:& BMI < 18.5 \\
\textrm{Normal} &:& 18.5 \le BMI < 25 \\
\textrm{Overweight} &:& 25 \le BMI
\end{aligned}
$$

体重・身長が与えられた場合に BMI と肥満度カテゴリーを返すプログラムを作成してみます。

## スクリプトの作成・実行

最初にスクリプトを作成します。
Python スクリプトの拡張子は `.py` です。
ここでは `bmi.py` というファイル名とします。
まだ何も書いてないスクリプトですが、スクリプトを実行してみましょう。
コマンドプロンプト（あるいはターミナル）で、作成ファイルがあるフォルダに移動して、以下のコマンドを実行します。

```bash
python3 bmi.py
```

> [!NOTE]
> 使用環境によって、`python3` を `python` に変えてください。
> コマンドの実行は Python が立ち上がっていない状態で行うことに注意してください。

このコマンドで、`bmi.py` に書かれているソースコードが Python によって実行されました。
もちろん、何も書いてないので何も起こりませんが、スクリプトを実行するという操作ができました。

では、機能を実装していきましょう。

コードを書いていく前に、何をすればよいか考えておくことをお勧めします。
この場合は、例えば

- BMI を計算する
- BMI から肥満度に分類する

TODO リストをコードに書いてみましょう。
Python ではコメントは前に `#` と記載します。
`#` の後に記載された行のコードはプログラム実行時に無視されます。
`bmi.py` に以下を追記します。

```python
# BMI を計算する
# BMI から肥満度に分類する
```

## 四則演算

私の身長・体重を元に BMI を計算してみましょう。

- 身長: 1.76 (m)
- 体重: 68 (kg)

基本的な Python の演算子は以下の通りです。

- `+`: 加算
- `-`: 減算
- `*`: 乗算
- `/`: 除算
  - `//` は整数を返します
- `**`: 累乗
- `%`: 剰余(mod)

```python
>>> 3 + 5
8
>>> 10 - 5 * 2
0
```

> [!NOTE]
> `>>>` という表記は、Python コンソール上で実行したことを表しています。
> コマンドをコピーする場合は、`>>>` や `...` を消して実行してください。

`()` でくくると、先に計算されます。

```python
>>> (10 - 5) * 2
10
```

では、BMI を計算してみましょう。

```python
>>> 68 / 1.76 ** 2
21.952479338842977
```

## 標準出力

上記のコードを `bmi.py` に記載します。

```python
# BMI を計算する
68 / 1.76 ** 2

# BMI から肥満度に分類する
```

スクリプトを実行してみましょう。

```bash
python3 bmi.py
```

何も出力されません。
コマンドプロンプトに結果を出力するには、`print` 関数を用います。

```python
# BMI を計算する
print(68 / 1.76 ** 2)

# BMI から肥満度に分類する
```

実行すると、結果がコマンドプロンプトに出力されます。

```bash
python3 bmi.py
21.952479338842977
```

## 変数

他でも使えるように結果を保存したいです。
次のように変数に値を代入します。

```python
>>> BMI = 68 / 1.76 ** 2
```

変数名をタイプすれば、中身を呼び出すことができます。

```python
>>> BMI
21.952479338842977
```

> [!NOTE]
> 変数は値を格納する「箱」と表現されることが多いですが、付箋のような「ラベル」と考えた方が良いです。
> この違いについては、後に説明します。

BMI の計算ができたので、BMI の値によって肥満度を返すロジックを組み込みたいです。
例えば、先の例では BMI は 21 なので、肥満度 Normal を返すようなロジックです。
つまり、数値に応じて文字列を返すことを行います。

## 文字列

Python で文字列をそのままタイプするとエラーが起きます（変数名として利用していない場合）。

```python
>>> EXAMPLE
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'EXAMPLE' is not defined
```

変数ではなく文字列を使用するには、`"` か `'` で文字列を囲みます。

```python
>>> "this is an example"
'this is an example'
>>> 'this is another example'
'this is another example'
```

## ブール値

Python では真偽値を `True`, `False` で表します。

```python
>>> True
True
>>> False
False
```

比較演算子はこの真偽値を返します。
基本的な比較演算子は以下のものがあります。

- `x == y`: `x` は `y` と等しい
- `x != y`: `x` は `y` と等しくない
- `x > y`: `x` は `y` より大きい
- `x >= y`: `x` は `y` より大きいか等しい
- `x < y`: `x` は `y` より小さい
- `x <= y`: `x` は `y` より小さいか等しい

```python
>>> 3 == 4
False
>>> 5 > 2
True
```

文字列では大文字・小文字は区別されます。
`>` などの大小関係は順番によって決まります。

```python
>>> 'abc' == 'abc'
True
>>> 'a' < 'b'
True
>>> 'abc' == 'ABC'
False
```

数値と文字列など、異なるものの大小は比較できません。

```python
>>> 3 == 'abc'
False
>>> 3 > 'abc'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'int' and 'str'
```

## 型

`1` や `2` という整数や `1.56` といった小数、`"japan"` のような文字列の分類を「型」といいます。
`1` や `2` は整数型 (`int`)、`1.56` は小数点型 (`float`) 、`"japan"` は文字列型 (`str`) です。
型のチェックは `type` 関数を用いることで判別できます。

```python
>>> type(1)
<class 'int'>
>>> type(1.56)
<class 'float'>
>>> type("japan")
<class 'str'>
```

### None

数値型 (`int, float` など) や文字列型とは異なり、`None` という特殊な型が存在します。
`None` を呼び出しても何も返ってきません。

```python
>>> None

```

`None` かどうかを確かめたい場合は、`==` ではなく `is` を使うことが推奨されています。

```python
>>> K = 10
>>> K is None
False
```

`None` でないことを確かめる場合は `is not` を使います。

```python
>>> K is not None
True
```

関数などにおいて、度々 `None` に出くわすため、覚えておいてください。

## 条件分岐

条件分岐は `if ~ else` で行います。
Python は他のプログラミング言語と異なり、インデントに意味があり、使える場面が限られます。
例えば、`3` はエラーになりませんが、その前に空白があるとエラーになります。

```python
>>> 3
3
>>>     3
  File "<stdin>", line 1
    3
    ^
IndentationError: unexpected indent
```

インデントは `if ~ else` などの場面で用います。
例えば、次のコードは、`<condition>` が真ならば `operation 1` が実行されます。
偽の場合は `operation 2` が実行されます。
`if <condition>`, `else` の後に `:` を使うことに注意してください。

```python
if <condition>:
    operation 1

else:
    operation 2
```

下のコードの場合、`A` は 2 より大きいので `1` が出力されます。

```python
>>> A = 3
>>> if A > 2:
...     print(1)
... else:
...     print(2)
... 
1
```

`if` 条件が真だった場合、それ以外の場合 (`else`) に実行するコードはインデントで区切ります。

```python
>>> B = 10
>>> if B < 2:
...     print(1)
... else:
...     print(2)
...     print(3)
... 
2
3
```

`else` は省略可能です。
その場合、条件式が真でない場合は無視されます。

```python
>>> if 3 < 2:
...     print(1)
...

```

条件分岐を増やす場合は、`elif` を使います。
例えば、`C > 10` かどうかを判定した後、`C < 0` なら別のコードを実行したい場合は次のようになります。

```python
>>> C = -5
>>> if C > 10:
...     print("C > 10")
... elif C < 0:
...     print("C < 0")
... else:
...     print("0 <= C <= 10")
...
C < 10
```

注意点として、条件分岐は上から評価され、条件が初めに真になったところで条件分岐は終了します。
細かい条件を最初に書かないと、意図しない挙動になります。

```python
>>> D = 15
>>> if D > 5:
...     print("D > 5")
... elif D > 10:
...     print("D > 10")
... else:
...     print("D <= 5")
...
D > 5
```

```python
>>> D = 15
>>> if D > 10:
...     print("D > 10")
... elif D > 5:
...     print("D > 5")
... else:
...     print("D <= 5")
...
D > 10
```

では、BMI に基づいて肥満度カテゴリーを出力するロジックを実装します。
`bmi.py` に以下のコードを追記します。

```python
# BMI を計算する
BMI = 68 / 1.76 ** 2
print(BMI)

# BMI から肥満度に分類する
if BMI > 25:
    CATEGORY = "Overweight"

elif BMI < 18.5:
    CATEGORY = "Underweight"

else:
    CATEGORY = "Normal"

print(CATEGORY)
```

実行すると、次の結果を得られます。

```bash
python3 bmi.py
21.952479338842977
Normal
```

## 関数

次に、以下の 3 パターンの BMI に対して肥満度カテゴリーを出力してみましょう。
新しいファイル（`bmi_func.py` とします）を作成します。

1. A さん: BMI = 30.5
2. B さん: BMI = 16.7
3. C さん: BMI = 23.4

```python
# BMI
BMI_A = 30.5
BMI_B = 16.7
BMI_C = 23.4

# 結果出力
print(BMI_A)
print(BMI_B)
print(BMI_C)
```

実行すると以下を得ます。

```bash
python3 bmi_func.py
30.5
16.7
23.4
```

各 BMI の肥満度カテゴリーを出力するために、同じロジックを実装するのは面倒です。
関数を作成することによって、使い回しすることができます。
BMI を入力すると、肥満度カテゴリーを出力する関数を作成します。

関数は `def` 構文を使用します。
関数で行うソースコードは、`if ~ else` の時と同様、インデントしたブロック内に記載します。

```python
def func_name(arg_name):
    return value
```

`func_name` は関数名、`arg_name` は引数名です。
`return` によって関数から値を出力します。

`arg_name` は省略可能です。

```python
>>> def get_one():
...     print("print 1")
...     return 1
...
```

`print` は関数内で実行されてもコマンドプロンプトに出力されます。
上で定義した関数は次のように実行します。
`()` をつけないと、関数を呼び出すだけになることに注意してください。

```python
>>> get_one()
print 1
1
>>> get_one
<function get_one at 0x7fe6f01de700>
```

`arg_name` を定義した場合、`()` に入れた値は `arg_name` という変数に代入されます。
以下の例では、`3` が `x` に代入されていることがわかります。

```python
>>> def add_two(x):
...     return x + 2
...
>>> add_two(3)
5
```

引数の数は複数にすることができます。
引数名は `,` で区切ります。

```python
>>> def sum_values(x, y):
...     return x + y
...
>>> sum_values(3, 5)
8
```

引数の入力の仕方は 2 種類あります。
値を入力しただけの場合、左から順番に値が代入されます (positional argument)。
先の関数を少し変更します。

```python
>>> def sum_values(x, y):
...     print("x:", x)
...     print("y:", y)
...     return x + y
...
```

```python
>>> sum_values(3, 5)
x: 3
y: 5
8
```

引数名を指定すると、対応する引数名に値が代入されます (keyword argument)。

```python
>>> sum_values(y = 3, x = 5)
x: 5
y: 3
8
```

positional argument は keyword argument の前にする必要があります。

```python
>>> sum_values(x = 3, 5)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
```

そのため、次もエラーになります。

```python
>>> sum_values(5, x = 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum_values() got multiple values for argument 'x'
```

これは、positional argument によって `x = 5` が代入されているにも関わらず、さらに `x = 3` を代入しているからです。

> [!NOTE] 
> 関数内で `return` を定義していない場合、`None` が出力されます。

`return` が実行されると、その後のコードは無視されます。

```python
>>> def check_return():
...     print("above")
...     return "return"
...     print("below")
...
check_return()
above
'return'
```

### ローカル変数

関数内で定義した変数は関数内でしか参照できません。
関数外で定義した変数は関数内でも参照できます。
こういった、変数の参照可能な範囲をスコープといいます。
また、関数内で定義した変数をローカル変数、関数外で定義した変数をグローバル変数といいます。
以下の例では、`K` という変数を関数内外で定義していますが、関数を実行しても関数外の変数には影響していません。

```python
>>> def define_K(c):
...     K = c + 5
...     return K
...
>>> K = 10
>>> K
10
>>> define_K(3)
8
>>> K
10
```

```python
>>> def call_global():
...     print(K)
...
>>> K = 5
>>> call_global()
5
```

一見ややこしく感じるかもしれませんが、これはとても役立ちます。
変数や関数を多く定義した場合、このような仕組みがないと、変数内の値が意図せず上書きされてしまう恐れがあります。
したがって、どの関数内でも変数名が被らないように覚えておく必要があります。
この仕組みによって、そのような心配をせずに関数の影響を最小限に留めておけるわけです。

> [!TIP]
> 一応、グローバル変数は関数内で呼び出すことができますが、おすすめしません。
> グローバル変数が変わった場合にどこが変化するかを追いきれなくなる可能性があるためです。

さて、`bmi_func.py` にカテゴリーを出力する関数を定義して、結果を出力しましょう。

```python
def classify_BMI(bmi):
    if bmi > 25:
        return "Overweight"

    elif bmi < 18.5:
        return "Underweight"
    
    else:
        return "Normal"

# 結果出力
print(BMI_A, classify_BMI(BMI_A))
print(BMI_B, classify_BMI(BMI_B))
print(BMI_C, classify_BMI(BMI_C))
```

`print` 関数は `,` で区切るとまとめて出力できます。

> [!TIP]
> 関数の名前は、`func1` などといった意味のないものではなく、分かりやすい名前にしましょう。

実行すると以下を得られます。

```bash
python3 bmi_func.py
30.5 Overweight
16.7 Underweight
23.4 Normal
```

ついでに、身長・体重が与えられた場合に、BMI を計算する関数も定義しましょう。

```python
>>> def calc_BMI(height, weight):
...     return weight / height ** 2
...
>>> calc_BMI(1.78, 68)
21.461936624163616
```

`bmi_func.py` にも追記してください。

## 辞書型

A、B、C さんの身長・体重はそれぞれ以下の通りです。

1. A さん: BMI = 30.5
   - 身長 = 1.64 m
   - 体重 = 82 kg
2. B さん: BMI = 16.7
   - 身長 = 1.83 m
   - 体重 = 56 kg
3. C さん: BMI = 23.4
   - 身長 = 1.60 m
   - 体重 = 60 kg

A さんの身長・体重を分けて変数として定義することもできますが、まとめた方がすっきりしそうです。
辞書型 (`dict`) というものは、このような用途に使えます。
Python では `{}` によって辞書型を定義します。
辞書型では、`key` と `value` をセットで登録する必要があります。
`key` は呼び出し用の名前で、`value` はその値です。
`{key: value}` で定義します。
`key` には数値型や文字列型などが使用できます。

```python
>>> {"apple": 1}
{'apple': 1}
```

複数の `key-value` をセットするときは、`,` で区切ります。

```python
>>> {"apple": 1, "lemon": 2}
{'apple': 1, 'lemon': 2}
```

`key` の値は一意である必要があることに注意してください。
後に定義されたものに上書きされます。

```python
>>> {"apple": 1, "apple": 2}
{'apple': 2}
```

定義した辞書型から値を呼び出すのは `dict_name[key]` で行えます。

```python
>>> fruits = {"apple": 1}
>>> fruits
{'apple': 1}
>>> fruits["apple"]
1
```

登録されていない `key` を与えるとエラーになります。

```python
>>> fruits["melon"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'melon'
```

`dict_name[key] = value` で新たに `key-value` を登録できます。
`key` がすでに存在している場合は上書きされます。

```python
>>> fruits["melon"] = 3
>>> fruits
{'apple': 1, 'melon': 3}
>>> fruits["apple"] = 2
>>> fruits
{'apple': 2, 'melon': 3}
```

A さん、B さん、C さんの身長・体重を辞書型を使って `bmi_func.py` 内に定義してみましょう。

```python
# 身長・体重
A = {"height": 1.64, "weight": 82}
B = {"height": 1.83, "weight": 56}
C = {"height": 1.60, "weight": 60}
```

以前定義した BMI の値を身長・体重から計算して置き換えましょう。

```python
# BMI
BMI_A = calc_BMI(A["height"], A["weight"])
BMI_B = calc_BMI(B["height"], B["weight"])
BMI_C = calc_BMI(C["height"], C["weight"])
```

実行すると以下を得ます。

```bash
python3 bmi_func.py
30.487804878048784 Overweight
16.72190868643435 Underweight
23.437499999999996 Normal
```

BMI の小数点が細かすぎるので、`round` 関数によって値を丸めます。
`round(value, precision)` とすると、`value` は小数点 `precision` 桁で丸められます。
`print` 関数部分を変更します。

```python
# 結果出力
print(round(BMI_A, 2), classify_BMI(BMI_A))
print(round(BMI_B, 2), classify_BMI(BMI_B))
print(round(BMI_C, 2), classify_BMI(BMI_C))
```

実行結果は以下の通りです。

```bash
python3 bmi_func.py
30.49 Overweight
16.72 Underweight
23.44 Normal
```
