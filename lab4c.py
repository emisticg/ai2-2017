def alpha_score(upper_letters):
    """Computers the alphanumeric sum of letters in a string.
    Prerequisite: upper_letters is composed entirely of capital letters.
    """
    return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))

alpha_score('ABC')  # => 6 = 1 ('A') + 2 ('B') + 3 ('C')

def two_best(words):
    words.sort(key=lambda word: alpha_score(filter(str.isupper, word)), reverse=True)
    return words[:2]

print (two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))
