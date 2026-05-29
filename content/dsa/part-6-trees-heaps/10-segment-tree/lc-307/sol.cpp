// LC 307. Range Sum Query - Mutable
#include <vector>
#include <algorithm>

class NumArray {
public:
    explicit NumArray(const std::vector<int>& nums)
        : n(static_cast<int>(nums.size())), tree(4 * std::max(n, 1)) {
        if (n > 0) build(nums, 1, 0, n - 1);
    }

    void update(int index, int val) {
        updateRec(1, 0, n - 1, index, val);
    }

    int sumRange(int left, int right) const {
        return queryRec(1, 0, n - 1, left, right);
    }

private:
    int n;
    std::vector<int> tree;

    void build(const std::vector<int>& nums, int v, int tl, int tr) {
        if (tl == tr) { tree[v] = nums[tl]; return; }
        int tm = (tl + tr) / 2;
        build(nums, 2 * v, tl, tm);
        build(nums, 2 * v + 1, tm + 1, tr);
        tree[v] = tree[2 * v] + tree[2 * v + 1];
    }

    void updateRec(int v, int tl, int tr, int pos, int newVal) {
        if (tl == tr) { tree[v] = newVal; return; }
        int tm = (tl + tr) / 2;
        if (pos <= tm) updateRec(2 * v, tl, tm, pos, newVal);
        else updateRec(2 * v + 1, tm + 1, tr, pos, newVal);
        tree[v] = tree[2 * v] + tree[2 * v + 1];
    }

    int queryRec(int v, int tl, int tr, int l, int r) const {
        if (l > r) return 0;
        if (l == tl && r == tr) return tree[v];
        int tm = (tl + tr) / 2;
        return queryRec(2 * v, tl, tm, l, std::min(r, tm))
             + queryRec(2 * v + 1, tm + 1, tr, std::max(l, tm + 1), r);
    }
};
