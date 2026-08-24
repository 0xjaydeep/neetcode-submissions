class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size_s1, size_s2 = len(s1), len(s2)

        if size_s1 > size_s2:
            return False

        count_s1 = Counter(s1)
        count_window = Counter(s2[:size_s1])

        if count_s1 == count_window:
            return True

        for right in range(size_s1, size_s2):
            r = s2[right]
            count_window[r] += 1
            l = s2[right - size_s1]
            count_window[l] -= 1
            if count_window[l] == 0:
                del count_window[l]
            if count_window == count_s1:
                return True

        return False
