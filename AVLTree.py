# username - ofirfoggel
# id1      - 315721332
# name1    - Ofir Foggel


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

	@type key: int or None
	@type value: any
	@param value: data of your node
	"""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0

    """returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""

    def get_left(self):
        # Check if the node has a key
        if self.key is None:
            return None  # If the node has no key, return None
        return self.left  # Otherwise, return the left child of the node

    """returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""

    def get_right(self):
        # Check if the node has a key
        if self.key is None:
            return None  # If the node has no key, return None
        return self.right  # Otherwise, return the right child of the node

    """returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""

    def get_parent(self):
        # Check if the node has a key
        if self.parent is None:
            return None  # If the node has no key, return None
        return self.parent  # Otherwise, return the parent of the node

    """returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""

    def get_key(self):
        return self.key

    """returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""

    def get_value(self):
        return self.value

    """returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""

    def get_height(self):
        if self.key is None:
            return -1  # If the node is invalid or has no key, return -1
            # Otherwise, calculate the height as 1 plus the maximum height of the left and right nodes
        return 1 + max(self.right.height, self.left.height)

    """
    Set the size attribute of the current node.

    @rtype: None
    @returns: None
    """

    def set_size(self):
        if self.key is None:
            self.size = 0  # If the node is virtual, set size to 0
        else:
            # Otherwise, set size to 1 plus the sizes of the right and left nodes
            self.size = 1 + self.right.size + self.left.size

    """sets left child

	@type node: AVLNode
	@param node: a node
	"""

    def set_left(self, node):
        self.left = node

    """sets right child

	@type node: AVLNode
	@param node: a node
	"""

    def set_right(self, node):
        self.right = node

    """sets parent

	@type node: AVLNode
	@param node: a node
	"""

    def set_parent(self, node):
        self.parent = node

    """sets key

	@type key: int or None
	@param key: key
	"""

    def set_key(self, key):
        self.key = key

    """returns the node balance factor

    	@rtype key: int 
    	@returns: The subtraction of the left child's height with the right child's height
    	"""

    def bf(self):
        return -self.right.get_height() + self.left.get_height()

    """sets value

	@type value: any
	@param value: data
	"""

    def set_value(self, value):
        self.value = value

    """sets the height of the node

	@type h: int
	@param h: the height
	"""

    def set_height(self, h):
        self.height = h

    """returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""

    def is_real_node(self):
        if self.key is None:
            return False  # If the node has no key, it's virtual node
        return True  # Otherwise, it's a real node

    """Find and returns the minimum value node in the subtree rooted at the current node.

    @rtype: AVLNode
    @returns: The node containing the minimum value, or None if the tree is empty.
    """

    def min(self):
        current = self  # Start from the current node
        while current.left.key is not None:  # Traverse left until reaching the leftmost node
            current = current.left
        return current  # Return the leftmost node, which contains the minimum value

    """Find and returns the successor of the current node in the tree.

    @rtype: AVLNode
    @returns: The successor node, or None if the node has no successor.
    """

    def successor(self):
        curr = self  # Start from the current node
        if curr.right.key is not None:  # If the right subtree is not empty
            return curr.right.min()  # Return the minimum node in the right subtree

        succ = curr.parent  # Otherwise, go up the tree to find the successor
        while succ.key is not None and curr == succ.right:  # Traverse up until finding the successor
            curr = succ
            succ = curr.parent
        return succ  # Return the successor node, or None if the node has no successor

    """Finds and returns the predecessor of the current node in the AVL tree.

    @rtype: AVLNode
    @returns: The predecessor node or None if no predecessor exists.
    """

    def predecessor(self):
        if self.left.key is None:
            # If the current node has no left child, it has no predecessor
            return self.left

        # Otherwise, follow the logic of finding the rightmost child in the left subtree
        tmp = self.left
        while tmp.right.key is not None:
            tmp = tmp.right
        return tmp

    """Extracts the subtree rooted at the current node.

    @rtype: AVLTree
    @returns: The subtree rooted at the current node.
    """

    def subtree(self):
        sub = AVLTree()  # Create a new AVLTree instance
        self.parent = None  # Remove the parent reference to isolate the subtree
        sub.root = self  # Set the current node as the root of the subtree
        sub.size = self.size  # Set the size of the subtree
        return sub


