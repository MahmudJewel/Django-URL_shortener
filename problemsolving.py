def get_aspected_index(two_pair_values, target_value):
    # write your code here
    # print(len(two_pair_values))
    # for i in range(len(two_pair_values)):
    #     if two_pair_values[i][0]+two_pair_values[i][1] == target_value:
    #         return i
    ln = len(two_pair_values)-1
    while (ln >= 0):
        if two_pair_values[ln][0]+two_pair_values[ln][1] == target_value:
            return ln
        ln = ln-1
    return None


two_pair_values = [
    [1, 5],
    [9, -7],
    [0, 8],
    [6, 3],
    [4, 11],
    [14, 0],
    [8, 1],
    [4, 9],
]
target_value = 9
result = get_aspected_index(two_pair_values, target_value)
print(result)  # result will be shown 6
