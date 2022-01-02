def string_times(str, n):
    """
    Given a string and a non-negative int n, return a larger string that is n copies of the original string.

    string_times('Hi', 2) → 'HiHi'
    string_times('Hi', 3) → 'HiHiHi'
    string_times('Hi', 1) → 'Hi'
    """
    return


def front_times(str, n):
    """
    Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

    front_times('Chocolate', 2) → 'ChoCho'
    front_times('Chocolate', 3) → 'ChoChoCho'
    front_times('Abc', 3) → 'AbcAbcAbc'
    """
    return


def string_bits(str):
    """
    Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

    string_bits('Hello') → 'Hlo'
    string_bits('Hi') → 'H'
    string_bits('Heeololeo') → 'Hello'"""
    return


def string_splosion(str):
    """
    Given a non-empty string like "Code" return a string like "CCoCodCode".

    string_splosion('Code') → 'CCoCodCode'
    string_splosion('abc') → 'aababc'
    string_splosion('ab') → 'aab'"""
    return


def last2(str):
    """
    Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

    last2('hixxhi') → 1
    last2('xaxxaxaxx') → 1
    last2('axxxaaxx') → 2"""
    return


if __name__ == "__main__":
    from _check import check_problems

    string_times_cases = [
        (("Hi", 2), "HiHi"),
        (("Hi", 3), "HiHiHi"),
        (("Hi", 1), "Hi"),
        (("Hi", 0), ""),
        (("Hi", 5), "HiHiHiHiHi"),
        (("Oh Boy!", 2), "Oh Boy!Oh Boy!"),
        (("x", 4), "xxxx"),
        (("", 4), ""),
        (("code", 2), "codecode"),
        (("code", 3), "codecodecode"),
    ]

    front_times_cases = [
        (("Chocolate", 2), "ChoCho"),
        (("Chocolate", 3), "ChoChoCho"),
        (("Abc", 3), "AbcAbcAbc"),
        (("Ab", 4), "AbAbAbAb"),
        (("A", 4), "AAAA"),
        (("", 4), ""),
        (("Abc", 0), ""),
    ]

    string_bits_cases = [
        (("Hello",), "Hlo"),
        (("Hi",), "H"),
        (("Heeololeo",), "Hello"),
        (("HiHiHi",), "HHH"),
        (("",), ""),
        (("Greetings",), "Getns"),
        (("Chocoate",), "Coot"),
        (("pi",), "p"),
        (("Hello Kitten",), "HloKte"),
        (("hxaxpxpxy",), "happy"),
    ]

    string_splosion_cases = [
        (("Code",), "CCoCodCode"),
        (("abc",), "aababc"),
        (("ab",), "aab"),
        (("x",), "x"),
        (("fade",), "ffafadfade"),
        (("There",), "TThTheTherThere"),
        (("Kitten",), "KKiKitKittKitteKitten"),
        (("Bye",), "BByBye"),
        (("Good",), "GGoGooGood"),
        (("Bad",), "BBaBad"),
    ]

    last2_cases = [
        (("hixxhi",), 1),
        (("xaxxaxaxx",), 1),
        (("axxxaaxx",), 2),
        (("xxaxxaxxaxx",), 3),
        (("xaxaxaxx",), 0),
        (("xxxx",), 2),
        (("13121312",), 1),
        (("11212",), 1),
        (("13121311",), 0),
        (("1717171",), 2),
        (("hi",), 0),
        (("h",), 0),
        (("",), 0),
    ]

    input = [
        (string_times, string_times_cases),
        (front_times, front_times_cases),
        (string_bits, string_bits_cases),
        (string_splosion, string_splosion_cases),
        (last2, last2_cases),
    ]

    check_problems(input)
