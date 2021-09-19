
## Linked List

- 2.Add Two Numbers (medium, dummy head): simple iteration
- 3.Longest Substring Without Repeating Characters (medium, two pointers(sliding window), hash table): for ele record the biggest index for it; update begin index for sliding window every step
- 21.Merge Two Sorted Lists (easy, dummy head)
- 61.Rotate List (medium, two pointer): fast_pointer, slow_pointer; mind the copy function in Python
    - fast = fast.next ==> only a reference, don't change the value
    - fast.next = c  ==> change the value
- 148.Sort List (medium, merge sort): apply merge sort to linked list

## Array


- 560.Subarray Sum Equals K (medium, hash table): hash table is used to record the appearance time of sum
- 523.Continuous Subarray Sum (medium, hash table): hash table is used to record appearance index of sum % k; n1%k = n1%k => abs(n1-n2) = n*k
- 525.Contiguous Array (medium, hash table): array lst consists of -1 and 1, if sum(lst[:a]) == sum(lst[:b]) => lst[a:b+1] consists of same number of -1 and 1
- 567.Permutation in String (medium, hash table): use hash table to compare permutation
- 16.3Sum Closest (medium, hash table): sort then enumerate
- 189.Rotate Array (medium, two pointers)
- 31.Next Permutation (medium, two pointers): 
    1. inspired from discussion: https://leetcode.com/problems/next-permutation/discuss/229211/Python-solution
    2. Two steps:
        1. find index a, change nums[a] to a bigger number --> we can only find the target number on the right of index a (Otherwise, the whole number will be smaller)
        2. change nums[a+1:] to the smallest number
- 41.First Missing Positive (hard, hash table): utilize the original list to store the information as a hash table
- 54.Spiral Matrix (medium): mind the corner cases
- 11.Container With Most Water (medium, greedy, two pointers):
    1. Why move the index of the shoter one: Prove: Assume height[right_idx]>height[left_idx], if we move right_idx to left
        1. if height[right_idx-1]>height[right_idx], the height of area is determined
            by height[left_idx], but width decreases by one  --> the area will decrease
        2. if height[right_idx -1]< height[right_idx], the height might decreased, 
            while the width decrease by one --> the area will decrease
- 76.Minimum Window Substring (hard, hash table, sliding windows): 
    1. Inspired from problem 209
- 209.Minimum Size Subarray Sum (medium, hash table, sliding windows)
    1. hash table stores info
- 84.Largest Rectangle in Histogram (hard, stack):
    1. Refer to [Youtube video](https://www.youtube.com/watch?v=zx5Sw9130L0&feature=emb_logo)
- 1423.Maximum Points You Can Obtain from Cards (medium, sliding window): need to go through several cases before finding the pattern
- 75.Sort Colors (medium, sort): compared to normal sort question, there are only 3 unique numbers. So take advantage of it.
- 912.Sort an Array (medium, sort): quick sort


## Tree

- 101.Symmetric Tree (easy): define symmetric tree with recursion
- 112.Path Sum (easy, DFS): root-to-leaf sum
- 543.Diameter of Binary Tree (easy, DFS): if root.left is None => l = 0; else: l = left_len+1
- 110.Balanced Binary Tree (medium, DFS): similar to problem 543, two values are returned
- 98.Validate Binary Search Tree (medium, DFS)


## Dynamic Programming

- 678.Valid Parenthesis String (medium, dynamic programming): left_paren_left, for valid parenthesis => left_paren_left >= 0 all the time and at the end left_paren_left=0; in this question, store the range of left_paren_left => check if 0 is included in the range
- 1963.Minimum Number of Swaps to Make the String Balanced (medium, greedy): same definition valid parenthesis at that of problem 678
    - [Explain Video - Youtube](https://www.youtube.com/watch?v=3YDBT9ZrfaU)
- 10.Regular Expression Matching (hard, dynamic programming)
- 300.Longest Increased Subsequence	Medium (medium, dynamic programming)
    1. Time complexity: O(n**2)
        2. dp[i] represents subsequence length of sublist that end at index i
        3. dp[i] = 1
        4. To update dp[idx], we'll iterate dp[:idx-1] 
    2. O(nlogn): dp[i] represents the smallest ending number for the subsequence with length i+i  (Refer to https://www.youtube.com/watch?v=l2rCz7skAlk)"
- 53.Maximum Subarray (easy, dynamic programming): dp[i] represents the max length of array that end in at the index of i-1; return max(dp)
- 121.Best Time to Buy and Sell Stock (easy, dynamic programming): dp[i] represent the max profit until ith day; use min_cost to represent the min cost until now



## Math
- 12.Integer to Roman (medium, math): module and remain
- 69.Sqrt(x) (easy, math): simple binary search
 