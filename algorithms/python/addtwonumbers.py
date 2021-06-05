# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        current = result
        list1 = []
        list2 = []
        hage = 0
        while(l1.next != None):
            list1.append(l1.val)
            l1 = l1.next
        list1.append(l1.val)
        while(l2.next != None):
            list2.append(l2.val)
            l2 = l2.next
        list2.append(l2.val)
        hoge = list(map(sum, zip(list1, list2)))
        if len(list1) > len(list2):
            hoge.extend(list1[len(hoge):])
        elif len(list2) > len(list1):
            hoge.extend(list2[len(hoge):])
        print(hoge)
        for i in hoge:
            unko = i + hage
            current.next = ListNode(unko%10)
            hage = int(unko / 10)
            current = current.next
        if hage != 0:
            current.next = ListNode(hage)
        return result.next
