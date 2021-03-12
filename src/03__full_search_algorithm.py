def input_num(description: str) -> int:
    while True:
        try:
            return int(input(description))
        except ValueError:
            print('Invalid input.')


def full_search_with_flag() -> None:
    N = input_num('Number: ')
    v = input_num('Value: ')
    a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

    exist = False
    for x in a:
        if x == v:
            exist = True

    print('result: {}'.format('Yes' if exist else 'No'))


def full_search_with_next() -> None:
    N = input_num('Number: ')
    v = input_num('Value: ')
    a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

    it = (True for x in a if x == v)
    exist = next(it, False)

    print('result: {}'.format('Yes' if exist else 'No'))


def full_search_with_index() -> None:
    def find(l: list, v: int) -> int:
        try:
            return l.index(v)
        except ValueError:
            return -1

    N = input_num('Number: ')
    v = input_num('Value: ')
    a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

    found_id = find(a, v)
    print('result: {}'.format(found_id))


def find_min_value() -> None:
    INF = 20_000_000

    N = input_num('Number: ')
    a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

    min_value = INF
    for x in a:
        if x < min_value:
            min_value = x

    print('Result: {}'.format(min_value))


def find_min_value_of_pair() -> None:
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


def find_min_value_of_pair() -> None:
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


def full_search_using_bits_for_subset_sum_problem() -> None:
    N = input_num('Number: ')
    W = input_num('Wa: ')
    a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

    exist = False
    for bit in range(1 << N):
        subset = [a[i] for i in range(N) if bit & 1 << i]
        if sum(subset) == W:
            exist = True

    print('result: {}'.format('Yes' if exist else 'No'))


def full_search_using_bits_for_subset_sum_problem_with_next() -> None:
    N = input_num('Number: ')
    W = input_num('Wa: ')
    a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

    def get_subset_sum(bit: int) -> int:
        subset = [a[i] for i in range(N) if bit & 1 << i]
        return sum(subset)

    it = (True for bit in range(1 << N) if get_subset_sum(bit) == W)
    exist = next(it, False)

    print('result: {}'.format('Yes' if exist else 'No'))


def exercise_3_2(arg):
    N = input_num('Number: ')
    v = input_num('Value: ')
    a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

    filtered = [x for x in a if x == v]
    print('result: {}'.format(len(filtered)))


def exercise_3_3() -> None:

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


def exercise_3_4() -> None:
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


def exercise_3_5() -> None:
    N = input_num('Number: ')
    a = [input_num('Array[{}]: '.format(i)) for i in range(N)]

    count = 0

    while True:
        even = [x / 2 for x in a if x % 2 == 0]
        if len(even) != N:
            break
        a = even
        count += 1
    print('result: {}'.format(count))


def exercise_3_6() -> None:
    from itertools import product

    N = input_num('Number N: ')
    K = input_num('Number K: ')

    count = 0

    for X, Y in product(range(K + 1), range(K + 1)):
        if X + Y >= N - K and X + Y <= N:
            count += 1

    print('result: {}'.format(count))


def exercise_3_7() -> None:
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
