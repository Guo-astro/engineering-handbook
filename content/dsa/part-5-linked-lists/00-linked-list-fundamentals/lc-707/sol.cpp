// LC 707. Design Linked List
// Sentinel-driven singly linked list. The dummy head removes the
// head-vs-mid case split: every insert and delete points at a
// non-null predecessor `prev`, so the wiring is the same at index 0
// and at index k.
#pragma once

class MyLinkedList {
public:
    MyLinkedList() : dummy(new ListNode(0)), length(0) {}

    ~MyLinkedList() {
        ListNode* curr = dummy;
        while (curr != nullptr) {
            ListNode* next = curr->next;
            delete curr;
            curr = next;
        }
    }

    int get(int index) {
        if (index < 0 || index >= length) return -1;
        ListNode* curr = dummy->next;
        for (int i = 0; i < index; ++i) curr = curr->next;
        return curr->val;
    }

    void addAtHead(int val) { addAtIndex(0, val); }
    void addAtTail(int val) { addAtIndex(length, val); }

    void addAtIndex(int index, int val) {
        if (index < 0 || index > length) return;
        ListNode* prev = dummy;
        for (int i = 0; i < index; ++i) prev = prev->next;
        ListNode* node = new ListNode(val);
        node->next = prev->next;
        prev->next = node;
        ++length;
    }

    void deleteAtIndex(int index) {
        if (index < 0 || index >= length) return;
        ListNode* prev = dummy;
        for (int i = 0; i < index; ++i) prev = prev->next;
        ListNode* victim = prev->next;
        prev->next = victim->next;
        delete victim;
        --length;
    }

private:
    struct ListNode {
        int val;
        ListNode* next;
        ListNode(int v) : val(v), next(nullptr) {}
    };
    ListNode* dummy;
    int length;
};
