class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            tree = BinaryTree(new_node)
            tree.left_child = self.left_child
            self.left_child = tree

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            tree = BinaryTree(new_node)
            tree.right_child = self.right_child
            self.right_child = tree

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, obj):
        self.key = obj

    def get_root_value(self):
        return self.key

    def __str__(self):
        return self.key


def parse_string(p_str, unknown):
    p_str = p_str.replace(" ", "")
    alist = []
    while len(p_str) > 0:
        if p_str[:3] in ['sin', 'cos', 'exp']:
            alist.append(p_str[:3])
            p_str = p_str[3:]
        elif p_str[:2] == 'ln':
            alist.append(p_str[:2])
            p_str = p_str[2:]
        elif p_str[0] in ['(', ')', '*', '+', '-', '/', '^', unknown]:
            alist.append(p_str[0])
            p_str = p_str[1:]
        elif p_str[0].isdigit():
            alist.append(p_str[0])
            p_str = p_str[1:]
    print(alist)
    return alist

#jakas proba
def build_parse_tree(fpexp: str, unknown='x'):
    fplist = parse_string(fpexp, unknown)
    stack = Stack()
    tree = BinaryTree('')
    stack.push(tree)
    current_tree = tree
    for i in fplist:
        if i == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['cos', 'sin', 'ln', 'exp', '+', '*', '^', '/', ')']:
            if i == '-':
                if current_tree.get_left_child() is None:  # zachowuje sie jak funckja
                    current_tree.set_root_value(i)
                    current_tree.insert_left('')
                    current_tree = current_tree.get_left_child()
                else:  # zachowuje sie jak operator
                    current_tree.set_root_value(i)
                    current_tree.insert_right('')
                    stack.push(current_tree)
                    current_tree = current_tree.get_right_child()
            elif i == unknown:
                current_tree.set_root_value(i)
                parent = stack.pop()
                current_tree = parent
            else:
                current_tree.set_root_value(int(i))
                parent = stack.pop()
                current_tree = parent
        elif i in ['+', '*', '/', '^']:
            current_tree.set_root_value(i)
            current_tree.insert_right('')
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i in ['cos', 'sin', 'ln', 'exp']:
            current_tree.set_root_value(i)
            current_tree.insert_left('')
            current_tree = current_tree.get_left_child()
        elif i == ')':
            current_tree = stack.pop()
        else:
            raise ValueError
    return tree

