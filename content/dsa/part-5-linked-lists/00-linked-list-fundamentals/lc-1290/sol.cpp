// LC 1290. Convert Binary Number in a Linked List to Integer
// Single-pass walk with a running accumulator. Each node holds 0 or 1;
// shift the result left and OR in the current bit.
#pragma once

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

class Solution {
public:
    int getDecimalValue(ListNode* head) {
        int result = 0;
        ListNode* curr = head;
        while (curr != nullptr) {
            result = (result << 1) | curr->val;
            curr = curr->next;
        }
        return result;
    }
};
