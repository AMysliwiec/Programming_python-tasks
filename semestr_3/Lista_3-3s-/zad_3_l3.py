def counting_chars_without_ifs(filename):
    """
    Function counts the number of times each character appears in the text
    :param filename: .txt file
    :return: a dictionary with a number summary
    """
    file_ref = open(filename, 'r')
    text = file_ref.read()
    text = text.lower()

    div_text = []
    for char in text:
        div_text.append(char)

    accepted_chars = [chr(x) for x in range(33, 126)]

    what_chars_to_count = list(set(div_text) & set(accepted_chars))
    # what_chars_to_count.sort()

    char_count = {}

    for char in what_chars_to_count:
        how_many_chars = div_text.count(char)
        key = '{}'.format(char)
        char_count[key] = how_many_chars

    return char_count
