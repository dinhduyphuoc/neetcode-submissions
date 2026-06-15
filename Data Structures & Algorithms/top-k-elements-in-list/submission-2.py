class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for key, item in freq.items():
            bucket[item].append(key)

        res = []
        for i in range(len(bucket) - 1, -1, -1):
            if not bucket[i]:
                continue
            for item in bucket[i]:
                res.append(item)
                if len(res) == k:
                    return res 