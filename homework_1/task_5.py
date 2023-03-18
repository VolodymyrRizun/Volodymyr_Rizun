# Den has invited some friends. His list is:

# s = "Fred:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";

# Could you make a program that
#· makes this string uppercase
#· gives it sorted in alphabetical order by last name.
#When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.
#So the result of function meeting(s) will be:
#Examples:

#"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"

#It can happen that in two distinct families with the same family name two people have the same first name too.

def to_upper_and_sort(input : str) -> str:
    # names is a list of tuples with 2 elements: last name and first name 
    names = [(name.partition(':')[2], name.partition(':')[0]) for name in input.upper().split(';')]
    names.sort(key=lambda name: (name[0], name[1])) # sort by last name and then by first name
    return '(' + ')('.join([name[0] + ', ' + name[1] for name in names]) + ')' # merges to a single string


def run():
    input_1 = 'Fred:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill'
    output_1 = '(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)'
    assert to_upper_and_sort(input_1) == output_1


if __name__ == "__main__":
    run()