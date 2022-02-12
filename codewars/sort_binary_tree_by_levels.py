# Sort binary tree by levels

from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    levels = []
    queue = deque([node])
    traverse_tree(levels, queue)
    return levels

def traverse_tree(levels, queue):
    if not queue:
        return 
    node = queue.popleft()
    if node is not None:
        levels.append(node.value) 
        queue.append(node.left)
        queue.append(node.right)
    traverse_tree(levels, queue)

print(tree_by_levels(None))
print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))
