class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        from typing import List
from collections import defaultdict

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = defaultdict(list)
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        last_seen = {}
        
        def dfs_reparent(u: int):
            char = s[u]
            prev = last_seen.get(char, -1)
            if prev != -1:
                new_parent[u] = prev
            last_seen[char] = u
            
            for v in adj[u]:
                dfs_reparent(v)
                
            if prev == -1:
                del last_seen[char]
            else:
                last_seen[char] = prev
                
        dfs_reparent(0)
        
        new_adj = defaultdict(list)
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        ans = [1] * n
        
        def dfs_size(u: int) -> int:
            size = 1
            for v in new_adj[u]:
                size += dfs_size(v)
            ans[u] = size
            return size
            
        dfs_size(0)
        return ans