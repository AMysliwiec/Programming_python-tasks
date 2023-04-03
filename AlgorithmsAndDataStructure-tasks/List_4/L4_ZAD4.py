class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __getitem__(self, item):
        return self.items[item]

    def __str__(self):
        return str(self.items)


def checking_HTML_correctness(filename):
    """
    The function is to validate the syntax of an HTML document.
    :param filename: name of the file to check
    :return: True if the file is syntactically valid, and False if it is not
    """
    file_obj = open(filename, 'r')
    text = file_obj.read()

    interesting_list = []
    checking_stack = Stack()

    while '>' in text:

        start = text.find("<") + len("<")
        end = text.find(">")
        end_comment = text.find("-->")
        substring = text[start:end]

        if substring[0:3] == "!--":
            text = text[0:start - 1] + text[end_comment + len("-->"):]
            continue

        if len(substring.split("<")) == 1:
            interesting_list.append(substring)
            text = text[0:start - 1] + text[end + 1:]

        else:
            start2 = substring.find("<") + len("<")
            subsubstring = substring[start2:end]
            interesting_list.append(subsubstring)
            text = text[0:start + len(substring.split("<")[0])] + text[end + 1:]

    for element in interesting_list:
        helping_list = element.split(" ")
        ele = helping_list[0]
        if ele in ['meta', 'link', 'img', '!DOCTYPE', 'br', 'hr', 'col', 'command', 'input', 'base', 'area']:
            continue
        if not checking_stack.isEmpty():
            if '/' + checking_stack[-1] == ele:
                checking_stack.pop()
            else:
                checking_stack.push(ele)
        else:
            checking_stack.push(ele)

    if checking_stack.isEmpty():
        return True
    return False


if __name__ == '__main__':
    print(checking_HTML_correctness("L4_ZAD4_sampleHTML_1.txt"))
    print(checking_HTML_correctness("L4_ZAD4_sampleHTML_2.txt"))
    print(checking_HTML_correctness("L4_ZAD4_sampleHTML_3.txt"))