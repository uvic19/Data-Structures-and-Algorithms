"""
Problem: 347. Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/

Description:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:    
        seen = {}
        h = []

        for n in nums:
            if n not in seen:
                seen[n] = 1
            else:
                seen[n] += 1
        
        for num, freq in seen.items():
            heapq.heappush(h, (freq,num))

            if len(h) > k:
                heapq.heappop(h)
        
        res = []
        for freq, num in h:
            res.append(num)

        return res

# --- Time & Space Complexity ---
# TC: O(n log k)
# SC: O(n)
