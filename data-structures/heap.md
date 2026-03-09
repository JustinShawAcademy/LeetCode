also known as *priority queue*.

As we know in queues, their queue is first in, first out. However, if we wanted to queue based on a priority value, we could do that will a *priority queue*. The two types of priority are min and max. For example, in a min priority queue, we also pop the smallest number first.

It's called a priority queue is the interface but under the hood, it's using a **binary heap** (however, the name's are interchangable)

![heap](./img/heap.png)

At first glance, a heap looks like a binary tree. That's because it is haha. However, it's not the Binary Search Tree that we all know. This is because at the root node, every value to the right of it will be bigger than it. It's not the case of heaps.

In fact, we can see in a min heap, that the decendant in the tree.

1) Structure property 
A binary heap is essentailly a binary tree that is considered a complete binary tree. 

![complete-binary-tree](./img/complete-binary-tree.png)

1. Full Levels: Every level of the tree must be completely filled with nodes, except possibly the very last level.
2. Left Alignment: In that last level, all nodes must be as far to the left as possible. There can be no "gaps" between nodes from left to right.

2) Order property 
Recall the reason for having this min/max heap is for finding the minimum/maximum as fast. Therefore, in our min heap, it makes sense to have the smallest value at the root node. It will take O(1) time.

So what order property should we give for it to do that? For every node, all the decendants **must** be greater than or equal to.

Binary heaps are drawn using a tree data structure but under the hood, they are implemented using arrays. Let's show how we can do this by using the given binary heap: `[14,19,16,21,26,19,68,65,30,null,null,null,null,null,null]`

We will take an array of size `n+1` where `n` is the number of nodes in our binary heap. This will make sense soon. We will visit our nodes in the same order as we visit nodes in breadth-first search (level by level, from left to right). We will insert these into our array in a contiguous fashion. However, we will start filling them from index 1 instead of 0, for reasons we will discuss soon.

![heap-array](./img/heap-array.png)

The reason why we start filling up our array from index `1` is because it helps us figure out the index at which a node's left child, right child, or the parent resides. Because binary heaps are complete binary trees, no space is required for pointers. Instead, a node's left child, right child and parent can be calculated using the following formulas, where $i$ is the index of a given node.

- `leftChild` = $2*i$
- `rightChild` = $2*i+1$
- `parent` = $i/1$

---

Suppose we wanted to find the children and parent of the node with value `19`. The following visual demonstrates how using the formulas helps us figure them out.

The number above a node (in blue) is the corresponding index in the array of each node. It is important to note that these formulas only work when the tree is a complete binary tree and the array is filled contiguously from left to right.

We can also now appreciate why we start at index `1`. Suppose we wanted to find `14`'s left and right child and `14` was at `0` . Well, any number multiplied by a $0$ is $0$, and would tell us that the left child resides at the `o`th index, which is of course not the case.

![heap-array-example](./img/heap-array-example.png)
