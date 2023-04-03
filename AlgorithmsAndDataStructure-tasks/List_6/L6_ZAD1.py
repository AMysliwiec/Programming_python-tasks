class TreeNode:
    def __init__(self, key, value='default', right_child=None, left_child=None, parent=None):
        self.key = key
        self.payload = [value, 0]
        self.rc = right_child
        self.lc = left_child
        self.parent = parent

    def has_rc(self):
        return self.rc

    def is_rc(self):
        return self.parent and (self.parent.rc == self)

    def has_lc(self):
        return self.lc

    def is_lc(self):
        return self.parent and (self.parent.lc == self)

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.rc or self.lc)

    def has_any_children(self):
        return self.rc or self.lc

    def has_both_children(self):
        return self.rc and self.lc

    def is_overload(self):
        return self.payload[1] > 0

    def splice_out(self):
        if self.is_leaf():
            if self.is_lc():
                self.parent.lc = None
            else:
                self.parent.rc = None
        elif self.has_any_children():
            if self.has_lc():
                if self.is_lc():
                    self.parent.lc = self.lc
            else:
                self.parent.rc = self.rc
                self.rc.parent = self.parent
        elif self is not None:
            if self.is_lc():
                self.parent.lc = self.rc
            else:
                self.parent.rc = self.rc
            self.rc.parent = self.parent

    def find_min(self):
        current = self
        while current.has_lc():
            current = current.lc
        return current

    def find_successor(self):
        successor = None
        if self.has_rc():
            successor = self.rc.find_min()
        else:
            if self.parent:
                if self.is_lc():
                    successor = self.parent
                else:
                    self.parent.rc = None
                    successor = self.parent.find_successor()
                    self.parent.rc = self
        return successor

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.lc = lc
        self.rc = rc
        if self.has_lc():
            self.lc.parent = self
        if self.has_rc():
            self.rc.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_lc():
                self._put(key, val, current_node.lc)
            else:
                current_node.lc = TreeNode(key, value=val, parent=current_node)
        elif key == current_node.key:  # nadpisanie klucza
            current_node.payload[0] = val
            current_node.payload[1] += 1
        else:
            if current_node.has_rc():
                self._put(key, val, current_node.rc)
            else:
                current_node.rc = TreeNode(key, value=val, parent=current_node)

    def __setitem__(self, key, val):
        self.put(key, val=val)

    def get(self, key):
        if self.root:
            res = self.find_node(key, self.root)
            if res:
                return res.payload[0]
            else:
                return None
        else:
            return None

    def get_count(self, key):
        if self.root:
            res = self.find_node(key, self.root)
            if res:
                return res.payload[1]
            else:
                return None
        else:
            return None

    def find_node(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self.find_node(key, current_node.lc)
        else:
            return self.find_node(key, current_node.rc)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.find_node(key, self.root):
            return True
        return False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self.find_node(key, self.root)
            if node_to_remove:
                if node_to_remove.is_overload():
                    node_to_remove.payload[1] -= 1
                else:
                    self.remove(node_to_remove)
                    self.size -= 1
            else:
                raise KeyError('Key not in the tree')
        elif self.size == 1 and self.root.key == key:
            if self.root.is_overload():
                self.root.payload[1] -= 1
            else:
                self.root = None
                self.size -= 1
        else:
            raise KeyError('Key not in the tree')

    def remove(self, current_node):
        if current_node.is_leaf():
            if current_node == current_node.parent.lc:
                current_node.parent.lc = None
            else:
                current_node.parent.rc = None
        elif current_node.has_both_children():
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.payload = successor.payload
        else:
            if current_node.has_lc():
                if current_node.is_lc():
                    current_node.lc.parent = current_node.parent
                    current_node.parent.lc = current_node.lc
                elif current_node.is_rc():
                    current_node.lc.parent = current_node.parent
                    current_node.parent.rc = current_node.lc
                else:
                    current_node.replace_node_data(current_node.lc.key, current_node.lc.payload,
                                                   current_node.lc.lc, current_node.lc.rc)
            else:
                if current_node.is_lc():
                    current_node.rc.parent = current_node.parent
                    current_node.parent.lc = current_node.rc
                elif current_node.is_rc():
                    current_node.rc.parent = current_node.parent
                    current_node.parent.rc = current_node.rc
                else:
                    current_node.replace_node_data(current_node.rc.key, current_node.rc.payload,
                                                   current_node.rc.lc, current_node.rc.rc)

    def __delitem__(self, key):
        self.delete(key)

    def show_tree(self, current_node, list_to_print=None, lvl=0):
        if list_to_print is None:
            list_to_print = []

        if current_node is not None:
            self.show_tree(current_node.rc, list_to_print, lvl + 1)
            text = "{} --- {}".format('     ' * lvl, current_node.key)
            list_to_print.append(text)
            self.show_tree(current_node.lc, list_to_print, lvl + 1)
            return list_to_print
        else:
            pass

    def print_tree(self):
        if self.root:
            list_to_print = self.show_tree(self.root)
            for line in list_to_print:
                print(line)
        else:
            raise NameError("There's no tree to show here yet")
