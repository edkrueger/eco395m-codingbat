def sleep_in(weekday, vacation):
    """
    The parameter weekday is True if it is a weekday, and the parameter vacation
    is True if we are on vacation. We sleep in if it is not a weekday or we're on
    vacation. Return True if we sleep in.
    
    sleep_in(False, False) → True
    sleep_in(True, False) → False
    sleep_in(False, True) → True
    """
    return


if __name__ == "__main__":
    from _check import check_problems

    sleep_in_cases = [
        ((False, False), True),
        ((True, False), False),
        ((False, True), True),
        ((True, True), True),
    ]

    input = [(sleep_in, sleep_in_cases)]

    check_problems(input)
