class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

def insert(root, item):
    if root is None:
        return Node(item)

    if item < root.val:
        root.left = insert(root.left, item)
    else:
        root.right = insert(root.right, item)

    return root

def preorder(root):
    if root is None:
        return ""

    return root.val + preorder(root.left) + preorder(root.right)

lines = []
while True:
    s = input().strip()
    if s == '*':
        break
    lines.append(s)

root = None
for line in reversed(lines):
    for ch in line:
        root = insert(root, ch)

print(preorder(root))