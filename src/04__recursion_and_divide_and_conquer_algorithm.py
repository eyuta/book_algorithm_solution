def input_num(description: str) -> int:
    while True:
        try:
            return int(input(description))
        except ValueError:
            print('Invalid input.')


def code_4_1() -> None:
    def func(N: int) -> int:
        return 0 if N == 0 else N + func(N - 1)

    result = func(input_num('Number: '))
    print('result: {}'.format(result))


def code_4_2() -> None:
    def func(N: int) -> int:
        print('func({}) を呼び出しました'.format(N))
        if N == 0:
            return 0

        result = N + func(N - 1)
        print('{} までの和 = {}'.format(N, result))
        return result

    result = func(input_num('Number: '))
    print('result: {}'.format(result))


def code_4_4() -> None:
    def GCD(m: int, n: int) -> int:
        return m if n == 0 else GCD(n, m % n)

    GCD(15, 51)  # 3
    GCD(51, 15)  # 3


def code_4_6() -> None:
    def fibo(N: int) -> int:
        print('fibo({}) を呼び出しました'.format(N))

        if N == 0:
            return 0
        if N == 1:
            return 1

        result = fibo(N-1) + fibo(N-2)
        print('{} 項目 = {}'.format(N, result))
        return result

    print('result: {}'.format(fibo(6)))


def code_4_7() -> None:
    K = input_num('Number: ')
    F = [0, 1]

    for N in range(2, K + 1):
        F.append(F[N - 1] + F[N - 2])
        print('{} 項目: {}'.format(N, F[N]))

    print('result: {}'.format(F))


def code_4_8() -> None:
    K = input_num('Number: ')
    memo = [-1] * (K + 1)
    memo[0] = 0
    memo[1] = 1

    def fibo(N: int) -> int:
        if memo[N] != -1:
            return memo[N]

        memo[N] = fibo(N-1) + fibo(N-2)
        return memo[N]

    fibo(K)
    print('result: {}'.format(memo))


def code_4_6_with_cache() -> None:
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


def code_4_9() -> None:
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


def exercise_4_1() -> None:
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


def exercise_4_5() -> None:
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


def exercise_4_5_check_complexity() -> None:
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


def exercise_4_6() -> None:

    from typing import Callable

    def memorize(func: Callable) -> Callable:
        memo = {}

        def wrapper(*args, **kwargs):
            if (args[:2]) not in memo:
                memo[args[:2]] = func(*args, **kwargs)
            return memo[args[:2]]
        return wrapper

    @memorize
    def func(i: int, w: int, a: list, count: Callable) -> bool:
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
        print('N       : {}'.format(N))
        print('W       : {}'.format(W))
        print('result  : {}'.format('Yes' if func(N, W, a, count) else 'No'))
        print('count   : {}'.format(count() - 1))

    N = input_num('Number N: ')
    W = input_num('Number W: ')

    main(N, W)


exercise_4_6()
