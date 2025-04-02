class SparseVector:
    def __init__(self, nums: List[int]):
        self.l=nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sum=0
        for i,j in zip(self.l,vec.l):
            if i!=0 and j!=0:
                sum+=i*j
        return sum

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)