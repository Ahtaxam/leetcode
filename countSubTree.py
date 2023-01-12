def countSubTrees(self, n: int, edges, labels: str):
    gr = [[] for _ in range(n)]
    for a, b in edges:
        gr[a].append(b)
        gr[b].append(a)
    ans = [0] * n
    def DFS(node: int, parent: int):
        returns = Counter([labels[node]])
        for child in gr[node]:
            if child != parent:
                returns += DFS(child, node)
        ans[node] = returns[labels[node]]
        return returns
    DFS(0, -1)
    return ans


n = 5
edges = [[0,1],[0,2],[1,3],[0,4]]
labels = "aabab"
countSubTrees(n , edges , labels)