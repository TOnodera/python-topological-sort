from linked_list import LinkedList


def test_データの挿入と削除が出来る():
    list = LinkedList()
    for i in range(10):
        list.insert(i, i*2)

    for i in range(10):
        assert list.index(i*2) == i
