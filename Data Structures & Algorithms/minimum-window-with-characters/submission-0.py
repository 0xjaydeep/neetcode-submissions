class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        window_freq = defaultdict(int)

        have, need = 0, len(count_t)
        ans = ""
        ans_len = float("inf")
        left = 0

        for right in range(len(s)) :
            r = s[right]
            window_freq[r] += 1

            if r in count_t and window_freq[r] == count_t[r] :
                have += 1

            # window is valid, try to shrink and update answer
            while have == need :
                # update the answer
                if (right - left + 1) < ans_len :
                    ans_len = right - left + 1
                    ans = s[left:right+1]
                
                # shrink from left
                l = s[left]
                window_freq[l] -= 1
                if l in count_t and window_freq[l] < count_t[l] :
                    have -= 1
                left += 1
        
        return ans

        