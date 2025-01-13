from src.data_structures.min_heap import MinHeap

def test_insert():
    heap = MinHeap(10)
    heap.insert(5)
    assert heap.getMin() == 5
    heap.insert(3) 
    assert heap.getMin() == 3
    heap.insert(1)
    assert heap.getMin() == 1
    heap.insert(10)
    assert heap.getMin() == 1
    assert heap.size == 4
    heap.insert(2)
    heap.insert(4)
    heap.insert(6)
    heap.insert(7)
    heap.insert(8)
    heap.insert(9)
    heap.print_heap()
    assert heap.size == heap.capacity
    try:
        heap.insert(11)
        assert False
    except ValueError:
        assert True

def test_remove_min():
    heap = MinHeap(10)
    heap.insert(3)
    heap.insert(5)
    heap.insert(1)
    assert heap.removeMin() == 1
    assert heap.getMin() == 3

def test_build_heap():
    heap = MinHeap(10)
    arr = [1,2,3,4,5,6,7,8,9,10]
    heap.buildHeap(arr)
    assert heap.getMin() == 1
    assert heap.size == heap.capacity
    heap.reset()
    assert heap.size == 0
    try:
        heap.buildHeap([1,2,3,4,5,6,7,8,9,10,11])
        assert False
    except ValueError:
        assert True
    heap.reset()
    heap.insert(7)
    try:
        heap.buildHeap([1,2,3,4,5,6,7,8,9,10])
        assert False
    except ValueError:
        assert True

def test_update():
    heap = MinHeap(10)
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    heap.insert(4)
    heap.insert(5)
    heap.insert(6)
    heap.insert(7)
    heap.update(0, 10)
    heap.print_heap()
    heap.delete(4)
    heap.print_heap()
    

