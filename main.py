# Naive recursive implementation of Levenshtein distance in Python
#
# Levenshtein distance between two words is the minimum number of
# single-character edits (insertions, deletions, or substitutions)
# required to change one word into the other.
#
# This implementation is unfortunately an inefficient one, as it
# constantly recomputes the Levenshtein distance of
# the same substrings many times.
#
# Retrieved from <https://en.wikipedia.org/wiki/Levenshtein_distance>

def lev(a: str, b: str):
    if len(b) == 0:
        # If "b" is blank, the Lev. dist. is how long "a" is
        return len(a)
    elif len(a) == 0:
        # If "a" is blank, the Lev. dist. is how long "b" is
        return len(b)
    elif a[0] == b[0]:
        # If "a" and "b" begin with the same char, the Lev. dist.
        # is the Lev. dist. of the succeeding chars of each
        return lev(a[1:], b[1:])
    else:
        # Otherwise, it is 1 + minimum of the ff.:
        #  1. Lev. dist. of the succeeding chars of a vs. b
        #  2. Lev. dist. of a vs. the succeeding chars of b
        #  3. Lev. dist. of the succeeding chars of a vs. the same of b
        return 1+min(
            [
                lev(a[1:], b),
                lev(a, b[1:]),
                lev(a[1:], b[1:])
            ]
            )

def main():
    a = input("String A: ")
    b = input("String B: ")
    print(lev(a, b))
    return 0

if __name__=="__main__":
    main()
