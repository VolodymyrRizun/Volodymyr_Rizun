# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits.

# If the digits can't be rearranged to form a bigger number, return -1

from itertools import permutations

def next_bigger(input_num : int) -> int:
    figures = list(str(input_num))
    perms = [''.join(i) for i in permutations(figures)]
    all_nums = [int(num) for num in filter(lambda x: x[0] != '0', perms)]
    for num in sorted(all_nums):
        if num > input_num:
            return num
    return -1


def run():
    assert next_bigger(12) == 21
    assert next_bigger(513)  ==  531 
    assert next_bigger(2017) == 2071
    assert next_bigger(9) == -1
    assert next_bigger(111) == -1
    assert next_bigger(531) == -1


if __name__ == "__main__":
    run()