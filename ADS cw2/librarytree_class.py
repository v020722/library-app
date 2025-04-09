class LibraryTreeNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class LibraryTree:
    def __init__(self):
        self.root = None

    def insert(self, item):
        if not self.root:
            self.root = LibraryTreeNode(item)
        else:
            self._insert_recursive(self.root, item)

    def _insert_recursive(self, current_node, item):
        if item.title < current_node.item.title:
            if current_node.left is None:
                current_node.left = LibraryTreeNode(item)
            else:
                self._insert_recursive(current_node.left, item)
        elif item.title > current_node.item.title:
            if current_node.right is None:
                current_node.right = LibraryTreeNode(item)
            else:
                self._insert_recursive(current_node.right, item)

    def remove(self, title):
        self.root = self._remove_recursive(self.root, title)

    def _remove_recursive(self, current_node, title):
        if current_node is None:
            return None

        if title < current_node.item.title:
            current_node.left = self._remove_recursive(current_node.left, title)
        elif title > current_node.item.title:
            current_node.right = self._remove_recursive(current_node.right, title)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            else:
                successor = self._find_min(current_node.right)
                current_node.item = successor.item
                current_node.right = self._remove_recursive(current_node.right, successor.item.title)

        return current_node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, title):
        return self._search_recursive(self.root, title)

    def _search_recursive(self, current_node, title):
        if current_node is None:
            return None
        if title == current_node.item.title:
            return current_node.item
        elif title < current_node.item.title:
            return self._search_recursive(current_node.left, title)
        else:
            return self._search_recursive(current_node.right, title)

    def display_in_order(self):
        self._display_in_order_recursive(self.root)

    def _display_in_order_recursive(self, current_node):
        if current_node:
            self._display_in_order_recursive(current_node.left)
            print(current_node.item.title)
            self._display_in_order_recursive(current_node.right)
