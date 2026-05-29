// LC 21. Merge Two Sorted Lists
struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    explicit ListNode(int v) : val(v), next(nullptr) {}
    ListNode(int v, ListNode* n) : val(v), next(n) {}
};

class Solution {
public:
    // Iterative dummy + tail-pointer merge. `<=` keeps l1 ahead of l2 on tie.
    // O(n + m) time, O(1) auxiliary (the dummy lives on the stack).
    ListNode* mergeTwoListsIterative(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* tail = &dummy;
        while (l1 != nullptr && l2 != nullptr) {
            if (l1->val <= l2->val) {
                tail->next = l1;
                l1 = l1->next;
            } else {
                tail->next = l2;
                l2 = l2->next;
            }
            tail = tail->next;
        }
        tail->next = (l1 != nullptr) ? l1 : l2;
        return dummy.next;
    }

    // Textbook recursive form. O(n + m) call-stack frames; prefer iterative.
    ListNode* mergeTwoListsRecursive(ListNode* l1, ListNode* l2) {
        if (l1 == nullptr) return l2;
        if (l2 == nullptr) return l1;
        if (l1->val <= l2->val) {
            l1->next = mergeTwoListsRecursive(l1->next, l2);
            return l1;
        }
        l2->next = mergeTwoListsRecursive(l1, l2->next);
        return l2;
    }
};
