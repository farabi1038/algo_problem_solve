class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        length =len(heights)-1
        index=[length]
        maxH=heights[length]
        for i in range(length,-1,-1):
            if heights[i]>maxH:
                index.append(i)
                maxH=heights[i]
        return index[::-1]        

        