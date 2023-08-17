# avl-tree

---

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

# Setup

---

It is essential you follow the steps below to correctly run my project.

### Cloning

To clone my github repository, you can simply insert the following command into the terminal:
<br>

```
git clone <github-repository-url>
```

### Requirements

It is essential that you have all the required dependencies installed before running my project. The dependencies to be installed are contained within the `requirements.txt` file. You can install all the dependencies with the following terminal command:
<br>

```
pip install -r requirements.txt
```

### Main

To run my project, you have to run the main driver code located in `./src/main.py` or simply run the following command through a terminal:
<br>

```
python src/main.py
```

# Contribution

---

Steps are provided below if you would like to contribute to the project:

1. [**Fork**](https://github.com/DuckyShine004/avl-tree/fork) my repository- this will create a copy of my repository to your account.
2. Create your branch.
3. Commit changes to your branch and push those changes.
4. Open a [**Pull Request**](https://github.com/DuckyShine004/avl-tree/pulls).

# Contact

---

- Linkedin: https://www.linkedin.com/in/gallon-zhou-a3739b278/
