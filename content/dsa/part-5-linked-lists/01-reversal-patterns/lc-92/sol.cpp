// LC 92. Reverse Linked List II
// One-pass head-insertion variant: walk a sentinel (left-1) steps to
// land just before the segment, then for (right-left) iterations splice
// each newly-encountered node to the front of the reversed prefix.
struct ListNode {
    int val;
    ListNode* next;
    explicit ListNode(int v) : val(v), next(nullptr) {}
    ListNode(int v, ListNode* n) : val(v), next(n) {}
};

class Solution {
public:
    // One-pass range reversal via head-insertion. Time O(n), space O(1).
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (head == nullptr || left == right) {
            return head;
        }

        ListNode dummy(0, head);
        ListNode* pre = &dummy;
        for (int i = 0; i < left - 1; ++i) {
            pre = pre->next;
        }

        // `curr` is the first node of the segment to reverse; it stays put
        // and becomes the segment's tail. Each iteration lifts curr->next out
        // and splices it to the front of the reversed prefix.
        ListNode* curr = pre->next;
        for (int i = 0; i < right - left; ++i) {
            ListNode* moved = curr->next;
            curr->next = moved->next;
            moved->next = pre->next;
            pre->next = moved;
        }

        return dummy.next;
    }
};
