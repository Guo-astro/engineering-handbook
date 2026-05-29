// LC 25. Reverse Nodes in k-Group
#include <cstddef>

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    explicit ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* nxt) : val(x), next(nxt) {}
};

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode dummy(0, head);
        ListNode* groupPrev = &dummy;

        while (true) {
            ListNode* kth = kthAfter(groupPrev, k);
            if (kth == nullptr) break;
            ListNode* groupNext = kth->next;

            ListNode* prev = groupNext;
            ListNode* curr = groupPrev->next;
            while (curr != groupNext) {
                ListNode* nxt = curr->next;
                curr->next = prev;
                prev = curr;
                curr = nxt;
            }

            ListNode* newGroupTail = groupPrev->next;
            groupPrev->next = kth;
            groupPrev = newGroupTail;
        }

        return dummy.next;
    }

private:
    ListNode* kthAfter(ListNode* node, int k) {
        ListNode* curr = node;
        while (curr != nullptr && k > 0) {
            curr = curr->next;
            --k;
        }
        return curr;
    }
};
