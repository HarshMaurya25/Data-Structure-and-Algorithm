# Heap

A Heap is a complete binary tree that follows a **specific ordering property between parent and child nodes**.

A heap is commonly implemented using an array or `ArrayList`, where the tree structure is represented through indices.

---

## Type

There are two common types of Binary Heap:

| Type         | Property          |
| ------------ | ----------------- |
| **Min Heap** | Parent ≤ Children |
| **Max Heap** | Parent ≥ Children |

This implementation is a **Min Heap**.

---

## Array Representation

A Binary Heap does not require explicit tree nodes.

For an element at index `i`:

| Relationship | Formula       |
| ------------ | ------------- |
| Parent       | `(i - 1) / 2` |
| Left Child   | `2 * i + 1`   |
| Right Child  | `2 * i + 2`   |

The heap is stored in an `ArrayList`, and these formulas are used to navigate between parent and child elements.

---

# Insert Algorithm

Insertion is performed using **Upheap / Bubble Up**.

### Steps

- Add the new element at the end of the `ArrayList`.
- Start from the index of the newly inserted element.
- Find its parent using `(index - 1) / 2`.
- Compare the current element with its parent.
- If the current element is smaller, swap them.
- Move to the parent's index.
- Continue until the element reaches the root or the parent is smaller than or equal to it.

---

# Delete Algorithm

In a Min Heap, deletion normally means **removing the minimum element**, which is the root.

Deletion is performed using **Downheap / Bubble Down**.

### Steps

- Store the root element.
- Remove the last element from the `ArrayList`.
- If the heap is not empty, place the last element at index `0`.
- Start from the root.
- Calculate the left and right child indices.
- Find the smaller child.
- If the smaller child is smaller than the current element, swap them.
- Move to the smaller child's index.
- Continue until the heap property is restored.
- Return the original root element.

---

# Operations

| Operation      | Description                                                           | Time Complexity |
| -------------- | --------------------------------------------------------------------- | --------------: |
| **Insert**     | Adds an element and restores heap property using Upheap               |      `O(log n)` |
| **Remove**     | Removes the minimum element and restores heap property using Downheap |      `O(log n)` |
| **Peek**       | Returns the minimum element without removing it                       |          `O(1)` |
| **Search**     | Searches for an element in the heap                                   |          `O(n)` |
| **Build Heap** | Converts an unordered collection into a heap                          |          `O(n)` |
| **Size**       | Returns the number of elements                                        |          `O(1)` |
| **Is Empty**   | Checks whether the heap is empty                                      |          `O(1)` |

---

# Space Complexity

A heap containing `n` elements requires:

**Space: `O(n)`**

The heap is stored inside an `ArrayList`, so the memory requirement grows linearly with the number of elements.

---

# Java Implementation

Java provides a built-in heap implementation through `PriorityQueue`.

By default, `PriorityQueue` works as a **Min Heap**.

### Import and Create

```java
import java.util.PriorityQueue;

PriorityQueue<Integer> minHeap = new PriorityQueue<>();
```

### Java Operations

| Operation      | Code                      |
| -------------- | ------------------------- |
| Insert         | `minHeap.offer(value)`    |
| Insert         | `minHeap.add(value)`      |
| Remove Minimum | `minHeap.poll()`          |
| Peek Minimum   | `minHeap.peek()`          |
| Check Empty    | `minHeap.isEmpty()`       |
| Get Size       | `minHeap.size()`          |
| Search         | `minHeap.contains(value)` |

---

# Python Implementation

Python provides a built-in Min Heap through the `heapq` module.

### Import and Create

```python
import heapq

min_heap = []
```

### Python Operations

| Operation      | Code                              |
| -------------- | --------------------------------- |
| Insert         | `heapq.heappush(min_heap, value)` |
| Remove Minimum | `heapq.heappop(min_heap)`         |
| Peek Minimum   | `min_heap[0]`                     |
| Build Heap     | `heapq.heapify(min_heap)`         |
| Get Size       | `len(min_heap)`                   |
| Check Empty    | `not min_heap`                    |
| Search         | `value in min_heap`               |
