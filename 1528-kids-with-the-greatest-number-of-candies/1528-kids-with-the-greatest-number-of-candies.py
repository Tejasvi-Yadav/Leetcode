class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy=max(candies)

        result=[]

        for num in candies:
            if num + extraCandies >=max_candy:
                result.append(True)
            else:
                result.append(False)

        return result
        