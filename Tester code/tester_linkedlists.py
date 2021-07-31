from helpful_data_structures.helpful_doubly_linked_list import DoublyLinkedList

def main():
    srt_lnk_lst1 = DoublyLinkedList()
    srt_lnk_lst1.add_last(1)
    srt_lnk_lst1.add_last(3)
    srt_lnk_lst1.add_last(5)
    srt_lnk_lst1.add_last(6)
    srt_lnk_lst1.add_last(8)
    print(srt_lnk_lst1)


    srt_lnk_lst2 = DoublyLinkedList()

    srt_lnk_lst2.add_last(2)
    srt_lnk_lst2.add_last(3)
    srt_lnk_lst2.add_last(5)
    srt_lnk_lst2.add_last(10)
    srt_lnk_lst2.add_last(15)
    srt_lnk_lst2.add_last(18)
    print(srt_lnk_lst2)

main()
