def collectApple(n , edges , hasApple):
    adj = {i:[] for i in range(n)}
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(node, parent):
        ans = 0
        for child in adj[node]:
            if child != parent:
                children = dfs(child, node)
                if children or hasApple[child]:
                    ans += children + 2
        return ans
    return dfs(0, -1)


n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]
print(collectApple(n, edges, hasApple))