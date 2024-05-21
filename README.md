Author Username : OfirFoggel

AVLNode Class Documentation

Description

The AVLNode class represents a node in an AVL tree data structure. AVL trees are self -
balancing binary search trees, ensuring logarithmic time complexity of insertion, 
deletion, and search operations. Each AVLNode instance encapsulates a key-value pair 
along with pointers to its left and right children, its parent node, and attributes 
representing its height and size. This class provides a comprehensive set of methods for 
accessing, manipulating, and analyzing the attributes and relationships of AVL tree 
nodes.

Attributes

- key (int or None) : The key associated with the node. For virtual nodes, the key is
  None.
- value (any) : The value associated with the node.
- left (AVLNode or None) : Pointer to the left child node. None if the node is virtual .
- right (AVLNode or None) : Pointer to the right child node. None if the node is virtual .
- parent (AVLNode or None): Pointer to the parent node. None if the node is the root .
- height (int) : Height of the node in the AVL tree. -1 for virtual nodes .
- size (int) : Size of the subtree rooted at the node .

Methods
- Constructor (key, value): Initializes a new AVLNode instance with the specified key 
  and value.
- get_left() : Returns the left child node of the current node.
- get_right() : Returns the right child node of the current node .
- get_parent() : Returns the parent node of the current node .
- get_key() : Returns the key associated with the current node.
- get_value() : Returns the value associated with the current node.
- get_height() : Returns the height of the current node in the AVL tree .
- set_size() : Recalculates and sets the size attribute of the current node and its 
  ancestors.
- set_left(node) : Sets the left child node of the current node.
- set_right(node) : Sets the right child node of the current node.
- set_parent(node) : Sets the parent node of the current node.
- set_key(key) : Sets the key associated with the current node.
- bf() : Calculates and returns the balance factor of the current node.
- set_value(value) : Sets the value associated with the current node.
- set_height(h) : Sets the height of the current node.
- is_real_node() : Checks if the current node is a real node (not a virtual node).
- min(): Finds and returns the node with the minimum key in the subtree rooted at the 
  current node.
- successor() : Finds and returns the successor node of the current node in the AVL 
  tree .
- predecessor() : Finds and returns the predecessor node of the current node in the 
  AVL tree .
- subtree() : Extracts and returns the subtree rooted at the current node.
  Time Complexity Analysis
- Constructor (__init__): Assigning values and pointers in fixed number of operations
  in time complexity of O(1).
- Accessor Methods (get_left, get_right, get_parent, get_key, get_value, 
  get_height) : These methods require simple calculations in fixed time operation
  O(1).
- Setter Methods (set_size, set_left, set_right, set_parent, set_key, set_value, 
  set_height) : As the above mentioned methods, require only fixed number of 
  operation hence O(1).
- Balance Factor (bf) : Accessing two of its children height field and subtract them. 
  Hnece, O(1).
- Successor (successor), Predecessor (predecessor), Minimum (min) : This 
  methods traverse throuth thre tree. Since the tree height is upper bounded by log2 𝑛
  where n is the number of nodes in the tree , the number of iterations is also bounded 
  by the same bound and hence required O(log2 𝑛)
- Is Real Node (is_real_node) : Involves only one condion checking. Hence, O(1).
- Subtree (subtree) : Spliting node from its tree and creating new tree required fixed 
  amount of operations causing O(1) time complexity.

Remark

- The AVLNode class provides essential functionality for building and maintaining AVL 
  trees ensuring efficient insertion, deletion, and retrieval operations while 
  maintaining the balance property of AVL trees .
- This class serves as a foundational component in the implementation of AVL tree 
  data structures and can be extended or customized to suit specific requirements 
  and applications.

AVLTree Class Documentation

Description

The AVLTree class implements the ADT Dictionary using an AVL tree data structure. AVL 
trees are self-balancing binary search trees, ensuring logarithmic time complexity for 
insertion, deletion, and search operations. This class provides a comprehensive set of 
methods for accessing, manipulating, and analyzing the AVL tree, including insertion, 
deletion, search, rotation operations, and conversion to array.

Attributes

- root (AVLNode or None) : The root node of the AVL tree.
- size (int) : The number of elements in the AVL tree.
  Methods
- __init__() : Initializes a new AVLTree instance with an empty root and size.
- search(key) : Searches for a node in the AVL tree corresponding to the given key.
  Time Complexity : O(log n) Calls: None
- rotate_right(node) : Performs a right rotation at the given node, balancing the AVL 
  tree.
- rotate_left(node): Performs a left rotation at the given node, balancing the AVL tree.
- rotate_rightleft(node, predecessor) : Performs a right-left rotation at the given 
  node, balancing the AVL tree. 
- rotate_leftright(node, predecessor) : Performs a left-right rotation at the given 
  node, balancing the AVL tree.
- insertBST(key, val) : Inserts a node with the given key and value into the AVL tree 
  using binary search tree insertion.
