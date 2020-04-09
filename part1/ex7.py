"""
fill missing numbers
data ascending order
"""
def fill_list(data):
    i = 1
    length = len(data)
    while i < length:
        expected = data[i-1] + 1
        if data[i] != expected:
            data.insert(i, expected)
            length += 1
        i += 1

    return data


# def fill_list(data):
#     for i in range(1, len(data)):
#         expected = data[i - 1] + 1
#         if data[i] != expected:
#             data.insert(i, expected)
#         i += 1
#
#     return data


assert fill_list([-1, 2, 3, 5]) == [-1, 0, 1, 2, 3, 4, 5]
assert fill_list([]) == []
assert fill_list([-1, 2, 3, 5]) == [-1, 0, 1, 2, 3, 4, 5]