from helpful_data_structures.helpful_queue import ArrayQueue

class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (left is not None):
                self.left.parent = self
            self.right = right
            if (right is not None):
                self.right.parent = self
            self.parent = None

    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)


    def count_nodes(self):
        def subtree_count(root):
            if (root is None):
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return left_count + right_count + 1

        return subtree_count(self.root)


    def sum(self):
        def subtree_sum(root):
            if(root is None):
                return 0
            else:
                left_sum = subtree_sum(root.left)
                right_sum = subtree_sum(root.right)
                return left_sum + right_sum + root.data

        return subtree_sum(self.root)


    def height(self):
        def subtree_height(root):
            if((root.left is None) and (root.right is None)):
                return 0
            elif(root.right is None): #left is not None
                left_height = subtree_height(root.left)
                return 1 + left_height
            elif(root.left is None): #right is not None
                right_height = subtree_height(root.right)
                return 1 + right_height
            else: #both subtrees are not None
                left_height = subtree_height(root.left)
                right_height = subtree_height(root.right)
                return 1 + max(left_height, right_height)

        if(self.is_empty()):
            raise Exception("Tree is empty")
        return subtree_height(self.root)


    def preorder(self):
        def subtree_preorder(root):
            if(root is None):
                pass
            else:
                yield root
                yield from subtree_preorder(root.left)
                yield from subtree_preorder(root.right)

        yield from subtree_preorder(self.root)


    def inorder(self):
        def subtree_inorder(root):
            if(root is None):
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)


    def postorder(self):
        def subtree_postorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_postorder(root.left)
                yield from subtree_postorder(root.right)
                yield root

        yield from subtree_postorder(self.root)


    def breadth_first(self):
        if(self.is_empty()):
            return
        bfs_queue = ArrayQueue()
        bfs_queue.enqueue(self.root)
        while(bfs_queue.is_empty() == False):
            curr_node = bfs_queue.dequeue()
            yield curr_node
            if(curr_node.left is not None):
                bfs_queue.enqueue(curr_node.left)
            if(curr_node.right is not None):
                bfs_queue.enqueue(curr_node.right)


    def __iter__(self):
        for node in self.breadth_first():
            yield node.data


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Extra: eval_exp_tree

def eval_exp_tree(exp_t):
    def subtree_eval_exp(root):
        if((root.left is None) and (root.right is None)):
            return root.data
        else:
            left_arg = subtree_eval_exp(root.left)
            right_arg = subtree_eval_exp(root.right)
            if (root.data == "+"):
                return left_arg + right_arg
            elif (root.data == "-"):
                return left_arg - right_arg
            if (root.data == "*"):
                return left_arg * right_arg
            if (root.data == "/"):
                return left_arg / right_arg

    return subtree_eval_exp(exp_t.root)

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.data)
        printTree(node.right, level + 1)


node_1 = LinkedBinaryTree.Node(1)
node_2 = LinkedBinaryTree.Node(2)
node_3 = LinkedBinaryTree.Node(3,node_1,node_2)
node_5 = LinkedBinaryTree.Node(5)
node_4 = LinkedBinaryTree.Node(4, node_3, node_5)
root = node_4
# printTree(root)

tree = LinkedBinaryTree(root)

# =============================================================================
# Uncomment this part to print the tree
# printTree(node_3)
#
# for each in tree:
#     print(each, end = " ")

# =============================================================================
# node_4 = Node(4)
# node_3 = Node(3)
# node_5 = Node(5)
# node_1 = Node(1)
# node_2 = Node(2)
#
# node_4.left = node_3
# node_4.right = node_5
# node_3.parent = node_4
# node_5.parnet = node_4
#
# node_3.left = node_1
# node_3.right = node_2
# node_1.parent = node_3
# node_2.parent = node_3
#
# =============================================================================


