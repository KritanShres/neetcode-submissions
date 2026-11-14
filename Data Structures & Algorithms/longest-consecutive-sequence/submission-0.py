class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_list = set(nums)
        seq_freq = 0
        for n in nums:
            if (n - 1) not in set_list: 
                count = 0 
                while n + count in set_list: 
                    count += 1 
                
                seq_freq = max(seq_freq, count)

        
        return seq_freq 