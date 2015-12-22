from BinarySearchTreeDS.BinarySearchTree import BinarySearchTree

bst = BinarySearchTree()

bst.insert("Bill")
bst.insert("Timmy")
bst.insert("Alfred")
bst.insert("Johnny")
bst.insert("Jamal")


bst.traverseInOrder()

print (bst.getMax())
print(bst.getMin())