def solution(message, K):
    final_sol = ''
    split_word = message.split(' ')
    print(split_word)
    if len(message) <= K:
        return message
    else:
        for word in split_word:
            if len(final_sol) + len(word) > K:
                return final_sol.strip()
            else:
                final_sol += (' ' + word)


print(solution("why not", 100))


def solution(A):
    count = 0
    A.sort(reverse=True)
    half = sum(A) / 2
    for val in A:
        reduced = A.pop(0) / 2
        A.append(reduced)
        A.sort(reverse=True)
        count += 1
        if sum(A) <= half:
            return count


