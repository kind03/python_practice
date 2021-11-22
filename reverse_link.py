# -*- coding:utf-8 -*-
from typing import Optional


class ListNode:
    def __repr__(self):
        return str(self.val)

    def __str__(self):
        return str(self.val)

    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    # 返回ListNode
    def ReverseList(self, node):
        if node is None:
            return None
        nodes = [node]
        while node.next:
            node = node.next
            nodes.append(node)

        rev_node: ListNode = node
        assert nodes[len(nodes)-1] == rev_node
        for i in range(len(nodes)-2, -1, -1):
            node.next = nodes[i]
            node = nodes[i]

        nodes[0].next = None

        return rev_node


if __name__ == '__main__':
    a = ListNode(0)
    b = ListNode(1)
    c = ListNode(2)
    d = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    sol = Solution()
    sol.ReverseList(None)