"""
A class implementing the ADT Dictionary, using an AVL tree.
"""


class AVLTree(object):
    """
	Constructor, you are allowed to add more fields.  

	"""

    def __init__(self):
        self.root = None
        self.size = 0

    # add your fields here

    """searches for a AVLNode in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: the AVLNode corresponding to key or None if key is not found.
	"""

    def search(self, key):
        current_node = self.root  # Start the search from the root node
        while current_node.key is not None:
            if key == current_node.key:  # If the key matches the current node's key
                return current_node  # Return the current node
            elif key < current_node.key:  # If the key is smaller, move to the left child
                current_node = current_node.left
            else:  # If the key is larger, move to the right child
                current_node = current_node.right
        return None  # Return None if the key is not found

    """
    Perform a right rotation at the given node.

    @param node: The node at which the right rotation is performed.
    @type node: AVLNode
    @returns: None
    """

    def rotate_right(self, node):
        if node.parent is None:  # If the node is the root
            # Perform the rotation
            self.root = node.left
            # Update parent references
            node.set_parent(node.left)
            node.set_left(node.parent.right)
            node.left.set_parent(node)
            node.parent.set_parent(None)
            # Update heights
            node.parent.set_right(node)
            node.parent.set_height(node.parent.get_height())
            node.set_height(node.get_height())
        else:
            if node.key > node.parent.key:  # If the node is a right child
                node.parent.set_right(node.left)
            else:  # If the node is a left child
                node.parent.set_left(node.left)
            # Update parent references
            node.left.set_parent(node.parent)
            node.set_parent(node.left)
            node.set_left(node.parent.right)
            node.left.set_parent(node)
            node.parent.set_right(node)
            # Update heights
            node.parent.set_height(node.parent.get_height())
            node.set_height(node.get_height())
            node.parent.parent.set_height(node.parent.parent.get_height())

    """Perform a left rotation at the given node.

    @param node: The node at which the left rotation is performed.
    @type node: AVLNode
    @returns: None
    """

    def rotate_left(self, node):
        if node.parent is None:  # If the node is the root
            # Perform the rotation
            self.root = node.right
            # Update parent references
            node.set_parent(node.right)
            node.set_right(node.parent.left)
            node.right.set_parent(node)
            node.parent.set_parent(None)
            # Update heights
            node.parent.set_left(node)
            node.parent.set_height(node.parent.get_height())
            node.set_height(node.get_height())
        else:
            if node.key > node.parent.key:  # If the node is a right child
                node.parent.set_right(node.right)
            else:  # If the node is a left child
                node.parent.set_left(node.right)
            # Update parent references
            node.right.set_parent(node.parent)
            node.set_parent(node.right)
            node.set_right(node.parent.left)
            node.right.set_parent(node)
            node.parent.set_left(node)
            # Update heights
            node.parent.set_height(node.parent.get_height())
            node.set_height(node.get_height())
            node.parent.parent.set_height(node.parent.parent.get_height())

    """Perform a right-left rotation at the given node.

    @param node: The node at which the right-left rotation is performed.
    @type node: AVLNode
    @param predecessor: The predecessor node.
    @type predecessor: AVLNode
    @returns: None
    """

    def rotate_rightleft(self, node, predecessor):
        # Perform the right rotation on the predecessor node
        self.rotate_right(predecessor)
        # Perform the left rotation on the current node
        self.rotate_left(node)

    """
    Perform a left-right rotation at the given node.

    @param node: The node at which the left-right rotation is performed.
    @type node: AVLNode
    @param predecessor: The predecessor node.
    @type predecessor: AVLNode
    @returns: None
    """

    def rotate_leftright(self, node, predecessor):
        # Perform the left rotation on the predecessor node
        self.rotate_left(predecessor)
        # Perform the right rotation on the current node
        self.rotate_right(node)

    """Insert a node with the given key and value into the AVL tree using binary search tree insertion.

    @param key: The key of the node to be inserted.
    @type key: Any
    @param val: The value of the node to be inserted.
    @type val: Any
    @rtype: AVLNode
    @returns: The parent node of the inserted node.
    """

    def insertBST(self, key, val):
        if self.root is None:  # If the tree is empty
            # Create a new node as the root
            self.size += 1
            self.root = AVLNode(key, val)
            # Initialize the root's children as virtual nodes
            self.root.set_right(AVLNode(None, None))
            self.root.right.set_parent(self.root)
            self.root.set_left(AVLNode(None, None))
            self.root.left.set_parent(self.root)
            # Set the height and size of the root
            self.root.set_height(0)
            self.root.size += 1
            return self.root.parent

        current_node = self.root
        # Find the appropriate position to insert the new node
        while current_node.key is not None:
            if key < current_node.key:
                if current_node.left.key is None:
                    # Insert the new node as the left child
                    current_node.set_left(AVLNode(key, val))
                    current_node.left.size += 1
                    current_node.left.set_parent(current_node)
                    current_node.left.set_right(AVLNode(None, None))  # Set right child as virtual
                    current_node.left.right.set_parent(current_node.left)
                    current_node.left.set_left(AVLNode(None, None))  # Set left child as virtual
                    current_node.left.left.set_parent(current_node.left)
                    current_node.left.set_height(0)  # Set height of the new node
                    break
                current_node = current_node.left
            else:
                if current_node.right.key is None:
                    # Insert the new node as the right child
                    current_node.set_right(AVLNode(key, val))
                    current_node.right.size += 1
                    current_node.right.set_parent(current_node)
                    current_node.right.set_right(AVLNode(None, None))  # Set right child as virtual
                    current_node.right.right.set_parent(current_node.right)
                    current_node.right.set_left(AVLNode(None, None))  # Set left child as virtual
                    current_node.right.left.set_parent(current_node.right)
                    current_node.right.set_height(0)  # Set height of the new node
                    break
                current_node = current_node.right

        self.size += 1
        return current_node

    """inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def insert(self, key, val):
        # Insert the node using binary search tree insertion
        parent_node = self.insertBST(key, val)

        # If the was empty before insertion, return 0 rebalancing operations
        if parent_node is None:
            return 0

        # Determine the predecessor node based on the insertion position
        if key < parent_node.key:
            predecessor = parent_node.left
        else:
            predecessor = parent_node.right

        rebalancing = 0  # Counter for the number of rotations performed

        # Balance the tree if necessary
        while parent_node is not None:
            balance_factor = parent_node.bf()
            # If the balance factor is within [-1, 1] and the height is correct, no rotation needed
            if abs(balance_factor) < 2 and parent_node.height == parent_node.get_height():
                parent_node.set_size()  # Update the size of the node
                break
            # If the balance factor is within [-1, 1] but the height is incorrect, adjust height and size
            elif abs(balance_factor) < 2 and parent_node.height != parent_node.get_height():
                parent_node.set_height(parent_node.get_height())
                parent_node.set_size()
                predecessor = parent_node
                parent_node = parent_node.parent
                rebalancing += 1
            else:
                # Perform rotations to balance the tree
                if balance_factor > 0 and predecessor.bf() > 0:
                    self.rotate_right(parent_node)
                    parent_node.set_height(parent_node.get_height())
                    predecessor.set_height(predecessor.get_height())
                    parent_node.set_size()
                    rebalancing += 1
                elif balance_factor < 0 and predecessor.bf() < 0:
                    self.rotate_left(parent_node)
                    parent_node.set_height(parent_node.get_height())
                    predecessor.set_height(predecessor.get_height())
                    parent_node.set_size()
                    rebalancing += 1
                elif balance_factor < 0 < predecessor.bf():
                    self.rotate_rightleft(parent_node, predecessor)
                    parent_node.set_height(parent_node.get_height())
                    predecessor.set_height(predecessor.get_height())
                    parent_node.set_size()
                    rebalancing += 2
                else:
                    self.rotate_leftright(parent_node, predecessor)
                    parent_node.set_height(parent_node.get_height())
                    predecessor.set_height(predecessor.get_height())
                    parent_node.set_size()
                    rebalancing += 2

        # Update heights of all nodes in the path
        while parent_node is not None:
            if parent_node.height != parent_node.get_height():
                parent_node.set_height(parent_node.get_height())
                parent_node.set_size()
                rebalancing += 1
            parent_node = parent_node.parent

        return rebalancing

    """Delete a node from the AVL tree using binary search tree deletion.

    @param node: The node to be deleted.
    @type node: AVLNode
    @rtype: AVLNode
    @returns: The parent node of the deleted node or None if the root is deleted.
    """

    def deleteBST(self, node):
        self.size -= 1
        if node.parent is not None:
            # If the node has no children
            if node.right.key is None and node.left.key is None:
                if node.key < node.parent.key:
                    parent = node.parent
                    node.parent.set_left(AVLNode(None, None))
                    node.set_parent(AVLNode(None, None))
                    return parent
                else:
                    parent = node.parent
                    node.parent.set_right(AVLNode(None, None))
                    node.set_parent(AVLNode(None, None))
                    return parent
            # If the node has one child
            elif node.right.key is None or node.left.key is None:
                if node.right.key is not None:
                    if node.key < node.parent.key:
                        parent = node.parent
                        node.parent.set_left(node.right)
                        node.right.set_parent(node.parent)
                        node.set_parent(AVLNode(None, None))
                        return parent
                    else:
                        parent = node.parent
                        node.parent.set_right(node.right)
                        node.right.set_parent(node.parent)
                        node.set_parent(AVLNode(None, None))
                        return parent
                else:
                    if node.key < node.parent.key:
                        parent = node.parent
                        node.parent.set_left(node.left)
                        node.left.set_parent(node.parent)
                        node.set_parent(AVLNode(None, None))
                        return parent
                    else:
                        parent = node.parent
                        node.parent.set_right(node.left)
                        node.left.set_parent(node.parent)
                        node.set_parent(AVLNode(None, None))
                        return parent
            # If the node has two children
            else:
                parent = node.parent
                successor = node.successor()
                # Update successor's parent and child pointers
                successor.right.set_parent(successor.parent)
                if successor.key < successor.parent.key:
                    successor.parent.set_left(successor.right)
                else:
                    successor.parent.set_right(successor.right)
                # Update parent's child pointer to point to the successor
                if node.key < parent.key:
                    parent.set_left(successor)
                    successor.set_parent(parent)
                    successor.set_left(node.left)
                    successor.set_right(node.right)
                    node.set_parent(AVLNode(None, None))
                    return parent
                else:
                    parent.set_right(successor)
                    successor.set_parent(parent)
                    successor.set_left(node.left)
                    successor.set_right(node.right)
                    node.set_parent(AVLNode(None, None))
                    return parent
        else:
            # If the root has no children
            if node.right.key is None and node.left.key is None:
                self.root = None
                return None
            # If the root has one child
            elif node.right.key is None or node.left.key is None:
                if node.right.key is not None:
                    self.root = node.right
                    node.right.set_parent(None)
                else:
                    self.root = node.left
                    node.left.set_parent(None)
                return None
            # If the root has two children
            else:
                successor = node.successor()
                parent = successor
                # Update successor's parent and child pointers
                successor.right.set_parent(successor.parent)
                if successor.key < successor.parent.key:
                    successor.parent.set_left(successor.right)
                else:
                    successor.parent.set_right(successor.right)
                # Set the root to be the successor
                self.root = successor
                successor.set_parent(None)
                successor.set_left(node.left)
                node.left.set_parent(successor)
                successor.set_right(node.right)
                node.right.set_parent(successor)
                return parent

    """deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def delete(self, node):
        # Delete the node using the regular deletion in BST Tree as appears in the `deleteBST` function
        parent_node = self.deleteBST(node)

        # If `deleteBST` returns None, the node wasn't found
        if parent_node is None or parent_node.key is None:
            return 0

        predecessor = AVLNode(None, None)  # Initialize predecessor
        rebalancing_steps = 0  # Initialize the number of rebalancing steps

        # Loop until the root is reached or balance factor is within bounds
        while parent_node is not None:
            balance_factor = parent_node.bf()  # Balance factor of the parent node
            if abs(balance_factor) < 2 and parent_node.height == parent_node.get_height():
                break  # Balance factor within bounds,and no change of height no need for rebalancing
            elif abs(balance_factor) < 2 and parent_node.height != parent_node.get_height():
                parent_node.set_height(parent_node.get_height())  # Update height calculation
                predecessor = parent_node
                parent_node = parent_node.parent
                rebalancing_steps += 1
            else:  # Single or double rotation needed
                # Determine rotation type based on balance factors
                if balance_factor > 0 and (predecessor.key is None or predecessor.bf() >= 0):
                    self.rotate_right(parent_node)
                    rebalancing_steps += 1  # Single right rotation, increment rebalancing steps by 1
                elif balance_factor < 0 and (predecessor.key is None or predecessor.bf() <= 0):
                    self.rotate_left(parent_node)
                    parent_node.set_height(parent_node.get_height())
                    rebalancing_steps += 1  # Single left rotation, increment rebalancing steps by 1
                elif balance_factor < 0 < (predecessor.key is None or predecessor.bf()):
                    self.rotate_rightleft(parent_node, predecessor)
                    parent_node.set_height(parent_node.get_height())
                    rebalancing_steps += 2  # Double rotation (right-left), increment rebalancing steps by 2
                else:  # balance_factor > 0 and predecessor.bf() < 0
                    self.rotate_leftright(parent_node, predecessor)
                    parent_node.set_height(parent_node.get_height())
                    rebalancing_steps += 2  # Double rotation (left-right), increment rebalancing steps by 2

                predecessor = parent_node
                parent_node = parent_node.parent

        return rebalancing_steps

    """returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""

    def avl_to_array(self):
        result = []  # Initialize list to store the result
        array_tmp = []  # Initialize temporary array for traversal
        current = self.root  # Start traversal from the root node

        # Loop until traversal is complete
        while True:
            if current:  # If the current node exists
                array_tmp.append(current)  # Append the current node to the temporary array
                current = current.left  # Move to the left child
            elif len(array_tmp) == 0:  # If the temporary array is empty, traversal is complete
                break
            else:  # If there are nodes in the temporary array
                current = array_tmp.pop()  # Pop a node from the temporary array
                if current.key is not None and current.value is not None:  # If the node is not None
                    result.append((current.key, current.value))  # Append the key-value pair to the result
                current = current.right  # Move to the right child

        return result  # Return the result list

    """returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""

    def size(self):
        return self.size

    """splits the dictionary at the i'th index

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""

    def split(self, node):
        if node.key is None:  # If the given node is None, return the original tree
            return self

        # Get subtrees T1 and T2 from left and right children of the given node
        T1 = node.left.subtree()
        T2 = node.right.subtree()

        parent = node.parent  # Get the parent of the given node

        # Iterate through the ancestors of the given node
        while parent is not None:
            if parent.key < node.key:  # If the parent's key is less than the node's key
                # Join T1 with the left subtree of the parent at the parent's key and value
                parent.left.subtree().join(T1, parent.key, parent.value)
                parent = parent.parent  # Move to the parent's parent
            else:
                # Join the right subtree of the parent with T2 at the parent's key and value
                T2.join(parent.right.subtree(), parent.key, parent.value)
                parent = parent.parent  # Move to the parent's parent

        # Reset the root of the original tree to an empty node make it unavailable to use
        self.root = AVLNode(None, None)

        # Return the list containing T1 and T2
        return [T1, T2]

    """joins self with key and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree2
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""

    def join(self, tree2, key, val):
        height_self = self.root.height  # Height of the current tree
        height_tree2 = tree2.root.height  # Height of the tree to be joined

        new_node = AVLNode(key, val)  # Create a new node with the given key and value

        # Case 1: Heights are equal and not -1
        if height_self == height_tree2 and height_self != -1 and height_tree2 != -1:
            # Set parent pointers and update root
            self.root.parent = new_node
            new_node.set_left(self.root)
            tree2.root.parent = new_node
            new_node.set_right(tree2.root)
            tree2.root = new_node
            self.root = new_node

            # Update sizes
            self.size += tree2.size + 1
            tree2.size = self.size

            # Perform rotations and update heights
            new_node.set_height(new_node.get_height())
            new_node.set_size()

            return 1  # the difference between the trees is 0,hence the cost is 1 since the insertion of new node

        # Case 2: One of the trees is empty
        elif height_self == -1 or height_tree2 == -1:
            # Both trees are empty
            if height_self == -1 and height_tree2 == -1:
                self.root.parent = new_node
                new_node.set_left(self.root)
                tree2.root.parent = new_node
                new_node.set_right(tree2.root)
                self.root = new_node
                tree2.root = new_node
                tree2.size = 1
                self.size = 1
                new_node.set_height(new_node.get_height())
                return 1  # creating of new tree with root new_node
            # If self tree is empty
            elif height_self == -1:
                tree2.insert(key, val)
                self.root = tree2.root
                self.size = tree2.size
                return height_tree2 + 1
            # If tree2 is empty
            else:
                self.insert(key, val)
                tree2.root = self.root
                tree2.size = self.size
                return height_self + 1

        # Case 3: Heights are different
        elif height_self > height_tree2:
            node = self.root
            while node.height > height_tree2:  # finding the node in which its height is <= tree2 height
                node = node.right
            new_node.set_left(node)
            new_node.set_parent(node.parent)
            new_node.parent.set_right(new_node)
            new_node.left.set_parent(new_node)
            new_node.set_right(tree2.root)
            tree2.root.set_parent(new_node)
            self.size += tree2.size + 1
            tree2.size = self.size
            tree2.root = self.root
            new_node.set_height(new_node.get_height())
            new_node.set_size()
        else:
            node = tree2.root
            while node.height > height_self:  # finding the node in which its height is <= self height
                node = node.left
            new_node.set_right(node)
            new_node.set_parent(node.parent)
            new_node.parent.set_left(new_node)
            new_node.right.set_parent(new_node)
            new_node.set_left(self.root)
            self.root.set_parent(new_node)
            self.size += tree2.size + 1
            tree2.size = self.size
            self.root = tree2.root
            new_node.set_height(new_node.get_height())
            new_node.set_size()

        # Rebalance the tree as conducted at the insertion algorithm
        parent_node = new_node.parent
        while parent_node is not None:
            balance_factor = parent_node.bf()
            if abs(balance_factor) < 2 and parent_node.height == parent_node.get_height():
                parent_node.set_size()
                break
            elif abs(balance_factor) < 2 and parent_node.height != parent_node.get_height():
                parent_node.set_height(parent_node.get_height())
                parent_node.set_size()
                new_node = parent_node
                parent_node = parent_node.parent
            else:
                if parent_node.bf() > 0 and new_node.bf() > 0:
                    self.rotate_right(parent_node)
                    parent_node.set_height(parent_node.get_height())
                    new_node.set_height(new_node.get_height())
                    parent_node.set_size()
                    break
                elif parent_node.bf() < 0 and new_node.bf() < 0:
                    self.rotate_left(parent_node)
                    parent_node.set_height(parent_node.get_height())
                    new_node.set_height(new_node.get_height())
                    parent_node.set_size()
                    break
                elif parent_node.bf() < 0 < new_node.bf():
                    self.rotate_rightleft(parent_node, new_node)
                    parent_node.set_height(parent_node.get_height())
                    new_node.set_height(new_node.get_height())
                    parent_node.set_size()
                    break
                else:
                    self.rotate_leftright(parent_node, new_node)
                    parent_node.set_height(parent_node.get_height())
                    new_node.set_height(new_node.get_height())
                    parent_node.set_size()
                    break

        # Update heights
        while parent_node is not None:
            parent_node.set_height(parent_node.get_height())
            parent_node.set_size()
            parent_node = parent_node.parent

        # Update root of the resulting tree
        if self.root.height > tree2.root.height:
            tree2.root = self.root
        else:
            self.root = tree2.root

        return abs(height_self - height_tree2) + 1

    """returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""

    def get_root(self):
        return self.root
