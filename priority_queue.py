def get_parent(pq, index):
    """ returns the index of the parent or none if already at the root """
    if index == 0:
        return None
    else:
        return (index - 1) // 2


def get_left_child(pq, index):
    """returns index of the left child if it exists, else none"""
    left_child_index = 2 * index + 1
    if left_child_index < len(pq):
        return left_child_index
    else:
        return None


def get_right_child(pq, index):
    """returns index of the right child if it exists, else none"""
    right_child_index = 2 * index + 2
    if right_child_index < len(pq):
        return right_child_index
    else:
        return None


def compare(v1, v2, comparator=lambda x, y: x < y) -> bool:
    """Lambda is a concept with which we can bind a function to a variable. X and Y are the parameters of the function.
    So comparator(x,y) returns True if x is smaller than y, and False if x is not smaller than y.
    Replace x and y with the correct variable names. Peek at the test functions for more hints"""
    return comparator(v1, v2)


def get_smallest_child(pq, index):
    """ return the smallest child, check the test function to find out what to do when one of the children doesn't exist"""
    left_child = get_left_child(pq, index)
    right_child = get_right_child(pq, index)

    if left_child is None and right_child is None:
        return None
    elif left_child is None:
        return right_child
    elif right_child is None:
        return left_child
    elif compare(pq[left_child], pq[right_child]):
        return left_child
    else:
        return right_child


def top(pq):
    """ return the index of the top of the priority queue"""
    return pq[0]


def swap(pq, i, j):
    """ swap two elements in the priority queue"""
    pq[i], pq[j] = pq[j], pq[i]


def insert(pq, value):
    """ Add the value at the end of the priority queue and keep swapping until the invariant is preserved again """
    pq.append(value)
    index = len(pq) - 1

    while index > 0:
        parent_index = get_parent(pq, index)

        # If the parent is smaller, swap and update the index
        if not compare(pq[parent_index], pq[index]):
            break

        swap(pq, index, parent_index)
        index = parent_index


def pop(pq):
    """ Remove the top element and reorder the priority queue to maintain the min-heap property.
    Finally, return the removed top element. """
    if not pq:
        return None

    top_element = pq[0]
    pq[0] = pq[-1]
    pq.pop()

    n = len(pq)
    index = 0

    while True:
        left_child = get_left_child(pq, index)
        right_child = get_right_child(pq, index)

        # Find the index of the smallest child
        if left_child is not None and (right_child is None or compare(pq[left_child], pq[right_child])):
            smallest_child = left_child
        else:
            smallest_child = right_child

        # Exit if there are no more children or the heap property is preserved
        if smallest_child is None or compare(pq[index], pq[smallest_child]):
            break

        # Swap with the smallest child
        swap(pq, index, smallest_child)
        index = smallest_child

    return top_element


def from_list(lst):
    """ Convert a list into a priority queue, only use functions insert, top, or pop """
    pq = []
    for value in lst:
        insert(pq, value)
    return pq
