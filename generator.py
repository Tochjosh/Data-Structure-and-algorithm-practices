
def chunker(iterable, size):
    """

    :param iterable: a given iterable
    :param size: amount of the data to be yielded in chunks
    :return: a given portion of the data
    """

    start = 0
    for i in range(iterable):
        if len(iterable[start:start + size]) >= size:
            yield iterable[start:start + size]
            start += size
        else:
            yield iterable[start:]
            break


def chunker(iterable, size):
    """
    does some as above but in another logic
    :param iterable: a given iterable
    :param size: amount of the data to be yielded in chunks
    :return: a given portion of the data
    """
    for i in range(0, len(iterable), size):
        yield iterable[i: i + size]
