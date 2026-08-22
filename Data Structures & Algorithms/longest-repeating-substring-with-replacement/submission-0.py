class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        max_freq = 0 # max times a char appears
        left = 0 
        res = 0

        for right in range(len(s)) :
            d[s[right]] += 1
            max_freq = max(max_freq, d[s[right]])

            window_size = right - left + 1
            if window_size - max_freq > k :
                d[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        return res

