def longestPath(parent, s):
    adj = {i:[] for i in range(len(parent))}
    for i in range(len(parent)):
        if parent[i] != -1:
            adj[parent[i]].append(i)

    ans = 1
    def dfs(v):
        if not adj[v]: return 1
        res = 1
        for w in adj[v]:
            length_of_child = dfs(w)
            if s[v] != s[w]:
                ans = max(ans, length_of_child+res)
                res = max(res, length_of_child+1)
        return res
    dfs(0)
    return ans
        


parent =[-1,0,1]
s ="aab"
print(longestPath(parent, s))