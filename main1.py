def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')


def _sort():
    lst1 = [1, 4, 6]
    lst2 = [11, 33, 22]
    lst = zip(lst2, lst1)
    sort_lst = [i for _, i in sorted(lst)]
    print(sort_lst)


def duplicate():
    A = ["cool", "lock", "cook"]
    n = len(A)
    res = []
    tmp = [[0 for i in range(26)] for j in range(n)]
    for i in range(n):
        for j in range(len(A[i])):
            tmp[i][ord(A[i][j]) - ord('a')] += 1
    for k in range(26):
        count = n
        for r in range(n):
            if tmp[r][k] < count:
                count = tmp[r][k]
        if count:
            res += count * chr(ord('a') + k)
    print(res)


def rom_to_arab():
    sub = {"IV": 2, "IX": 2, "XL": 20, "XC": 20, "CD": 200, "CM": 200}
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    string = 'XXVII'

    number = sum(values[char] for char in string)
    number -= sum(val for key, val in sub.items() if key in string)

    print(number)
