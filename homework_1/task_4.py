# There is an array of numbers - arr [1, 3, 6, 2, 2, 0, 4, 5] 
# there is a number target = 5.
# Count the number of pairs in the array, the sum of which will give target

from typing import List

def number_of_pairs(nums : List[int], target : int) -> int:
    '''
    Time complexity will be O(n^2) anyway, so 
    here is the most simple and intuitive solution
    '''
    res = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                res += 1
    return res


def run():
    assert number_of_pairs([1, 5, 7, -1], 6) == 2
    assert number_of_pairs([1, 5, 7, -1, 5], 6) == 3
    assert number_of_pairs([1, 1, 1, 1], 2) == 6


if __name__ == "__main__":
    run()