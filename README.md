# avl-tree

My implementation of the infamous AVL tree data structure. In computer science, an AVL tree is a self-balancing binary search tree. In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property. Source: [Wikipedia](https://en.wikipedia.org/wiki/AVL_tree)
<br>
<br>
**Insertion Animation**:<br>
![](https://upload.wikimedia.org/wikipedia/commons/f/fd/AVL_Tree_Example.gif)

### Optimization

Currently, my implementation is not fully optimized- the remove method has to check if a node with the queried value exist in the binary tree using the contains method. If it does, then proceed to search for the node.
<br>
<br>
However, the remove method is fairly optimized. The only difference between the remove method for a normal BST and the remove method for an AVL tree, is that the AVL tree utilizes a height heuristic to determine the successor node.
