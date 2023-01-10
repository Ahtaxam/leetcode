def isSameTree(self, p,q) -> bool:
    if p == None or q == None:
        return p == q
    return (p.val == q.val) and self.isSameTree(p.left , q.left) and self.isSameTree(p.right , q.right)




# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false


# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false