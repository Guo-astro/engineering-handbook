// LC 307. Range Sum Query - Mutable
public final class Sol {
    static class NumArray {
        private final int n;
        private final int[] tree;

        public NumArray(int[] nums) {
            this.n = nums.length;
            this.tree = new int[4 * Math.max(n, 1)];
            if (n > 0) build(nums, 1, 0, n - 1);
        }

        private void build(int[] nums, int v, int tl, int tr) {
            if (tl == tr) { tree[v] = nums[tl]; return; }
            int tm = (tl + tr) / 2;
            build(nums, 2 * v, tl, tm);
            build(nums, 2 * v + 1, tm + 1, tr);
            tree[v] = tree[2 * v] + tree[2 * v + 1];
        }

        public void update(int index, int val) {
            update(1, 0, n - 1, index, val);
        }

        private void update(int v, int tl, int tr, int pos, int newVal) {
            if (tl == tr) { tree[v] = newVal; return; }
            int tm = (tl + tr) / 2;
            if (pos <= tm) update(2 * v, tl, tm, pos, newVal);
            else update(2 * v + 1, tm + 1, tr, pos, newVal);
            tree[v] = tree[2 * v] + tree[2 * v + 1];
        }

        public int sumRange(int left, int right) {
            return query(1, 0, n - 1, left, right);
        }

        private int query(int v, int tl, int tr, int l, int r) {
            if (l > r) return 0;
            if (l == tl && r == tr) return tree[v];
            int tm = (tl + tr) / 2;
            return query(2 * v, tl, tm, l, Math.min(r, tm))
                 + query(2 * v + 1, tm + 1, tr, Math.max(l, tm + 1), r);
        }
    }
}
