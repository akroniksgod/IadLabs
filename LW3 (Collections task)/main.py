import random


def get_random_list() -> list:
    lower_bound = 0
    upper_bound = 100
    count = 5
    return random.sample(range(lower_bound, upper_bound), count)


def solve_first() -> None:
    random_list = get_random_list()
    print(random_list)
    print(list(reversed(random_list)))


def solve_second() -> None:
    random_first_list = get_random_list()
    random_second_list = get_random_list()

    length1 = len(random_first_list)
    length2 = len(random_second_list)

    if length1 != length2:
        return

    third_list = []
    for i in range(length1):
        is_odd_index = i % 2 > 0
        third_list.append(random_second_list[i] if is_odd_index else random_first_list[i])

    print(random_first_list)
    print(random_second_list)
    print(third_list)


def solve_third() -> None:
    types = ['int', 'float', 'str']
    lower_bound = 0
    upper_bound = 100
    length = 10
    lst = []
    for i in range(length):
        current_type = types[random.randint(0, len(types) - 1)]
        if current_type == 'int':
            lst.append(random.randint(lower_bound, upper_bound))
            continue

        if current_type == 'float':
            lst.append(random.uniform(lower_bound, upper_bound))
            continue

        if current_type == 'str':
            lst.append(str(random.randint(lower_bound, upper_bound)))

    print(lst)
    new_lst = []
    for i in lst:
        item = str(i) if type(i) != 'str' else i
        if item not in new_lst:
            new_lst.append(i)

    print(new_lst)


def get_keys_for_value(value, d: dict) -> list:
    keys = []
    for key, curr_value in d.items():
        if curr_value != value:
            continue

        keys.append(key)

    return keys


def get_random_dict() -> dict:
    d = {}
    count = 10
    lower_bound = 0
    upper_bound = 100

    for i in range(count):
        d = {**d, str(i): random.randint(lower_bound, upper_bound)}

    return d


def solve_fourth() -> None:
    d = get_random_dict()

    unique_values = set(d.values())

    lst = []
    for value in unique_values:
        this_tuple = (value, get_keys_for_value(value, d))
        lst.append(this_tuple)

    print(d)
    print(lst)


def get_key_by_value(value, dictionary: dict) -> str:
    for key, curr_value in dictionary.items():
        if curr_value == value:
            return key


def solve_fifth() -> None:
    dict1 = get_random_dict()
    dict2 = get_random_dict()
    print(dict1)
    print(dict2)
    values1 = set(dict1.values())
    values2 = set(dict2.values())

    values_intersection = values1.intersection(values2)

    print(values_intersection)
    dict3 = {}
    for item in values_intersection:
        k1 = get_key_by_value(item, dict1)
        dict3 = {**dict3, k1: item}
        k2 = get_key_by_value(item, dict2)
        dict3 = {**dict3, k2: item}

    print(dict3)


if __name__ == '__main__':
    solve_first()
    solve_second()
    solve_third()
    solve_fourth()
    solve_fifth()
