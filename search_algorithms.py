def is_subscript(string, substring):
    """
    returns true if the substring exists in the string and false if otherwise
    """
    length = len(substring)
    for i in range(len(string)):
        if string[i: i + length] == substring:
            return True
    return False


def count_substring(substring, string):
    """
    returns the count of the substring in the string
    """
    length = len(substring)
    count = 0
    for i in range(len(string)):
        sub = string[i:i + length]
        if sub == substring:
            count += 1
    return count


def locate_first_substring(substring, string):
    """
    returns the index of the first occurrence of the substring in the string or -1 if it does not exist in the string
    """
    length = len(substring)
    for i in string:
        sub = string[i:i + length]
        if sub == substring:
            return i
    return -1


def locate_all_substring(substring, string):
    """
    returns the indices of all the occurrence of the substring in the string or -1 if it does not exist in the string
    """
    lis = []
    length = len(substring)
    for i in range(len(string)):
        sub = string[i:i + length]
        if sub == substring:
            lis.append(i)
    if lis:
        return lis
    else:
        return -1


def check_number_of_rotations(string, an_str):
    """
    :param string: a string of characters
    :param an_str: a rotated version of the string
    :return: number of rotations or -1 if there's no rotation
    """

    for i in range(len(string)):
        search = string[len(string) - i:] + string[:len(string) - i]
        print(search)
        if string == an_str:
            return 0
        else:
            if search == an_str:
                return i
    return -1


def word_count(list_of_words, word):
    word_counter = {}
    for i in list_of_words:
        if i == word:
            word_counter[word] = word_counter.get(word, 0) + 1 # uses the get method of a dict


def check_prime(num_lis):
    for num in num_lis:
        for n in range(2, int(num/2)):  # exclude 1 and the number and check other number in-between
            if num % n == 0:
                print("{} is not a prime number because {} is a factor of {}.".format(num, n, num))
                break

            if n == num - 1:  # searches until the end of the range
                print("{} is a prime number".format(num))


def is_prime(num):
    for n in range(2, int(num / 2)):
        if num % n == 0:
            return False

    return True
