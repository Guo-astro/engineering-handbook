// LC linear search — Knuth Algorithm B (The Art of Computer Programming Vol 3 §6.1).
//
// std::size_t is the natural type against vector::size; the cast to int
// happens only at the return site to match the chapter's int-based contract.
// std::find(nums.begin, nums.end, target) is the standard-library
// equivalent and what production C++ would call; the explicit loop is what
// the chapter teaches because it is what an interviewer asks you to write.
#include <cstddef>
#include <vector>

int linearSearch(const std::vector<int>& nums, int target) {
    for (std::size_t i = 0; i < nums.size(); ++i) {
        if (nums[i] == target) {
            return static_cast<int>(i);
        }
    }
    return -1;
}
