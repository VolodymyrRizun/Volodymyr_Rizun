# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
# The input will be a non-negative integer.

def digital_root(num : int) -> int:
    if num < 10:
        return num
    return digital_root(num % 10 + digital_root(num // 10))


def run():
    assert digital_root(16) == 7
    assert digital_root(942) == 6
    assert digital_root(132189) == 6
    assert digital_root(493193) == 2


if __name__ == "__main__":
    run()