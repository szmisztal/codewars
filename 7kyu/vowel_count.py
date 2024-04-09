"""Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces."""


def get_count(sentence):
    result = 0
    for i in sentence:
        if i in ["a", "e", "i", "o", "u"]:
            result += 1
    return result
