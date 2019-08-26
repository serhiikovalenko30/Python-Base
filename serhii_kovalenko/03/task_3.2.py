# Implement custom_map function, which will behave like the original Python map() function.


# declaration of map function
def custom_map(function, sequence):
    """ This function applies the function passed as the first argument to each element passed as the second argument
        :param function: function to be applied to all elements of the sequence
        :param sequence: list of iterators to which the function should apply
        :type function: function
        :type sequence: list
        :return: an array of elements after applying the function to them
        :rtype: map(list) object
    """
    result_list = []

    for i in sequence:

        value = function(i)
        result_list.append(value)

    return result_list


# declaration of conversion function
conversion = lambda x: course * x


# entering a course and a value list
course = 24.15
numbers_list = [100, 300]

result_conversion_list = custom_map(conversion, numbers_list)

print(result_conversion_list)
