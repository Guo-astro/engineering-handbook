// LC 2. Add Two Numbers
// Synchronized two-list walk with carry propagation. The dummy head
// lets every iteration append unconditionally; `return dummy.next`
// skips the sentinel.
#pragma once

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy;
        ListNode* tail = &dummy;
        int carry = 0;
        while (l1 != nullptr || l2 != nullptr || carry != 0) {
            int v1 = (l1 != nullptr) ? l1->val : 0;
            int v2 = (l2 != nullptr) ? l2->val : 0;
            int total = v1 + v2 + carry;
            carry = total / 10;
            tail->next = new ListNode(total % 10);
            tail = tail->next;
            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;
        }
        return dummy.next;
    }
};
