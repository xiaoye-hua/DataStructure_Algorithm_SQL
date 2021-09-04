


# Top interview Questions (medium level) 0904

## Linked List

- 2.Add Two Numbers (medium, dummy head): simple iteration
- 3.Longest Substring Without Repeating Characters (medium, two pointers(sliding window), hash table): for ele record the biggest index for it; update begin index for sliding window every step


## Array

- 560.Subarray Sum Equals K (medium, hash table): hash table is used to record the appearance time of sum
- 523.Continuous Subarray Sum (medium, hash table): hash table is used to record appearance index of sum % k; n1%k = n1%k => abs(n1-n2) = n*k
- 525.Contiguous Array (medium, hash table): array lst consists of -1 and 1, if sum(lst[:a]) == sum(lst[:b]) => lst[a:b+1] consists of same number of -1 and 1

## Tree

- 101.Symmetric Tree (easy): define symmetric tree with recursion
- 112.Path Sum (easy, DFS): root-to-leaf sum

## Dynamic Programming


 