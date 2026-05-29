// LC 23. Merge k Sorted Lists
// Custom comparator via lambda; std::priority_queue<T*> defaults to
// pointer-address ordering, which is wrong for ListNode*.
#include <queue>
#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    explicit ListNode(int v) : val(v), next(nullptr) {}
    ListNode(int v, ListNode* n) : val(v), next(n) {}
};

class Solution {
public:
    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        auto cmp = [](ListNode* a, ListNode* b) { return a->val > b->val; };
        std::priority_queue<ListNode*, std::vector<ListNode*>, decltype(cmp)> h(cmp);
        for (auto* p : lists) {
            if (p) h.push(p);
        }
        ListNode dummy;
        ListNode* tail = &dummy;
        while (!h.empty()) {
            ListNode* node = h.top();
            h.pop();
            tail->next = node;
            tail = node;
            if (node->next) {
                h.push(node->next);
            }
        }
        tail->next = nullptr;
        return dummy.next;
    }
};
