class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        maxCandy = max(candies)
        for i in candies:
            if i + extraCandies >= maxCandy:
                res.append(True)
            else:
                res.append(False)
        return res