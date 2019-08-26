# Implement a difference function, which subtracts one list from another and returns the result.


def difference_lists(main_list, list_a):
    """ This function remove all values from main_list, which are present in list a.
        :param main_list: main list from which the values will be deleted
        :param list_a: list with values to be removed from the main list
        :type main_list: list
        :type list_a: list
        :return: list with values that remained after deletion
        :rtype: list
    """
    diff_list = [i for i in set(main_list) if i not in list_a]

    return diff_list


last_a = [1, 2, 2, 2, 3, 4, 4, 4]
list_b = [1, 3, 3]

diff_list = difference_lists(last_a, list_b)

print(diff_list)
