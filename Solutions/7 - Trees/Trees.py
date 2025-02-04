class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    # Define build_product_tree as a static method or a class method
    @staticmethod
    def build_product_tree():
        root = TreeNode('Electronics')
        laptop = TreeNode('Laptop')
        pc = TreeNode('Dell')
        root.add_child(laptop)
        root.add_child(pc)
        return root  # Return the root of the tree

# Call the build_product_tree method correctly
sol = TreeNode.build_product_tree()

# Print the tree structure (implementing a simple print function)
def print_tree(node, level=0):
    print(" " * level * 2 + node.data)
    for child in node.children:
        print_tree(child, level + 1)

print_tree(sol)
