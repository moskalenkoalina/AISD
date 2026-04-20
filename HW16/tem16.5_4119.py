n = int(input())

tree = {}

for _ in range(n):
    path = input().strip().split("\\")
    cur = tree

    for folder in path:
        if folder not in cur:
            cur[folder] = {}
        cur = cur[folder]

def dfs(node, depth):
    for name in sorted(node.keys()):
        print(" " * depth + name)
        dfs(node[name], depth + 1)

dfs(tree, 0)