class Node:
    def __init__(self):
        self.left = ''
        self.right = ''
        self.left_count = 0
        self.right_count = 0
        self.best = 0
        self.length = 0


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:

        n = len(s)
        tree = [Node() for _ in range(4 * n)]

        def build(node, l, r):
            if l == r:
                tree[node].left = s[l]
                tree[node].right = s[l]
                tree[node].left_count = 1
                tree[node].right_count = 1
                tree[node].best = 1
                tree[node].length = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node, node * 2, node * 2 + 1)

        def merge(parent, left_node, right_node):
            a = tree[left_node]
            b = tree[right_node]
            c = tree[parent]

            c.length = a.length + b.length
            c.left = a.left
            c.right = b.right

            c.left_count = a.left_count
            c.right_count = b.right_count

            if a.left == b.left and a.left_count == a.length:
                c.left_count += b.left_count

            if a.right == b.right and b.right_count == b.length:
                c.right_count += a.right_count

            c.best = max(a.best, b.best)

            if a.right == b.left:
                c.best = max(
                    c.best,
                    a.right_count + b.left_count
                )

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node].left = ch
                tree[node].right = ch
                tree[node].left_count = 1
                tree[node].right_count = 1
                tree[node].best = 1
                tree[node].length = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)

            merge(node, node * 2, node * 2 + 1)

        build(1, 0, n - 1)

        answer = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            answer.append(tree[1].best)

        return answer