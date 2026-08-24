class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        size = len(s2)
        for left in range(size) :
            if s2[left] in count_s1 :
                count_s2 = defaultdict(int)
                right = left
                while right < size and s2[right] in count_s1 :
                    l, r = s2[left], s2[right]
                    count_s2[r] += 1
                    if count_s2[r] > count_s1[r] :
                        break
                    if count_s1 == count_s2 :
                        return True
                    right += 1
        
        return False
        