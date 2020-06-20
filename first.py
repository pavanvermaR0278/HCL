
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def findPath(root, path, k):

    if root is None:
        return False

    path.append(root.key)

    if root.key == k:
        return True

    if ((root.left != None and findPath(root.left, path, k)) or (root.right != None and findPath(root.right, path, k))):
        return True

    path.pop()
    return False

def findLCA(root, n1, n2):
    path1 = []
    path2 = []

    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1
    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    print(path1,path2)
    # if i > 1:
    #     return path1[i-2],path1[i - 1]
    if i==len(path1) or i==len(path2):
        return path1[i-2]
    elif i > 1:
        return path1[i-2],path1[i - 1]
    else:
        return path1[i - 1]


## -----------------test case 1---------------------
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

#print("LCA(4, 5) = " , (findLCA(root, 4, 5)))
#print("LCA(4, 6) =" , (findLCA(root, 4, 6)))
#print("LCA(3, 4) = " , (findLCA(root, 3, 4)))
#print("LCA(2, 4) = " , (findLCA(root, 2, 4)))


## ---------------------------test case 2----------------------------
root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.right.left = Node(6)
#root.right.right = Node(7)

#print("LCA(1, 5) = " , (findLCA(root, 1, 5)))
#print("LCA(3, 6) =" , (findLCA(root, 3, 6)))
print("LCA(4, 6) = " , (findLCA(root, 4, 6)))
#print("LCA(2, 4) = " , (findLCA(root, 2, 4)))

