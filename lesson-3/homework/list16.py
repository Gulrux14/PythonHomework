def count_odd_numbers(lst):
    return sum(1 for x in lst if x % 2 != 0)