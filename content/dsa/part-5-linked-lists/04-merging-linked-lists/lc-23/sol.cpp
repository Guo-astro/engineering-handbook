// LC 23. Merge k Sorted Lists
#include <queue>
#include <tuple>
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
    // Min-heap of (val, listIndex, ListNode*). std::greater<> turns the
    // default max-heap into a min-heap; listIndex breaks ties so the
    // comparator is a total order. O(N log k) time, O(k) auxiliary.
    ListNode* mergeKListsHeap(std::vector<ListNode*>& lists) {
        ListNode dummy(0);
        ListNode* tail = &dummy;
        using Entry = std::tuple<int, int, ListNode*>;
        std::priority_queue<Entry, std::vector<Entry>, std::greater<Entry>> pq;
        for (std::size_t i = 0; i < lists.size(); ++i) {
            if (lists[i] != nullptr) {
                pq.emplace(lists[i]->val, static_cast<int>(i), lists[i]);
            }
        }
        while (!pq.empty()) {
            auto [val, idx, node] = pq.top();
            pq.pop();
            (void)val;
            tail->next = node;
            tail = tail->next;
            if (node->next != nullptr) {
                pq.emplace(node->next->val, idx, node->next);
            }
        }
        tail->next = nullptr;
        return dummy.next;
    }

    // Pairwise divide-and-conquer. log k merge levels, O(N) work per
    // level. O(N log k) time, O(log k) recursion stack.
    ListNode* mergeKListsDivideConquer(std::vector<ListNode*>& lists) {
        if (lists.empty()) return nullptr;
        std::vector<ListNode*> current = lists;
        while (current.size() > 1) {
            std::vector<ListNode*> merged;
            merged.reserve((current.size() + 1) / 2);
            for (std::size_t i = 0; i < current.size(); i += 2) {
                ListNode* a = current[i];
                ListNode* b = (i + 1 < current.size()) ? current[i + 1] : nullptr;
                merged.push_back(mergeTwo(a, b));
            }
            current = std::move(merged);
        }
        return current[0];
    }

private:
    // LC 21's iterative merge, used as the leaf step of d-and-c.
    ListNode* mergeTwo(ListNode* a, ListNode* b) {
        ListNode dummy(0);
        ListNode* tail = &dummy;
        while (a != nullptr && b != nullptr) {
            if (a->val <= b->val) {
                tail->next = a;
                a = a->next;
            } else {
                tail->next = b;
                b = b->next;
            }
            tail = tail->next;
        }
        tail->next = (a != nullptr) ? a : b;
        return dummy.next;
    }
};
