# In this task you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

from typing import List

def filter_list(input : List) -> List:
    return list(filter(lambda x: isinstance(x, int), input)
)


def run():
    assert filter_list([1, 2, 'a', 'b']) == [1, 2] 
    assert filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15] 
    assert filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123]


if __name__ == "__main__":
    run()