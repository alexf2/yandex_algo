def find_two_indexes(data, expected_sum):
    lookup = dict((v, i) for i, v in enumerate(data))

    for i, v in enumerate(data):
        partSum = expected_sum - v

        if partSum in lookup:
            index = lookup[partSum]
            if index != i:
                return i, index

    return None


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes(data, expected_sum))
