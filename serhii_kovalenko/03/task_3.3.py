# Implement custom_filter function, which will behave like the original Python filter() function.


# declaration of filter function
def custom_filter(function, sequence):
    """ This function returns an iterator, which will include only those elements from the iterated collection
        for which the function returns True.
        :param function: function with condition
        :param sequence: sequence of elements
        :type function: function
        :type sequence: list
        :return: array of elements after applying conditions to them
        :rtype: map(list) object
    """
    result_list = []
    for i in sequence:

        if function(i):

            result_list.append(i)

    return result_list


# declaration of condition
condition = lambda x: x > 100


# entering a value list
numbers_list = [10, 50, 101, 300]

result = custom_filter(condition, numbers_list)

print(result)