- insert(key, val) : Inserts a node into the AVL tree using insertBST at first then
  rebalances if necessary according to the algorithm learned in class using the 
  different rotations according the balnce factors and heights differences.
- deleteBST(node) : Deletes a node from the AVL tree using binary search tree 
  deletion.
- delete(node) : Deletes a node from the AVL tree using the deleteBST function and 
  rebalances if necessary calling the different above mentioned rotations functions.
- avl_to_array() : Converts the AVL tree to a sorted array of (key, value) tuples.
- size() : Returns the number of items in the AVL tree.
- split(node) : Splits the AVL tree into two AVL trees at the specified node. Calls the 
  join methond in order to combine the different subtreees as we traverse to tree root.
- join(tree2, key, val) : Joins the current AVL tree with another AVL tree at the 
  specified key and value. require
- get_root() : Returns the root node of the AVL tree.
  Time Complexity Analysis
- Search (search) : O(log2 𝑛)
  Explanation : The search operation involves traversing the tree from the root to the 
  target node or reaching a leaf node if the target key is not found. Each step in the 
  traversal reduces the search space by half, resulting in logarithmic time complexity. 
  The time complexity is not affected by other functions in the class.
- Insertion (insert) : O(log2 𝑛)
  Explanation : The insertion operation first performs binary search tree insertion to 
  find the appropriate position for the new node in O(log2 𝑛). If rebalancing is 
  required, additional rotations may be performed to maintain the AVL tree's balance
  requiring O(1) operations following by traversing to the tree root in order to update 
  all ancestors height causing O(log2 𝑛) operations. The time complexity of insertion 
  is logarithmic due to the binary search tree insertion and potential rebalancing steps. 
- Deletion (delete) : O(log2 𝑛)
  Explanation : Deletion involves first locating the node to be deleted using binary 
  search tree deletion. If rebalancing is necessary, rotations are performed to restore 
  the AVL tree's balance. The time complexity is logarithmic due to the binary search 
  tree deletion O(log2 𝑛) and potential rebalancing steps. Since each rotation costs 
  O(1) operations and the number of iterations are bounded by the tree height sums 
  to O(log2 𝑛) as well. Hence, O(log2 𝑛) operations overall. 
- Rotation Operations : O(1)
  Explanation : Rotation operations involve rearranging the tree structure around a 
  pivot node to restore balance. These operations have a constant time complexity as 
  they only involve changing node pointers and updating heights. The time complexity
  is not affected by other functions in the class.
- Binary Search Tree Insertion (insertBST) : O(log2 𝑛)
  Explanation : Binary search tree insertion inserts a new node into the tree based on 
  the comparison of keys. The time complexity is logarithmic because each 
  comparison reduces the search space by half. Assigning operations causing fixed 
  amount of operations which don't impact the overall time complexity.
- Binary Search Tree Deletion (deleteBST) : O(log2 𝑛)
  Explanation : Binary search tree deletion removes a node from the tree while 
  maintaining the binary search tree property. The time complexity is logarithmic as it 
  involves traversing the tree to locate the node to be deleted and then restructuring 
  the tree if necessary. The algorithm requires traversing back to the root to ensure the 
  unique properties of the tree is maintained causing O(log2 𝑛) at the worst case. 
  Hence to overall time complexity is O(log2 𝑛).
- Conversion to Array (avl_to_array) : O(𝑛)
  Explanation : Converting the AVL tree to an array requires traversing all nodes in the 
  tree to retrieve their keys and values. The time complexity is linear with respect to 
  the number of nodes in the tree since using stack like properties to ensure only one 
  visit at node in the tree.
- Size (size) : O(1)
  Explanation : Retrieving the size of the AVL tree involves accessing the size attribute 
  of the class, which has constant time complexity. The time complexity is not 
  affected by other functions in the class.
- Split (split) : O(log2 𝑛)
  Explanation : Splitting the AVL tree into two parts involves locating the specified 
  node and detaching its left and right subtrees. The time complexity is logarithmic as 
  it requires traversing the tree to find the node. As we traverse to the tree root we're 
  using the join function. Hence, as we learned in class the most significant(as a result 
  of telescopic series) join is the last which cause at most O(log2 𝑛) maintaining the 
  overall time complexity to be O(log2 𝑛).
- Join (join) : O(log2 𝑛)
  Explanation : Joining two AVL trees involves inserting one tree into the other at a 
  specified key and value. The time complexity is logarithmic as it involves inserting 
  nodes into the tree causing at most O(log2 𝑛) as it first finds the node which 
  satisfies the condition that its height is smaller or equal to tree height. The insertion 
  that follows cause at most O(log2 𝑛) if it uses the insert function that been 
  discussed earlier and O(1) at the best case causing potentially triggering 
  rebalancing operations which sums to O(1) operations for rotations and 
  O(log2 𝑛) at the worst case, leading to overall O(log2 𝑛) time complexity. 

Remarks

- The AVLTree class offers efficient and balanced storage and retrieval of key-value 
  pairs.
- By maintaining the balance property of AVL trees, this class ensures optimal 
performance for various dictionary operations.
