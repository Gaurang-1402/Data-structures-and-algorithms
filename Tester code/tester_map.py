from helpful_data_structures.helpful_binary_search_tree_map import BinarySearchTreeMap
from helpful_data_structures.helpful_binary_search_tree_map import printBST


def main():
        ### TEST CASE 001 ###
    itemOne = BinarySearchTreeMap.Item(1, 'a')
    leafOne = BinarySearchTreeMap.Node(itemOne)

    itemTwo = BinarySearchTreeMap.Item(3, 'b')
    leafTwo = BinarySearchTreeMap.Node(itemTwo)

    itemThree = BinarySearchTreeMap.Item(5, 'c')
    leafThree = BinarySearchTreeMap.Node(itemThree)

    innerTwoItem = BinarySearchTreeMap.Item(4, 'd')
    innerTwo = BinarySearchTreeMap.Node(innerTwoItem)
    innerTwo.left = leafTwo
    innerTwo.right = leafThree

    innerOneItem = BinarySearchTreeMap.Item(2, 'e')
    innerOne = BinarySearchTreeMap.Node(innerOneItem)
    innerOne.left = leafOne
    innerOne.right = innerTwo

    itemFour = BinarySearchTreeMap.Item(11, 'f')
    leafFour = BinarySearchTreeMap.Node(itemFour)


    itemFive = BinarySearchTreeMap.Item(15, 'g')
    leafFive = BinarySearchTreeMap.Node(itemFive)

    innerItemThree = BinarySearchTreeMap.Item(14, 'h')
    innerThree = BinarySearchTreeMap.Node(innerItemThree)
    innerThree.left = leafFour
    innerThree.right = leafFive

    itemSix = BinarySearchTreeMap.Item(75, 'i')
    leafSix = BinarySearchTreeMap.Node(itemSix)

    innerItemFour = BinarySearchTreeMap.Item(72, 'j')
    innerFour = BinarySearchTreeMap.Node(innerItemFour)
    innerFour.right = leafSix

    innerItemFive = BinarySearchTreeMap.Item(16, 'k')
    innerFive = BinarySearchTreeMap.Node(innerItemFive)
    innerItemFive.left = innerThree
    innerItemFive.right = innerFour

    root1Item =BinarySearchTreeMap.Item(6, 'l')

    root1 = BinarySearchTreeMap.Node(root1Item)
    root1.left = innerOne
    root1.right = innerFive

    lbt = BinarySearchTreeMap()
    lbt.root = root1
    printBST(root1)

main()
