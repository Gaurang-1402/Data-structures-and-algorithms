from helpful_data_structures.helpful_linked_binary_tree import LinkedBinaryTree
from helpful_data_structures.helpful_linked_binary_tree import printTree


def main():

#======================================================================================

    l_3_branch_left = LinkedBinaryTree.Node(5)
    l_3_branch_right = LinkedBinaryTree.Node(1)

    l_2_branch_left = LinkedBinaryTree.Node(9, l_3_branch_left, l_3_branch_right)

    l_1_branch_left = LinkedBinaryTree.Node(2, l_2_branch_left)

    r_2_branch_left = LinkedBinaryTree.Node(8)
    r_2_branch_right = LinkedBinaryTree.Node(4)
    r_1_branch_right = LinkedBinaryTree.Node(7, r_2_branch_left, r_2_branch_right)

    root_test_1 = LinkedBinaryTree.Node(3, l_1_branch_left, r_1_branch_right)

    # printTree(root_test_1)

    binary_tree_test_1 = LinkedBinaryTree(root_test_1)

#======================================================================================

    empty_binary_tree_test = LinkedBinaryTree()

#======================================================================================

    # THIS IS A BALANCED TREE

    # variable naming convention
    # t stands for tree whose output should give an answer true
    # l stands for left subtree right is for right subtree
    # the number is always the level
    # left or right is to indicate the node for a root

    t_l_2_branch_left = LinkedBinaryTree.Node(9)

    t_l_1_branch_left = LinkedBinaryTree.Node(2, t_l_2_branch_left)

    t_r_3_branch_left = LinkedBinaryTree.Node(5)
    t_r_3_branch_right = LinkedBinaryTree.Node(1)
    t_r_2_branch_left = LinkedBinaryTree.Node(8, t_r_3_branch_left, t_r_3_branch_right)
    t_r_2_branch_right = LinkedBinaryTree.Node(4)
    t_r_1_branch_right = LinkedBinaryTree.Node(7, t_r_2_branch_left, t_r_2_branch_right)


    root_test_2 = LinkedBinaryTree.Node(3, t_l_1_branch_left, t_r_1_branch_right)

    # printTree(root_test_2)



    binary_tree_test_2 = LinkedBinaryTree(root_test_2)

#======================================================================================
    # THIS IS A BINARY SEARCH TREE

    # Left side build
    leafOne = LinkedBinaryTree.Node(1)
    leafTwo = LinkedBinaryTree.Node(3)
    leafThree = LinkedBinaryTree.Node(5)
    innerTwo = LinkedBinaryTree.Node(4, leafTwo, leafThree)
    innerOne = LinkedBinaryTree.Node(2, leafOne, innerTwo)


    # Right side build
    leafFour = LinkedBinaryTree.Node(11)
    leafFive = LinkedBinaryTree.Node(15)
    innerThree = LinkedBinaryTree.Node(14, leafFour, leafFive)

    leafSix = LinkedBinaryTree.Node(75)
    innerFour = LinkedBinaryTree.Node(72, None, leafSix)

    innerFive = LinkedBinaryTree.Node(16, innerThree, innerFour)

    root_test_3 = LinkedBinaryTree.Node(6, innerOne, innerFive)

    binary_tree_test_3 = LinkedBinaryTree(root_test_3)


#===============================================

    # Juan's cases


    ### TEST CASE 002 ###
    l1 = LinkedBinaryTree.Node(1)
    l2 = LinkedBinaryTree.Node(9)
    p1_l1_l2 = LinkedBinaryTree.Node(3, l1, l2)

    l3 = LinkedBinaryTree.Node(7)
    p2_l3 = LinkedBinaryTree.Node(10, l3)
    l4 = LinkedBinaryTree.Node(12)
    p3_p2_l4 = LinkedBinaryTree.Node(11, p2_l3, l4)

    R = LinkedBinaryTree.Node(8, p1_l1_l2, p3_p2_l4)
    LBT = LinkedBinaryTree(R)


    ### TEST CASE 003 ###
    l1 = LinkedBinaryTree.Node(1)
    l2 = LinkedBinaryTree.Node(3)
    p1_l1_l2 = LinkedBinaryTree.Node(2, l1, l2)

    l3 = LinkedBinaryTree.Node(6)
    l4 = LinkedBinaryTree.Node(9)
    p2_l3_l4 = LinkedBinaryTree.Node(7, l3, l4)

    R = LinkedBinaryTree.Node(4, p1_l1_l2, p2_l3_l4)
    LBT = LinkedBinaryTree(R)


    ### TEST CASE 004 ###
    l1 = LinkedBinaryTree.Node(3)
    LBT = LinkedBinaryTree(l1)


    ### TEST CASE 005 ###
    l1 = LinkedBinaryTree.Node(2)
    l2 = LinkedBinaryTree.Node(4)
    R = LinkedBinaryTree.Node(1, l1, l2)


    ### TEST CASE 006 ###
    l1 = LinkedBinaryTree.Node(3)
    R = LinkedBinaryTree.Node(4, l1)
    LBT = LinkedBinaryTree(R)


    ### TEST CASE 007 ###
    l1 = LinkedBinaryTree.Node(3)
    R = LinkedBinaryTree.Node(1, l1)
    LBT = LinkedBinaryTree(R)


main()

#======================================================================================



