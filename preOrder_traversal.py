def preorderTraversal(self, root):
    res = []
    self.traverse(root , res)
    return res
    
def traverse(self , root , res):
    if root:
        res.append(root.val)
        self.traverse(root.left , res)
        self.traverse(root.right , res)