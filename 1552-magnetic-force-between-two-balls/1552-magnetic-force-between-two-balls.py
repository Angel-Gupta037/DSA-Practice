class Solution:
    def maxDistance(self, position: List[int], balls: int) -> int:
        position.sort()
        low = 1
        high = position[len(position)-1] - position[0]
        ans = -1

        while low <= high:
            mid = (low+high)//2
            cntballs = 1
            last = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last >= mid:
                    cntballs += 1
                    last = position[i]
            
            if cntballs >= balls:
                ans = mid
                low = mid+1   # try larger force
            else:
                high = mid-1  # try smaller force

        return ans