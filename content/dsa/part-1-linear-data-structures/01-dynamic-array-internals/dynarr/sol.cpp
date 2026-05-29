// DynArr<T> — geometric-resize dynamic array reference template.
// Parameterized growth factor (growth_num / growth_den) for studying the
// amortized-O(1) push proof; tracks reallocation count. Not an LC problem.
#include <cstddef>
#include <stdexcept>
#include <utility>

namespace dsa {

template <class T>
class DynArr {
public:
    DynArr(std::size_t initial_cap, int growth_num, int growth_den)
        : buf_(nullptr), size_(0), cap_(initial_cap),
          growth_num_(growth_num), growth_den_(growth_den), reallocs_(0) {
        if (initial_cap < 1) throw std::invalid_argument("initial_cap must be >= 1");
        if (growth_num <= growth_den) throw std::invalid_argument("growth factor must be > 1");
        buf_ = new T[initial_cap];
    }

    ~DynArr() { delete[] buf_; }
    DynArr(const DynArr&) = delete;
    DynArr& operator=(const DynArr&) = delete;

    std::size_t size() const noexcept { return size_; }
    std::size_t capacity() const noexcept { return cap_; }
    int reallocations() const noexcept { return reallocs_; }

    const T& get(std::size_t i) const {
        if (i >= size_) throw std::out_of_range("get out of range");
        return buf_[i];
    }

    void push(const T& x) {
        if (size_ == cap_) grow();
        buf_[size_] = x;
        size_ += 1;
    }

private:
    T* buf_;
    std::size_t size_;
    std::size_t cap_;
    int growth_num_;
    int growth_den_;
    int reallocs_;

    void grow() {
        // Ceiling division so factors like 9/8 still grow on small caps.
        std::size_t new_cap = (cap_ * static_cast<std::size_t>(growth_num_)
                               + static_cast<std::size_t>(growth_den_) - 1)
                              / static_cast<std::size_t>(growth_den_);
        // Guard against rounding to a no-op (would loop forever on next push).
        if (new_cap <= cap_) new_cap = cap_ + 1;
        T* new_buf = new T[new_cap];
        for (std::size_t i = 0; i < size_; ++i) new_buf[i] = std::move(buf_[i]);
        delete[] buf_;
        buf_ = new_buf;
        cap_ = new_cap;
        reallocs_ += 1;
    }
};

}  // namespace dsa
