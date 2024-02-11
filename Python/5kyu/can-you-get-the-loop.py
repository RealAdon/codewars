# You are given a node that is the beginning of a linked list. This list contains a dangling piece and a loop. Your objective is to determine the length of the loop.

# For example in the following picture the size of the dangling piece is 3 and the loop size is 12:

# Use the `next' attribute to get the following node
# node.next

# Notes:

#     do NOT mutate the nodes!
#     in some cases there may be only a loop, with no dangling piece

# Solution:

def loop_size(node):
    slow = node
    fast = node.next
    while fast != slow:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    size = 1
    fast = slow.next
    while fast != slow:
        fast = fast.next
        size += 1
    return size