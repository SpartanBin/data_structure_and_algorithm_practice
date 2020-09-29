class node:

    def __init__(self, body):
        self.name = body
        self.next = None

    def __str__(self):
        return str(self.name)


def producing_linked_list(body_list):
    for i, body in enumerate(body_list):
        if i == 0:
            a = node(body)
            head = a
        else:
            a.next = node(body)
            a = a.next
    return head


def reverse_linked_list(head):

    prior_node, cur_node, next_node = None, head, head.next

    while next_node is not None:
        cur_node.next = prior_node
        prior_node, cur_node, next_node = cur_node, next_node, next_node.next

    cur_node.next = prior_node

    return cur_node


# def swap_linked_list(head):
#
#     loc1, loc2 = head, head.next
#
#     head_swap = loc2
#
#     stop = 'no'
#     step = 1
#     while stop == 'no':
#
#         if step % 2 == 1:
#             loc2.next = loc1
#             try:
#                 loc1.next = loc3.next
#             except:
#                 pass
#
#         try:
#             loc1, loc2, loc3 = loc2, loc3, loc3.next
#         except:
#             stop = 'yes'
#
#         step = step + 1
#
#     return head_swap


def detect_cycle(head):
    slow = fast = head
    while slow is not None and fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
        return False


if __name__ == '__main__':

    head = producing_linked_list([1, 2, 3, 6, 8, 12, 13, 14, 16])

    # head_reverse = reverse_linked_list(head)
    # print(head_reverse.next.next.next.next.next)

    head_swap = swap_linked_list(head)
    print(head_swap)
    print(head_swap.next)
    print(head_swap.next.next)
    print(head_swap.next.next.next)
    print(head_swap.next.next.next.next)
    print(head_swap.next.next.next.next.next)
    print(head_swap.next.next.next.next.next.next)
    print(head_swap.next.next.next.next.next.next.next)
    print(head_swap.next.next.next.next.next.next.next.next)