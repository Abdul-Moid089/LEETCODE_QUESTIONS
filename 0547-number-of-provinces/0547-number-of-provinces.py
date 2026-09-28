class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [0] * n
        count = 0

        for i in range(n):
            if vis[i] == 0:
                q = [i]
                vis[i] = 1
                count += 1

                while len(q) > 0:
                    x = q.pop(0)

                    for j in range(n):
                        if x != j and isConnected[x][j] == 1 and vis[j] == 0:
                            vis[j] = 1
                            q.append(j)

        return count