# Text Analyzer
#
# Features:
# - Calculate words quantity;
# - Extract text dictionary - unique words;
# - Find keywords - top 3 most frequent words;
# - Calculate frequency for each word - word quantity / all words quantity * 100.

text = 'This, is my favourite text. Let\'s try to analyze it. I love this text. I love Python'
exclude_symbol = [',', '.', '!', '?', '(', ')']
exclude_words = ['a', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could', 'and', 'or',
                 'if', 'he', 'she', 'it', 'this', 'my', 'i']


def clear_text(text):
    """ This function cleans text from characters, interjections, and pronouns
        :param text: text for clean
        :type text: str
        :return: list words with out characters, interjections, and pronouns
        :rtype: list
    """
    for i in exclude_symbol:

        text = text.replace(i, '')

    text = [i for i in text.lower().split(' ') if i not in exclude_words]

    return text


def words_quantity(text):
    """ This function counts the number of words
        :param text: list words
        :type text: list
        :return: word count
        :rtype: int
    """
    return len(text)


def unique_words(text):
    """ This function counts the number of unique words
        :param text: list words
        :type text: list
        :return: list words
        :rtype: list
    """
    return ', '.join([i for i in set(text)])


def sorted_dict(text):
    """ This function counts the number of occurrences of each word, sorts and gives the top 3
        :param text: list words
        :type text: list
        :return: top 3 common words
        :rtype: str
    """
    words_dict = {}
    sort_list = ''

    for i in text:

        words_dict[i] = words_dict.get(i, 0) + 1

    for k, v in sorted(words_dict.items(), key=lambda x: x[1], reverse=True)[:3]:

        sort_list += f'{k} - {v}, '

    return sort_list[:-2]


def frequency(text):
    """ This function counts the weight of each word inside the text as a percentage
        :param text: list words
        :type text: list
        :return: word and its weight in%
        :rtype: str
    """
    freq = {}
    freq_list = ''

    for i in text:

        freq[i] = int(text.count(i) / len(text) * 100)

    for k, v in freq.items():

        freq_list += f'{k} - {v}%, '

    return freq_list[:-2]


print(f'Our text: {text}')

# Overwrite text after cleaning
text = clear_text(text)

print(f'Words quantity: {words_quantity(text)}')
print(f'Text dictionary: {unique_words(text)}')
print(f'Top keywords: {sorted_dict(text)}')
print(f'Frequency: {frequency(text)}')



