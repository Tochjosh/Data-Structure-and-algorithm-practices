def factorial(n):
    if n < 0:
        return f'Error! Number must be positive integer'
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def recur_factorial(n):
    if n < 0:
        return f'Error! Number must be positive integer'
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n - 1)


# for i in range(0, 11):
#     print(f"factorial of {i} is \t\t\t\t", factorial(i))
#
# for i in range(0, 11):
#     print(f"factorial of {i} is \t\t\t\t", recur_factorial(i))


# Your Previous code is preserved below: var cards = ['Jack', 8, 2, 6, 'King', 5,3, 'Queen'];
# Required Output = [2, 3, 5, 6, 8, 'Jack', 'Queen', 'King'] Q: Sort the array as per the rules of card
# game using generic method. Choose language of your choice. Sample output is attached.

def sort_cards(array):
    card_rank = {
        2: 0,
        3: 1,
        4: 2,
        5: 3,
        6: 4,
        7: 5,
        8: 6,
        9: 7,
        10: 8,
        "Jack": 9,
        "Queen": 10,
        "King": 11,
        "Ace": 12
    }
    card_code = [card_rank[card] for card in array]
    card_code.sort()
    return [k for k, v in card_rank.items() if v in card_code]


# print(sort_cards(['Jack', 8, 'Ace', 2, 6, 'King', 5, 3, 'Queen']))


def sort_card2(array):
    card_rank = dict(enumerate([2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", 'Ace']))
    card_code = [k for k, v in card_rank.items() if v in array]
    card_code.sort()
    return [v for k, v in card_rank.items() if k in card_code]


# print(sort_card2(['Jack', 8, 'Ace', 2, 6, 'King', 5, 3, 'Queen']))



# Given a sorted array and a number x, find the pair in array whose sum is closest to x
def sorte(arr, x):
    dist = x
    result = dict()
    for i in arr:
        for y in arr:
            diff = abs(x - (i + y))
            if diff < dist:
                dist = diff
                arranged = tuple(sorted([i, y]))
                result[arranged] = dist
    print(result)
    return list([k for k, v in result.items() if v == min([v for k, v in result.items()])][0])


print(sorte([2, 2, 4, 5, 6, 8], 15))
